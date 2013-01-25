# -*- coding: utf-8 -*-
#    Copyright (C) 2008-2013  Luis Falcon
#    Copyright (C) 2012-2012  Sebastián Marró

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import datetime as dt
from datetime import timedelta, datetime
import random
import linecache

from proteus import config, Model, Wizard

config = config.set_trytond('gnuhealth_demo', database_type='postgresql', 
    user='admin', password='admin')

def RandomDate(start, end):
    """
    This function will return a random datetime between two datetime 
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return (start + timedelta(seconds=random_second))

def InitDatabase():
    Module = Model.get('ir.module.module')
    health_profile, = Module.find([('name', '=', 'health_profile')])
    Module.install([health_profile.id], config.context)
    Wizard('ir.module.module.install_upgrade').execute('upgrade')

def LoadBetzFamilyInfo():
    Party = Model.get('party.party')
    User = Model.get('res.user')
    Family = Model.get('gnuhealth.family')
    FamilyMember = Model.get('gnuhealth.family_member')
    Patient = Model.get('gnuhealth.patient')
    Physician = Model.get('gnuhealth.physician')
    MedicalSpecialty = Model.get('gnuhealth.specialty')
    Occupation = Model.get('gnuhealth.occupation')
    Pathology = Model.get('gnuhealth.pathology')
    PatientDiseaseInfo = Model.get('gnuhealth.patient.disease')
    PatientMedication = Model.get('gnuhealth.patient.medication')
    MedicationTemplate = Model.get('gnuhealth.medication.template')
    Medicament = Model.get('gnuhealth.medicament')
    FamilyDiseases = Model.get('gnuhealth.patient.family.diseases')
    PatientGeneticRisk = Model.get('gnuhealth.patient.genetic.risk')
    DiseaseGene = Model.get('gnuhealth.disease.gene')
    Newborn = Model.get('gnuhealth.newborn')

    party = Party()
    party.name = 'GNU SOLIDARIO Hospital'
    party.is_institution = True
    party.save()

    party = Party()
    party.name = 'Insurator'
    party.is_insurance_company = True
    party.save()

    party = Party()
    party.name = 'Cameron'
    party.lastname = 'Cordara'
    party.is_doctor = True
    party.is_person = True
    party.internal_user, = User.find([('login', '=', 'admin')])
    party.save()

    physician = Physician()
    physician.name = party
    physician.specialty, = MedicalSpecialty.find([('code', '=', 'GP')])
    physician.code = '765870'
    physician.save()

    party = Party()
    party.name = 'John'
    party.lastname = 'Betz'
    party.ref = '55576584'
    party.is_patient = True
    party.is_person = True
    party.save()

    party = Party()
    party.name = 'Ana'
    party.lastname = 'Betz'
    party.ref = '55567890'
    party.is_patient = True
    party.is_person = True
    party.save()

    family = Family()
    family.name = 'Betz family'
    family.save()

    FamilyMember(name=family, party=party, role='Mother').save()

    family_member = FamilyMember()
    family_member.name = family
    family_member.party, = Party.find([('ref', '=', '55576584')])
    family_member.role = 'Father'
    family_member.save()

    patient = Patient()
    patient.name = party
    patient.sex = 'f'
    patient.dob = datetime.strptime('10/4/1985', '%m/%d/%Y')
    patient.marital_status = 'm'
    patient.primary_care_doctor = physician
    patient.occupation, = Occupation.find([('name', '=', 'Teacher')])
    patient.ses = '2'
    patient.housing = '2'
    patient.education = '5'
    patient.critical_info = 'β-lactam hypersensitivity'
    patient.gpa = 'G1P1A0'
    patient.ex_smoker = True
    patient.sexual_preferences = 'h'
    patient.sexual_partners = 'm'
    patient.sexual_practices = 's'
    patient.save()

    patient_disease = PatientDiseaseInfo()
    patient_disease.name = patient
    patient_disease.pathology, = Pathology.find([
        ('name', '=', 'Insulin-dependent diabetes mellitus'),
    ])
    patient_disease.diagnosed_date = datetime.strptime('11/10/1993', '%m/%d/%Y')
    patient_disease.save()

    medication_template = MedicationTemplate()
    medication_template.medicament, = Medicament.find([
        ('name.name', '=', 'insulin injection (soluble)'),
    ])
    medication_template.indication, = Pathology.find([
        ('name', '=', 'Insulin-dependent diabetes mellitus'),
    ])
    medication_template.start_treatment = datetime.strptime('11/10/1993', '%m/%d/%Y')
    medication_template.save()

    patient_medication = PatientMedication()
    patient_medication.template = medication_template
    patient_medication.name = patient
    patient_medication.doctor = physician
    patient_medication.is_active = True
    patient_medication.diagnosed_date = datetime.strptime('11/10/1993', '%m/%d/%Y')
    patient_medication.save()

    family_diseases = FamilyDiseases()
    family_diseases.patient = patient
    family_diseases.name, = Pathology.find([('name', '=', "Marfan's syndrome")])
    family_diseases.xory = 'm'
    family_diseases.relative = 'grandfather'
    family_diseases.save()

    family_diseases = FamilyDiseases()
    family_diseases.patient = patient
    family_diseases.name, = Pathology.find([
        ('name', '=', 'Essential (primary) hypertension'),
    ])
    family_diseases.xory = 'f'
    family_diseases.relative = 'father'
    family_diseases.save()

    patient_genetic_risk = PatientGeneticRisk()
    patient_genetic_risk.patient = patient
    patient_genetic_risk.disease_gene, = DiseaseGene.find([('name', '=', 'BRCA1')])
    patient_genetic_risk.save()

    newborn = Newborn()
    newborn.mother = patient
    newborn.newborn_name = 'Matt'
    newborn.birth_date = datetime.strptime('3/15/2010', '%m/%d/%Y')
    newborn.sex = 'm'
    newborn.save()

if __name__ == '__main__':
    InitDatabase()
    LoadBetzFamilyInfo()
