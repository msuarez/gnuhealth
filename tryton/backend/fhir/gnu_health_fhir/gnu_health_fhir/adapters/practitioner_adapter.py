from operator import attrgetter
from pendulum import instance
from fhirclient.models.practitioner import Practitioner as fhir_practitioner
from .base import BaseAdapter
from re import sub

__all__ = ["Practitioner"]


class Practitioner(BaseAdapter):
    @classmethod
    def to_fhir_object(cls, hp):
        jsondict = {}
        jsondict["active"] = cls.build_fhir_active(hp)
        jsondict["telecom"] = cls.build_fhir_telecom(hp)
        jsondict["name"] = cls.build_fhir_name(hp)
        jsondict["identifier"] = cls.build_fhir_identifier(hp)
        jsondict["gender"] = cls.build_fhir_gender(hp)
        jsondict["communication"] = cls.build_fhir_communication(hp)
        return fhir_practitioner(jsondict=jsondict)

    @classmethod
    def get_fhir_resource_type(cls):
        return "Practitioner"

    @classmethod
    def get_fhir_object_id_from_gh_object(cls, hp):
        return hp.id

    @classmethod
    def build_fhir_active(cls, hp):
        return hp.name.active

    @classmethod
    def build_fhir_telecom(cls, hp):
        return cls.build_fhir_telecom_for_person(hp.name)

    @classmethod
    def build_fhir_name(cls, hp):
        return cls.build_fhir_name_for_person(hp.name)

    @classmethod
    def build_fhir_identifier(cls, hp):
        idents = []
        if hp.puid:
            i = {
                "use": "usual",
                "value": hp.puid or "<UNKNOWN>",
                "type": {"text": "PUID/MRN"},
            }
            idents.append(i)

        for alt in hp.name.alternative_ids:
            i = {
                "use": "official",
                "value": alt.code or "<UNKNOWN>",
                "type": {"text": alt.alternative_id_type},
            }
            idents.append(i)
        return idents

    @classmethod
    def build_fhir_gender(cls, hp):
        g = hp.name.gender
        if g:
            if g == "f":
                l = "female"
            elif g == "m":
                l = "male"
            else:
                l = "other"
        else:
            l = "unknown"
        return l

    @classmethod
    def build_fhir_communication(cls, hp):
        lang = hp.name.lang
        if lang:
            return [
                cls.build_codeable_concept(
                    sub("_", "-", lang.code), "urn:ietf:bcp:47", lang.name
                )
            ]

        # TODO Handle the specialties and roles better
        #     Specifically, output better job titles -- e.g., radiology tech, etc.
        # inst = self.hp.institution
        # occ = self.hp.name.occupation.name #Is this the right place for employee job title?

        # role = CodeableConcept(text=occ, coding=[Coding(display=occ)])

        # organization = Reference(display=inst.rec_name,
        # reference='/'.join(['Organization', str(inst.id)]))

        # specialties = []
        # for spec in self.hp.specialties:
        # code, name = attrgetter('specialty.code', 'specialty.name')(spec)
        # cc = CodeableConcept(text=name)
        # cc.coding = [Coding(code=code,
        # display=name)]
        # specialties.append(cc)

        # pr = practitionerRole(role=role, specialty=specialties,
        # managingOrganization=organization)
