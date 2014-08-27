from flask import current_app
from StringIO import StringIO
from datetime import datetime
import fhir_xml as supermod
import sys

class gnu_patient(supermod.Patient):
    '''Mediate between XML/JSON schema bindings and
        the GNU Health models

        For now, focus on XML (because that is required)
    '''

    def set_gnu_patient(self, gnu):
        self.gnu_patient = gnu #gnu health model

    def import_from_gnu_patient(self):
        # Get info, and set from, gnu model
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

    def get_gnu_patient(self):
        # Return dicts for models
        ex = {}
        ex['party']={'name': self.__get_firstname(),
                        'activation_date': datetime.today().date().isoformat(),
                        'alias': self.__get_alias(),
                        'is_patient': True,
                        'is_person': True,
                        'sex': self.__get_gender(),
                        'dob': self.__get_birthdate(),
                        'photo': self.__get_photo(),
                        'marital_status': self.__get_marital_status(),
                        'ref': self.__get_identifier(),
                        'lastname': self.__get_lastname(),
                        'alias': self.__get_alias()
                    }
        ex['patient']={
                          'deceased': self.__get_deceased_status(),
                          'dod': self.__get_deceased_datetime()
                      }
        #self.__get_address()
        #self.__get_telecom()
        return ex

    def __set_identifier(self):
        if getattr(self.gnu_patient, 'puid', None):
            ident = supermod.Identifier(
                        use=supermod.IdentifierUse(value='usual'),
                        label=supermod.string(value='PUID'),
                        system=supermod.uri(value='gnuhealth::0'),
                                #value=current_app.config.get(
                                    #'INSTITUTION_ODI', None)),
                        value=supermod.string(value=self.gnu_patient.puid))

        elif getattr(self.gnu_patient, 'alternative_identification', None):
            ident = supermod.Identifier(
                        use=supermod.IdentifierUse(value='usual'),
                        label=supermod.string(value='ALTERNATE_ID'),
                        system=supermod.system(
                            supermod.uri(
                                value=current_app.config.get(
                                    'INSTITUTION_ODI',None))),
                        value=supermod.string(
                            value=self.gnu_patient.alternative_identification))
        else:
            return
        self.add_identifier(value=ident)

    def __get_identifier(self):
        if self.identifier:
            return self.identifier[0].value.value

    def __set_name(self):
        # TODO: Discuss these meanings more
        name = []
        if getattr(self.gnu_patient, 'lastname', None):
            family=[supermod.string(value=x) for x in self.gnu_patient.lastname.split()]
        else:
            family=None
        name.append(supermod.HumanName(
                    use=supermod.NameUse(value='usual'),
                    family=family,
                    given=[supermod.string(value=x) for x in self.gnu_patient.name.name.split()]))


        if getattr(self.gnu_patient.name, 'alias', None):
            name.append(supermodHumanName(
                        use=supermod.NameUse(value='nickname'),
                        given=[supermod.string(value=self.gnu_patient.name.alias)]))
        for x in name:
            self.add_name(x)

    def __get_alias(self):
        if getattr(self, 'name', None):
            if getattr(self.name[0].use, 'value') == 'nickname':
                return self.name[0].given[0].value

    def __get_lastname(self):
        if getattr(self, 'name', None):
            if getattr(self.name[0].use, 'value') in ('usual', 'official'):
                return ' '.join([m.value for m in self.name[0].family])

    def __get_firstname(self):
        if getattr(self, 'name', None):
            if getattr(self.name[0].use, 'value') in ('official', 'usual'):
                return self.name[0].given[0].value

    def __set_telecom(self):
        telecom = []
        if getattr(self.gnu_patient.name, 'phone', None):
            telecom.append(supermod.Contact(
                    system=supermod.ContactSystem(value='phone'),
                    value=supermod.string(value=self.gnu_patient.name.phone),
                    use=supermod.ContactUse(value='home')))
        if getattr(self.gnu_patient.name, 'mobile', None):
            telecom.append(supermod.Contact(
                    system=supermod.ContactSystem(value='phone'),
                    value=supermod.string(value=self.gnu_patient.name.mobile),
                    use=supermod.ContactUse(value='mobile')))
        if getattr(self.gnu_patient.name, 'email', None):
            telecom.append(supermod.Contact(
                    system=supermod.ContactSystem(value='email'),
                    value=supermod.string(value=self.gnu_patient.name.email),
                    use=supermod.ContactUse(value='email')))
        for x in telecom:
            self.add_telecom(x)

    def __get_telecom(self):
        if getattr(self, 'telecom', None):
            tc={}
            for c in self.telecom:
                if c.use.value == 'home':
                    if c.value:
                        tc['phone']=c.value.value
                elif c.use.value == 'mobile':
                    if c.value:
                        tc['mobile']=c.value.value
                elif c.use.value == 'email':
                    if c.value:
                        tc['email']=c.value.value
            return tc

    def __set_gender(self):
        if getattr(self.gnu_patient, 'sex', None):
            coding = supermod.Coding(
                        system=supermod.uri(value='http://hl7.org/fhir/v3/AdministrativeGender'),
                        code=supermod.code(value=self.gnu_patient.sex.upper()),
                        display=supermod.string(value='Male' if self.gnu_patient.sex == 'm' else 'Female')
                        )
            gender=supermod.CodeableConcept(coding=[coding])
            self.set_gender(gender)

    def __get_gender(self):
        if getattr(self, 'gender', None):
            return 'm' if self.gender.coding[0].code.value == 'M' else 'f'

    def __set_birthdate(self):
        if getattr(self.gnu_patient, 'dob', None):
            self.set_birthDate(supermod.dateTime(value=self.gnu_patient.dob))

    def __get_birthdate(self):
        if getattr(self, 'birthDate', None):
            return self.birthDate.value

    def __set_deceased_status(self):
        if getattr(self.gnu_patient, 'deceased', None):
            status=supermod.boolean(value='true')
        else:
            status=supermod.boolean(value='false')
        self.set_deceasedBoolean(status)

    def __get_deceased_status(self):
        if getattr(self.deceasedBoolean,'value', None) in (None ,'False', 'false'):
            deceased=False
        else:
            deceased=True
        return deceased

    def __set_deceased_datetime(self):
        if getattr(self.gnu_patient, 'dod', None):
            self.set_deceasedDateTime(supermod.dateTime(value=str(self.gnu_patient.dod)))

    def __get_deceased_datetime(self):
        if getattr(self, 'deceasedDateTime', None) is not None:
            return self.deceasedDateTime.value

    def __set_address(self):
        if getattr(self.gnu_patient.name, 'du', None):
            address=supermod.Address()
            address.set_use(supermod.string(value='home'))
            address.add_line(supermod.string(value=' '.join([
                                        str(self.gnu_patient.name.du.address_street_number),
                                        self.gnu_patient.name.du.address_street])))
            address.set_city(supermod.string(value=self.gnu_patient.name.du.address_city))
            address.set_state(supermod.string(value=self.gnu_patient.name.du.address_subdivision.name))
            address.set_zip(supermod.string(value=self.gnu_patient.name.du.address_zip))
            address.set_country(supermod.string(value=self.gnu_patient.name.du.address_country.name))

            self.add_address(address)

    def __get_address(self):
        # TODO Add tests (?) and line
        ad={}
        if getattr(self, 'address', None):
            if self.address[0].zip:
                ad['zip']=self.address[0].zip.value
            if self.address[0].country:
                ad['country']=self.address[0].country.value
            if self.address[0].state:
                ad['state']=self.address[0].state.value
            if self.address[0].city:
                ad['city']=self.address[0].city.value
            if self.address[0].line:
                ad['street']=[]
                for x in self.address[0].line[0].value.split():
                    try:
                        m=int(x)
                        ad['number']=m
                    except ValueError:
                        ad['street'].append(x)
                ad['street']=' '.join(ad['street'])
            return ad

    def __set_active(self):
        self.set_active(supermod.boolean(value='true'))

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
            data = supermod.base64Binary(value=base64.encodestring(self.gnu_patient.photo))
            im = supermod.Attachment(data=data)
            self.add_photo(im)

    def __get_photo(self):
        # Python 2 and Python 3 have bytes and string/bytes .... issues
        #  Need to talk about this more with tryton storage
        import base64
        if getattr(self,'photo', None):
            return base64.decodestring(self.photo[0].data.value)

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
                code = supermod.code(value=status)
                display = supermod.string(value=statuses[status])
            else:
                code = supermod.code(value='OTH')
                display = supermod.string(value='other')
            coding = supermod.Coding(
                        system=supermod.uri(value='http://hl7.org/fhir/v3/MaritalStatus'),
                        code=code,
                        display=display
                        )
            marital_status=supermod.CodeableConcept(coding=[coding])
            self.set_maritalStatus(marital_status)

    def __get_marital_status(self):
        # TODO: Discuss categories
        if getattr(self,'maritalStatus', None):
            t=self.maritalStatus.coding[0].code.value.lower()
            if t in ['m', 'w', 'd', 's']:
                return t

    def export_to_xml_string(self):
        output = StringIO()
        self.export(outfile=output, pretty_print=False, level=4)
        content = output.getvalue()
        output.close()
        return content

    def export_to_json_string(self):
        #TODO More difficult
        pass
supermod.Patient.subclass=gnu_patient

def get_root_tag(node):
    tag = supermod.Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = supermod.GDSClassesMapping.get(tag)
    if rootClass is None and hasattr(supermod, tag):
        rootClass = getattr(supermod, tag)
    return tag, rootClass

def parse(inFileName, silence=False):
    doc = supermod.parsexml_(inFileName)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Element'
        rootClass = supermod.Element
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='',
            pretty_print=True)
    return rootObj
