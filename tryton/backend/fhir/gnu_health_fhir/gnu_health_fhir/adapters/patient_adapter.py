from gnu_health_fhir.common.utils import safe_attrgetter
from pendulum import instance
from fhirclient.models.patient import Patient as fhir_patient
from .base import BaseAdapter
from .practitioner_adapter import Practitioner
from ..config import MaritalStatus as ms
from re import sub

__all__ = ["Patient"]


class Patient(BaseAdapter):
    @classmethod
    def to_fhir_object(cls, patient):
        # TODO Add general_info field - where appropriate?
        # TODO Link - other links to same person
        # TODO Photo - Figure out contentType of photo
        # TODO managingOrganization
        jsondict = {}
        jsondict["identifier"] = cls.build_fhir_identifier(patient)
        jsondict["name"] = cls.build_fhir_name(patient)
        jsondict["telecom"] = cls.build_fhir_telecom(patient)
        jsondict["birthDate"] = cls.build_fhir_birthdate(patient)
        jsondict["deceasedBoolean"] = cls.build_fhir_deceased_boolean(patient)
        jsondict["deceasedDateTime"] = cls.build_fhir_deceased_datetime(patient)
        jsondict["address"] = cls.build_fhir_address(patient)
        jsondict["gender"] = cls.build_fhir_gender(patient)
        jsondict["generalPractitioner"] = cls.build_fhir_general_practitioner(patient)
        jsondict["active"] = cls.build_fhir_active(patient)
        jsondict["maritalStatus"] = cls.build_fhir_marital_status(patient)
        jsondict["communication"] = cls.build_fhir_communication(patient)
        return fhir_patient(jsondict=jsondict)

    @classmethod
    def get_fhir_object_id_from_gh_object(cls, patient):
        return patient.id

    @classmethod
    def get_fhir_resource_type(cls):
        return "Patient"

    @classmethod
    def build_fhir_identifier(cls, patient):
        idents = []
        if patient.puid:
            i = {}
            i["use"] = "usual"
            i["value"] = patient.puid or "<UNKNOWN>"
            i["type"] = {"text": "PUID/MRN"}
            idents.append(i)

        for alt in patient.name.alternative_ids:
            i = {}
            i["use"] = "official"
            i["value"] = alt.code or "<UNKNOWN>"
            i["type"] = {"text": alt.alternative_id_type}
            idents.append(i)

        return idents

    @classmethod
    def build_fhir_name(cls, patient):
        return cls.build_fhir_name_for_person(patient.name)

    @classmethod
    def build_fhir_telecom(cls, patient):
        return cls.build_fhir_telecom_for_person(patient.name)

    @classmethod
    def build_fhir_gender(cls, patient):
        # TODO Mate helper function
        # NOTE This is a difficult decision - what is gender for record-keeping
        # Currently, simply take biological sex and make further decisions later
        bs = patient.biological_sex
        g = None
        if bs:
            if bs == "f":
                g = "female"
            elif bs == "m":
                g = "male"
            else:
                g = "other"

        else:
            g = "unknown"
        return g

    @classmethod
    def build_fhir_birthdate(cls, patient):
        try:
            return instance(patient.name.dob).to_iso8601_string()
        except:
            return None

    @classmethod
    def build_fhir_deceased_boolean(cls, patient):
        return patient.deceased

    @classmethod
    def build_fhir_deceased_datetime(cls, patient):
        try:
            return instance(patient.dod).to_iso8601_string()
        except:
            return None

    @classmethod
    def build_fhir_address(cls, patient):
        # Only one currently
        du = patient.name.du
        if du:
            ad = {}
            ad["use"] = "home"
            ad["type"] = "physical"  # TODO Check for this
            ad["text"] = patient.name.du_address
            line = []
            number, street, zip_, city, state, country = safe_attrgetter(
                du,
                "address_street_number",
                "address_street",
                "address_zip",
                "address_city",
                "address_subdivision.name",
                "address_country.name",
            )

            if number:
                line.append(str(number))

            if street:
                line.append(street)

            if line:
                ad["line"] = [" ".join(line)]

            if city:
                ad["city"] = city

            if state:
                ad["state"] = state

            if zip_:
                ad["postalCode"] = zip_

            if country:
                ad["country"] = country

            return [ad]

    @classmethod
    def build_fhir_active(cls, patient):
        return patient.name.active

    @classmethod
    def build_fhir_general_practitioner(cls, patient):
        pcp = patient.primary_care_doctor
        if pcp:
            return [cls.build_fhir_reference_from_adapter_and_object(Practitioner, pcp)]

    @classmethod
    def build_fhir_communication(cls, patient):
        lang = patient.name.lang
        if lang:
            return [
                {
                    "preferred": "true",
                    "language": cls.build_codeable_concept(
                        sub("_", "-", lang.code),  # Standard requires dashes
                        "urn:ietf:bcp:47",
                        lang.name,
                    ),
                }
            ]

        # import base64
        # if patient.name.photo:
        # b64 = base64.encodestring(patient.name.photo.decode('utf-8')) #Standard requires base64
        # if b64:
        # jsondict['photo'] = {'data': b64}]

    @classmethod
    def build_fhir_marital_status(cls, patient):
        return ms.build_fhir_object_from_health(patient.name.marital_status)
