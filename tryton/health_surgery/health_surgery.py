# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2008-2012  Luis Falcon <lfalcon@gnusolidario.org>
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


class Surgery(ModelSQL, ModelView):
    'Surgery Functionality'
    _name = 'gnuhealth.surgery'
    _description = __doc__

    patient = fields.Many2One('gnuhealth.patient', 'Patient ID')
    admission = fields.Many2One('gnuhealth.appointment', 'Admission')
    operating_room = fields.Many2One('gnuhealth.hospital.or', 'Operating Room')
    code = fields.Char('Code', required=True, help="Health Center Unique code")
    procedures = fields.One2Many('gnuhealth.operation', 'name', 'Procedures',
        help="List of the procedures in the surgery. Please enter the first " \
        "one as the main procedure")
    pathology = fields.Many2One('gnuhealth.pathology', 'Base condition',
        help="Base Condition / Reason")
    classification = fields.Selection([
        ('o', 'Optional'),
        ('r', 'Required'),
        ('u', 'Urgent'),
        ], 'Classification', sort=False)
    surgeon = fields.Many2One('gnuhealth.physician', 'Surgeon',
        help="Surgeon who did the procedure")
    anesthetist = fields.Many2One('gnuhealth.physician', 'Anesthetist',
        help="Anesthetist in charge")
    date = fields.DateTime('Date')
    age = fields.Char('Patient age',
        help="Patient age at the moment of the surgery. Can be estimative")
    description = fields.Char('Description', required = True)
    preop_mallampati = fields.Selection([
        ('Class 1', 'Class 1: Full visibility of tonsils, uvula and soft palate'),
        ('Class 2', 'Class 2: Visibility of hard and soft palate, ' \
                    'upper portion of tonsils and uvula'),
        ('Class 3', 'Class 3: Soft and hard palate and base of the uvula are visible'),
        ('Class 4', 'Class 4: Only Hard Palate visible'),
        ], 'Mallampati Score', sort=False)
    preop_bleeding_risk = fields.Boolean('Risk of Massive bleeding',
        help="Check this box if patient has a risk of loosing more than 500 " \
        "ml in adults of over 7ml/kg in infants. If so, make sure that " \
        "intravenous access and fluids are available")
    preop_oximeter = fields.Boolean('Pulse Oximeter in place',
        help="Check this box when verified the pulse oximeter is in place " \
        "and functioning")
    preop_site_marking = fields.Boolean('Surgical Site Marking',
        help="The surgeon has marked the surgical incision")
    preop_antibiotics = fields.Boolean('Antibiotic Prophylaxis',
        help="Prophylactic antibiotic treatment within the last 60 minutes")
    preop_sterility = fields.Boolean('Sterility confirmed',
        help="Nursing team has confirmed sterility of the devices and room")
    extra_info = fields.Text('Extra Info')

Surgery()


class MedicalOperation(ModelSQL, ModelView):
    'Operation - Surgical Procedures'
    _name = 'gnuhealth.operation'
    _description = __doc__

    name = fields.Many2One('gnuhealth.surgery', 'Surgery')
    procedure = fields.Many2One('gnuhealth.procedure', 'Code', required=True,
        select=True,
        help="Procedure Code, for example ICD-10-PCS Code 7-character string")
    notes = fields.Text('Notes')

MedicalOperation()


class MedicalPatient(ModelSQL, ModelView):
    'Add to the Medical patient_data class (medical.patient) the surgery ' \
    'field.'
    _name = 'gnuhealth.patient'
    _description = __doc__

    surgery = fields.One2Many('gnuhealth.surgery', 'patient', 'Surgeries')

MedicalPatient()
