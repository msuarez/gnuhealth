from StringIO import StringIO
from operator import attrgetter
import server.fhir as supermod
from .health_mixin import ExportXMLMixin
from server.common import safe_attrgetter

try:
    from flask import url_for
    RUN_FLASK=True
except:
    from .datastore import dumb_url_generate
    RUN_FLASK=False

class Condition_Map:
    """Holds essential mappings and information for
        the Condition class
    """
    root_search=[]
    url_prefixes={}
    resource_search_params={
            '_id': 'token',
            'subject': 'reference',
            'severity': 'token',
            'date-asserted': 'date',
            'code': 'token',
            '_language': None,
            'status': None,
            'stage': None,
            'related-item': None,
            'related-code': None,
            'onset': None,
            'location': None,
            'evidence': None,
            'encounter': None,
            'category': None}
    chain_map={'subject': 'Patient'}
    search_mapping={
            '_id': ['id'],
            'subject': ['name'],
            'asserter': ['healthprof'],
            'date-asserted': ['diagnosed_date'],
            'severity': ['disease_severity'],
            'code': ['pathology.code'],
            'code:text': ['pathology.name']}

    model_mapping={'gnuhealth.patient.disease':
            {
                'subject': 'name',
                'notes': 'short_comment',
                'asserter': 'healthprof',
                'dateAsserted': 'diagnosed_date',
                'severity': 'disease_severity',
                'abatementDate': 'healed_date',
                'code': 'pathology'
            }}

class health_Condition(supermod.Condition, Condition_Map, ExportXMLMixin):
    """Extends the FHIR condition class

    Handles parsing, getting, and setting values between
    a Health model and FHIR condition class
    """
    def __init__(self, *args, **kwargs):
        rec = kwargs.pop('gnu_record', None)
        super(health_Condition, self).__init__(*args, **kwargs)
        if rec:
            self.set_gnu_condition(rec)

    def set_gnu_condition(self, condition):
        """Set the GNU Health record

        Keywoard arguments:
        condition -- Health model
        """
        self.condition = condition
        self.model_type = self.condition.__name__

        # Only certain models
        if self.model_type not in self.model_mapping:
            raise ValueError('Not a valid model')

        self.map = self.model_mapping[self.model_type]

        self.__import_from_gnu_condition()
        self.__set_feed_info()

    def __import_from_gnu_condition(self):
        """Sets the data from the model"""
        if self.condition:
            self.set_code(safe_attrgetter(self.condition, self.map['code']))
            self.set_subject(safe_attrgetter(self.condition, self.map['subject']))
            self.set_asserter(safe_attrgetter(self.condition, self.map['asserter']))
            self.set_dateAsserted(safe_attrgetter(self.condition, self.map['dateAsserted']))
            self.set_notes(safe_attrgetter(self.condition, self.map['notes']))
            self.set_abatement(safe_attrgetter(self.condition, self.map['abatementDate']))
            self.set_severity(safe_attrgetter(self.condition, self.map['severity']))
            self.set_status('confirmed')


    def __set_feed_info(self):
        """Sets the feed-relevant info"""
        if self.condition:
            if RUN_FLASK:
                uri = url_for('co_record',
                                log_id=self.condition.id,
                                _external=True)
            else:
                uri = dumb_url_generate(['Condition', self.condition.id])
            self.feed={'id': uri,
                    'published': self.condition.create_date,
                    'updated': self.condition.write_date or self.condition.create_date,
                    'title': attrgetter('pathology.name')(self.condition)
                        }

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
            super(health_Condition, self).set_subject(ref)

    def set_asserter(self, asserter):
        """Extends superclass for convenience

        Keyword arguments:
        asserter -- the practitioner (Health model)
        """

        if asserter:
            if RUN_FLASK:
                uri = url_for('hp_record', log_id=asserter.id)
            else:
                uri = dumb_url_generate(['Practitioner', asserter.id])
            display = asserter.rec_name
            ref=supermod.ResourceReference()
            ref.display = supermod.string(value=display)
            ref.reference = supermod.string(value=uri)
            super(health_Condition, self).set_asserter(ref)

    def set_dateAsserted(self, dateAsserted):
        """Extends superclass for convenience

        Keyword arguments:
        dateAsserted -- the date (datetime object)
        """

        if dateAsserted is not None:
            d=supermod.date(value=dateAsserted.strftime('%Y/%m/%d'))
            super(health_Condition, self).set_dateAsserted(d)

    def set_notes(self, notes):
        """Extends superclass for convenience

        Keyword arguments:
        notes -- notes to add
        """

        if notes:
            n = supermod.string(value=str(s))
            super(health_Condition, self).set_notes(n)

    def set_abatement(self, abatementDate):
        """Extends superclass for convenience

        Keyword arguments:
        abatementDate -- the date (datetime object)
        """

        if abatementDate is not None:
            d = supermod.date(value=d.strftime('%Y/%m/%d'))
            super(health_Condition, self).set_abatementDate(d)

    def set_status(self, status='confirmed'):
        """Extends superclass for convenience

        Keyword arguments:
        status -- status
        """
        # TODO This is required, but no corresponding Health equivalent
        #    so, default is 'confirmed'

        if status:
            st = supermod.ConditionStatus(value='confirmed')
            super(health_Condition, self).set_status(st)

    def set_severity(self, severity):
        """Extends superclass for convenience

        Keyword arguments:
        severity -- the disease severity
        """

        if severity:
            # These are the snomed codes
            sev={'1_mi': ('Mild', '255604002'),
                '2_mo': ('Moderate', '6736007'),
                '3_sv': ('Severe', '24484000')}
            t=sev.get(severity)
            if t:
                c = supermod.CodeableConcept()
                c.coding = [supermod.Coding()]
                c.coding[0].display=supermod.string(value=t[0])
                c.coding[0].code=supermod.code(value=t[1])
                c.coding[0].system=supermod.uri(value='http://snomed.info/sct')
                c.text = supermod.string(value=t[0])
                super(health_Condition, self).set_severity(c)

    def set_code(self, code):
        """Extends superclass for convenience

        Keyword arguments:
        code -- the pathology info (Health model)
        """

        if code:
            c = supermod.CodeableConcept()
            c.coding=[supermod.Coding()]
            c.coding[0].display=supermod.string(value=code.name)
            c.coding[0].code=supermod.code(value=code.code)
            #ICD-10-CM
            c.coding[0].system=supermod.uri(value='urn:oid:2.16.840.1.113883.6.90')
            c.text = supermod.string(value=code.name)
            super(health_Condition, self).set_code(c)

supermod.Condition.subclass=health_Condition
