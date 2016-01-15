from collections import namedtuple
from server.common import tryton
from server.health_fhir import health_Condition
from server.health_fhir import health_DiagnosticReport
from server.health_fhir import health_FamilyHistory
from server.health_fhir import health_Immunization
from server.health_fhir import health_MedicationStatement
from server.health_fhir import health_Observation
from server.health_fhir import health_Organization
from server.health_fhir import health_Practitioner
from server.health_fhir import health_Procedure
from server.health_fhir import health_Medication
from server.health_fhir import health_Patient
from server.health_fhir import Bundle
from server.health_fhir import health_Search

# Trying to keep consistent naming across all parts of the app
#   Consequently, bring all the pieces together and pass that around
Resource = namedtuple('Resource', ['model', 'adapter'])

mappings = {}

mappings['patient'] = Resource(
                    tryton.pool.get('gnuhealth.patient'),
                    health_Patient)

mappings['condition'] = Resource(
                    tryton.pool.get('gnuhealth.patient.disease'),
                    health_Condition)

mappings['diagnostic_report'] = Resource(
                    tryton.pool.get('gnuhealth.lab'),
                    health_DiagnosticReport)

mappings['family_history'] = Resource(
                    tryton.pool.get('gnuhealth.patient'), #Search from patient!
                    health_FamilyHistory)

mappings['immunization'] = Resource(
                    tryton.pool.get('gnuhealth.vaccination'),
                    health_Immunization)

mappings['medication'] = Resource(
                    tryton.pool.get('gnuhealth.medicament'),
                    health_Medication)

mappings['medication_statement'] = Resource(
                    tryton.pool.get('gnuhealth.patient.medication'),
                    health_MedicationStatement)

mappings['observation'] = Resource(
                    tryton.pool.get('gnuhealth.lab.test.critearea'),
                    health_Observation)

mappings['organization'] = Resource(
                    tryton.pool.get('gnuhealth.institution'),
                    health_Organization)

mappings['practitioner'] = Resource(
                    tryton.pool.get('gnuhealth.healthprofessional'),
                    health_Practitioner)

mappings['procedure'] = Resource(
                    tryton.pool.get('gnuhealth.operation'),
                    health_Procedure)

mappings['bundle'] = Resource(
                    None,
                    Bundle)

mappings['search'] = Resource(
                    None,
                    health_Search)

__all__ = ['mappings']
