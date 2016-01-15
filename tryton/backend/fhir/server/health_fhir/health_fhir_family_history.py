from StringIO import StringIO
from operator import attrgetter
import server.fhir as supermod
from server.common import safe_attrgetter
from .health_mixin import ExportXMLMixin

try:
    from flask import url_for
    RUN_FLASK=True
except:
    from .datastore import dumb_url_generate
    RUN_FLASK=False


class FamilyHistory_Map:
    """Holds essential mappings and information for
        the FamilyHistory class
    """
    # NOTE We are searching from the gnuhealth.patient view,
    #   since it is easier since family_history is many_to_one

    root_search=[]

    resource_search_params={
            '_id': 'token',
            'subject': 'reference',
            '_language': None}

    chain_map={'subject': 'Patient'}

    search_mapping={
            '_id': ['id'], #Multiple rows, use patient id as *the* id
            'subject': None} #DEBUG Hacky, could cause later problems


    url_prefixes={}
    model_mapping={'gnuhealth.patient.family.diseases':
            {
                'relation': 'relative',
                'relationship': 'xory',
                'condition': 'name'
            }}
# TODO This class should accept a list of dicts, not rows

# DEBUG FamilyHistory stores the entire history in one resource
#    Consequently, the class must process multiple records
#    WATCH FOR BUGS

class health_FamilyHistory(supermod.FamilyHistory, FamilyHistory_Map, ExportXMLMixin):
    def __init__(self, *args, **kwargs):
        rec = kwargs.pop('gnu_record', None)
        super(health_FamilyHistory, self).__init__(*args, **kwargs)
        if rec:
            self.set_gnu_family_history(rec)

    def set_gnu_family_history(self, patient):
        """Set the GNU Health records
        ::::
            params:
                patient ===> Health model
            returns:
                instance

        """

        self.patient = patient
        self.model_type = self.patient.__name__

        ## Only certain models
        if self.model_type not in ['gnuhealth.patient']:
            raise ValueError('Not a valid model')

        self.map_ = self.model_mapping['gnuhealth.patient.family.diseases']

        self.__import_from_gnu_family_history()
        self.__set_feed_info()

    def __import_from_gnu_family_history(self):
        """Import data from the model"""

        if self.patient:
            self.set_relation(self.patient.family_history)
            self.set_subject(self.patient)
            #self.set_note()

    def __set_feed_info(self):
        """Set the feed-relevant data"""

        if self.patient:
            if RUN_FLASK:
                uri = url_for('fh_record',
                                log_id=self.patient.id,
                                _external=True)
            else:
                uri = dumb_url_generate(['FamilyHistory',
                                self.patient.id])
            self.feed={'id': uri,
                    #'published': self.family_history[0].create_date,
                    #'updated': self.family_history[0].write_date or self.family_history[0].create_date,
                    'published': self.patient.create_date,
                    'updated': self.patient.write_date or self.patient.create_date,
                    'title': 'Family history for {}'.format(self.patient.rec_name)
                        }

    def set_subject(self, subject):
        """Extends superclass for convenience

        Keyword arguments:
        subject -- the patient (Health model)
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
            super(health_FamilyHistory, self).set_subject(ref)

    def set_note(self, note):
        super(health_FamilyHistory, self).set_note(note)

    def set_relation(self, familyHistory):
        """Extends superclass for convenience

        Keyword arguments:
        familyHistory -- the relatives
        """

        # TODO Combine multiple conditions for same person
        from server.fhir.value_sets import familyMember
        for member in familyHistory:
            rel = supermod.FamilyHistory_Relation()
            rel.relationship = supermod.CodeableConcept()

            # Add relationship
            t = {'s': 'sibling', 'm': 'maternal', 'f': 'paternal'}
            k = ' '.join((t.get(member.xory, ''), member.relative))
            info = [d for d in familyMember.contents if d['display'] == k]

            c = supermod.Coding()
            if info:
                c.code = supermod.code(value=info[0]['code'])
                c.system = supermod.uri(value=info[0]['system'])
            rel.relationship.text = supermod.string(value=k)
            c.display = supermod.string(value=k)
            rel.relationship.text = supermod.string(value=k)
            rel.relationship.coding=[c]

            # Add the condition
            s = attrgetter(self.map_['condition'])(member)
            if s:
                con = supermod.FamilyHistory_Condition()
                t = supermod.CodeableConcept()
                t.coding=[supermod.Coding()]
                t.coding[0].display=supermod.string(value=s.name)
                t.coding[0].code=supermod.code(value=s.code)
                #ICD-10-CM
                t.coding[0].system=supermod.uri(value='urn:oid:2.16.840.1.113883.6.90')
                t.text = supermod.string(value=s.name)
                con.set_type(t)
                rel.add_condition(con)

            super(health_FamilyHistory, self).add_relation(rel)

supermod.FamilyHistory.subclass=health_FamilyHistory
