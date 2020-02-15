from .base import BaseConfig

__all__ = ["ImmunizationSite"]


class ImmunizationSite(BaseConfig):
    @classmethod
    def build_fhir_object_from_health(cls, health_site):
        # Health equivalents
        # ('lvl', 'left vastus lateralis'),
        # ('rvl', 'right vastus lateralis'),
        # ('ld', 'left deltoid'),
        # ('rd', 'right deltoid'),
        # ('lalt', 'left anterolateral fat of thigh'),
        # ('ralt', 'right anterolateral fat of thigh'),
        # ('lpua', 'left posterolateral fat of upper arm'),
        # ('rpua', 'right posterolateral fat of upper arm'),
        # ('lfa', 'left fore arm'),
        # ('rfa', 'right fore arm')
        # The FHIR value set is limited -- use Health's
        if health_site == "lvl":
            return cls.get_fhir_lvl()
        elif health_site == "rvl":
            return cls.get_fhir_rvl()
        elif health_site == "ld":
            return cls.get_fhir_ld()
        elif health_site == "rd":
            return cls.get_fhir_rd()
        elif health_site == "lalt":
            return cls.get_fhir_lalt()
        elif health_site == "ralt":
            return cls.get_fhir_ralt()
        elif health_site == "lpua":
            return cls.get_fhir_lpua()
        elif health_site == "rpua":
            return cls.get_fhir_rpua()
        elif health_site == "lfa":
            return cls.get_fhir_lfa()
        elif health_site == "rfa":
            return cls.get_fhir_rfa()
        else:
            return None

    @classmethod
    def build_health_object_from_fhir(cls, fhir_site):
        if fhir_site in [
            "LVL",
            "RVL",
            "LD",
            "RD",
            "LALT",
            "RALT",
            "LPUA",
            "RPUA",
            "LFA",
            "RFA",
        ]:
            return fhir_site.lower()
        else:
            return None

    @classmethod
    def get_fhir_lvl(cls):
        return cls.build_codeable_concept(code="LVL", text="left vastus lateralis")

    @classmethod
    def get_fhir_rvl(cls):
        return cls.build_codeable_concept(code="RVL", text="right vastus lateralis")

    @classmethod
    def get_fhir_ld(cls):
        return cls.build_codeable_concept(code="LD", text="left deltoid")

    @classmethod
    def get_fhir_rd(cls):
        return cls.build_codeable_concept(code="RD", text="right deltoid")

    @classmethod
    def get_fhir_lalt(cls):
        return cls.build_codeable_concept(
            code="LALT", text="left anterolateral fat of thigh"
        )

    @classmethod
    def get_fhir_ralt(cls):
        return cls.build_codeable_concept(
            code="RALT", text="right anterolateral fat of thigh"
        )

    @classmethod
    def get_fhir_lpua(cls):
        return cls.build_codeable_concept(
            code="LPUA", text="left posterolateral fat of thigh"
        )

    @classmethod
    def get_fhir_rpua(cls):
        return cls.build_codeable_concept(
            code="RPUA", text="right posterolateral fat of thigh"
        )

    @classmethod
    def get_fhir_lfa(cls):
        return cls.build_codeable_concept(code="LFA", text="left forearm")

    @classmethod
    def get_fhir_rfa(cls):
        return cls.build_codeable_concept(code="RFA", text="right forearm")
