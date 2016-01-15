from StringIO import StringIO
from operator import attrgetter
from .datastore import find_record
import server.fhir as supermod
from server.common import safe_attrgetter
from .health_mixin import ExportXMLMixin

# URL values
try:
    from flask import url_for
    RUN_FLASK=True
except:
    from .datastore import dumb_url_generate
    RUN_FLASK=False

class Immunization_Map:
    """Holds essential mappings and information for
        the Immunization class
    """

    root_search=[]

    resource_search_params={
            '_id': 'token',
            'date': 'date',
            'lot-number': 'string',
            'dose-sequence': 'number',
            'performer': 'reference',
            'vaccine-type': 'token',
            'subject': 'reference',
            '_language': None,
            'identifier': None,
            'location': None,
            'manufacturer': None,
            'reaction': None,
            'reaction-date': None,
            'reason': None,
            'refusal-reason': None,
            'refused': None,
            'requester': None}

    chain_map={ 'subject': 'Patient',
            'performer': 'Practitioner',
            'requester': 'Practitioner'}
            #'reaction': 'Observation', #TODO AdverseReaction
            #'location': 'Location', #TODO
            #'manufacturer': 'Organization'} #TODO

    search_mapping={
            '_id': ['id'],
            'date': ['date'],
            'subject': ['name'],
            'lot-number': ['lot.number'],
            'dose-sequence': ['dose'],
            'performer': ['healthprof'],
            'vaccine-type': ['vaccine.name.code'],
            'vaccine-type:text': ['vaccine.name.name']
        }

    url_prefixes={}
    model_mapping={'gnuhealth.vaccination':
            {
                'date': 'date',
                'expirationDate': 'lot.expiration_date',
                'lotNumber': 'lot.number',
                'performer': 'healthprof',
                'subject': 'name',
                'doseQuantity': 'amount',
                'site': 'admin_site',
                'route': 'admin_route',
                'vaccine-type': 'vaccine'
            }}


