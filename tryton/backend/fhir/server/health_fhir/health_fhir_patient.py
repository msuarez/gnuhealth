from operator import attrgetter
from StringIO import StringIO
from datetime import datetime
from .datastore import find_record
import server.fhir as supermod
from server.common import get_address

try:
    from flask import current_app, url_for
    RUN_FLASK=True
except:
    from .datastore import dumb_url_generate
    RUN_FLASK=False


class Patient_Map:
    model_mapping={
            'gnuhealth.patient': {
                'birthDate': 'name.dob',
                'identifier': 'puid',
                'gender': 'name.sex',
                'photo': 'photo',
                'phone': 'name.phone',
                'email': 'name.email',
                'mobile': 'name.mobile',
                'given': 'name.name',
                'family': 'name.lastname',
                'nickname': 'name.alias',
                'maritalStatus': 'name.marital_status',
                'careProvider': 'primary_care_doctor',
                'communicationCode': 'name.lang.code',
                'communicationDisplay': 'name.lang.name',
                'deceased': 'deceased',
                'deceasedDateTime': 'dod',
                'addressNumber': 'name.du.address_street_number',
                'addressStreet': 'name.du.address_street',
                'addressZip': 'name.du.address_zip',
                'addressCity': 'name.du.address_city',
                'addressState': 'name.du.address_subdivision.name',
                'addressCountry': 'name.du.address_country.name'
                }}
    url_prefixes={}
    search_mapping={
            'patient':{
                '_id': (['id'], 'token'), 
                '_language': None,
                'active': None,
                'address': None,
                'animal-breed': None,
                'animal-species': None,
                'birthdate': (['name.dob'], 'date'),
                'family': (['name.lastname'], 'string'),
                'gender': (['name.sex'], 'token'),
                'given': (['name.name'], 'string'),
                'identifier': (['puid'], 'token'),
                'language': (['name.lang.code'], 'token'),
                'language:text': (['name.lang.rec_name'], 'string'),
                'link': None,
                'name': (['name.lastname', 'name.name'], 'string'),
                'phonetic': None,
                'provider': None,
                'telecom': None}}


