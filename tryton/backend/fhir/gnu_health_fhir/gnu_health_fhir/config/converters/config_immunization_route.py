from .base import BaseConfig

__all__ = ["ImmunizationRoute"]


class ImmunizationRoute(BaseConfig):
    @classmethod
    def build_fhir_object_from_health(cls, health):
        # Health routes
        # ('im', 'Intramuscular'),
        # ('sc', 'Subcutaneous'),
        # ('id', 'Intradermal'),
        # ('nas', 'Intranasal'),
        # ('po', 'Oral'),
        if health == "im":
            return cls.get_fhir_intramuscular()
        elif health == "sc":
            return cls.get_fhir_subcutaneous()
        elif health == "id":
            return cls.get_fhir_intradermal()
        elif health == "nas":
            return cls.get_fhir_intranasal()
        elif health == "po":
            return cls.get_fhir_oral()
        else:
            return cls.get_fhir_unknown()

    @classmethod
    def build_health_object_from_fhir(cls, fhir):
        routes = {
            "IM": "im",
            "PO": "po",
            "NASINHLC": "nas",
            "TRNSDERM": None,
            "IDINJ": "id",
            "SQ": "sc",
            "IVINJ": None,
        }
        return routes.get(fhir, None)

    @classmethod
    def get_fhir_intramuscular(cls):
        return cls.build_codeable_concept(
            code="IM",
            system="http://terminology.hl7.org/CodeSystem/v3-RouteOfAdministration",
            text="Intramuscular",
        )

    @classmethod
    def get_fhir_oral(cls):
        return cls.build_codeable_concept(
            code="PO",
            system="http://terminology.hl7.org/CodeSystem/v3-RouteOfAdministration",
            text="Oral",
        )

    @classmethod
    def get_fhir_intranasal(cls):
        return cls.build_codeable_concept(
            code="NASINHLC",
            system="http://terminology.hl7.org/CodeSystem/v3-RouteOfAdministration",
            text="Intranasal",
        )

    @classmethod
    def get_fhir_intravenous(cls):
        return cls.build_codeable_concept(
            code="IVINJ",
            system="http://terminology.hl7.org/CodeSystem/v3-RouteOfAdministration",
            text="Intravenous",
        )

    @classmethod
    def get_fhir_subcutaneous(cls):
        return cls.build_codeable_concept(
            code="SQ",
            system="http://terminology.hl7.org/CodeSystem/v3-RouteOfAdministration",
            text="Subcutaneous",
        )

    @classmethod
    def get_fhir_intradermal(cls):
        return cls.build_codeable_concept(
            code="IDINJ",
            system="http://terminology.hl7.org/CodeSystem/v3-RouteOfAdministration",
            text="Intradermal",
        )

    @classmethod
    def get_fhir_transdermal(cls):
        return cls.build_codeable_concept(
            code="TRNSDERM",
            system="http://terminology.hl7.org/CodeSystem/v3-RouteOfAdministration",
            text="Transdermal",
        )

    @classmethod
    def get_fhir_unknown(cls):
        return cls.build_codeable_concept(
            code="UNK",
            system="http://terminology.hl7.org/CodeSystem/v3-RouteOfAdministration",
            text="Unkown",
        )