class health_Immunization(supermod.Immunization, Immunization_Map, ExportXMLMixin):

    def __init__(self, *args, **kwargs):
        rec = kwargs.pop('gnu_record', None)
        super(health_Immunization, self).__init__(*args, **kwargs)
        if rec:
            self.set_gnu_immunization(rec)

    def set_gnu_immunization(self, immunization):
        """Set immunization"""

        self.immunization = immunization
        self.model_type = self.immunization.__name__

        # Only certain models
        if self.model_type not in self.model_mapping:
            raise ValueError('Not a valid model')

        self.map = self.model_mapping[self.model_type]

        self.__import_from_gnu_immunization()
        self.__set_feed_info()

    def __import_from_gnu_immunization(self):
        """Import the data from the Health model"""

        if self.immunization:
            self.set_date(safe_attrgetter(self.immunization,
                    self.map['date']))
            self.set_expirationDate(safe_attrgetter(self.immunization,
                    self.map['expirationDate']))
            self.set_subject(safe_attrgetter(self.immunization,
                    self.map['subject']))
            self.set_performer(safe_attrgetter(self.immunization,
                    self.map['performer']))
            self.set_lotNumber(safe_attrgetter(self.immunization,
                    self.map['lotNumber']))
            self.set_doseQuantity(safe_attrgetter(self.immunization,
                    self.map['doseQuantity']))
            self.set_route(safe_attrgetter(self.immunization,
                    self.map['route']))
            self.set_site(safe_attrgetter(self.immunization,
                    self.map['site']))
            self.set_vaccineType(safe_attrgetter(self.immunization,
                    self.map['vaccine-type']))
            self.set_reported(reported=False)
            self.set_refusedIndicator(refusedIndicator=False)

    def __set_feed_info(self):
        """Set the feed-relevant data"""

        if self.immunization:
            if RUN_FLASK:
                uri = url_for('im_record',
                            log_id=self.immunization.id,
                            _external=True)
            else:
                uri = dumb_url_generate(['Immunization', self.immunization.id])
            self.feed={'id': uri,
                        'published': self.immunization.create_date,
                        'updated': self.immunization.write_date or \
                                self.immunization.create_date,
                        'title': '{} for {}'.format(
                            self.immunization.vaccine.name.name,
                            self.immunization.name.rec_name)
                        }

    def set_date(self, date):
        """Extends superclass for convenience

        Keyword arguments:
        date -- date (datetime object)
        """

        if date is not None:
            d = supermod.dateTime(value=date.strftime("%Y/%m/%d"))
            super(health_Immunization, self).set_date(d)

    def set_subject(self, subject):
        """Extends superclass for convenience

        Keyword arguments:
        subject -- patient (Health model)
        """

        if subject:
            if RUN_FLASK:
                uri = url_for('pat_record', log_id=subject.id)
            else:
                uri = dumb_url_generate(['Patient', subject.id])
            display = subject.rec_name
            ref=supermod.ResourceReference()
            ref.display = supermod.string(value=display)
            ref.reference = supermod.string(value=uri)
            super(health_Immunization, self).set_subject(ref)

    def set_performer(self, performer):
        """Extends superclass for convenience

        Keyword arguments:
        performer -- practitioner (Health model)
        """

        if performer:
            if RUN_FLASK:
                uri = url_for('hp_record', log_id=performer.id)
            else:
                uri = dumb_url_generate(['Practitioner', performer.id])
            display = performer.rec_name
            ref=supermod.ResourceReference()
            ref.display = supermod.string(value=display)
            ref.reference = supermod.string(value=uri)
            super(health_Immunization, self).set_performer(ref)

    def set_lotNumber(self, lotNumber):
        """Extends superclass for convenience

        Keyword arguments:
        lotNumber -- lot id (string, number, etc.)
        """

        if lotNumber is not None:
            s = supermod.string(value=str(lotNumber))
            super(health_Immunization, self).set_lotNumber(s)

    def set_expirationDate(self, expirationDate):
        """Extends superclass for convenince

        Keyword arguments:
        expirationDate -- date (datetime object)
        """

        if expirationDate is not None:
            d = supermod.date(value=expirationDate.strftime("%Y/%m/%d"))
            super(health_Immunization, self).set_expirationDate(d)

    def set_doseQuantity(self, doseQuantity):
        """Extends superclass for convenience

        Keyword arguments:
        doseQuantity -- amount in mL
        """

        if doseQuantity is not None:
            v = supermod.decimal(value=str(float(doseQuantity)))
            u = supermod.string(value='mL')
            s = supermod.uri(value='http://snomed.info/sct')
            c = supermod.code(value='258773002')
            dq = supermod.Quantity(value=v, units=u, system=s, code=c)
            super(health_Immunization, self).set_doseQuantity(dq)

    def set_refusedIndicator(self, refusedIndicator=False):
        """Extends superclass for convenience

        Keyword argument:
        refusedIndicator -- refused? True/False (default: False)
        """

        b = 'false'
        if refusedIndicator:
            b = 'true'
        ri = supermod.boolean(value=b)
        super(health_Immunization, self).set_refusedIndicator(ri)

    def set_reported(self, reported=False):
        """Extends superclass for convenience

        Keyword argument:
        reported -- self reported? True/False (default: False)
        """

        b = 'false'
        if reported:
            b = 'true'
        r = supermod.boolean(value=b)
        super(health_Immunization, self).set_reported(r)

    def set_route(self, route):
        """Extends superclass for convenience

        Keyword argument:
        route -- how vaccine entered body
        """

        from server.fhir.value_sets import immunizationRoute
        if route:
            ir=[i for i in immunizationRoute.contents if i['code'] == route.upper()]
            if ir:
                cc=supermod.CodeableConcept()
                c = supermod.Coding()
                c.display = cc.text = supermod.string(value=ir[0]['display'])
                c.code = supermod.code(value=ir[0]['code'])
                cc.coding=[c]
                super(health_Immunization, self).set_route(cc)

    def set_site(self, site):
        """Extends superclass for convenience

        Keyword arguments:
        site -- site code where the vaccine was administered
        """

        from server.fhir.value_sets import immunizationSite
        if site:
            m=[i for i in immunizationSite.contents if i['code'] == site.upper()]
            if m:
                cc=supermod.CodeableConcept()
                c = supermod.Coding()
                c.display = cc.text = supermod.string(value=m[0]['display'])
                c.code = supermod.code(value=m[0]['code'])
                cc.coding=[c]
                super(health_Immunization, self).set_site(cc)

    def set_vaccineType(self, vaccineType):
        """Extends superclass for convenience

        Keyword arguments:
        vaccineType -- the vaccine (Health model)
        """
        #TODO Need better coding, much better!

        if vaccineType:
            cc = supermod.CodeableConcept()
            c = supermod.Coding()
            c.display = cc.text = supermod.string(value=vaccineType.name.name)
            if vaccineType.name.code:
                c.code = supermod.code(value=vaccineType.name.code)
                cc.coding=[c]
            super(health_Immunization, self).set_vaccineType(cc)

supermod.Immunization.subclass=health_Immunization
