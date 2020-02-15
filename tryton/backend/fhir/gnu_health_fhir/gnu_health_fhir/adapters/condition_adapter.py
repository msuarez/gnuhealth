from pendulum import instance, parse
from gnu_health_fhir.config import COMMON_SYSTEMS, SNOMED
from fhirclient.models.condition import Condition as fhir_condition
from .base import BaseAdapter
from .patient_adapter import Patient
from .practitioner_adapter import Practitioner

__all__ = ["Condition"]


class Condition(BaseAdapter):
    @classmethod
    def to_fhir_object(cls, condition):
        # TODO verificationStatus No corresponding Health equivalent (I think?)
        jsondict = {}
        jsondict["subject"] = cls.build_fhir_subject(condition)
        jsondict["asserter"] = cls.build_fhir_asserter(condition)
        jsondict["assertedDate"] = cls.build_fhir_asserted_date(condition)
        jsondict["note"] = cls.build_fhir_note(condition)
        jsondict["code"] = cls.build_fhir_code(condition)
        jsondict["severity"] = cls.build_fhir_severity(condition)
        # jsondict["verificationStatus"] = cls.build_fhir_verificationStatus(condition)
        jsondict["abatementDateTime"] = cls.build_fhir_abatement_datetime(condition)
        return fhir_condition(jsondict=jsondict)

    @classmethod
    def get_fhir_resource_type(cls):
        return "Condition"

    @classmethod
    def get_fhir_object_id_from_gh_object(cls, condition):
        return condition.id

    @classmethod
    def build_fhir_subject(cls, condition):
        return cls.build_fhir_reference_from_adapter_and_object(Patient, condition.name)

    @classmethod
    def build_fhir_asserter(cls, condition):
        return cls.build_fhir_reference_from_adapter_and_object(
            Practitioner, condition.healthprof
        )

    @classmethod
    def build_fhir_asserted_date(cls, condition):
        if condition.diagnosed_date:
            return parse(str(condition.diagnosed_date)).to_iso8601_string()

    @classmethod
    def build_fhir_note(cls, condition):
        # Add comments about specific food allergy here, too
        allergies = {
            "da": "Drug Allergy",
            "fa": "Food Allergy",
            "ma": "Misc Allergy",
            "mc": "Misc Contraindication",
        }
        notes = []
        if condition.allergy_type:
            notes.append({"text": allergies.get(condition.allergy_type)})
        if condition.short_comment:
            notes.append({"text": condition.short_comment})
        if condition.extra_info:
            notes.append({"text": condition.extra_info})
        if notes:
            return notes

    @classmethod
    def build_fhir_abatement_datetime(cls, condition):
        if condition.healed_date:
            return instance(condition.healed_date).to_iso8601_string()

    @classmethod
    def build_fhir_severity(cls, condition):
        severity = condition.disease_severity
        if severity == "1_mi":
            return SNOMED.get_mild()
        elif severity == "2_mo":
            return SNOMED.get_moderate()
        elif severity == "3_sv":
            return SNOMED.get_severe()
        else:
            return None

    @classmethod
    def build_fhir_code(cls, condition):
        code = condition.pathology
        if code:
            return cls.build_codeable_concept(
                code=code.code,
                system=COMMON_SYSTEMS.get_icd_10_cm_system(),
                text=code.name,
            )
