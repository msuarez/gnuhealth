# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2008-2017 Luis Falcon <lfalcon@gnusolidario.org>
#    Copyright (C) 2011-2017 GNU Solidario <health@gnusolidario.org>
#
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from trytond.pool import Pool
from .health import *
from .wizard import *
from .report import *

def register():
    Pool.register(
        OperationalArea,
        OperationalSector,
        DomiciliaryUnit,
        Occupation,
        Ethnicity,
        BirthCertificate,
        DeathCertificate,
        Party,
        ContactMechanism,
        PersonName,
        PartyAddress,
        DrugDoseUnits,
        MedicationFrequency,
        DrugForm,
        DrugRoute,
        MedicalSpecialty,
        HealthInstitution,
        HealthInstitutionSpecialties,
        HealthInstitutionOperationalSector,
        HealthInstitutionO2M,
        HospitalBuilding,
        HospitalUnit,
        HospitalOR,
        HospitalWard,
        HospitalBed,
        HealthProfessional,
        HealthProfessionalSpecialties,        
        PhysicianSP,
        Family,
        FamilyMember,
        MedicamentCategory,
        Medicament,
        ImmunizationSchedule,
        ImmunizationScheduleLine,
        ImmunizationScheduleDose,
        PathologyCategory,
        PathologyGroup,
        Pathology,
        DiseaseMembers,
        BirthCertExtraInfo,
        DeathCertExtraInfo,
        DeathUnderlyingCondition,
        ProcedureCode,
        InsurancePlan,
        Insurance,
        AlternativePersonID,
        Product,
        GnuHealthSequences,
        PatientData,
        PatientDiseaseInfo,
        Appointment,
        AppointmentReport,
        OpenAppointmentReportStart,
        PatientPrescriptionOrder,
        PrescriptionLine,
        PatientMedication,
        PatientVaccination,
        PatientEvaluation,
        Directions,
        SecondaryCondition,
        DiagnosticHypothesis,
        SignsAndSymptoms,
        PatientECG,
        CheckImmunizationStatusInit,
        ProductTemplate,
        module='health', type_='model')
    Pool.register(
        OpenAppointmentReport,
        CreateAppointmentEvaluation,
        CheckImmunizationStatus,
        module='health', type_='wizard')
    Pool.register(
        PatientDiseaseReport,
        PatientMedicationReport,
        PatientVaccinationReport,
        ImmunizationStatusReport,
        module='health', type_='report')
