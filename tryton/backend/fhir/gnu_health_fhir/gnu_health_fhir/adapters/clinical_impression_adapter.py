from gnu_health_fhir.common.utils import safe_attrgetter
from pendulum import instance
from fhirclient.models.clinicalimpression import ClinicalImpression as fhir_impression
from .base import BaseAdapter
from .patient_adapter import Patient
from .encounter_adapter import Encounter
from .practitioner_adapter import Practitioner


__all__ = ["ClinicalImpression"]


class ClinicalImpression(BaseAdapter):
    """Immature resource somewhat equivalent to SOAP notes, H&P, etc

    Eventually, should support 3 models:
        - evaluations (most important)
        - roundings
        - ambulatory care
    """

    @classmethod
    def to_fhir_object(cls, impression):
        jsondict = {}
        jsondict["identifier"] = cls.build_fhir_identifier(impression)
        jsondict["status"] = cls.build_fhir_status(impression)
        jsondict["code"] = cls.build_fhir_code(impression)
        dt_or_period = cls.build_fhir_effective_datetime_or_period(impression)
        if isinstance(dt_or_period, dict):
            jsondict["effectivePeriod"] = dt_or_period
        else:
            jsondict["effectiveDateTime"] = dt_or_period
        jsondict["context"] = cls.build_fhir_context(impression)
        jsondict["subject"] = cls.build_fhir_subject(impression)
        jsondict["assessor"] = cls.build_fhir_assessor(impression)
        jsondict["date"] = cls.build_fhir_date(impression)
        jsondict["summary"] = cls.build_fhir_summary(impression)
        return fhir_impression(jsondict=jsondict)

    @classmethod
    def get_fhir_object_id_from_gh_object(cls, impression):
        return impression.id

    @classmethod
    def get_fhir_resource_type(cls):
        return "ClinicalImpression"

    @classmethod
    def build_fhir_identifier(cls, impression):
        try:
            return [{"value": impression.code}]
        except:
            return None

    @classmethod
    def build_fhir_status(cls, impression):
        # GNU Health states - in_progress, done, signed, None
        if impression.state in ["done", "signed"] or (
            impression.evaluation_start and impression.evaluation_endtime
        ):
            status = "completed"
        elif impression.state == "in_progress" or impression.appointment:
            status = "draft"
        else:
            status = "unknown"
        return status

    @classmethod
    def build_fhir_code(cls, impression):
        # TODO More information
        return {"text": "Patient evaluation"}

    @classmethod
    def build_fhir_context(cls, impression):
        return cls.build_fhir_reference_from_adapter_and_object(Encounter, impression)

    @classmethod
    def build_fhir_subject(cls, impression):
        return cls.build_fhir_reference_from_adapter_and_object(
            Patient, impression.patient
        )

    @classmethod
    def build_fhir_effective_datetime_or_period(cls, impression):
        try:
            start = instance(impression.evaluation_start).to_iso8601_string()
            if impression.evaluation_endtime:
                end = instance(impression.evaluation_endtime).to_iso8601_string()
                return {"start": start, "end": end}
            else:
                return start
        except:
            return None

    @classmethod
    def build_fhir_assessor(cls, impression):
        return cls.build_fhir_reference_from_adapter_and_object(
            Practitioner, impression.healthprof
        )

    @classmethod
    def build_fhir_date(cls, impression):
        try:
            last = impression.write_date or impression.evaluation_start
            return instance(last).to_iso8601_string()
        except:
            return None

    @classmethod
    def build_fhir_summary(cls, impression):
        # Shove Objective in here - evaluation_summary
        # Shove HPI in here - present_illness + chief_complaint
        # Shove Plan in here - directions
        return "CC: {}\n\nHPI: {}\n\nObjective: {}\n\nPlan: {}".format(
            *safe_attrgetter(
                impression,
                "chief_complaint",
                "present_illness",
                "evaluation_summary",
                "directions",
                default="",
            )
        )

        # investigation - put all the s/s, pe findings there
        # clinical_findings = {"code": {"text": "Clinical findings"}}

        # Other misc garbage
        # extras = [{'text': x} for x in safe_attrgetter(note, 'notes', 'notes_complaint', 'info_diagnosis', default='') if x.strip()]
        # if extras: jsondict['note'] = extras
