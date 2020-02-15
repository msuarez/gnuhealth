class encounterStatus:
    contents = [
        {
            "code": "planned",
            "display": "Planned",
            "description": "The encounter has not started",
        },
        {
            "code": "arrived",
            "display": "Arrived",
            "description": "The Patient is present for the encounter, however is not currently meeting with a practitioner.",
        },
        {
            "code": "triaged",
            "display": "Triaged",
            "description": "The patient has been assessed for the priority of their treatment based on the severity of their condition.",
        },
        {
            "code": "in-progress",
            "display": "In Progress",
            "description": "The Encounter has begun and the patient is present / the practitioner and the patient are meeting.",
        },
        {
            "code": "onleave",
            "display": "On Leave",
            "description": "The Encounter has begun, but the patient is temporarily on leave.",
        },
        {
            "code": "finished",
            "display": "Finished",
            "description": "The Encounter has ended.",
        },
        {
            "code": "cancelled",
            "display": "Cancelled",
            "description": "The Encounter has ended before it has begun.",
        },
        {
            "code": "entered-in-error",
            "display": "Entered in Error",
            "description": "This instance should not have been part of this patient's medical record.",
        },
        {
            "code": "unknown",
            "display": "Unknown",
            "description": "The encounter status is unknown. Note that 'unknown' is a value of last resort and every attempt should be made to provide a meaningful value other than 'unknown'.",
        },
    ]


__all__ = ["encounterStatus"]
