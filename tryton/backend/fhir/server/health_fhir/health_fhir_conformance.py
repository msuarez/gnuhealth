from datetime import datetime
from operator import attrgetter
from StringIO import StringIO
from .health_fhir_patient import Patient_Map
from .health_fhir_observation import Observation_Map
from .health_fhir_practitioner import Practitioner_Map
from .health_fhir_procedure import Procedure_Map
from .health_fhir_condition import Condition_Map
from .health_fhir_diagnostic_report import DiagnosticReport_Map
from .health_fhir_family_history import FamilyHistory_Map
import server.fhir as supermod

UPDATED=datetime(2015, 2, 5).strftime('%Y/%m/%d')

class health_Conformance(supermod.Conformance):
    def __init__(self, *args, **kwargs):
        institution = kwargs.pop('publisher', None)
        super(health_Conformance, self).__init__(*args, **kwargs)

        # Need access to search mappings
        #    to see what is working
        self.patient=Patient_Map()
        self.observation=Observation_Map()
        self.practitioner=Practitioner_Map()
        self.procedure=Procedure_Map()
        self.condition=Condition_Map()
        self.diagnostic_report=DiagnosticReport_Map()
        self.family_history=FamilyHistory_Map()

        self.__set_rest()
        self.__set_format()
        self.__set_publisher(institution)
        self.__set_description()
        self.__set_date()
        self.__set_unknown()
        self.__set_implementation()
        self.__set_name()
        self.__set_version()

    def __set_name(self):
        n = supermod.string(value='Conformance Statement')
        self.set_name(n)

    def __set_publisher(self, publisher=None):
        if publisher:
            p = supermod.string(value=publisher)
            self.set_publisher(p)

    def __set_description(self):
        s = supermod.string(value='This is the conformance statement. It describes the capabilities of this FHIR installation')
        self.set_description(s)

    def __set_date(self):
        self.set_date(supermod.dateTime(value=UPDATED))

    def __set_implementation(self):
        i = supermod.Conformance_Implementation()
        i.url = supermod.uri(value='/')
        i.description=supermod.string(value='FHIR installation')
        self.set_implementation(i)
    
    def __set_version(self):
        v = supermod.id(value='0.0.82')
        self.set_fhirVersion(v)

    def __set_unknown(self):
        u = supermod.boolean(value='false')
        self.set_acceptUnknown(u)

    def __set_format(self):
        # When JSON supported, add it to here
        f = [supermod.code(value='xml')]
        self.set_format(f)

    def __set_rest(self):
        #TODO Add SearchParam
        r = supermod.Conformance_Rest()
        r.mode = supermod.RestfulConformanceMode(value='server')
        endpoints = []
        for endpoint, mapping in [('Patient', self.patient),
                            ('DiagnosticReport', self.diagnostic_report),
                            ('Practitioner', self.practitioner),
                            ('Procedure', self.procedure),
                            ('Observation', self.observation),
                            ('Condition', self.condition),
                            ('FamilyHistory', self.family_history)]:
            e = supermod.Conformance_Resource()
            e.type_=supermod.code(value=endpoint)
            e.operation=[supermod.code(value=operation) for operation in ['read', 'validate', 'search']]
            for k,v in mapping.resource_search_params.items():
                if v is not None: #None are non-implemented
                    s = supermod.Conformance_SearchParam()
                    s.name = supermod.string(value=str(k))
                    s.type_ = supermod.code(value=str(v))
                    e.add_searchParam(s)
            endpoints.append(e)
        r.resource = endpoints
        self.set_rest([r])

    def export_to_xml_string(self):
        output = StringIO()
        self.export(outfile=output, namespacedef_='xmlns="http://hl7.org/fhir"', pretty_print=False, level=4)
        content = output.getvalue()
        output.close()
        return content

supermod.Conformance.subclass=health_Conformance
