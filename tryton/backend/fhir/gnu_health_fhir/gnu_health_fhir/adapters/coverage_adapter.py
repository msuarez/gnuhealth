from pendulum import instance, now, parse
from fhirclient.models.coverage import Coverage as fhir_coverage
from .base import BaseAdapter

__all__ = ["Coverage"]


class Coverage(BaseAdapter):
    @classmethod
    def to_fhir_object(cls, coverage):
        jsondict = {}
        jsondict["identifier"] = cls.build_fhir_identifier(coverage)
        jsondict["status"] = cls.build_fhir_status(coverage)
        jsondict["type"] = cls.build_fhir_type(coverage)
        jsondict["network"] = cls.build_fhir_network(coverage)
        jsondict["beneficiary"] = cls.build_fhir_beneficiary(coverage)
        jsondict["subscriberId"] = cls.build_fhir_subscriber_id(coverage)
        jsondict["period"] = cls.build_fhir_period(coverage)
        return fhir_coverage(jsondict=jsondict)

    @classmethod
    def get_fhir_resource_type(cls):
        return "Coverage"

    @classmethod
    def get_fhir_object_id_from_gh_object(cls, coverage):
        return coverage.id

    @classmethod
    def build_fhir_identifier(cls, coverage):
        return [{"value": coverage.number}]

    @classmethod
    def build_fhir_status(cls, coverage):
        if coverage.member_exp:
            if now() < parse(str(coverage.member_exp)):
                return "active"
            else:
                return "cancelled"
        else:  # assume active
            return "active"

    @classmethod
    def build_fhir_period(cls, coverage):
        period = {}
        if coverage.member_exp:
            period["end"] = parse(str(coverage.member_exp)).to_iso8601_string()
        if coverage.member_since:
            period["start"] = parse(str(coverage.member_since)).to_iso8601_string()
        return period

    @classmethod
    def build_fhir_type(cls, coverage):
        # TODO There are preferred codes in FHIR
        if coverage.insurance_type:
            return cls.build_codeable_concept(code=coverage.insurance_type)

    @classmethod
    def build_fhir_beneficiary(cls, coverage):
        # DEBUG Access patient from party
        return {
            "display": coverage.name.rec_name,
            # "reference": "".join(["Patient/", str(coverage.name.name.id)]),
        }

    @classmethod
    def build_fhir_network(cls, coverage):
        return coverage.company.rec_name

    @classmethod
    def build_fhir_subscriber_id(cls, coverage):
        return coverage.number
