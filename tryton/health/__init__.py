# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2008-2013  Luis Falcon <falcon@gnu.org>
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


def register():
    Pool.register(
        DrugDoseUnits,
        MedicationFrequency,
        DrugForm,
        DrugRoute,
        Occupation,
        Ethnicity,
        MedicalSpecialty,
        HealthProfessional,
        HealthProfessionalSpecialties,        
        PhysicianSP,
        OperationalArea,
        OperationalSector,
        Family,
        FamilyMember,
        DomiciliaryUnit,
        MedicamentCategory,
        Medicament,
        PathologyCategory,
        PathologyGroup,
        Pathology,
        DiseaseMembers,
        ProcedureCode,
        InsurancePlan,
        Insurance,
        AlternativePersonID,
        PartyPatient,
        PartyAddress,
        ProductCategory,
        ProductTemplate,
        Product,
        GnuHealthSequences,
        PatientData,
        PatientDiseaseInfo,
        Appointment,
        AppointmentReport,
        OpenAppointmentReportStart,
        PatientMedication,
        PatientVaccination,
        PatientPrescriptionOrder,
        PrescriptionLine,
        PatientEvaluation,
        Directions,
        SecondaryCondition,
        DiagnosticHypothesis,
        SignsAndSymptoms,
        HospitalBuilding,
        HospitalUnit,
        HospitalOR,
        HospitalWard,
        HospitalBed,
        module='health', type_='model')
    Pool.register(
        OpenAppointmentReport,
        module='health', type_='wizard')
