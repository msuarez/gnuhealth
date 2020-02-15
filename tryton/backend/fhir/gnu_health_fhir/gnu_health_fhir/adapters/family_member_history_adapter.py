from fhirclient.models.familymemberhistory import FamilyMemberHistory as fhir_fmh
from pendulum import instance
from .base import BaseAdapter
from ..config import familyMember
from .patient_adapter import Patient

__all__ = ["FamilyMemberHistory"]


class FamilyMemberHistory(BaseAdapter):
    @classmethod
    def to_fhir_object(cls, member):
        # TODO Add more info to family history data model on Health side
        jsondict = {}
        jsondict["gender"] = cls.build_fhir_gender(member)
        jsondict["date"] = cls.build_fhir_date(member)
        jsondict["patient"] = cls.build_fhir_patient(member)
        jsondict["relationship"] = cls.build_fhir_relationship(member)
        jsondict["status"] = cls.build_fhir_status(member)
        jsondict["condition"] = cls.build_fhir_condition(member)
        return fhir_fmh(jsondict=jsondict)

    @classmethod
    def get_fhir_resource_type(cls):
        return "FamilyMemberHistory"

    @classmethod
    def get_fhir_object_id_from_gh_object(cls, member):
        return member.id

    @classmethod
    def build_fhir_gender(cls, member):
        # TODO Consider as helper / config
        ### NOTE KEEP THIS UPDATED ###
        # Possible selections (currently)
        #
        # Female
        # 'mother'
        # 'sister'
        # 'aunt'
        # 'niece'
        # 'grandmother'
        #
        # Male
        # 'father'
        # 'brother'
        # 'uncle'
        # 'nephew'
        # 'grandfather'
        #
        # Unknown
        # 'cousin'

        females = ["mother", "sister", "aunt", "niece", "grandmother"]
        males = ["father", "brother", "uncle", "nephew", "grandfather"]
        rel = member.relative
        if rel in females:
            g = "female"
        elif rel in males:
            g = "male"
        else:
            g = "unknown"
        return g

    @classmethod
    def build_fhir_date(cls, member):
        date = member.write_date or member.create_date
        if date:
            return instance(date).to_iso8601_string()

    @classmethod
    def build_fhir_patient(cls, member):
        return cls.build_fhir_reference_from_adapter_and_object(Patient, member.patient)

    @classmethod
    def build_fhir_relationship(cls, member):
        t = {"m": "maternal", "f": "paternal"}  # ignore sibling code
        k = " ".join((t.get(member.xory, ""), member.relative)).strip()
        info = [d for d in familyMember.contents if d["display"] == k]

        if info:
            return cls.build_codeable_concept(info[0]["code"], info[0]["system"], k)
        else:
            return cls.build_codeable_concept(code=k, text=k)

    @classmethod
    def build_fhir_status(cls, member):
        # TODO Unknown equivalent in Health
        return "completed"

    @classmethod
    def build_fhir_condition(cls, member):
        path = member.name
        if path:
            return [
                {
                    "code": cls.build_codeable_concept(
                        path.code,
                        "urn:oid:2.16.840.1.113883.6.90",
                        path.name,  # ICD-10-CM
                    )
                }
            ]
