from .base import BaseAdapter


class Appointment(BaseAdapter):
    @classmethod
    def to_fhir_object(cls, appt):
        pass

    @classmethod
    def get_fhir_resource_type(cls):
        return "Appointment"

    @classmethod
    def get_fhir_object_id_from_gh_object(cls, appt):
        if appt.__name__ == "gnuhealth.appointment":
            return appt.id

    @classmethod
    def get_fhir_identifier(cls, appt):
        return [{"use": "official", "value": appt.name}]

    @classmethod
    def get_fhir_status(cls, appt):
        pass

    @classmethod
    def get_fhir_cancellation_reason(cls, appt):
        pass

    @classmethod
    def get_fhir_service_category(cls, appt):
        pass

    @classmethod
    def get_fhir_service_type(cls, appt):
        pass

    @classmethod
    def get_fhir_specialty(cls, appt):
        try:
            return cls.build_codeable_concept(
                code=appt.speciality.code, text=appt.speciality.name
            )
        except:
            return None

    @classmethod
    def get_fhir_appointment_type(cls, appt):
        pass

    @classmethod
    def get_fhir_reason_code(cls, appt):
        pass

    @classmethod
    def get_fhir_reason_reference(cls, appt):
        pass

    @classmethod
    def get_fhir_priority(cls, appt):
        pass

    @classmethod
    def get_fhir_description(cls, appt):
        pass

    @classmethod
    def get_fhir_start(cls, appt):
        pass

    @classmethod
    def get_fhir_end(cls, appt):
        pass

    @classmethod
    def get_fhir_create(cls, appt):
        pass

    @classmethod
    def get_fhir_comment(cls, appt):
        return appt.comments

    @classmethod
    def get_fhir_patient_instruction(cls, appt):
        pass

    @classmethod
    def get_fhir_participant(cls, appt):
        pass

    @classmethod
    def get_fhir_requested_period(cls, appt):
        pass
