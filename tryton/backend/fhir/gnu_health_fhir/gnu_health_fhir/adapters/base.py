from pendulum import instance, parse
from ..common import helper_mixin

__all__ = ["BaseAdapter"]


class BaseAdapter(helper_mixin):
    """The base adapter class:
            - defines multiple functions to be implemented by child classes (CRUD)
            - conversion methods
            - helper methods
    """

    ##### CONVERSION ######
    @classmethod
    def to_fhir_object(cls, gh_object):
        raise NotImplemented()

    @classmethod
    def to_health_object(cls, fhir_object):
        raise NotImplemented()

    ###### CRUD #######
    @classmethod
    def read(cls, gh_object):
        raise NotImplemented()

    @classmethod
    def create(cls, fhir_objects):
        raise NotImplemented()

    @classmethod
    def update(cls, fhir_obj, gh_object):
        raise NotImplemented()

    @classmethod
    def delete(cls, gh_object):
        raise NotImplemented()

    ##### REFERENCE CONVERSIONS #####

    @classmethod
    def get_fhir_object_id_from_gh_object(cls, gh_object):
        raise NotImplemented("Each adapter should implement this method")

    @classmethod
    def get_fhir_resource_type(cls):
        raise NotImplemented("Each adapter should implement this method")

    @classmethod
    def get_gh_object_from_fhir_reference(cls, reference):
        """Assume <Resource>/<id>"""
        raise NotImplemented()

    @classmethod
    def build_fhir_reference_from_adapter_and_object(cls, adapter, gh_object):
        if gh_object is None:
            return None
        return {
            "display": gh_object.rec_name,
            "reference": "/".join(
                [
                    adapter.get_fhir_resource_type(),
                    str(adapter.get_fhir_object_id_from_gh_object(gh_object)),
                ]
            ),
        }

    ##### HELPER METHODS #####

    @classmethod
    def build_fhir_name_for_person(cls, gh_person_object):
        """Assumes model from party.party"""
        names = []
        for name in gh_person_object.person_names:
            n = {}
            n["given"] = [x for x in name.given.split()]
            n["family"] = name.family if name.family else "<unknown>"
            n["prefix"] = [name.prefix] if name.prefix else []
            n["suffix"] = [name.suffix] if name.suffix else []
            n["use"] = name.use if name.use else "<unknown>"
            if name.date_from:
                n["period"] = {"start": parse(str(name.date_from)).to_iso8601_string()}
                if name.date_to:
                    n["period"]["end"] = parse(str(name.date_to)).to_iso8601_string()
            names.append(n)
        return names

    @classmethod
    def build_fhir_telecom_for_person(cl, gh_person_object):
        """Assumes model from party.party"""
        telecom = []
        for contact in gh_person_object.contact_mechanisms:
            c = {}
            c["value"] = contact.value
            if contact.type == "phone":
                c["system"] = "phone"
                c["use"] = "home"
            elif contact.type == "mobile":
                c["system"] = "phone"
                c["use"] = "mobile"
            else:
                c["use"] = c["system"] = contact.type
            telecom.append(c)
        return telecom
