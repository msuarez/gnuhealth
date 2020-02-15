from gnu_health_fhir.common import helper_mixin

__all__ = ["COMMON_SYSTEMS", "SNOMED"]


class COMMON_SYSTEMS:
    @classmethod
    def get_icd_10_cm_system(cls):
        return "urn:oid:2.16.840.1.113883.6.90"

    @classmethod
    def get_icd_10_pcs_system(cls):
        return "urn:oid:2.16.840.1.113883.6.4"

    @classmethod
    def get_bcp_47_language_system(cls):
        return "urn:ietf:bcp:47"


class SNOMED(helper_mixin):
    @classmethod
    def get_system(cls):
        return "http://snomed.info/sct"

    @classmethod
    def get_mild(cls):
        cls.build_codeable_concept(
            code="255604002", system="http://snomed.info/sct", text="Mild"
        )

    @classmethod
    def get_moderate(cls):
        cls.build_codeable_concept(
            code="6736007", system="http://snomed.info/sct", text="Moderate"
        )

    @classmethod
    def get_severe(cls):
        cls.build_codeable_concept(
            code="24484000", system="http://snomed.info/sct", text="Severe"
        )
