from operator import attrgetter
from StringIO import StringIO
from datetime import datetime
from .datastore import find_record
import server.fhir as supermod
from .health_mixin import ExportXMLMixin
from server.common import get_address, safe_attrgetter
import sys

try:
    from flask import current_app, url_for
    RUN_FLASK=True
except:
    from .datastore import dumb_url_generate
    RUN_FLASK=False

class Patient_Map:
    model_mapping={
            'gnuhealth.patient': {
                'active': 'name.active',
                'birthDate': 'name.dob',
                'identifier': 'puid',
                'alternative': 'name.alternative_ids',
                'gender': 'name.sex',
                'contacts': 'name.contact_mechanisms',
                'photo': 'photo',
                'phone': 'name.phone',
                'email': 'name.email',
                'mobile': 'name.mobile',
                'given': 'name.name',
                'family': 'name.lastname',
                'nickname': 'name.alias',
                'maritalStatus': 'name.marital_status',
                'careProvider': 'primary_care_doctor',
                'communication': 'name.lang',
                'deceased': 'deceased',
                'deceasedDateTime': 'dod',
                'address': 'name.du',
                }}
    # No requierements (as of yet)
    root_search = []

    # Use row id
    url_prefixes={}

    resource_search_params={
                '_id': 'token',
                '_language': None,
                'active': None,
                'address': None,
                'animal-breed': None,
                'animal-species': None,
                'birthdate': 'date',
                'family': 'string',
                'gender': 'token',
                'given': 'string',
                'identifier': 'token',
                'language': 'token',
                'link': None,
                'name': 'string',
                'phonetic': None,
                'provider': None,
                'telecom': None}
    search_mapping={
                '_id': ['id'],
                #'address': ['name.du'] #TODO Add searcher
                #'active': ['name.active'], #FIX boolean conversion
                'birthdate': ['name.dob'],
                'family': ['name.lastname'],
                'gender': ['name.sex'],
                'given': ['name.name'],
                'identifier': ['puid'],
                'language': ['name.lang.code'],
                'language:text': ['name.lang.rec_name'],
                #'telecom': ['name.email', 'name.phone', 'name.mobile'], #FIX no searcher
                'name': ['name.lastname', 'name.name']}

