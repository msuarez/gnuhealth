from StringIO import StringIO
from operator import attrgetter
from .datastore import find_record
from server.common import safe_attrgetter
from .health_mixin import ExportXMLMixin
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
                'nickname': 'name.alias',
                'name': 'name'}}

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

class health_Practitioner(supermod.Practitioner, Practitioner_Map, ExportXMLMixin):
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
        self.__set_feed_info()

    def __import_from_gnu_practitioner(self):
        """Set data from model"""
        if self.practitioner:
            self.set_specialty(safe_attrgetter(self.practitioner, self.map['specialty']))
            self.set_role(safe_attrgetter(self.practitioner, self.map['role']))
            self.set_communication(safe_attrgetter(self.practitioner, self.map['communication']))
            self.set_gender(safe_attrgetter(self.practitioner, self.map['gender']))
            self.set_name(safe_attrgetter(self.practitioner, self.map['name']))
            self.set_identifier(safe_attrgetter(self.practitioner, self.map['identifier']))

    def __set_feed_info(self):
        """Set the feed-relevant data"""
        if self.practitioner:
            if RUN_FLASK:
                uri = url_for('hp_record',
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

    def set_name(self, name):
        """Extends superclass for convenience

        Keyword arguments:
        name -- patient party model (Health model)
        """

        if name:
            family=[]
            full_given_name = name.name
            full_family_name = name.lastname
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

            super(health_Practitioner, self).set_name(name)

    def set_identifier(self, identifier):
        """Extends superclass for convenience

        Keyword arguments:
        identifier -- puid
        """

        if identifier:
            ident = supermod.Identifier(
                        use=supermod.IdentifierUse(value='usual'),
                        label=supermod.string(value='PUID'),
                        value=supermod.string(value=identifier))
            super(health_Practitioner, self).add_identifier(ident)


    def set_gender(self, gender):
        """Extends superclass for convenience

        Keyword arguments:
        gender -- practitioner's gender
        """

        if gender:
            from server.fhir.value_sets import administrativeGender as codes
            us = gender.upper()
            sd = [x for x in codes.contents if x['code'] == us][0]
            coding = supermod.Coding(
                        system=supermod.uri(value=sd['system']),
                        code=supermod.code(value=sd['code']),
                        display=supermod.string(value=sd['display'])
                        )
            g=supermod.CodeableConcept(coding=[coding])
            super(health_Practitioner, self).set_gender(g)

    def set_communication(self, communication):
        """Extends superclass for convenience

        Keyword arguments:
        communication -- language
        """

        if communication:
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
            super(health_Practitioner, self).add_communication(com)

    def set_specialty(self, specialty):
        """Extends superclass for convenience

        Keyword arguments
        specialty -- person's specialties
        """

        for spec in  specialty:
            code, name = attrgetter('specialty.code', 'specialty.name')(spec)
            coding = supermod.Coding(code=supermod.string(value=code),
                    display=supermod.string(value=name))
            com=supermod.CodeableConcept(coding=[coding])
            super(health_Practitioner, self).add_specialty(com)

    def set_role(self, role):
        """Extends superclass for convenience

        Keyword arguments:
        role -- occupation name
        """

        if role:
            coding = supermod.Coding(display=supermod.string(value=str(role)))
            com=supermod.CodeableConcept(coding=[coding])
            super(health_Practitioner, self).set_role([com])

supermod.Practitioner.subclass=health_Practitioner
