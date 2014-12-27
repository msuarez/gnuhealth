from StringIO import StringIO
from operator import attrgetter
from datetime import datetime
from .datastore import find_record
import server.fhir as supermod

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

    url_prefixes={'gnuhealth.rounding_procedure': 'rounds',
                    'gnuhealth.ambulatory_care_procedure': 'amb',
                    'gnuhealth.operation': 'surg'}

    # Since these models are pretty similar, all can share same mapping
    #       i.e., no weird or special cases
    #       so we can generate the searches from the model_mapping
    search_mapping={}
    for t,m in url_prefixes.items():
        search_mapping[t]={
            '_id': (['id'], 'token'),
            '_language': ([], 'token'),
            'date': ([model_mapping[t]['date']], 'date'),
            'subject': ([model_mapping[t]['subject']], 'reference'),
            'type': ([model_mapping[t]['code']], 'token'),
            'type:text': ([model_mapping[t]['name'],
                        model_mapping[t]['description']], 'string')}

class health_Procedure(supermod.Procedure, Procedure_Map):
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

        self.search_prefix = self.url_prefixes[self.model_type]
        self.map = self.model_mapping[self.model_type]

        self.__import_from_gnu_procedure()

    def __import_from_gnu_procedure(self):
        if self.procedure:
            self.__set_gnu_identifier()
            self.__set_gnu_type()
            self.__set_gnu_subject()
            self.__set_feed_info()

    def __set_feed_info(self):
        ''' Sets the feed-relevant info
        '''
        if self.procedure:
            self.feed={'id': self.procedure.id,
                    'published': self.procedure.create_date,
                    'updated': self.procedure.write_date or self.procedure.create_date,
                    'title': attrgetter(self.map['name'])(self.procedure)
                        }

    def __set_gnu_identifier(self):
        if self.procedure:
            patient, time, name = attrgetter(self.map['subject'], self.map['date'], self.map['name'])(self.procedure)
            if RUN_FLASK:
                value = supermod.string(value=url_for('op_record', log_id=(self.search_prefix, self.procedure.id, None)))
            else:
                value = supermod.string(value=dumb_url_generate(['Procedure',
                                                                self.search_prefix,
                                                                self.procedure.id]))
            ident = supermod.Identifier(
                        label = supermod.string(value='{0} performed on {1} on {2}'.format(name, patient.rec_name, time.strftime('%Y/%m/%d'))),
                        value=value)
            self.add_identifier(ident)

    def __set_gnu_subject(self):
        if self.procedure:
            patient = attrgetter(self.map['subject'])(self.procedure)
            if RUN_FLASK:
                uri = url_for('pat_record', log_id=patient.id)
            else:
                uri = dumb_url_generate(['Patient', patient.id])
            display = patient.rec_name
            ref=supermod.ResourceReference()
            ref.display = supermod.string(value=display)
            ref.reference = supermod.string(value=uri)
            self.set_subject(ref)

    def __set_gnu_type(self):
        if self.procedure:
            concept = supermod.CodeableConcept()
            des= attrgetter(self.map['description'])(self.procedure)
            if des:
                concept.text = supermod.string(value=des)
            concept.coding=[supermod.Coding()]
            name = attrgetter(self.map['name'])(self.procedure)
            if name:
                concept.coding[0].display = supermod.string(value=name)
            concept.coding[0].code=supermod.code(value=attrgetter(self.map['code'])(self.procedure))
            self.set_type(concept)

    def export_to_xml_string(self):
        """Export"""
        output = StringIO()
        self.export(outfile=output, namespacedef_='xmlns="http://hl7.org/fhir"', pretty_print=False, level=4)
        content = output.getvalue()
        output.close()
        return content

supermod.Procedure.subclass=health_Procedure

class health_Procedure_Performer(supermod.Procedure_Performer):
    pass

class health_Procedure_RelatedItem(supermod.Procedure_RelatedItem):
    pass

class health_ProcedureRelationshipType(supermod.ProcedureRelationshipType):
    pass
