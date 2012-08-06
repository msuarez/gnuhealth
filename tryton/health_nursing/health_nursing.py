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
    _inherits = {'gnuhealth.patient.evaluation': 'rounding'}

    rounding = fields.Many2One('gnuhealth.patient.evaluation',
        'Patient Rounding')
    environmental_assessment = fields.Char('Environment', help="Environment" \
        "assessment . State any disorder in the room.") 
    
    # The 6 P's of rounding
    pain = fields.Integer('Pain', help="Enter the pain in a 1 to 10 scale")
    potty = fields.Boolean ('Potty', help="Check if the patient needs to urinate / defecate")
    position = fields.Boolean ('Position', help="Check if the patient needs to be repositioned or is unconfortable")
    proximity = fields.Boolean ('Proximity', help="Check if personal items, water, alarm, ... are not in easy reach")
    pump = fields.Boolean ('Pumps', help="Check if there is any issues with the pumps - IVs ... ")
    personal_needs = fields.Boolean ('Personal needs',help="Check if the patient requests anything")
    
    glycemia = fields.Float('Glycemia', help='Glucose level')

PatientRounding()
