from pendulum import instance
from fhirclient.models.diagnosticreport import DiagnosticReport as fhir_report
from .base import BaseAdapter
from .practitioner_adapter import Practitioner
from .patient_adapter import Patient
from .observation_adapter import Observation

__all__ = ["DiagnosticReport"]


class DiagnosticReport(BaseAdapter):
    @classmethod
    def to_fhir_object(cls, report):
        jsondict = {}
        jsondict["status"] = cls.build_fhir_status(report)
        jsondict["effectiveDateTime"] = cls.build_fhir_effective_datetime(report)
        jsondict["identifier"] = cls.build_fhir_identifier(report)
        jsondict["code"] = cls.build_fhir_code(report)
        jsondict["issued"] = cls.build_fhir_issued(report)
        jsondict["result"] = cls.build_fhir_result(report)
        jsondict["performer"] = cls.build_fhir_performer(report)
        jsondict["subject"] = cls.build_fhir_subject(report)
        jsondict["conclusion"] = cls.build_fhir_conclusion(report)
        return fhir_report(jsondict=jsondict)

    @classmethod
    def get_fhir_resource_type(cls):
        return "DiagnosticReport"

    @classmethod
    def get_fhir_object_id_from_gh_object(cls, report):
        return report.id

    @classmethod
    def build_fhir_status(cls, report):
        # TODO No clear correlate in Health (?)
        return "final"

    @classmethod
    def build_fhir_effective_datetime(cls, report):
        try:
            return instance(report.date_analysis).to_iso8601_string()
        except:
            return None

    @classmethod
    def build_fhir_identifier(cls, report):
        # identifier
        # TODO Return more information
        # patient = self.report.patient
        # date = self.report.date_analysis
        # report = self.report.test

        # if report and patient and date:
        # label = '{0}: {1} on {2}'.format(report.name, patient.rec_name or '<unknown>', date.strftime('%Y-%m-%d'))
        return [{"value": str(report.id), "use": "official"}]

    @classmethod
    def build_fhir_code(cls, report):
        # TODO Use LOINC coding
        try:
            return cls.build_codeable_concept(
                code=report.test.code, text=report.test.name
            )
        except:
            return None

    @classmethod
    def build_fhir_issued(cls, report):
        try:
            return instance(report.write_date).to_iso8601_string()
        except:
            return None

    @classmethod
    def build_fhir_result(cls, report):
        # TODO output actual observations, not links
        return [
            cls.build_fhir_reference_from_adapter_and_object(Observation, test)
            for test in report.critearea
        ]

    @classmethod
    def build_fhir_performer(cls, report):
        performers = []
        path = report.pathologist
        tech = report.done_by
        if path:
            performers.append(
                {
                    "actor": cls.build_fhir_reference_from_adapter_and_object(
                        Practitioner, path
                    ),
                    "role": {"text": "Pathologist"},
                }
            )
        if tech:
            performers.append(
                {
                    "actor": cls.build_fhir_reference_from_adapter_and_object(
                        Practitioner, tech
                    ),
                    "role": {"text": "Technician"},
                }
            )
        return performers

    @classmethod
    def build_fhir_subject(cls, report):
        cls.build_fhir_reference_from_adapter_and_object(Patient, report.patient)

    @classmethod
    def build_fhir_conclusion(cls, report):
        return report.results or report.diagnosis
