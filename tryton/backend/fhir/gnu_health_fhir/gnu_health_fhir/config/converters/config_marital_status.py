from .base import BaseConfig


class MaritalStatus(BaseConfig):
    @classmethod
    def build_fhir_object_from_health(cls, health):
        # Current FHIR values
        #   ('s', 'Single'),
        #   ('m', 'Married'),
        #   ('c', 'Concubinage'),
        #   ('w', 'Widowed'),
        #   ('d', 'Divorced'),
        #   ('x', 'Separated'),
        if health == "s":
            return cls.get_fhir_unmarried()
        elif health == "m":
            return cls.get_fhir_married()
        elif health == "c":
            return cls.get_fhir_domestic_partner()
        elif health == "w":
            return cls.get_fhir_widowed()
        elif health == "d":
            return cls.get_fhir_divorced()
        elif health == "x":
            return cls.get_fhir_separated()
        else:
            return cls.get_fhir_unknown()

    @classmethod
    def build_health_object_from_fhir(cls, fhir):
        statuses = {
            "A": None,
            "D": "d",
            "I": None,
            "S": "x",
            "M": "m",
            "P": None,
            "N": None,
            "T": "c",
            "U": "s",
            "W": "w",
            "UNK": None,
        }
        return statuses.get(fhir, None)

    @classmethod
    def get_fhir_annulled(cls):
        return cls.build_codeable_concept(
            code="A", system="http://hl7.org/fhir/v3/MaritalStatus", text="Annulled",
        )

    @classmethod
    def get_fhir_divorced(cls):
        return cls.build_codeable_concept(
            code="D", system="http://hl7.org/fhir/v3/MaritalStatus", text="Divorced"
        )

    @classmethod
    def get_fhir_interlocutory(cls):
        return cls.build_codeable_concept(
            code="I",
            system="http://hl7.org/fhir/v3/MaritalStatus",
            text="Interlocutory",
        )

    @classmethod
    def get_fhir_separated(cls):
        return cls.build_codeable_concept(
            code="L",
            system="http://hl7.org/fhir/v3/MaritalStatus",
            text="Legally separated",
        )

    @classmethod
    def get_fhir_married(cls):
        return cls.build_codeable_concept(
            code="M", system="http://hl7.org/fhir/v3/MaritalStatus", text="Married"
        )

    @classmethod
    def get_fhir_polygamous(cls):
        return cls.build_codeable_concept(
            code="P", system="http://hl7.org/fhir/v3/MaritalStatus", text="Polygamous",
        )

    @classmethod
    def get_fhir_never_married(cls):
        return cls.build_codeable_concept(
            code="S",
            system="http://hl7.org/fhir/v3/MaritalStatus",
            text="Never married",
        )

    @classmethod
    def get_fhir_domestic_partner(cls):
        return cls.build_codeable_concept(
            code="T",
            system="http://hl7.org/fhir/v3/MaritalStatus",
            text="Domestic partner",
        )

    @classmethod
    def get_fhir_unmarried(cls):
        return cls.build_codeable_concept(
            code="U", system="http://hl7.org/fhir/v3/MaritalStatus", text="Unmarried"
        )

    @classmethod
    def get_fhir_widowed(cls):
        return cls.build_codeable_concept(
            code="W", system="http://hl7.org/fhir/v3/MaritalStatus", text="Widowed",
        )

    @classmethod
    def get_fhir_unknown(cls):
        return cls.build_codeable_concept(
            code="UNK", system="http://hl7.org/fhir/v3/MaritalStatus", text="unknown",
        )
