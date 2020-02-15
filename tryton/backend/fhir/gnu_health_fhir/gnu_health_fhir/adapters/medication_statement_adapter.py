from gnu_health_fhir.common.utils import safe_attrgetter
from pendulum import instance
from fhirclient.models.medicationstatement import MedicationStatement as fhir_med
from .base import BaseAdapter
from .patient_adapter import Patient

__all__ = ["MedicationStatement"]


class MedicationStatement(BaseAdapter):
    @classmethod
    def to_fhir_object(cls, med):
        # TODO informationSource #See if we can determine this in Health?
        jsondict = {}
        jsondict["identifier"] = cls.build_fhir_identifier(med)
        jsondict["subject"] = cls.build_fhir_subject(med)
        jsondict["dateAsserted"] = cls.build_fhir_date_asserted(med)
        jsondict["status"] = cls.build_fhir_status(med)
        jsondict["dosage"] = cls.build_fhir_dosage(med)
        jsondict["taken"] = cls.build_fhir_taken(med)
        jsondict["reasonNotTaken"] = cls.build_fhir_reason_not_taken(med)
        jsondict["reasonCode"] = cls.build_fhir_reason_code(med)
        jsondict["effectivePeriod"] = cls.build_fhir_effective_period(med)
        jsondict["note"] = cls.build_fhir_note(med)
        jsondict[
            "medicationCodeableConcept"
        ] = cls.build_fhir_medication_codeable_concept(med)
        return fhir_med(jsondict=jsondict)

    @classmethod
    def get_fhir_resource_type(cls):
        return "MedicationStatement"

    @classmethod
    def get_fhir_object_id_from_gh_object(cls, med):
        return med.id

    @classmethod
    def build_fhir_identifier(cls, med):
        return [
            {
                "use": "official",
                "value": "-".join([med.medicament.rec_name, str(med.id)]),
            }
        ]

    @classmethod
    def build_fhir_subject(cls, med):
        return cls.build_fhir_reference_from_adapter_and_object(Patient, med.name)

    @classmethod
    def build_fhir_date_asserted(cls, med):
        # TODO accurate date
        date = med.create_date
        if date:
            return instance(date).to_iso8601_string()

    @classmethod
    def build_fhir_status(cls, med):
        if med.is_active:
            s = "active"
        elif med.course_completed:
            s = "completed"
        elif med.discontinued:
            s = "stopped"
        else:
            s = "intended"
        return s

    @classmethod
    def build_fhir_dosage(cls, med):
        # TODO Can always add more information!
        # TODO make into converter / config
        code_conv = {
            "seconds": "s",
            "minutes": "min",
            "hours": "h",
            "days": "d",
            "months": "mo",
            "years": "a",
        }
        dose = {}
        # Amount (this should be listed, but could be patient reported)
        if med.dose:
            dose["doseQuantity"] = {"value": med.dose, "unit": med.dose_unit.name}

        # Route
        #     TODO Standard route values
        route = med.route
        if route:
            cc = {}
            c = {}
            cc["text"] = c["display"] = route.name
            c["code"] = route.code
            cc["coding"] = [c]
            dose["route"] = cc

        # PRN
        if med.frequency_prn or (
            safe_attrgetter(med, "common_dosage.abbreviation") == "prn"
        ):
            dose["asNeededBoolean"] = True
        else:
            dose["asNeededBoolean"] = False

        # TODO
        # Site and Method

        # timing
        # BID | TID | QID | AM | PM | QD | QOD | Q4H | Q6H +.
        timing = {}
        if med.frequency:  # prefer specific information
            rep = {}
            if med.duration_period != "indefinite":
                rep["duration"] = med.duration
                rep["durationUnits"] = code_conv.get(med.duration_period)

            # Health stores timing as 1 per X s/min/hr
            rep["frequency"] = "1"
            rep["period"] = med.frequency
            rep["periodUnits"] = code_conv.get(med.frequency_unit)

            timing["repeat"] = rep

        elif med.common_dosage:

            c = {
                "display": med.common_dosage.abbreviation,
                "system": "http://snomed.info/sct",
                "code": med.common_dosage.code,
            }

            timing["code"] = {"text": med.common_dosage.name, "coding": [c]}

        else:  # No dosage information (either unknown or incomplete)
            timing = None
        if timing:
            dose["timing"] = timing

        # Rate - rateRatio
        #    Only if an infusion -- always mL/hr (I think?)
        if med.infusion:
            num = {"value": med.infusion_rate, "unit": "mL"}
            den = {"value": 1, "unit": "hr"}
            dose["rateRatio"] = {"numerator": num, "denominator": den}
        return [dose]

    @classmethod
    def build_fhir_taken(cls, med):
        # TODO Health equivalent?
        # y | n | unk | na
        if not med.discontinued:
            return "y"
        else:
            return "n"

    @classmethod
    def build_fhir_reason_not_taken(cls, med):
        if med.discontinued:
            return {"text": med.discontinued_reason or "<unknown>"}

    @classmethod
    def build_fhir_reason_code(cls, med):
        # TODO Ideally should make indication connect to patient condition
        cls.build_codeable_concept(
            med.indication.code,
            "urn:oid:2.16.840.1.113883.6.90",  # ICD-10-CM
            med.indication.name,
        )

    @classmethod
    def build_fhir_effective_period(cls, med):
        start, end = med.start_treatment, med.end_treatment
        if start:
            p = {"start": instance(start).to_iso8601_string()}
            if end:
                p["end"] = instance(end).to_iso8601_string()
            return p

    @classmethod
    def build_fhir_note(cls, med):
        if med.notes:
            return {"text": med.notes}

    @classmethod
    def build_fhir_medication_codeable_concept(cls, med):
        # TODO Fill this out more
        return {"text": med.medicament.rec_name}
