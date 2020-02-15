from .base import BaseConfig


class AdministrativeGender(BaseConfig):
    @classmethod
    def build_fhir_object_from_health(cls, health):
        # biological_sex
        #   m --> male
        #   f --> female
        if health == "m":
            return cls.get_fhir_male()
        elif health == "f":
            return cls.get_fhir_female()
        else:
            return cls.get_fhir_unknown()

    @classmethod
    def build_health_object_from_fhir(cls, fhir):
        codes = {
            "female": "f",
            "male": "m",
        }
        return codes.get(fhir, None)

    @classmethod
    def get_fhir_female(cls):
        return cls.build_codeable_concept(
            code="female",
            system="http://hl7.org/fhir/administrative-gender",
            text="Female",
        )

    @classmethod
    def get_fhir_male(cls):
        return cls.build_codeable_concept(
            code="male",
            system="http://hl7.org/fhir/administrative-gender",
            text="Male",
        )

    @classmethod
    def get_fhir_other(cls):
        return cls.build_codeable_concept(
            code="other",
            system="http://hl7.org/fhir/administrative-gender",
            text="Other",
        )

    @classmethod
    def get_fhir_unknown(cls):
        return cls.build_codeable_concept(
            code="unknown",
            system="http://hl7.org/fhir/administrative-gender",
            text="Unknown",
        )
