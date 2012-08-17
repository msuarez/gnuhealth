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
from trytond.pyson import Eval, Not, Bool
from datetime import datetime
from trytond.pool import Pool


# Class : PatientRounding
# Assess the patient and evironment periodically
# Usually done by nurses

class PatientRounding(ModelSQL, ModelView):
    'Patient Rounding'
    _name = 'gnuhealth.patient.rounding'
    _description = __doc__


    patient = fields.Many2One('gnuhealth.patient', 'Patient')
    health_professional = fields.Many2One('gnuhealth.physician', 'Health Professional', readonly=True)

    evaluation_start = fields.DateTime('Start', required=True)
    evaluation_endtime = fields.DateTime('End', required=True)

    environmental_assessment = fields.Char('Environment', help="Environment" \
        "assessment . State any disorder in the room.") 
    
    # The 6 P's of rounding
    pain = fields.Integer('Pain', help="Enter the pain in a 1 to 10 scale")
    potty = fields.Boolean ('Potty', help="Check if the patient needs to urinate / defecate")
    position = fields.Boolean ('Position', help="Check if the patient needs to be repositioned or is unconfortable")
    proximity = fields.Boolean ('Proximity', help="Check if personal items, water, alarm, ... are not in easy reach")
    pump = fields.Boolean ('Pumps', help="Check if there is any issues with the pumps - IVs ... ")
    personal_needs = fields.Boolean ('Personal needs',help="Check if the patient requests anything")

    # Vital Signs
    systolic = fields.Integer('Systolic Pressure')
    diastolic = fields.Integer('Diastolic Pressure')
    bpm = fields.Integer('Heart Rate',
        help='Heart rate expressed in beats per minute')
    respiratory_rate = fields.Integer('Respiratory Rate',
        help='Respiratory rate expressed in breaths per minute')
    osat = fields.Integer('Oxygen Saturation',
        help='Oxygen Saturation(arterial).')
    temperature = fields.Float('Temperature',
        help='Temperature in celcius')

    weight = fields.Float('Weight', help='Weight in Kilos')
    height = fields.Float('Height', help='Height in centimeters, eg 175')
    bmi = fields.Float('Body Mass Index',
        on_change_with=['weight', 'height', 'bmi'])

    #Glycemia
    glycemia = fields.Float('Glycemia', help='Blood Glucose level')
    
    depression = fields.Boolean ('Depression signs',help="Check this if the patient shows signs of depression")

    evolution = fields.Selection([
        ('n', 'Status Quo'),
        ('i', 'Improving'),
        ('w', 'Worsening'),
        ], 'Evolution', required=True, help="Check your judgement of current patient condition", sort=False)

    round_summary = fields.Text('Round Summary')

PatientRounding()
