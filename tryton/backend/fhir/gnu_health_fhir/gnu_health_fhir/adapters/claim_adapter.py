from fhirclient.models.claim import Claim as fhir_claim
from .base import BaseAdapter

__all__ = ["Claim"]


class Claim(BaseAdapter):
    @classmethod
    def to_fhir_object(cls, claim):
        jsondict = {}
        jsondict["identifier"] = cls.build_fhir_identifier(claim)
        jsondict["status"] = cls.build_fhir_status(claim)
        jsondict["type"] = cls.build_fhir_type(claim)
        jsondict["network"] = cls.build_fhir_network(claim)
        jsondict["beneficiary"] = cls.build_fhir_beneficiary(claim)
        jsondict["subscriberId"] = cls.build_fhir_subscriber_id(claim)
        jsondict["period"] = cls.build_fhir_period(claim)
        return fhir_claim(jsondict=jsondict)

    @classmethod
    def get_fhir_resource_type(cls):
        return "Claim"

    @classmethod
    def get_fhir_object_id_from_gh_object(cls, coverage):
        return claim.id
