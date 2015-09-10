# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2008-2015 Luis Falcon <lfalcon@gnusolidario.org>
#    Copyright (C) 2011-2015 GNU Solidario <health@gnusolidario.org>
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
from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta, date
from sql import Literal, Join, Table
from trytond.model import ModelView, ModelSingleton, ModelSQL, fields
from trytond.transaction import Transaction
from trytond import backend
from trytond.pyson import Eval, Not, Bool, PYSONEncoder, Equal, And, Or, If
from trytond.pool import Pool
import string
import pytz

__all__ = ['BodyFunctionCategory','BodyFunction',
    'BodyStructureCategory','BodyStructure',
    'ActivityAndParticipationCategory', 'ActivityAndParticipation',
    'EnvironmentalFactorCategory','EnvironmentalFactor',
    'PatientDisabilityAssessment',
    'PatientBodyFunctionAssessment']


class BodyFunctionCategory(ModelSQL, ModelView):
    'Body Function Category'
    __name__ = 'gnuhealth.body_function.category'

    name = fields.Char('Name', required=True)
    code = fields.Char('code', required=True)

    @classmethod
    def __setup__(cls):
        super(BodyFunctionCategory, cls).__setup__()
        cls._sql_constraints = [
            ('code', 'UNIQUE(code)',
                'The code must be unique !'),
        ]

class BodyFunction(ModelSQL, ModelView):
    'Body Functions'
    __name__ = 'gnuhealth.body_function'

    name = fields.Char('Function', required=True)
    code = fields.Char('code', required=True)
    category = fields.Char('Category')
    
    @classmethod
    def __setup__(cls):
        super(BodyFunction, cls).__setup__()
        cls._sql_constraints = [
            ('code', 'UNIQUE(code)',
                'The code must be unique !'),
        ]

class BodyStructureCategory(ModelSQL, ModelView):
    'Body Structure Category'
    __name__ = 'gnuhealth.body_structure.category'

    name = fields.Char('Name', required=True)
    code = fields.Char('code', required=True)

    @classmethod
    def __setup__(cls):
        super(BodyStructureCategory, cls).__setup__()
        cls._sql_constraints = [
            ('code', 'UNIQUE(code)',
                'The code must be unique !'),
        ]

class BodyStructure(ModelSQL, ModelView):
    'Body Functions'
    __name__ = 'gnuhealth.body_structure'

    name = fields.Char('Structure', required=True)
    code = fields.Char('code', required=True)
    category = fields.Char('Category')
    
    @classmethod
    def __setup__(cls):
        super(BodyStructure, cls).__setup__()
        cls._sql_constraints = [
            ('code', 'UNIQUE(code)',
                'The code must be unique !'),
        ]

class ActivityAndParticipationCategory(ModelSQL, ModelView):
    'Activity and Participation Category'
    __name__ = 'gnuhealth.activity_and_participation.category'

    name = fields.Char('Name', required=True)
    code = fields.Char('code', required=True)

    @classmethod
    def __setup__(cls):
        super(ActivityAndParticipationCategory, cls).__setup__()
        cls._sql_constraints = [
            ('code', 'UNIQUE(code)',
                'The code must be unique !'),
        ]

class ActivityAndParticipation(ModelSQL, ModelView):
    'Activity limitations and participation restrictions'
    __name__ = 'gnuhealth.activity_and_participation'

    name = fields.Char('A & P', required=True)
    code = fields.Char('code', required=True)
    category = fields.Char('Category')
    
    @classmethod
    def __setup__(cls):
        super(ActivityAndParticipation, cls).__setup__()
        cls._sql_constraints = [
            ('code', 'UNIQUE(code)',
                'The code must be unique !'),
        ]


class EnvironmentalFactorCategory(ModelSQL, ModelView):
    'Environmental Factor Category'
    __name__ = 'gnuhealth.environmental_factor.category'

    name = fields.Char('Name', required=True)
    code = fields.Char('code', required=True)

    @classmethod
    def __setup__(cls):
        super(EnvironmentalFactorCategory, cls).__setup__()
        cls._sql_constraints = [
            ('code', 'UNIQUE(code)',
                'The code must be unique !'),
        ]

class EnvironmentalFactor(ModelSQL, ModelView):
    'Environmental factors restrictions'
    __name__ = 'gnuhealth.environmental_factor'

    name = fields.Char('Environment', required=True)
    code = fields.Char('code', required=True)
    category = fields.Char('Category')
    
    @classmethod
    def __setup__(cls):
        super(EnvironmentalFactor, cls).__setup__()
        cls._sql_constraints = [
            ('code', 'UNIQUE(code)',
                'The code must be unique !'),
        ]


class PatientDisabilityAssessment(ModelSQL, ModelView):
    'Patient Disability Information'
    __name__ = 'gnuhealth.patient.disability_assessment'

    patient = fields.Many2One('gnuhealth.patient','Patient', required=True)

    assessment = fields.Char('Code')

    crutches = fields.Boolean('Crutches')
    wheelchair = fields.Boolean('Wheelchair')

    hand_function = fields.Selection([
        (None, ''),
        ('normal', 'Normal'),
        ('moderate', 'Moderate impairment'),
        ('severe', 'Severe impairment'),
        ], 'Hand', sort=False)

    visual_function = fields.Selection([
        (None, ''),
        ('normal', 'Normal'),
        ('moderate', 'Moderate impairment'),
        ('severe', 'Severe impairment'),
        ('blind', 'Blind'),
        ], 'Visual', sort=False)

    speech_function = fields.Selection([
        (None, ''),
        ('normal', 'Normal'),
        ('moderate', 'Moderate impairment'),
        ('severe', 'Severe impairment'),
        ('mute', 'Mute'),
        ], 'Speech', sort=False)

    hearing_function = fields.Selection([
        (None, ''),
        ('normal', 'Normal'),
        ('moderate', 'Moderate impairment'),
        ('severe', 'Severe impairment'),
        ('deaf', 'Deaf'),
        ], 'Hearing', sort=False)

    cognitive_function = fields.Selection([
        (None, ''),
        ('normal', 'Normal'),
        ('moderate', 'Moderate impairment'),
        ('severe', 'Severe impairment'),
        ], 'Cognitive', sort=False)

    locomotor_function = fields.Selection([
        (None, ''),
        ('normal', 'Normal'),
        ('moderate', 'Moderate impairment'),
        ('severe', 'Severe impairment'),
        ], 'Locomotor', sort=False)

    activity_participation = fields.Selection([
        (None, ''),
        ('normal', 'Normal'),
        ('moderate', 'Moderate impairment'),
        ('severe', 'Severe impairment'),
        ], 'A & P', sort=False)

    body_functions = fields.One2Many('gnuhealth.body_function.assessment',
        'assessment','Body Functions')


class PatientBodyFunctionAssessment(ModelSQL, ModelView):
    'Body Functions Assessment'
    __name__ = 'gnuhealth.body_function.assessment'

    assessment = fields.Many2One('gnuhealth.patient.disability_assessment',
        'Assessment', required=True)
    body_function = fields.Many2One('gnuhealth.body_function', 'Body Function')
    qualifier = fields.Selection([
        (None, ''),
        ('0', '0 - No impairment'),
        ('1', '1 - Mild impairment'),
        ('2', '2 - Severe impairment'),
        ('3', '3 - Complete impairment'),
        ('8', '8 - Not specified'),
        ('9', '9 - Not applicable'),
        ], 'Qualifier', sort=False)
