from flask import current_app
from StringIO import StringIO
import fhir_xml

class meta_patient(object):
    '''Mediate between XML/JSON schema bindings and
        the GNU Health models

        For now, focus on XML (because that is required)
    '''

    def __init__(self, record=None, xml_patient=None):
        self.record = record #gnu health model
        self.patient = xml_patient or fhir_xml.Patient() #patient xml
        if self.record and getattr(self.record, 'name', None):
            self.set_gender()
            self.set_deceased_status()
            self.set_deceased_datetime()
            self.set_birthdate()
            self.set_telecom()
            self.set_name()
            self.set_identifier()
            self.set_address()
            self.set_active()
            self.set_photo()
            self.set_communication()
            self.set_contact()
            self.set_care_provider()
            self.set_marital_status()

    def set_identifier(self):
        if getattr(self.record, 'puid', None):
            ident = fhir_xml.Identifier(
                        use=fhir_xml.IdentifierUse(value='usual'),
                        label=fhir_xml.string(value='PUID'),
                        system=fhir_xml.uri(value='gnuhealth::0'),
                                #value=current_app.config.get(
                                    #'INSTITUTION_ODI', None)),
                        value=fhir_xml.string(value=self.record.puid))

        elif getattr(self.record, 'alternative_identification', None):
            ident = fhir_xml.Identifier(
                        use=fhir_xml.IdentifierUse(value='usual'),
                        label=fhir_xml.string(value='ALTERNATE_ID'),
                        system=fhir_xml.system(
                            fhir_xml.uri(
                                value=current_app.config.get(
                                    'INSTITUTION_ODI',None))),
                        value=fhir_xml.string(
                            value=self.record.alternative_identification))
        else:
            return
        self.patient.add_identifier(value=ident)

    def set_name(self):
        name = []
        name.append(fhir_xml.HumanName(
                    use=fhir_xml.NameUse(value='official'),
                    family=[fhir_xml.string(value=x) for x in self.record.lastname.split()],
                    given=[fhir_xml.string(value=x) for x in self.record.name.name.split()]))

        if getattr(self.record.name, 'alias', None):
            name.append(fhir_xmlHumanName(
                        use=fhir_xml.NameUse(value='usual'),
                        given=[fhir_xml.string(value=self.record.name.alias)]))
        for x in name:
            self.patient.add_name(x)

    def set_telecom(self):
        telecom = []
        if getattr(self.record.name, 'phone', None):
            telecom.append(fhir_xml.Contact(
                    system=fhir_xml.ContactSystem(value='phone'),
                    value=fhir_xml.string(value=self.record.name.phone),
                    use=fhir_xml.ContactUse(value='home')))
        if getattr(self.record.name, 'mobile', None):
            telecom.append(fhir_xml.Contact(
                    system=fhir_xml.ContactSystem(value='phone'),
                    value=fhir_xml.string(value=self.record.name.mobile),
                    use=fhir_xml.ContactUse(value='mobile')))
        if getattr(self.record.name, 'email', None):
            telecom.append(fhir_xml.Contact(
                    system=fhir_xml.ContactSystem(value='email'),
                    value=fhir_xml.string(value=self.record.name.email),
                    use=fhir_xml.ContactUse(value='email')))
        for x in telecom:
            self.patient.add_telecom(x)

    def set_gender(self):
        if getattr(self.record, 'sex', None):
            coding = fhir_xml.Coding(
                        system=fhir_xml.uri(value='http://hl7.org/fhir/v3/AdministrativeGender'),
                        code=fhir_xml.code(value=self.record.sex.upper()),
                        display=fhir_xml.string(value='Male' if self.record.sex == 'm' else 'Female')
                        )
            gender=fhir_xml.CodeableConcept(coding=[coding])
            self.patient.set_gender(gender)

    def set_birthdate(self):
        if getattr(self.record, 'dob', None):
            self.patient.set_birthDate(fhir_xml.dateTime(value=self.record.dob))

    def set_deceased_status(self):
        if getattr(self.record, 'deceased', None):
            status=fhir_xml.boolean(value='true')
        else:
            status=fhir_xml.boolean(value='false')
        self.patient.set_deceasedBoolean(status)

    def set_deceased_datetime(self):
        if getattr(self.record, 'deceased', None):
            self.patient.set_deceasedDateTime(fhir_xml.dateTime(value=str(self.record.dod)))

    def set_address(self):
        if getattr(self.record.name, 'du', None):
            address=fhir_xml.Address()
            address.set_use(fhir_xml.string(value='home'))
            address.add_line(fhir_xml.string(value=' '.join([
                                        str(self.record.name.du.address_street_number),
                                        self.record.name.du.address_street])))
            address.set_city(fhir_xml.string(value=self.record.name.du.address_city))
            address.set_state(fhir_xml.string(value=self.record.name.du.address_subdivision.name))
            address.set_zip(fhir_xml.string(value=self.record.name.du.address_zip))
            address.set_country(fhir_xml.string(value=self.record.name.du.address_country.name))

            self.patient.add_address(address)

    def set_active(self):
        self.patient.set_active(fhir_xml.boolean(value='true'))

    def set_contact(self):
        pass

    def set_care_provider(self):
        #primary care doctor
        if getattr(self.record, 'primary_care_doctor', None):
            pass

    def set_communication(self):
        # Is this even in Health?
        pass

    def set_photo(self):
        import base64
        if getattr(self.record, 'photo', None):
            data = fhir_xml.base64Binary(value=base64.encodestring(self.record.photo))
            im = fhir_xml.Attachment(data=data)
            self.patient.add_photo(im)

    def set_marital_status(self):
        if getattr(self.record.name, 'marital_status', None):
            #Health has concubinage and separated, which aren't truly
            # matching to the FHIR defined statuses
            status = self.record.marital_status.upper()
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
            self.patient.set_maritalStatus(marital_status)

    def export_to_xml(self):
        if self.patient:
            output = StringIO()
            self.patient.export(outfile=output, pretty_print=False, level=4)
            content = output.getvalue()
            output.close()
            return content
        else:
            return '<error>No record(s) returned</error>'

    def export_to_json(self):
        #TODO More difficult
        pass
