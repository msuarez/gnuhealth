from trytond.pool import Pool
from .health_synchro import *


def register():
    Pool.register(
        Party,
        PartyAddress,
        OperationalArea,
        OperationalSector,
        DomiciliaryUnit,
        MedicalSpecialty,
        HealthInstitution,
        HealthInstitutionSpecialties,
        HealthInstitutionOperationalSector,
        AlternativePersonID,
        PatientData, 
        #Appointment, 
        #DiagnosticHypothesis, 
        #HealthProfessional, 
        #HospitalUnit, 
        #HospitalWard, 
        #HealthProfessionalSpecialties, 
        #PathologyCategory, 
        #PatientDiseaseInfo, 
        #PatientEvaluation, 
        #PatientVaccination, 
        #SecondaryCondition, 
        #SignsAndSymptoms,
        module='health_synchro', type_='model')
