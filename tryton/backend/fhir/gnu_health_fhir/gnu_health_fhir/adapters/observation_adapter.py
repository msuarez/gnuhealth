from gnu_health_fhir.common.utils import safe_attrgetter
from pendulum import instance
from fhirclient.models.observation import Observation as fhir_observation
from .base import BaseAdapter
from .patient_adapter import Patient
from .practitioner_adapter import Practitioner

__all__ = ["Observation"]


class Observation(BaseAdapter):
    @classmethod
    def to_fhir_object(cls, observation):
        jsondict = {}
        jsondict["comment"] = cls.build_fhir_comment(observation)
        jsondict["identifier"] = cls.build_fhir_identifier(observation)
        jsondict["interpretation"] = cls.build_fhir_interpretation(observation)
        jsondict["issued"] = cls.build_fhir_issued(observation)
        jsondict["code"] = cls.build_fhir_code(observation)
        jsondict["performer"] = cls.build_fhir_performer(observation)
        jsondict["referenceRange"] = cls.build_fhir_reference_range(observation)
        jsondict["status"] = cls.build_fhir_status(observation)
        jsondict["valueQuantity"] = cls.build_fhir_value_quantity(observation)
        jsondict["subject"] = cls.build_fhir_subject(observation)
        jsondict["effectiveDateTime"] = cls.build_fhir_effective_datetime(observation)
        return fhir_observation(jsondict=jsondict)

    @classmethod
    def get_fhir_resource_type(cls):
        return "Observation"

    @classmethod
    def get_fhir_object_id_from_gh_object(cls, observation):
        return observation.id

    @classmethod
    def build_fhir_comment(cls, observation):
        return observation.remarks

    @classmethod
    def build_fhir_identifier(cls, observation):
        return [
            {
                "use": "official",
                "value": "-".join([observation.name, str(observation.id)]),
            }
        ]

    @classmethod
    def build_fhir_interpretation(cls, observation):
        # TODO: Interpretation is complicated
        value = observation.result
        lower_limit = observation.lower_limit
        upper_limit = observation.upper_limit

        if value is not None and lower_limit is not None and upper_limit is not None:
            if value < lower_limit:
                v = "L"
                d = "Low"
            elif value > upper_limit:
                v = "H"
                d = "High"
            else:
                v = "N"
                d = "Normal"
            return cls.build_codeable_concept(v, "http://hl7.org/fhir/v2/0078", d)

    @classmethod
    def build_fhir_issued(cls, observation):
        issued = observation.write_date or observation.create_date
        if issued:
            return instance(issued).to_iso8601_string()

    @classmethod
    def build_fhir_code(cls, observation):
        # TODO Better coding!!
        return cls.build_codeable_concept(code=observation.name, text=observation.name)

    @classmethod
    def build_fhir_performer(cls, observation):
        performers = [
            x
            for x in safe_attrgetter(
                observation, "gnuhealth_lab_id.pathologist", "gnuhealth_lab_id.done_by"
            )
            if x
        ]
        return [
            cls.build_fhir_reference_from_adapter_and_object(Practitioner, performer)
            for performer in performers
        ]

    @classmethod
    def build_fhir_reference_range(cls, observation):
        units = safe_attrgetter(observation, "units.name", default="unknown")
        lower_limit = observation.lower_limit
        upper_limit = observation.upper_limit

        if units is not None and lower_limit is not None and upper_limit is not None:
            ref = {
                "low": {"value": lower_limit, "unit": units},
                "high": {"value": upper_limit, "unit": units},
            }
            # 'meaning': {
            # 'text': 'Normal range',
            # 'coding': [{
            # 'system':'http://hl7.org/fhir/referencerange-meaning',
            # 'code': 'normal'}]}}
            return [ref]

    @classmethod
    def build_fhir_status(cls, observation):
        value = observation.result
        if observation.excluded:
            if value is not None:
                status = "cancelled"
            else:
                status = "entered in error"
        else:
            if value is not None:
                status = "final"
            else:
                status = "registered"
        return status

    @classmethod
    def build_fhir_value_quantity(cls, observation):
        # TODO More information
        value = observation.result
        units = safe_attrgetter(observation, "units.name", default="unknown")
        # code = None
        if value is not None:
            return {"value": value, "unit": units}

    @classmethod
    def build_fhir_subject(cls, observation):
        subject = safe_attrgetter(observation, "gnuhealth_lab_id.patient")
        if subject:
            cls.build_fhir_reference_from_adapter_and_object(Patient, subject)

    @classmethod
    def build_fhir_effective_datetime(cls, observation):
        t = safe_attrgetter(observation, "gnuhealth_lab_id.date_analysis")
        if t:
            return instance(t).to_iso8601_string()
