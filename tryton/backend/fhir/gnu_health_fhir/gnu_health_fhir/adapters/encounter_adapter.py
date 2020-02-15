from pendulum import instance
from fhirclient.models.encounter import Encounter as fhir_encounter
from .base import BaseAdapter
from .patient_adapter import Patient
from .practitioner_adapter import Practitioner
from .condition_adapter import Condition

__all__ = ["Encounter"]


class Encounter(BaseAdapter):
    """In GNU Health, `encounters` are patient evaluations, or at least part of that model.

    We shall add the more clinical data to a ClinicalImpression attached to the encounter
    """

    @classmethod
    def to_fhir_object(cls, enc):
        jsondict = {}
        jsondict["class"] = cls.build_fhir_class(enc)
        jsondict["type"] = cls.build_fhir_type(enc)
        jsondict["priority"] = cls.build_fhir_priority(enc)
        jsondict["subject"] = cls.build_fhir_subject(enc)
        jsondict["participant"] = cls.build_fhir_participant(enc)
        jsondict["period"] = cls.build_fhir_period(enc)
        jsondict["length"] = cls.build_fhir_length(enc)
        jsondict["status"] = cls.build_fhir_status(enc)
        jsondict["identifier"] = cls.build_fhir_identifier(enc)
        # jsondict["reasonCode"] = cls.build_fhir_reason_code(enc)
        jsondict["diagnosis"] = cls.build_fhir_diagnosis(enc)
        return fhir_encounter(jsondict=jsondict)

    @classmethod
    def get_fhir_resource_type(cls):
        return "Encounter"

    @classmethod
    def get_fhir_object_id_from_gh_object(cls, enc):
        return enc.id

    @classmethod
    def build_fhir_identifier(cls, enc):
        if enc.code:
            return [{"value": enc.code}]

    @classmethod
    def build_fhir_status(cls, enc):
        # GNU Health states - in_progress, done, signed, None
        if enc.state in ["done", "signed"] or (
            enc.evaluation_start and enc.evaluation_endtime
        ):
            status = "finished"
        elif enc.state == "in_progress":
            status = "in-progress"
        elif enc.appointment:
            if enc.appointment.checked_in_date:
                status = "arrived"
            else:
                status = "planned"
        else:
            status = "unknown"
        return status

    @classmethod
    def build_fhir_class(cls, enc):
        # GNU Health types - outpatient, inpatient
        if enc.evaluation_type == "outpatient":
            return {"code": "AMB", "display": "ambulatory"}
        elif enc.evaluation_type == "inpatient":
            return {"code": "IMP", "display": "inpatient encounter"}
        else:
            return None  # TODO

    @classmethod
    def build_fhir_type(cls, enc):
        # GNU Health - well_woman/man/child, followup, new
        if enc.visit_type == "new":
            g = {"text": "New health condition", "coding": [{"code": "new"}]}
        elif enc.visit_type == "well_woman":
            g = {"text": "Well woman visit", "coding": [{"code": "well_woman"}]}
        elif enc.visit_type == "well_child":
            g = {"text": "Well child visit", "coding": [{"code": "well_child"}]}
        elif enc.visit_type == "well_man":
            g = {"text": "Well man visit", "coding": [{"code": "well_man"}]}
        elif enc.visit_type == "followup":
            g = {"text": "Followup visit", "coding": [{"code": "followup"}]}
        else:
            g = {}
        if g:
            return [g]

    @classmethod
    def build_fhir_priority(cls, enc):
        # GNU Health - a = Normal, b = Urgent, c = Medical Emergency
        if enc.urgency == "a":
            g = {"text": "Normal", "coding": [{"code": "a"}]}
        elif enc.urgency == "b":
            g = {"text": "Urgent", "coding": [{"code": "b"}]}
        elif enc.urgency == "c":
            g = {"text": "Medical Emergency", "coding": [{"code": "c"}]}
        else:
            g = {}
        if g:
            return g

    @classmethod
    def build_fhir_subject(cls, enc):
        return cls.build_fhir_reference_from_adapter_and_object(Patient, enc.patient)

    @classmethod
    def build_fhir_participant(cls, enc):
        # signed_by (sign), healthprof (initiate)
        parts = []
        if enc.signed_by:
            parts.append(
                {
                    "individual": cls.build_fhir_reference_from_adapter_and_object(
                        Practitioner, enc.signed_by
                    )
                }
            )
        if enc.healthprof:
            parts.append(
                {
                    "individual": cls.build_fhir_reference_from_adapter_and_object(
                        Practitioner, enc.healthprof
                    )
                }
            )
        if parts:
            if len(parts) > 1:
                return parts[:1] if parts[0] == parts[1] else parts
            else:
                return parts

    @classmethod
    def build_fhir_period(cls, enc):
        # Period
        period = {}
        if enc.evaluation_start:
            period["start"] = instance(enc.evaluation_start).to_iso8601_string()
        if enc.evaluation_endtime:
            period["end"] = instance(enc.evaluation_endtime).to_iso8601_string()
        if period:
            return period

    @classmethod
    def build_fhir_length(cls, enc):
        # timedelta object
        # Use minutes
        if enc.evaluation_length:
            return {
                "code": "min",
                "value": enc.evaluation_length.seconds // 60,
                "unit": "minute",
                "system": "http://unitsofmeasure.org",
            }

    # @classmethod
    # def build_fhir_reason_code(cls, enc):
    # return [
    # cls.build_codeable_concept(
    # code=enc.diagnosis.name,
    # text=enc.diagnosis.name
    # )]

    @classmethod
    def build_fhir_diagnosis(cls, enc):
        # Diagnosis/Reason
        # TODO better information, add note to Condition reference
        # diagnosis, related_condition, secondary_conditions
        diags, temp = [], False
        if enc.diagnosis:
            diags.append({"rank": 1, "condition": {"display": enc.diagnosis.name}})
        if enc.related_condition:
            # This is set for a followup appt - consequently add this to reason, too
            diags.append(
                {
                    "rank": 2,
                    "condition": cls.build_fhir_reference_from_adapter_and_object(
                        Condition, enc.related_condition
                    ),
                }
            )
            temp = True
        for x, y in enumerate(enc.secondary_conditions, start=3 if temp else 2):
            diags.append({"rank": x, "condition": {"display": y.pathology.name}})
        return diags
