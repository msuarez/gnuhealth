from flask import current_app
from StringIO import StringIO
import fhir_xml

class gnu_patient(fhir_xml.Patient):
    '''Mediate between XML/JSON schema bindings and
        the GNU Health models

        For now, focus on XML (because that is required)
    '''

    def set_gnu_patient(self, gnu):
        self.gnu_patient = gnu #gnu health model
        if self.gnu_patient and getattr(self.gnu_patient, 'name', None):
            self.__set_gender()
            self.__set_deceased_status()
            self.__set_deceased_datetime()
            self.__set_birthdate()
            self.__set_telecom()
            self.__set_name()
            self.__set_identifier()
            self.__set_address()
            self.__set_active()
            self.__set_photo()
            self.__set_communication()
            self.__set_contact()
            self.__set_care_provider()
            self.__set_marital_status()

    def __set_identifier(self):
        if getattr(self.gnu_patient, 'puid', None):
            ident = fhir_xml.Identifier(
                        use=fhir_xml.IdentifierUse(value='usual'),
                        label=fhir_xml.string(value='PUID'),
                        system=fhir_xml.uri(value='gnuhealth::0'),
                                #value=current_app.config.get(
                                    #'INSTITUTION_ODI', None)),
                        value=fhir_xml.string(value=self.gnu_patient.puid))

        elif getattr(self.gnu_patient, 'alternative_identification', None):
            ident = fhir_xml.Identifier(
                        use=fhir_xml.IdentifierUse(value='usual'),
                        label=fhir_xml.string(value='ALTERNATE_ID'),
                        system=fhir_xml.system(
                            fhir_xml.uri(
                                value=current_app.config.get(
                                    'INSTITUTION_ODI',None))),
                        value=fhir_xml.string(
                            value=self.gnu_patient.alternative_identification))
        else:
            return
        self.add_identifier(value=ident)

    def __set_name(self):
        name = []
        name.append(fhir_xml.HumanName(
                    use=fhir_xml.NameUse(value='official'),
                    family=[fhir_xml.string(value=x) for x in self.gnu_patient.lastname.split()],
                    given=[fhir_xml.string(value=x) for x in self.gnu_patient.name.name.split()]))

        if getattr(self.gnu_patient.name, 'alias', None):
            name.append(fhir_xmlHumanName(
                        use=fhir_xml.NameUse(value='usual'),
                        given=[fhir_xml.string(value=self.gnu_patient.name.alias)]))
        for x in name:
            self.add_name(x)

    def __set_telecom(self):
        telecom = []
        if getattr(self.gnu_patient.name, 'phone', None):
            telecom.append(fhir_xml.Contact(
                    system=fhir_xml.ContactSystem(value='phone'),
                    value=fhir_xml.string(value=self.gnu_patient.name.phone),
                    use=fhir_xml.ContactUse(value='home')))
        if getattr(self.gnu_patient.name, 'mobile', None):
            telecom.append(fhir_xml.Contact(
                    system=fhir_xml.ContactSystem(value='phone'),
                    value=fhir_xml.string(value=self.gnu_patient.name.mobile),
                    use=fhir_xml.ContactUse(value='mobile')))
        if getattr(self.gnu_patient.name, 'email', None):
            telecom.append(fhir_xml.Contact(
                    system=fhir_xml.ContactSystem(value='email'),
                    value=fhir_xml.string(value=self.gnu_patient.name.email),
                    use=fhir_xml.ContactUse(value='email')))
        for x in telecom:
            self.add_telecom(x)

    def __set_gender(self):
        if getattr(self.gnu_patient, 'sex', None):
            coding = fhir_xml.Coding(
                        system=fhir_xml.uri(value='http://hl7.org/fhir/v3/AdministrativeGender'),
                        code=fhir_xml.code(value=self.gnu_patient.sex.upper()),
                        display=fhir_xml.string(value='Male' if self.gnu_patient.sex == 'm' else 'Female')
                        )
            gender=fhir_xml.CodeableConcept(coding=[coding])
            self.set_gender(gender)

    def __set_birthdate(self):
        if getattr(self.gnu_patient, 'dob', None):
            self.set_birthDate(fhir_xml.dateTime(value=self.gnu_patient.dob))

    def __set_deceased_status(self):
        if getattr(self.gnu_patient, 'deceased', None):
            status=fhir_xml.boolean(value='true')
        else:
            status=fhir_xml.boolean(value='false')
        self.set_deceasedBoolean(status)

    def __set_deceased_datetime(self):
        if getattr(self.gnu_patient, 'deceased', None):
            self.set_deceasedDateTime(fhir_xml.dateTime(value=str(self.gnu_patient.dod)))

    def __set_address(self):
        if getattr(self.gnu_patient.name, 'du', None):
            address=fhir_xml.Address()
            address.set_use(fhir_xml.string(value='home'))
            address.add_line(fhir_xml.string(value=' '.join([
                                        str(self.gnu_patient.name.du.address_street_number),
                                        self.gnu_patient.name.du.address_street])))
            address.set_city(fhir_xml.string(value=self.gnu_patient.name.du.address_city))
            address.set_state(fhir_xml.string(value=self.gnu_patient.name.du.address_subdivision.name))
            address.set_zip(fhir_xml.string(value=self.gnu_patient.name.du.address_zip))
            address.set_country(fhir_xml.string(value=self.gnu_patient.name.du.address_country.name))

            self.add_address(address)

    def __set_active(self):
        self.set_active(fhir_xml.boolean(value='true'))

    def __set_contact(self):
        pass

    def __set_care_provider(self):
        #primary care doctor
        if getattr(self.gnu_patient, 'primary_care_doctor', None):
            pass

    def __set_communication(self):
        # Is this even in Health?
        pass

    def __set_photo(self):
        import base64
        if getattr(self.gnu_patient, 'photo', None):
            data = fhir_xml.base64Binary(value=base64.encodestring(self.gnu_patient.photo))
            im = fhir_xml.Attachment(data=data)
            self.add_photo(im)

    def __set_marital_status(self):
        if getattr(self.gnu_patient.name, 'marital_status', None):
            #Health has concubinage and separated, which aren't truly
            # matching to the FHIR defined statuses
            status = self.gnu_patient.marital_status.upper()
            statuses = { 'M': 'Married',
                    'W': 'Widowed',
                    'D': 'Divorced',
                    'S': 'Single'}
            if status in statuses:
                code = fhir_xml.code(value=status)
                display = fhir_xml.string(value=statuses[status])
            else:
                code = fhir_xml.code(value='OTH')
                display = fhir_xml.string(value='other')
            coding = fhir_xml.Coding(
                        system=fhir_xml.uri(value='http://hl7.org/fhir/v3/MaritalStatus'),
                        code=code,
                        display=display
                        )
            marital_status=fhir_xml.CodeableConcept(coding=[coding])
            self.set_maritalStatus(marital_status)

    def export_to_xml_string(self):
        output = StringIO()
        self.export(outfile=output, pretty_print=False, level=4)
        content = output.getvalue()
        output.close()
        return content

    def export_to_json_string(self):
        #TODO More difficult
        pass
