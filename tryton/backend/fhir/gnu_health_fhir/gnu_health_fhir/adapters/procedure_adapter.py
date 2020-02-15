from gnu_health_fhir.common.utils import safe_attrgetter
from gnu_health_fhir.config import COMMON_SYSTEMS
from pendulum import instance
from fhirclient.models.procedure import Procedure as fhir_procedure
from .base import BaseAdapter
from .patient_adapter import Patient
from .practitioner_adapter import Practitioner

__all__ = ["Procedure"]


class Procedure(BaseAdapter):
    @classmethod
    def to_fhir_object(cls, procedure):
        # TODO category
        # TODO usedCode Use procedure.name.supplies
        # TODO location - room = procedure.name.operating_room
        jsondict = {}
        jsondict["identifier"] = cls.build_fhir_identifier(procedure)
        jsondict["subject"] = cls.build_fhir_subject(procedure)
        jsondict["status"] = cls.build_fhir_status(procedure)
        jsondict["code"] = cls.build_fhir_code(procedure)
        jsondict["notDone"] = cls.build_fhir_not_done(procedure)
        jsondict["reasonCode"] = cls.build_fhir_reason_code(procedure)
        jsondict["performer"] = cls.build_fhir_performer(procedure)
        jsondict["performedPeriod"] = cls.build_fhir_performed_period(procedure)
        jsondict["note"] = cls.build_fhir_note(procedure)
        return fhir_procedure(jsondict=jsondict)

    @classmethod
    def get_fhir_resource_type(cls):
        return "Procedure"

    @classmethod
    def get_fhir_object_id_from_gh_object(cls, procedure):
        return procedure.id

    @classmethod
    def build_fhir_identifier(cls, procedure):
        return [
            {
                "use": "official",
                "value": "-".join([procedure.procedure.name, str(procedure.id)]),
            }
        ]

    @classmethod
    def build_fhir_subject(cls, procedure):
        try:
            return cls.build_fhir_reference_from_adapter_and_object(
                Patient, procedure.name.patient
            )
        except:
            return None

    @classmethod
    def build_fhir_status(cls, procedure):
        state = procedure.name.state
        s = None
        if state == "in_progress":
            s = "in-progress"
        elif state == "cancelled":
            s = "aborted"
        elif state in ["done", "signed"]:
            s = "completed"
        elif state in ["draft", "confirmed"]:  # NOT in standard
            s = "scheduled"
        else:
            s = "entered-in-error"
        return s

    @classmethod
    def build_fhir_code(cls, procedure):
        return cls.build_codeable_concept(
            code=procedure.procedure.name,
            system=COMMON_SYSTEMS.get_icd_10_pcs_system(),
            text=procedure.procedure.description.capitalize(),
        )

    @classmethod
    def build_fhir_not_done(cls, procedure):
        # There is no Health equivalent (I think?)
        return False

    @classmethod
    def build_fhir_reason_code(cls, procedure):
        return [
            cls.build_codeable_concept(
                code=procedure.name.pathology.code,
                system=COMMON_SYSTEMS.get_icd_10_cm_system(),
                text=procedure.name.pathology.name,
            )
        ]

    @classmethod
    def build_fhir_performer(cls, procedure):
        actors = []
        surgeon = procedure.name.surgeon
        if surgeon:
            ref = cls.build_fhir_reference_from_adapter_and_object(
                Practitioner, surgeon
            )
            role = cls.build_codeable_concept(
                "304292004", "urn:oid:2.16.840.1.113883.4.642.2.420", "Surgeon"
            )
            actors.append({"actor": ref, "role": role})

        anesthetist = procedure.name.anesthetist
        if anesthetist:
            ref = cls.build_fhir_reference_from_adapter_and_object(
                Practitioner, anesthetist
            )
            role = cls.build_codeable_concept(
                "158970007", "urn:oid:2.16.840.1.113883.4.642.2.420", "Anesthetist"
            )
            actors.append({"actor": ref, "role": role})
        for m in procedure.name.surgery_team:
            ref = cls.build_fhir_reference_from_adapter_and_object(Practitioner, m)
            if m.role:
                code, name = safe_attrgetter(
                    m, "role.specialty.code", "role.specialty.name"
                )
                role = cls.build_codeable_concept(code=code, text=name)
                actors.append({"actor": ref, "role": role})
            else:
                actors.append({"actor": ref})
        return actors

    @classmethod
    def build_fhir_performed_period(cls, procedure):
        start, end = safe_attrgetter(
            procedure, "name.surgery_date", "name.surgery_end_date"
        )
        if start is not None:
            period = {"start": instance(start).to_iso8601_string()}
            if end is not None:
                period["end"] = instance(end).to_iso8601_string()
            return period

    @classmethod
    def build_fhir_note(cls, procedure):
        if procedure.name.extra_info:
            return [{"text": procedure.name.extra_info}]
