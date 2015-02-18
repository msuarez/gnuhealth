from StringIO import StringIO
from operator import attrgetter
import server.fhir as supermod

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

class health_Condition(supermod.Condition, Condition_Map):
    def __init__(self, *args, **kwargs):
        rec = kwargs.pop('gnu_record', None)
        super(health_Condition, self).__init__(*args, **kwargs)
        if rec:
            self.set_gnu_condition(rec)

    def set_gnu_condition(self, condition):
        """Set the GNU Health record
        ::::
            params:
                condition ===> Health model
            returns:
                instance
        """
        self.condition = condition
        self.model_type = self.condition.__name__

        # Only certain models
        if self.model_type not in self.model_mapping:
            raise ValueError('Not a valid model')

        self.map = self.model_mapping[self.model_type]

        self.__import_from_gnu_condition()

    def __import_from_gnu_condition(self):
        if self.condition:
            self.__set_gnu_subject()
            self.__set_gnu_asserter()
            self.__set_gnu_dateAsserted()
            self.__set_gnu_code()
            self.__set_gnu_severity()
            self.__set_gnu_abatement()
            self.__set_gnu_status()
            self.__set_gnu_notes()

            self.__set_feed_info()

    def __set_feed_info(self):
        ''' Sets the feed-relevant info
        '''
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

    def __set_gnu_subject(self):
        if self.condition:
            patient = attrgetter(self.map['subject'])(self.condition)
            if RUN_FLASK:
                uri = url_for('pat_record', log_id=patient.id)
            else:
                uri = dumb_url_generate(['Patient', patient.id])
            display = patient.rec_name
            ref=supermod.ResourceReference()
            ref.display = supermod.string(value=display)
            ref.reference = supermod.string(value=uri)
            self.set_subject(ref)

    def __set_gnu_asserter(self):
        if self.condition:
            hp = attrgetter(self.map['asserter'])(self.condition)
            if hp:
                if RUN_FLASK:
                    uri = url_for('hp_record', log_id=hp.id)
                else:
                    uri = dumb_url_generate(['Practitioner', hp.id])
                display = hp.rec_name
                ref=supermod.ResourceReference()
                ref.display = supermod.string(value=display)
                ref.reference = supermod.string(value=uri)
                self.set_asserter(ref)

    def __set_gnu_dateAsserted(self):
        if self.condition:
            d = attrgetter(self.map['dateAsserted'])(self.condition)
            if d:
                self.set_dateAsserted(supermod.date(value=d.strftime('%Y/%m/%d')))

    def __set_gnu_notes(self):
        if self.condition:
            s = attrgetter(self.map['notes'])(self.condition)
            if s:
                self.set_notes(supermod.string(value=str(s)))

    def __set_gnu_abatement(self):
        if self.condition:
            d = attrgetter(self.map['abatementDate'])(self.condition)
            if d:
                self.set_abatementDate(supermod.date(value=d.strftime('%Y/%m/%d')))

    def __set_gnu_status(self):
        # TODO This is required, but no corresponding Health equivalent
        #    so, default is 'confirmed'
        if self.condition:
            st = supermod.ConditionStatus(value='confirmed')
            self.set_status(st)

    def __set_gnu_severity(self):
        if self.condition:
            s = attrgetter(self.map['severity'])(self.condition)
            if s:
                # These are the snomed codes
                sev={'1_mi': ('Mild', '255604002'),
                    '2_mo': ('Moderate', '6736007'),
                    '3_sv': ('Severe', '24484000')}
                t=sev.get(s)
                if t:
                    c = supermod.CodeableConcept()
                    c.coding = [supermod.Coding()]
                    c.coding[0].display=supermod.string(value=t[0])
                    c.coding[0].code=supermod.code(value=t[1])
                    c.coding[0].system=supermod.uri(value='http://snomed.info/sct')
                    c.text = supermod.string(value=t[0])
                    self.set_severity(c)

    def __set_gnu_code(self):
        if self.condition:
            s = attrgetter(self.map['code'])(self.condition)
            if s:
                c = supermod.CodeableConcept()
                c.coding=[supermod.Coding()]
                c.coding[0].display=supermod.string(value=s.name)
                c.coding[0].code=supermod.code(value=s.code)
                #ICD-10-CM
                c.coding[0].system=supermod.uri(value='urn:oid:2.16.840.1.113883.6.90')
                c.text = supermod.string(value=s.name)
                self.set_code(c)

    def export_to_xml_string(self):
        """Export"""
        output = StringIO()
        self.export(outfile=output, namespacedef_='xmlns="http://hl7.org/fhir"', pretty_print=False, level=4)
        content = output.getvalue()
        output.close()
        return content

supermod.Condition.subclass=health_Condition
