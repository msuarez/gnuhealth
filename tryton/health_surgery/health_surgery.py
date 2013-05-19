# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2008-2013  Luis Falcon <lfalcon@gnusolidario.org>
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
from trytond.model import ModelView, ModelSQL, fields
from datetime import datetime


__all__ = ['RCRI','Surgery', 'MedicalOperation', 'MedicalPatient']


class RCRI(ModelSQL, ModelView):
    'Revised Cardiac Risk Index'
    __name__ = 'gnuhealth.rcri'
    
    patient = fields.Many2One('gnuhealth.patient', 'Patient ID', required=True)
    rcri_date = fields.DateTime('Date', required=True)
    health_professional = fields.Many2One('gnuhealth.physician', 'Health Professional',
        help="Health professional / Cardiologist who signed the assesment RCRI")
    rcri_high_risk_surgery = fields.Boolean ('High Risk surgery',help='suprainguinal vascular, intraperitoneal, or intrathoracic surgery')
    rcri_ischemic_history = fields.Boolean ('History of ischemic heart disease')
    rcri_congestive_history = fields.Boolean ('History of congestive heart disease')
    rcri_diabetes_history = fields.Boolean ('Preoperative Diabetes')
    rcri_cerebrovascular_history = fields.Boolean ('History of Cerebrovascular disease')
    rcri_kidney_history = fields.Boolean ('Preoperative Kidney disease')
    
    rcri_total = fields.Integer('Score',
        on_change_with=['rcri_high_risk_surgery', 'rcri_ischemic_history',
        'rcri_congestive_history', 'rcri_diabetes_history', 'rcri_cerebrovascular_history', 'rcri_kidney_history'])

    rcri_class = fields.Selection([
        (None, ''),
        ('I', 'I'),
        ('II', 'II'),
        ('III', 'III'),
        ('IV', 'IV'),
        ], 'RCRI Class',sort=False,
        on_change_with=['rcri_high_risk_surgery', 'rcri_ischemic_history',
        'rcri_congestive_history', 'rcri_diabetes_history', 'rcri_cerebrovascular_history', 'rcri_kidney_history'])


    def on_change_with_rcri_total(self):
        
        total = 0
        if self.rcri_high_risk_surgery :
            total=total + 1
        if self.rcri_ischemic_history :
            total=total + 1
        if self.rcri_congestive_history :
            total=total + 1
        if self.rcri_diabetes_history :
            total=total + 1
        if self.rcri_kidney_history :
            total=total + 1
        if self.rcri_cerebrovascular_history :
            total=total + 1
            
        return total
        
    def on_change_with_rcri_class (self):
        rcri_class = ''
 
        total = 0
        if self.rcri_high_risk_surgery :
            total=total + 1
        if self.rcri_ischemic_history :
            total=total + 1
        if self.rcri_congestive_history :
            total=total + 1
        if self.rcri_diabetes_history :
            total=total + 1
        if self.rcri_kidney_history :
            total=total + 1
        if self.rcri_cerebrovascular_history :
            total=total + 1
        
        if total == 0:
            rcri_class = 'I'
        if total == 1:
            rcri_class = 'II'
        if total == 2:
            rcri_class = 'III'
        if (total > 2):
            rcri_class = 'IV'
            
        return rcri_class        

    @staticmethod
    def default_rcri_date():
        return datetime.now()

    @staticmethod
    def default_rcri_total():
        return 0

    @staticmethod
    def default_rcri_class():
        return 'I'

class Surgery(ModelSQL, ModelView):
    'Surgery'
    __name__ = 'gnuhealth.surgery'

    patient = fields.Many2One('gnuhealth.patient', 'Patient ID')
    admission = fields.Many2One('gnuhealth.appointment', 'Admission')
    operating_room = fields.Many2One('gnuhealth.hospital.or', 'Operating Room')
    code = fields.Char('Code', required=True, help="Health Center Unique code")
    procedures = fields.One2Many('gnuhealth.operation', 'name', 'Procedures',
        help="List of the procedures in the surgery. Please enter the first "
        "one as the main procedure")
    pathology = fields.Many2One('gnuhealth.pathology', 'Base condition',
        help="Base Condition / Reason")
    classification = fields.Selection([
        (None, ''),
        ('o', 'Optional'),
        ('r', 'Required'),
        ('u', 'Urgent'),
        ('e', 'Emergency'),
        ], 'Classification', sort=False)
    surgeon = fields.Many2One('gnuhealth.physician', 'Surgeon',
        help="Surgeon who did the procedure")
    anesthetist = fields.Many2One('gnuhealth.physician', 'Anesthetist',
        help="Anesthetist in charge")
    date = fields.DateTime('Date')
    age = fields.Char('Patient age',
        help="Patient age at the moment of the surgery. Can be estimative")
    description = fields.Char('Description', required=True)
    preop_mallampati = fields.Selection([
        (None, ''),
        ('Class 1', 'Class 1: Full visibility of tonsils, uvula and soft '
                    'palate'),
        ('Class 2', 'Class 2: Visibility of hard and soft palate, '
                    'upper portion of tonsils and uvula'),
        ('Class 3', 'Class 3: Soft and hard palate and base of the uvula are '
                    'visible'),
        ('Class 4', 'Class 4: Only Hard Palate visible'),
        ], 'Mallampati Score', sort=False)
    preop_bleeding_risk = fields.Boolean('Risk of Massive bleeding',
        help="Check this box if patient has a risk of loosing more than 500 "
        "ml in adults of over 7ml/kg in infants. If so, make sure that "
        "intravenous access and fluids are available")
    preop_oximeter = fields.Boolean('Pulse Oximeter in place',
        help="Check this box when verified the pulse oximeter is in place "
        "and functioning")
    preop_site_marking = fields.Boolean('Surgical Site Marking',
        help="The surgeon has marked the surgical incision")
    preop_antibiotics = fields.Boolean('Antibiotic Prophylaxis',
        help="Prophylactic antibiotic treatment within the last 60 minutes")
    preop_sterility = fields.Boolean('Sterility confirmed',
        help="Nursing team has confirmed sterility of the devices and room")
    preop_asa = fields.Selection([
        (None, ''),
        ('ps1', 'PS 1 : Normal healthy patient'),
        ('ps2', 'PS 2 : Patients with mild systemic disease'),
        ('ps3', 'PS 3 : Patients with severe systemic disease'),
        ('ps4', 'PS 4 : Patients with severe systemic disease that is a constant threat to life '),
        ('ps5', 'PS 5 : Moribund patients who are not expected to survive without the operation'),
        ('ps6', 'PS 6 : A declared brain-dead patient who organs are being removed for donor purposes'),
        ], 'ASA Preoperative Physical Status', sort=False)
    preop_rcri = fields.Many2One('gnuhealth.rcri', 'RCRI',
        help="Patient Revised Cardiac Risk Index")

    extra_info = fields.Text('Extra Info')


class MedicalOperation(ModelSQL, ModelView):
    'Operation - Surgical Procedures'
    __name__ = 'gnuhealth.operation'

    name = fields.Many2One('gnuhealth.surgery', 'Surgery')
    procedure = fields.Many2One('gnuhealth.procedure', 'Code', required=True,
        select=True,
        help="Procedure Code, for example ICD-10-PCS Code 7-character string")
    notes = fields.Text('Notes')


class MedicalPatient(ModelSQL, ModelView):
    'Add to the Medical patient_data class (medical.patient) the surgery ' \
    'field.'
    __name__ = 'gnuhealth.patient'

    surgery = fields.One2Many('gnuhealth.surgery', 'patient', 'Surgeries')
