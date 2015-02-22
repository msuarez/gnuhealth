from StringIO import StringIO
from operator import attrgetter
from .datastore import find_record
import server.fhir as supermod
import sys

try:
    from flask import current_app, url_for
    RUN_FLASK=True
except:
    from .datastore import dumb_url_generate
    RUN_FLASK=False

class Practitioner_Map:

    #No requirements yet
    root_search=[]

    #Just use row id
    url_prefixes={}
            #'gnuhealth.healthprofessional': ''}

    model_mapping={
            'gnuhealth.healthprofessional': {
                'communication': 'name.lang',
                'specialty': 'specialties',
                'role': 'name.occupation.name',
                'gender': 'name.sex',
                'identifier': 'name.puid',
                'given': 'name.name',
                'family': 'name.lastname',
                'nickname': 'name.alias'}}
    resource_search_params={
                    '_id': 'token',
                    '_language': None,
                    'address': None,
                    'family': 'string',
                    'gender': 'token',
                    'given': 'string',
                    'identifier': 'token',
                    'name': 'string',
                    'organization': None,
                    'phonetic': None,
                    'telecom': None}
    search_mapping={
                '_id': ['id'],
                    'family': ['name.lastname'],
                    'gender': ['name.sex'],
                    'given': ['name.name'],
                    'identifier': ['name.puid'],
                    'name': ['name.lastname', 'name.name']}

class health_Practitioner(supermod.Practitioner, Practitioner_Map):
    def __init__(self, *args, **kwargs):
        rec = kwargs.pop('gnu_record', None)
        super(health_Practitioner, self).__init__(*args, **kwargs)
        if rec:
            self.set_gnu_practitioner(rec)

    def set_gnu_practitioner(self, practitioner):
        """Set the GNU Health record
        ::::
            params:
                practitioner ===> Health model
            returns:
                instance
        """
        self.practitioner = practitioner
        self.model_type = self.practitioner.__name__

        # Only certain models
        if self.model_type not in self.model_mapping:
            raise ValueError('Not a valid model')

        self.map = self.model_mapping[self.model_type]
        #self.search_prefix=self.url_prefixes[self.model_type]

        self.__import_from_gnu_practitioner()

    def __import_from_gnu_practitioner(self):
        if self.practitioner:
            self.__set_gnu_specialty()
            self.__set_gnu_communication()
            self.__set_gnu_identifier()
            self.__set_gnu_gender()
            self.__set_gnu_name()
            self.__set_gnu_role()
            self.__set_feed_info()

    def __set_feed_info(self):
        ''' Sets the feed-relevant info
        '''
        if self.practitioner:
            if RUN_FLASK:
                uri = url_for('pat_record',
                                log_id=self.practitioner.id,
                                _external=True)
            else:
                uri = dumb_url_generate(['Practitioner',
                                self.practitioner.id])
            self.feed={'id': uri,
                    'published': self.practitioner.name.create_date,
                    'updated': self.practitioner.name.write_date or self.practitioner.name.create_date,
                    'title': self.practitioner.name.rec_name
                        }

    def __set_gnu_name(self):
        try:
            family=[]
            full_given_name = attrgetter(self.map['given'])(self.practitioner)
            full_family_name = attrgetter(self.map['family'])(self.practitioner)
            given=[supermod.string(value=x) for x in full_given_name.split()]
            after_names=[supermod.string(value=x) for x in full_family_name.split()]
            if len(after_names) > 1:
                family=after_names[-1:]
                given.extend(after_names[:-1])
            else:
                family=after_names
            name=supermod.HumanName(
                        use=supermod.NameUse(value='usual'),
                        family=family,
                        given=given)

            self.set_name(name)
        except:
            pass

    def __set_gnu_identifier(self):
        try:
            puid = attrgetter(self.map['identifier'])(self.practitioner)
            ident = supermod.Identifier(
                        use=supermod.IdentifierUse(value='usual'),
                        label=supermod.string(value='PUID'),
                        #system=supermod.uri(value='gnuhealth::0'),
                                #value=current_app.config.get(
                                    #'INSTITUTION_ODI', None)),
                        value=supermod.string(value=puid))
            self.add_identifier(value=ident)

        except:
            pass
            #if getattr(self.practitioner.name, 'alternative_identification', None):
                #ident = supermod.Identifier(
                            #use=supermod.IdentifierUse(value='usual'),
                            #label=supermod.string(value='ALTERNATE_ID'),
                            #system=supermod.system(
                                #supermod.uri(
                                    #value=current_app.config.get(
                                        #'INSTITUTION_ODI',None))),
                            #value=supermod.string(
                                #value=self.practitioner.name.alternative_identification))
                #self.add_identifier(value=ident)

    def __set_gnu_gender(self):
        try:
            from server.fhir.value_sets import administrativeGender as gender
            us = attrgetter(self.map['gender'])(self.practitioner).upper()
            sd = [x for x in gender.contents if x['code'] == us][0]
            coding = supermod.Coding(
                        system=supermod.uri(value=sd['system']),
                        code=supermod.code(value=sd['code']),
                        display=supermod.string(value=sd['display'])
                        )
            g=supermod.CodeableConcept(coding=[coding])
            self.set_gender(g)
        except:
            pass

    def __set_gnu_communication(self):
        try:
            communication=attrgetter(self.map['communication'])(self.practitioner)
            from re import sub
            code=sub('_','-', communication.code)
            name=communication.name
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

    def __set_gnu_specialty(self):
        try:
            for spec in attrgetter(self.map['specialty'])(self.practitioner):
                code, name = attrgetter('specialty.code', 'specialty.name')(spec)
                coding = supermod.Coding(code=supermod.string(value=code),
                        display=supermod.string(value=name))
                com=supermod.CodeableConcept(coding=[coding])
                self.add_specialty(com)
        except:
            pass

    def __set_gnu_role(self):
        try:
            name=attrgetter(self.map['role'])(self.practitioner)
            coding = supermod.Coding(display=supermod.string(value=name))
            com=supermod.CodeableConcept(coding=[coding])
            self.set_role([com])
        except:
            pass

    def export_to_xml_string(self):
        output = StringIO()
        self.export(outfile=output, namespacedef_='xmlns="http://hl7.org/fhir"', pretty_print=False, level=4)
        content = output.getvalue()
        output.close()
        return content

supermod.Practitioner.subclass=health_Practitioner
