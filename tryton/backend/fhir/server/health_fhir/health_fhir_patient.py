from flask import current_app
from StringIO import StringIO
from datetime import datetime
import fhir as supermod
import sys


#TODO: Use and add to parent methods
#TODO: Have standard None/True/False checks and conventions


class health_Patient(supermod.Patient):
    '''Mediate between XML/JSON schema bindings and
        the GNU Health models for Patient resource
    '''

    def set_gnu_patient(self, gnu):
        self.gnu_patient = gnu #gnu health model

    def import_from_gnu_patient(self):
        '''Get info from gnu model and set it'''
        if self.gnu_patient and getattr(self.gnu_patient, 'name', None):
            self.__set_identifier()
            self.__set_name()
            self.__set_telecom()
            self.__set_gender()
            self.__set_birthdate()
            self.__set_deceased_status()
            self.__set_deceased_datetime()
            self.__set_address()
            self.__set_marital_status()
            self.__set_photo()
            self.__set_communication()
            self.__set_contact()
            self.__set_care_provider()
            self.__set_managing_organization()
            self.__set_link()
            self.__set_active()

    def get_gnu_patient(self):
        '''Return dicts for models'''
        telecom=self.__get_telecom()
        address=self.__get_address()
        com=self.__get_communication()
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
                        'alias': self.__get_alias()}
        if telecom:
            ex['contact_mechanism']=[
                        {'type': 'phone', 'value': telecom.get('phone')},
                        {'type': 'mobile', 'value': telecom.get('mobile')},
                        {'type': 'email', 'value': telecom.get('email')}]
        ex['patient']={
                          'deceased': self.__get_deceased_status(),
                          'dod': self.__get_deceased_datetime()
                      }
        if address:
            ex['du']={
                        #TODO Name needs to be unique
                        'name': ''.join([str(x) for x in [address['city'],
                                                            address['street'],
                                                            address['number']] if x is not None]),
                        'address_zip': address.get('zip'),
                        'address_street': address.get('street'),
                        'address_street_number': address.get('number'),
                        'address_city': address.get('city')
                        }
        ex['lang']={
                    'code': com.get('code'),
                    'name': com.get('name')
                    }
                #TODO
                    #'address_country'
                    #'address_subdivision'
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
        #   REMEMBER: Middle names are defined as given names
        name = []
        family=[]
        given=[supermod.string(value=x) for x in self.gnu_patient.name.name.split()]
        if getattr(self.gnu_patient, 'lastname', None):
            after_names=[supermod.string(value=x) for x in self.gnu_patient.lastname.split()]
            if len(after_names) > 1:
                family=after_names[-1:]
                given.extend(after_names[:-1])
            else:
                family=after_names
        name.append(supermod.HumanName(
                    use=supermod.NameUse(value='usual'),
                    family=family,
                    given=given))


        if getattr(self.gnu_patient.name, 'alias', None):
            name.append(supermodHumanName(
                        use=supermod.NameUse(value='nickname'),
                        given=[supermod.string(value=self.gnu_patient.name.alias)]))
        for x in name:
            self.add_name(x)

    def __get_alias(self):
        if getattr(self, 'name', None):
            if getattr(self.name[0].use, 'value') == 'nickname':
                try:
                    return self.name[0].given[0].value
                except:
                    return None

    def __get_lastname(self):
        if getattr(self, 'name', None):
            middles=[]
            if len(self.name[0].given) > 1:
                middles=self.name[0].given[1:]
            if getattr(self.name[0].use, 'value') in ('usual', 'official'):
                lasts=self.name[0].family
                return ' '.join([m.value for m in middles+lasts])

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
                if getattr(c.system, 'value', None) == 'phone':
                    if c.use.value in ('home', 'work', 'temp'):
                        if c.value:
                            tc['phone']=c.value.value
                    elif c.use.value == 'mobile':
                        if c.value:
                            tc['mobile']=c.value.value
                    else:
                        pass
                elif getattr(c.system, 'value', None) == 'email':
                        if c.value:
                            tc['email']=c.value.value
                else:
                    pass
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
            line=[]
            if getattr(self.gnu_patient.name.du, 'address_street_number', None):
                line.append(str(self.gnu_patient.name.du.address_street_number))
            if getattr(self.gnu_patient.name.du, 'address_street', None):
                line.append(self.gnu_patient.name.du.address_street)
            if getattr(self.gnu_patient.name.du, 'address_city', None):
                address.set_city(supermod.string(value=self.gnu_patient.name.du.address_city))
            if getattr(self.gnu_patient.name.du.address_subdivision, 'name', None):
                address.set_state(supermod.string(value=self.gnu_patient.name.du.address_subdivision.name))
            if getattr(self.gnu_patient.name.du, 'address_zip', None):
                address.set_zip(supermod.string(value=self.gnu_patient.name.du.address_zip))
            if getattr(self.gnu_patient.name.du.address_country, 'name', None):
                address.set_country(supermod.string(value=self.gnu_patient.name.du.address_country.name))
            if line:
                address.add_line(supermod.string(value=' '.join(line)))
            self.add_address(address)

    def __get_address(self):
        ad={}
        try:
            ad['zip']=self.address[0].zip.value
        except:
            pass

        try:
            ad['country']=self.address[0].country.value
        except:
            pass

        try:
            ad['state']=self.address[0].state.value
        except:
            pass

        try:
            ad['city']=self.address[0].city.value
        except:
            pass

        try:
            line=self.address[0].line[0].value.split()
            if not line:
                raise AttributeError
        except:
            pass
        else:
            ad['street']=[]
            for x in line:
                try:
                    #Apt numbers?
                    ad['number']=int(x)
                except ValueError:
                    ad['street'].append(x)
            ad['street']=' '.join(ad['street']) or None
        return ad

    def __set_active(self):
        self.set_active(supermod.boolean(value='true'))

    def __set_contact(self):
        pass

    def __set_care_provider(self):
        #primary care doctor
        if getattr(self.gnu_patient, 'primary_care_doctor', None):
            pass

    def __set_managing_organization(self):
        pass

    def __set_communication(self):
        if getattr(self.gnu_patient.name, 'lang', None):
            from re import sub
            code=sub('_','-', self.gnu_patient.name.lang.code)
            name=self.gnu_patient.name.lang.name
            coding = supermod.Coding(
                        system=supermod.uri(value='urn:ietf:bcp:47'),
                        code=supermod.code(value=code),
                        display=supermod.string(value=name)
                        )
            com=supermod.CodeableConcept(coding=[coding],
                                    text=supermod.string(value=name))
            self.add_communication(com)

    def __get_communication(self):
        #TODO Discuss how to handle multiple languages,
        # and close matches, etc.
        lang={}
        if getattr(self, 'communication', None):
            try:
                lang['code']=self.communication[0].coding[0].code.value
            except AttributeError:
                lang['code']=None
            try:
                lang['name']=self.communication[0].coding[0].display.value
            except AttributeError:
                lang['name']=None
        return lang


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
        try:
            return base64.decodestring(self.photo[0].data.value)
        except:
            return None

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
        try:
            t=self.maritalStatus.coding[0].code.value.lower()
            if t in ['m', 'w', 'd', 's']:
                return t
        except:
            return None

    def __set_link(self):
        pass

    def export_to_xml_string(self):
        output = StringIO()
        self.export(outfile=output, namespacedef_='xmlns="http://hl7.org/fhir"', pretty_print=False, level=4)
        content = output.getvalue()
        output.close()
        return content

    def export_to_json_string(self):
        #TODO More difficult
        pass
supermod.Patient.subclass=health_Patient
