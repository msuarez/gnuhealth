from StringIO import StringIO
from operator import attrgetter
from datetime import datetime
from .datastore import find_record
from .health_mixin import ExportXMLMixin
import server.fhir as supermod
from server.common import safe_attrgetter

try:
    from flask import url_for
    RUN_FLASK=True
except:
    from .datastore import dumb_url_generate
    RUN_FLASK=False

class Procedure_Map:
    model_mapping={
            'gnuhealth.ambulatory_care_procedure':
                {'subject': 'name.patient',
                    'date': 'name.session_start',
                    'type': 'procedure',
                    'description': 'procedure.description',
                    'name': 'procedure.rec_name',
                    'code': 'procedure.name'},
            'gnuhealth.operation':
                {'subject': 'name.patient',
                    'subject_name': 'name.patient.rec_name',
                    'date': 'name.surgery_date',
                    'type': 'procedure',
                    'description': 'procedure.description',
                    'name': 'procedure.rec_name',
                    'code': 'procedure.name'},
            'gnuhealth.rounding_procedure':
                {'subject': 'name.name.patient',
                    'date': 'name.evaluation_start',
                    'type': 'procedure',
                    'description': 'procedure.description',
                    'name': 'procedure.rec_name',
                    'code': 'procedure.name'}}

    url_prefixes={}
                    #'gnuhealth.rounding_procedure': 'rounds',
                    #'gnuhealth.ambulatory_care_procedure': 'amb',
                    #'gnuhealth.operation': 'surg'}

    resource_search_params= {
            '_id': 'token',
            '_language': None,
            'date': 'date',
            'subject': 'reference',
            'type': 'token',
            }

    # Reference parameter to resource type
    chain_map={
            'subject': 'Patient'}

    # Since these models are pretty similar, all can share same mapping
    #       i.e., no weird or special cases
    #       so we can generate the searches from the model_mapping
    #    But for now, ignore other models = only gnuhealth.operation
    t='gnuhealth.operation'
    search_mapping={
            '_id': ['id'],
            'date': [model_mapping[t]['date']],
            'subject': [model_mapping[t]['subject']],
            'type': [model_mapping[t]['code']],
            'type:text': [model_mapping[t]['name'],
                        model_mapping[t]['description']]}

class health_Procedure(supermod.Procedure, Procedure_Map, ExportXMLMixin):
    def __init__(self, *args, **kwargs):
        rec = kwargs.pop('gnu_record', None)
        super(health_Procedure, self).__init__(*args, **kwargs)
        if rec:
            self.set_gnu_procedure(rec)

    def set_gnu_procedure(self, procedure):
        """Set procedure;

        GNU Health uses 'operation' and 'procedure'
        sometimes interchangeably
        """
        self.procedure = procedure
        self.model_type = self.procedure.__name__

        # Only certain models
        if self.model_type not in self.model_mapping:
            raise ValueError('Not a valid model')

        #self.search_prefix = self.url_prefixes[self.model_type]
        self.map = self.model_mapping[self.model_type]

        self.__import_from_gnu_procedure()
        self.__set_feed_info()

    def __import_from_gnu_procedure(self):
        """Set the data from the model"""
        if self.procedure:
            self.set_subject(safe_attrgetter(self.procedure, self.map['subject']))
            self.set_type(safe_attrgetter(self.procedure, self.map['type']))
            self.set_date(safe_attrgetter(self.procedure, self.map['date']),
                            safe_attrgetter(self.procedure, self.map['date']))
            self.set_identifier(
                    safe_attrgetter(self.procedure, self.map['subject_name']),
                    safe_attrgetter(self.procedure, self.map['type']),
                    safe_attrgetter(self.procedure, self.map['date']))

    def __set_feed_info(self):
        """Set the feed-relevant data"""
        if self.procedure:
            if RUN_FLASK:
                uri = url_for('op_record',
                                log_id=self.procedure.id,
                                _external=True)
            else:
                uri = dumb_url_generate(['Procedure',
                                self.procedure.id])
            self.feed={'id': uri,
                    'published': self.procedure.create_date,
                    'updated': self.procedure.write_date or self.procedure.create_date,
                    'title': attrgetter(self.map['name'])(self.procedure)
                        }

    def set_identifier(self, patient, procedure, date):
        """Extends superclass for convenience

        Keyword arguments:
        patient -- patient name
        procedure -- procedure (Health model)
        date -- date (datetime object)
        """

        if procedure and patient and date:
            if RUN_FLASK:
                value = supermod.string(value=url_for('op_record', log_id=self.procedure.id))
            else:
                value = supermod.string(value=dumb_url_generate(['Procedure',
                                                                self.procedure.id]))
            ident = supermod.Identifier(
                    label = supermod.string(
                        value='{0} performed on {1} on {2}'.format(
                            procedure.rec_name, patient, date.strftime('%Y/%m/%d'))),
                        value=value)
            super(health_Procedure, self).add_identifier(ident)

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
            super(health_Procedure, self).set_subject(ref)

    def set_date(self, start, end):
        """Extends superclass for convenience

        Keyword arguments:
        start -- the start date (datetime object)
        end -- the end date (datetime object)
        """
        #TODO Better specifics

        if start is not None:
            p = supermod.Period()
            p.start = supermod.dateTime(value=start.strftime("%Y/%m/%d"))
            if end is not None:
                p.end = supermod.dateTime(value=end.strftime("%Y/%m/%d"))
            super(health_Procedure, self).set_date(p)

    def set_type(self, type_):
        """Extends superclass for convenience

        Keyword arguments:
        type_ -- procedure (Health model)
        """

        if type_:
            concept = supermod.CodeableConcept()
            des= type_.description
            if des:
                concept.text = supermod.string(value=des)
            concept.coding=[supermod.Coding()]
            name = type_.rec_name
            if name:
                concept.coding[0].display = supermod.string(value=name)
                concept.text=supermod.string(value=name)
            concept.coding[0].code=supermod.code(value=type_.name)
            #ICD-10-PCS
            concept.coding[0].system=supermod.uri(value='urn:oid:2.16.840.1.113883.6.4')
            super(health_Procedure, self).set_type(concept)

supermod.Procedure.subclass=health_Procedure
