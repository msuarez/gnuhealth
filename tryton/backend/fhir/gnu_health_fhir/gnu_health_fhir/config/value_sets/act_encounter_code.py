class actEncounterCode:
    contents = [
        {
            "code": "AMB",
            "display": "ambulatory",
            "description": "A comprehensive term for health care provided in a healthcare facility (e.g. a practitioner's office, clinic setting, or hospital) on a nonresident basis. The term ambulatory usually implies that the patient has come to the location and is not assigned to a bed. Sometimes referred to as an outpatient encounter.",
        },
        {
            "code": "EMER",
            "display": "emergency",
            "description": "A patient encounter that takes place at a dedicated healthcare service delivery location where the patient receives immediate evaluation and treatment, provided until the patient can be discharged or responsibility for the patient's care is transferred elsewhere (for example, the patient could be admitted as an inpatient or transferred to another facility.)",
        },
        {
            "code": "FLD",
            "display": "field",
            "description": "A patient encounter that takes place both outside a dedicated service delivery location and outside a patient's residence. Example locations might include an accident site and at a supermarket.",
        },
        {
            "code": "HH",
            "display": "home health",
            "description": "Healthcare encounter that takes place in the residence of the patient or a designee",
        },
        {
            "code": "IMP",
            "display": "inpatient encounter",
            "description": "A patient encounter where a patient is admitted by a hospital or equivalent facility, assigned to a location where patients generally stay at least overnight and provided with room, board, and continuous nursing service.",
        },
        {
            "code": "ACUTE",
            "display": "inpatient",
            "description": "An acute inpatient encounter.",
        },
        {
            "code": "NONAC",
            "display": "inpatient non-acute",
            "description": "Any category of inpatient encounter except 'acute'",
        },
        {
            "code": "PRENC",
            "display": "pre-admission",
            "description": "A patient encounter where patient is scheduled or planned to receive service delivery in the future, and the patient is given a pre-admission account number. When the patient comes back for subsequent service, the pre-admission encounter is selected and is encapsulated into the service registration, and a new account number is generated. Usage Note: This is intended to be used in advance of encounter types such as ambulatory, inpatient encounter, virtual, etc.",
        },
        {
            "code": "SS",
            "display": "short stay",
            "description": "An encounter where the patient is admitted to a health care facility for a predetermined length of time, usually less than 24 hours.",
        },
        {
            "code": "VR",
            "display": "virtual",
            "description": "A patient encounter where the patient and the practitioner(s) are not in the same physical location. Examples include telephone conference, email exchange, robotic surgery, and televideo conference.",
        },
    ]


__all__ = ["actEncounterCode"]