class health_Patient(supermod.Patient, Patient_Map, ExportXMLMixin):
    """ Mediate between the FHIR standard and
        the GNU Health models relavant for the
        Patient resource
    """

    def __init__(self, *args, **kwargs):
        gnu=kwargs.pop('gnu_record', None)
        super(health_Patient, self).__init__(*args, **kwargs)
        if gnu:
            self.set_gnu_patient(gnu)

    def set_gnu_patient(self, gnu):
        """Set gnu patient record"""
        if gnu:
            self.patient = gnu #gnu health model
            if self.patient.__name__ not in self.model_mapping:
                raise ValueError('Not a valid model')

            self.map_ = self.model_mapping[self.patient.__name__]
            self.__import_from_gnu_patient()
            self.__set_feed_info()

    def __import_from_gnu_patient(self):
        """Set data from the Patient model"""
        if self.patient:
            self.set_identifier(
                    safe_attrgetter(
                        self.patient, self.map_['identifier']),
                    safe_attrgetter(
                        self.patient, self.map_['alternative']))
            self.set_name(
                    safe_attrgetter(
                        self.patient, 'name'))
            self.set_telecom(
                    safe_attrgetter(
                        self.patient, self.map_['contacts']))
            self.set_gender(
                    safe_attrgetter(
                        self.patient, self.map_['gender']))
            self.set_birthDate(
                    safe_attrgetter(
                        self.patient, self.map_['birthDate']))
            self.set_deceasedBoolean(
                    safe_attrgetter(
                        self.patient, self.map_['deceased']))
            self.set_deceasedDatetime(
                    safe_attrgetter(
                        self.patient, self.map_['deceasedDateTime']))
            self.set_address(
                    safe_attrgetter(
                        self.patient, self.map_['address']))
            self.set_maritalStatus(
                    safe_attrgetter(
                        self.patient, self.map_['maritalStatus']))
            self.set_photo(
                    safe_attrgetter(
                        self.patient, self.map_['photo']))
            self.set_communication(
                    safe_attrgetter(
                        self.patient, self.map_['communication']))
            self.set_careProvider(
                    safe_attrgetter(
                        self.patient, self.map_['careProvider']))
            self.set_active(
                    safe_attrgetter(
                        self.patient, self.map_['active']))

    def __set_feed_info(self):
        """Set the feed-relevant data"""
        if self.patient:
            if RUN_FLASK:
                uri = url_for('pat_record', log_id=self.patient.id, _external=True)
            else:
                uri = dumb_url_generate(['Patient', self.patient.id])
            self.feed={'id': uri,
                    'published': self.patient.create_date,
                    'updated': self.patient.write_date or self.patient.create_date,
                    'title': self.patient.name.rec_name
                        }

    def set_models(self):
        """Set info for models"""
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

    def set_identifier(self, puid, alternative):
        """Extends superclass for convenience

        Set patient identifiers

        Keyword arguments:
        puid -- the puid/mrn
        alternate -- alternate ids (SSN, etc)
        """

        idents = []
        if puid:
            idents.append(supermod.Identifier(
                        use=supermod.IdentifierUse(value='usual'),
                        label=supermod.string(value='PUID'),
                        value=supermod.string(value=puid)))

        for alt in alternative:
            idents.append(supermod.Identifier(
                        use=supermod.IdentifierUse(value='official'),
                        label=supermod.string(value=alt.alternative_id_type),
                        value=supermod.string(value=alt.code)))

        if idents:
            super(health_Patient, self).set_identifier(idents)

    def __get_identifier(self):
        if self.identifier:
            return self.identifier[0].value.value

    def set_name(self, name):
        """Extends superclass for convenience

        Set patient's name and nickname

        Keyword arguments:
        name -- patient party model
        """

        if name:
            names=[]
            family=[]
            full_given_name = name.name
            full_family_name = name.lastname
            nickname = name.alias
            given=[supermod.string(value=x) for x in full_given_name.split()]
            after_names=[supermod.string(value=x) for x in full_family_name.split()]
            if len(after_names) > 1:
                family=after_names[-1:]
                given.extend(after_names[:-1])
            else:
                family=after_names
            names.append(supermod.HumanName(
                        use=supermod.NameUse(value='usual'),
                        family=family,
                        given=given))
            if nickname:
                names.append(supermod.HumanName(
                            use=supermod.NameUse(value='nickname'),
                            given=[supermod.string(value=nickname)]))

            super(health_Patient, self).set_name(names)

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

    def set_telecom(self, contacts):
        """Extends superclass for convenience

        Set telecom information

        Keyword arguments:
        contacts -- contacts info (Party model)
        """

        telecom = []
        for contact in contacts:
            c=supermod.Contact()
            c.value = supermod.string(value=contact.value)
            if contact.type == 'phone':
                system='phone'
                use='home'
            elif contact.type == 'mobile':
                system='phone'
                use='mobile'
            else:
                use = system = contact.type
            c.system=supermod.ContactSystem(value=system)
            c.use=supermod.ContactUse(value=use)
            telecom.append(c)

        if telecom:
            super(health_Patient, self).set_telecom(telecom)

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

    def set_gender(self, gender):
        """Extends superclass for convenience

        Set patient gender

        Keyword arguments:
        gender -- gender code
        """

        from server.fhir.value_sets import administrativeGender as gender_codes
        if gender:
            us = gender.upper() #Standard requires uppercase
            try:
                sd = [x for x in gender_codes.contents if x['code'] == us][0]
            except:
                return None
            coding = supermod.Coding(
                        system=supermod.uri(value=sd['system']),
                        code=supermod.code(value=sd['code']),
                        display=supermod.string(value=sd['display'])
                        )
            g=supermod.CodeableConcept(coding=[coding])
            super(health_Patient, self).set_gender(g)

    def __get_gender(self):
        if getattr(self, 'gender', None):
            return 'm' if self.gender.coding[0].code.value == 'M' else 'f'

    def set_birthDate(self, birthdate):
        """Extends superclass for convenience

        Set patient's birthdate

        Keyword arguments:
        birthdate -- birthdate datetime object
        """

        if birthdate is not None:
            dob = supermod.dateTime(value=birthdate.strftime("%Y/%m/%d"))
            super(health_Patient, self).set_birthDate(dob)

    def __get_birthdate(self):
        if getattr(self, 'birthDate', None):
            return self.birthDate.value

    def set_deceasedBoolean(self, status=False):
        """Extends superclass for convenience

        Set whether patient is deceased or not

        Keyword arguments:
        status -- deceased status (True or False)
        """

        if status:
            status = 'true'
        else:
            status = 'false'
        b=supermod.boolean(value=status)
        super(health_Patient, self).set_deceasedBoolean(b)

    def __get_deceased_status(self):
        if getattr(self.deceasedBoolean,'value', None) in (None ,'False', 'false'):
            deceased=False
        else:
            deceased=True
        return deceased

    def set_deceasedDatetime(self, dod):
        """Extends superclass for convenience

        Set the deceased date and time

        Keyword arguments:
        dod -- deceased datetime object
        """

        if dod is not None:
            super(health_Patient, self).set_deceasedDateTime(
                        supermod.dateTime(value=dod.strftime("%Y/%m/%d")))


    def __get_deceased_datetime(self):
        if getattr(self, 'deceasedDateTime', None) is not None:
            return self.deceasedDateTime.value

    def set_address(self, address):
        """Extends superclass for convenience

        Set patient's home address

        Keyword arguments:
        address -- domiciliary unit model
        """

        if address:
            ad=supermod.Address()
            ad.set_use(supermod.string(value='home'))
            line=[]
            number, street, zip_, city, state, country = safe_attrgetter(
                                    address,
                                    'address_street_number',
                                    'address_street',
                                    'address_zip',
                                    'address_city',
                                    'address_subdivision.name',
                                    'address_country.name')

            if number:
                line.append(str(number))
            if street:
                line.append(street)
            if line:
                ad.add_line(supermod.string(value=' '.join(line)))

            if city:
                ad.set_city(supermod.string(value=city))

            if state:
                ad.set_state(supermod.string(value=state))

            if zip_:
                ad.set_zip(supermod.string(value=zip_))

            if country:
                ad.set_country(supermod.string(value=country))

            super(health_Patient, self).set_address([ad])

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

    def set_active(self, active=True):
        """Extends superclass for convenience

        Set active status

        Keyword arguments:
        active -- status ('true' or 'false')
        """

        if active:
            active = 'true'
        else:
            active = 'false'
        super(health_Patient, self).set_active(
                supermod.boolean(value=active))

    def __get_contact(self):
        pass

    def __set_gnu_contact(self):
        pass

    def __get_care_provider(self):
        pass

    def set_careProvider(self, care_provider):
        """Extends superclass for convienience

        Set patient's care provider

        Keyword arguments:
        care_provider -- health professional model
        """

        if care_provider:
            if RUN_FLASK:
                uri = url_for('hp_record', log_id=care_provider.id)
            else:
                uri = dumb_url_generate(['Practitioner', care_provider.id])
            display = care_provider.rec_name
            ref=supermod.ResourceReference()
            ref.display = supermod.string(value=display)
            ref.reference = supermod.string(value=uri)
            super(health_Patient, self).set_careProvider([ref])

    def __set_gnu_managing_organization(self):
        pass

    def set_communication(self, communication):
        """Extends superclass for convenience

        Set patient language

        Keyword arguments:
        communication -- the language model
        """

        if communication:
            from re import sub
            code=sub('_','-', communication.code) #Standard requires dashes
            name=communication.name
            coding = supermod.Coding(
                        system=supermod.uri(value='urn:ietf:bcp:47'),
                        code=supermod.code(value=code),
                        display=supermod.string(value=name)
                        )
            com=supermod.CodeableConcept(coding=[coding],
                                    text=supermod.string(value=name))
            super(health_Patient, self).set_communication([com])

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

    def set_photo(self, photo):
        """Extends superclass for convenience

        Set patient photo

        Keyword arguments:
        photo -- photo data
        """

        import base64
        if photo:
            b64 = base64.encodestring(photo) #Standard requires base64
            if b64:
                data = supermod.base64Binary(value=b64)
                im = supermod.Attachment(data=data)
                super(health_Patient, self).set_photo([im])

    def __get_photo(self):
        # Python 2 and Python 3 have bytes and string/bytes .... issues
        #  Need to talk about this more with tryton storage
        import base64
        try:
            return base64.decodestring(self.photo[0].data.value)
        except:
            return None

    def set_maritalStatus(self, marital_status):
        """Extends superclass for convenience

        Set the marital status

        Keyword arguments:
        marital_status --  marital status code
        """

        from server.fhir.value_sets import maritalStatus as ms
        #Health has concubinage and separated, which aren't truly
        # matching to the FHIR defined statuses
        if marital_status:
            us = marital_status.upper() #Codes are uppercase
            fhir_status = [x for x in ms.contents\
                                    if x['code'] == us]
            if fhir_status:
                code = supermod.code(value=fhir_status[0]['code'])
                display = supermod.string(value=fhir_status[0]['display'])
            else:
                code = supermod.code(value='OTH')
                display = supermod.string(value='other')
            coding = supermod.Coding(
                        system=supermod.uri(value='http://hl7.org/fhir/v3/MaritalStatus'),
                        code=code,
                        display=display)
            ms=supermod.CodeableConcept(coding=[coding])
            super(health_Patient, self).set_maritalStatus(ms)

    def __get_marital_status(self):
        try:
            t=self.maritalStatus.coding[0].code.value.lower()
            if t in ['m', 'w', 'd', 's']:
                return t
        except:
            return None

    def __set_gnu_link(self):
        pass

supermod.Patient.subclass=health_Patient