#TODO: Use and add to parent methods
#TODO: Have standard None/True/False checks and conventions
class health_Patient(supermod.Patient, Patient_Map):
    '''Mediate between XML/JSON schema bindings and
        the GNU Health models for Patient resource
    '''

    def __init__(self, *args, **kwargs):
        gnu=kwargs.pop('gnu_record', None)
        super(health_Patient, self).__init__(*args, **kwargs)
        if gnu:
            self.set_gnu_patient(gnu)

    def set_gnu_patient(self, gnu):
        '''Set gnu patient record'''
        if gnu:
            self.patient = gnu #gnu health model
            if self.patient.__name__ not in self.model_mapping:
                raise ValueError('Not a valid model')

            self.map = self.model_mapping[self.patient.__name__]
            self.__import_from_gnu_patient()

    def __import_from_gnu_patient(self):
        '''Get info from gnu model and set it'''
        if self.patient:
            self.__set_gnu_identifier()
            self.__set_gnu_name()
            self.__set_gnu_telecom()
            self.__set_gnu_gender()
            self.__set_gnu_birthdate()
            self.__set_gnu_deceased_status()
            self.__set_gnu_deceased_datetime()
            self.__set_gnu_address()
            self.__set_gnu_marital_status()
            self.__set_gnu_photo()
            self.__set_gnu_communication()
            self.__set_gnu_contact()
            self.__set_gnu_care_provider()
            self.__set_gnu_managing_organization()
            self.__set_gnu_link()
            self.__set_gnu_active()

            self.__set_feed_info()

    def __set_feed_info(self):
        ''' Sets the feed-relevant info
        '''
        if self.patient:
            self.feed={'id': self.patient.id,
                    'published': self.patient.create_date,
                    'updated': self.patient.write_date or self.patient.create_date,
                    'title': self.patient.name.rec_name
                        }

    def set_models(self):
        '''Set info for models'''
        telecom=self.__get_telecom()
        address=self.__get_address()
        com=self.__get_communication()
        self.models = {}
        self.models['party']={'name': self.__get_firstname(),
                        'activation_date': datetime.today().date().isoformat(),
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
            self.models['contact_mechanism']=[
                        {'type': 'phone', 'value': telecom.get('phone')},
                        {'type': 'mobile', 'value': telecom.get('mobile')},
                        {'type': 'email', 'value': telecom.get('email')}]
        self.models['patient']={
                          'deceased': self.__get_deceased_status(),
                          'dod': self.__get_deceased_datetime()
                      }
        if address:
            self.models['du']={
                        #TODO Name needs to be unique
                        'name': ''.join([str(x) for x in [address['city'],
                                                            address['street'],
                                                            address['number']] if x is not None]),
                        'address_zip': address.get('zip'),
                        'address_street': address.get('street'),
                        'address_street_number': address.get('number'),
                        'address_city': address.get('city')
                        }
            self.models['subdivision']=address.get('state')
            self.models['country']=address.get('country')
        self.models['lang']={
                    'code': com.get('code'),
                    'name': com.get('name')
                    }

    def create_patient(self, country, du, lang, patient, party, subdivision, contact):
        '''Create the patient record

            (better structure? better way to import models?)'''

        #Find language (or not!)
        if self.models.get('lang'):
            self.models['party']['lang']=None
            comm = find_record(lang, [['OR', [('code', 'like', '{0}%'.format(self.models['lang'].get('code', None)))],
                                    [('name', 'ilike', '%{0}%'.format(self.models['lang'].get('name', None)))]]])
            if comm:
                self.models['party']['lang']=comm

        #Find du (or not!)
        #TODO Shared addresses (apartments, etc.)
        if self.models.get('du'):
            d = find_record(du, [('name', '=', self.models['du'].get('name', -1))]) # fail better
            if d:
                self.models['party']['du']=d.id
            else:
                #This uses Nominatim to give complete address details
                query = ', '.join([str(v) for k,v in self.models['du'].items() if k in ['address_street_number','address_street','address_city']])
                query = ', '.join([query, self.models['subdivision'] or '', self.models['country'] or ''])
                details = get_address(query)
                if details:
                    pass

                # Find subdivision (or not!)
                if self.models['subdivision']:
                    self.models['du']['address_subdivision']= None
                    s = find_record(subdivision, [['OR', [('code', 'ilike', '%{0}%'.format(self.models['subdivision']))],
                                            [('name', 'ilike', '%{0}%'.format(self.models['subdivision']))]]])
                    if s:
                        self.models['du']['address_subdivision']=s.id
                        self.models['du']['address_country']=s.country.id

                # Find country (or not!)
                if self.models['du'].get('address_country', None):
                    self.models['du']['address_country']=None
                    if self.models['country']:
                        co = find_record(country, [['OR', [('code', 'ilike', '%{0}%'.format(self.models['country']))],
                                            [('name', 'ilike', '%{0}%'.format(self.models['country']))]]])
                        if co:
                            self.models['du']['address_country']=co.id

                d = du.create([self.models['du']])[0]
                self.models['party']['du']=d

        n = party.create([self.models['party']])[0]

        if self.models.get('contact_mechanism'):
            for c in self.models['contact_mechanism']:
                if c['value'] is not None:
                    c['party']=n
                    contact.create([c])

        self.models['patient']['name']=n
        p=patient.create([self.models['patient']])[0]
        return p

    def __set_gnu_identifier(self):
        if getattr(self.patient, 'puid', None):
            ident = supermod.Identifier(
                        use=supermod.IdentifierUse(value='usual'),
                        label=supermod.string(value='PUID'),
                        #system=supermod.uri(value='gnuhealth::0'),
                                #value=current_app.config.get(
                                    #'INSTITUTION_ODI', None)),
                        value=supermod.string(value=self.patient.puid))

        elif getattr(self.patient, 'alternative_identification', None):
            ident = supermod.Identifier(
                        use=supermod.IdentifierUse(value='usual'),
                        label=supermod.string(value='ALTERNATE_ID'),
                        #system=supermod.system(
                            #supermod.uri(
                                #value=current_app.config.get(
                                    #'INSTITUTION_ODI',None))),
                        value=supermod.string(
                            value=self.patient.alternative_identification))
        else:
            return
        self.add_identifier(value=ident)

    def __get_identifier(self):
        if self.identifier:
            return self.identifier[0].value.value

    def __set_gnu_name(self):
        # TODO: Discuss these meanings more
        #   REMEMBER: Middle names are defined as given names
        name = []
        family=[]
        given=[supermod.string(value=x) for x in self.patient.name.name.split()]
        if getattr(self.patient, 'lastname', None):
            after_names=[supermod.string(value=x) for x in self.patient.lastname.split()]
            if len(after_names) > 1:
                family=after_names[-1:]
                given.extend(after_names[:-1])
            else:
                family=after_names
        name.append(supermod.HumanName(
                    use=supermod.NameUse(value='usual'),
                    family=family,
                    given=given))


        if getattr(self.patient.name, 'alias', None):
            name.append(supermodHumanName(
                        use=supermod.NameUse(value='nickname'),
                        given=[supermod.string(value=self.patient.name.alias)]))
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

    def __set_gnu_telecom(self):
        telecom = []
        if getattr(self.patient.name, 'phone', None):
            telecom.append(supermod.Contact(
                    system=supermod.ContactSystem(value='phone'),
                    value=supermod.string(value=self.patient.name.phone),
                    use=supermod.ContactUse(value='home')))
        if getattr(self.patient.name, 'mobile', None):
            telecom.append(supermod.Contact(
                    system=supermod.ContactSystem(value='phone'),
                    value=supermod.string(value=self.patient.name.mobile),
                    use=supermod.ContactUse(value='mobile')))
        if getattr(self.patient.name, 'email', None):
            telecom.append(supermod.Contact(
                    system=supermod.ContactSystem(value='email'),
                    value=supermod.string(value=self.patient.name.email),
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

    def __set_gnu_gender(self):
        try:
            gender = attrgetter(self.map['gender'])(self.patient)
            coding = supermod.Coding(
                        system=supermod.uri(value='http://hl7.org/fhir/v3/AdministrativeGender'),
                        code=supermod.code(value=gender.upper()),
                        display=supermod.string(value='Male' if gender == 'm' else 'Female')
                        )
            gender=supermod.CodeableConcept(coding=[coding])
            self.set_gender(gender)
        except:
            raise ValueError('No gender')

    def __get_gender(self):
        if getattr(self, 'gender', None):
            return 'm' if self.gender.coding[0].code.value == 'M' else 'f'

    def __set_gnu_birthdate(self):
        try:
            dob = attrgetter(self.map['birthDate'])(self.patient)
            if dob:
                self.set_birthDate(supermod.dateTime(value=dob))
        except:
            pass

    def __get_birthdate(self):
        if getattr(self, 'birthDate', None):
            return self.birthDate.value

    def __set_gnu_deceased_status(self):
        try:
            stat = attrgetter(self.map['deceased'])(self.patient)
            if stat:
                status=supermod.boolean(value='true')
            else:
                status=supermod.boolean(value='false')
        except:
            status=supermod.boolean(value='false')
        finally:
            self.set_deceasedBoolean(status)

    def __get_deceased_status(self):
        if getattr(self.deceasedBoolean,'value', None) in (None ,'False', 'false'):
            deceased=False
        else:
            deceased=True
        return deceased

    def __set_gnu_deceased_datetime(self):
        try:
            dod = attrgetter(self.map['deceasedDateTime'])(self.patient)
            if dod:
                self.set_deceasedDateTime(supermod.dateTime(value=str(dod)))
        except:
            pass


    def __get_deceased_datetime(self):
        if getattr(self, 'deceasedDateTime', None) is not None:
            return self.deceasedDateTime.value

    def __set_gnu_address(self):
        #FIX Ugly, but clear
        if self.patient:
            try:
                address=supermod.Address()
                address.set_use(supermod.string(value='home'))
                line=[]
                try:
                    line.append(str(attrgetter(self.map['addressNumber'](self.patient))))
                except:
                    pass

                try:
                    line.append(attrgetter(self.map['addressStreet'])(self.patient))
                except:
                    pass

                try:
                    city = attrgetter(self.map['addressCity'])(self.patient)
                    if city:
                        address.set_city(supermod.string(value=city))
                except:
                    pass

                try:
                    state = attrgetter(self.map['addressState'])(self.patient)
                    if state:
                        address.set_state(supermod.string(value=state))
                except:
                    pass

                try:
                    z = attrgetter(self.map['addressZip'])(self.patient)
                    if z:
                        address.set_zip(supermod.string(value=z))
                except:
                    pass

                try:
                    country = attrgetter(self.map['addressCountry'])(self.patient)
                    if country:
                        address.set_country(supermod.string(value=value))
                except:
                    pass

                if line:
                    address.add_line(supermod.string(value=' '.join(line)))
                self.add_address(address)
            except:
                pass

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

    def __set_gnu_active(self):
        self.set_active(supermod.boolean(value='true'))

    def __get_contact(self):
        pass

    def __set_gnu_contact(self):
        pass

    def __get_care_provider(self):
        pass

    def __set_gnu_care_provider(self):
        try:
            gp = attrgetter(self.map['careProvider'])(self.patient)
            if RUN_FLASK:
                uri = url_for('hp_record', log_id=gp.id)
            else:
                uri = dumb_url_generate(['Practitioner', gp.id])
            display = gp.rec_name
            ref=supermod.ResourceReference()
            ref.display = supermod.string(value=display)
            ref.reference = supermod.string(value=uri)
            self.set_careProvider([ref])
        except:
            pass

    def __set_gnu_managing_organization(self):
        pass

    def __set_gnu_communication(self):
        if self.patient:
            from re import sub
            try:
                code=sub('_','-', \
                        attrgetter(self.map['communicationCode'])(self.patient))
                name=attrgetter(self.map['communicationDisplay'])(self.patient)
                coding = supermod.Coding(
                            system=supermod.uri(value='urn:ietf:bcp:47'),
                            code=supermod.code(value=code),
                            display=supermod.string(value=name)
                            )
                com=supermod.CodeableConcept(coding=[coding],
                                        text=supermod.string(value=name))
                self.add_communication(com)
            except:
                pass

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

    def __set_gnu_photo(self):
        import base64
        if self.patient:
            try:
                b64 = base64.encodestring(attrgetter(self.map['photo'])(self.patient))
                if b64:
                    data = supermod.base64Binary(value=b64)
                    im = supermod.Attachment(data=data)
                    self.add_photo(im)
            except:
                pass

    def __get_photo(self):
        # Python 2 and Python 3 have bytes and string/bytes .... issues
        #  Need to talk about this more with tryton storage
        import base64
        try:
            return base64.decodestring(self.photo[0].data.value)
        except:
            return None

    def __set_gnu_marital_status(self):
        if self.patient:
            try:
                #Health has concubinage and separated, which aren't truly
                # matching to the FHIR defined statuses
                status = attrgetter(self.map['maritalStatus'])(self.patient).upper()
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
            except:
                pass

    def __get_marital_status(self):
        # TODO: Discuss categories
        try:
            t=self.maritalStatus.coding[0].code.value.lower()
            if t in ['m', 'w', 'd', 's']:
                return t
        except:
            return None

    def __set_gnu_link(self):
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
