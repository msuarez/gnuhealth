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
from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta, date
from sql import Literal, Join, Table
from trytond.model import ModelView, ModelSingleton, ModelSQL, fields, Unique
from trytond.transaction import Transaction
from trytond import backend
from trytond.pyson import Eval, Not, Bool, PYSONEncoder, Equal, And, Or, If
from trytond.pool import Pool
import string
import pytz

__all__ = ['GnuHealthPatient','Product','BodyFunctionCategory','BodyFunction',
    'BodyStructureCategory','BodyStructure',
    'ActivityAndParticipationCategory', 'ActivityAndParticipation',
    'EnvironmentalFactorCategory','EnvironmentalFactor',
    'PatientDisabilityAssessment',
    'PatientBodyFunctionAssessment',
    'PatientBodyStructureAssessment',
    'PatientActivityAndParticipationAsssessment',
    'PatientEnvironmentalFactorAssessment',
    'PatientAmputation','PatientProthesis',
    'PatientData']


    
# Include disabilty amputation and UXO casualty information on patient model
class GnuHealthPatient(ModelSQL, ModelView):
    __name__ = 'gnuhealth.patient'

    disability = fields.Boolean('Disabilities / Barriers', help="Mark this "
        "box if the patient has history of significant disabilities and/or "
        "barriers. Review the Disability Assessments, socioeconomic info,  "
        "diseases and surgeries for more details")
    uxo = fields.Boolean('UXO', help="UXO casualty")
    amputee = fields.Boolean('Amputee', help="Person has had one or more"
        " limbs removed by amputation. Includes congenital conditions")
    amputee_since = fields.Date('Since', help="Date of amputee status")
    
    amputations = fields.One2Many('gnuhealth.patient.amputation','patient','Amputations')

    protheses = fields.One2Many('gnuhealth.patient.prothesis','patient','Protheses')

class Product(ModelSQL, ModelView):
    'Product'
    __name__ = 'product.product'
    
    is_prothesis = fields.Boolean(
        'Prothesis', help='Check if the product is a prothesis')

class BodyFunctionCategory(ModelSQL, ModelView):
    'Body Function Category'
    __name__ = 'gnuhealth.body_function.category'

    name = fields.Char('Name', required=True)
    code = fields.Char('code', required=True)

    @classmethod
    def __setup__(cls):
        super(BodyFunctionCategory, cls).__setup__()
        t = cls.__table__()
        cls._sql_constraints = [
            ('code_uniq', Unique(t,t.code),
                'The code must be unique !'),
        ]

class BodyFunction(ModelSQL, ModelView):
    'Body Functions'
    __name__ = 'gnuhealth.body_function'

    name = fields.Char('Function', required=True)
    code = fields.Char('code', required=True)
    category = fields.Many2One('gnuhealth.body_function.category','Category')
    
    @classmethod
    def __setup__(cls):
        super(BodyFunction, cls).__setup__()
        t = cls.__table__()
        cls._sql_constraints = [
            ('code_uniq', Unique(t,t.code),
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
        t = cls.__table__()
        cls._sql_constraints = [
            ('code_uniq', Unique(t,t.code),
                'The code must be unique !'),
        ]

class BodyStructure(ModelSQL, ModelView):
    'Body Functions'
    __name__ = 'gnuhealth.body_structure'

    name = fields.Char('Structure', required=True)
    code = fields.Char('code', required=True)
    category = fields.Many2One('gnuhealth.body_structure.category','Category')
    
    @classmethod
    def __setup__(cls):
        super(BodyStructure, cls).__setup__()
        t = cls.__table__()
        cls._sql_constraints = [
            ('code_uniq', Unique(t,t.code),
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
        t = cls.__table__()
        cls._sql_constraints = [
            ('code_uniq', Unique(t,t.code),
                'The code must be unique !'),
        ]

class ActivityAndParticipation(ModelSQL, ModelView):
    'Activity limitations and participation restrictions'
    __name__ = 'gnuhealth.activity_and_participation'

    name = fields.Char('A & P', required=True)
    code = fields.Char('code', required=True)
    category = fields.Many2One(
        'gnuhealth.activity_and_participation.category','Category')
    
    @classmethod
    def __setup__(cls):
        super(ActivityAndParticipation, cls).__setup__()
        t = cls.__table__()
        cls._sql_constraints = [
            ('code_uniq', Unique(t,t.code),
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
        t = cls.__table__()
        cls._sql_constraints = [
            ('code_uniq', Unique(t,t.code),
                'The code must be unique !'),
        ]

class EnvironmentalFactor(ModelSQL, ModelView):
    'Environmental factors restrictions'
    __name__ = 'gnuhealth.environmental_factor'

    name = fields.Char('Environment', required=True)
    code = fields.Char('code', required=True)
    category = fields.Many2One(
        'gnuhealth.environmental_factor.category','Category')
    
    @classmethod
    def __setup__(cls):
        super(EnvironmentalFactor, cls).__setup__()
        t = cls.__table__()
        cls._sql_constraints = [
            ('code_uniq', Unique(t,t.code),
                'The code must be unique !'),
        ]


class PatientDisabilityAssessment(ModelSQL, ModelView):
    'Patient Disability Information'
    __name__ = 'gnuhealth.patient.disability_assessment'

    patient = fields.Many2One('gnuhealth.patient','Patient', required=True)

    assessment_date = fields.Date('Date')

    assessment = fields.Char('Code')

    crutches = fields.Boolean('Crutches')
    wheelchair = fields.Boolean('Wheelchair')

    uxo = fields.Function(fields.Boolean('UXO'), 'get_uxo_status')
    amputee = fields.Function(fields.Boolean('Amputee'),
        'get_amputee_status')
    amputee_since = fields.Function(fields.Date('Since'),
        'get_amputee_date')
    
    notes = fields.Text('Notes', help="Extra Information")

    hand_function = fields.Selection([
        (None, ''),
        ('0', 'No impairment'),
        ('1', 'Mild impairment'),
        ('2', 'Moderate impairment'),
        ('3', 'Severe impairment'),
        ('4', 'Complete impairment'),
        ], 'Hand', sort=False)

    visual_function = fields.Selection([
        (None, ''),
        ('0', 'No impairment'),
        ('1', 'Mild impairment'),
        ('2', 'Moderate impairment'),
        ('3', 'Severe impairment'),
        ('4', 'Complete impairment'),
        ], 'Visual', sort=False)

    speech_function = fields.Selection([
        (None, ''),
        ('0', 'No impairment'),
        ('1', 'Mild impairment'),
        ('2', 'Moderate impairment'),
        ('3', 'Severe impairment'),
        ('4', 'Complete impairment'),
        ], 'Speech', sort=False)

    hearing_function = fields.Selection([
        (None, ''),
        ('0', 'No impairment'),
        ('1', 'Mild impairment'),
        ('2', 'Moderate impairment'),
        ('3', 'Severe impairment'),
        ('4', 'Complete impairment'),
        ], 'Hearing', sort=False)

    cognitive_function = fields.Selection([
        (None, ''),
        ('0', 'No impairment'),
        ('1', 'Mild impairment'),
        ('2', 'Moderate impairment'),
        ('3', 'Severe impairment'),
        ('4', 'Complete impairment'),
        ], 'Cognitive', sort=False)

    locomotor_function = fields.Selection([
        (None, ''),
        ('0', 'No impairment'),
        ('1', 'Mild impairment'),
        ('2', 'Moderate impairment'),
        ('3', 'Severe impairment'),
        ('4', 'Complete impairment'),
        ], 'Mobility', sort=False)

    activity_participation = fields.Selection([
        (None, ''),
        ('0', 'No impairment'),
        ('1', 'Mild impairment'),
        ('2', 'Moderate impairment'),
        ('3', 'Severe impairment'),
        ('4', 'Complete impairment'),
        ], 'A & P', sort=False)

    body_functions = fields.One2Many('gnuhealth.body_function.assessment',
        'assessment','Body Functions Impairments')

    body_structures = fields.One2Many('gnuhealth.body_structure.assessment',
        'assessment','Body Structures Impairments')

    activity_and_participation = fields.One2Many(
        'gnuhealth.activity.assessment',
        'assessment','Activities and Participation Impairments')

    environmental_factor = fields.One2Many(
        'gnuhealth.environment.assessment',
        'assessment','Environmental Factors Barriers')

    healthprof = fields.Many2One(
        'gnuhealth.healthprofessional', 'Health Prof',
        help="Authorized health professional")

    def get_uxo_status(self, name):
        return self.patient.uxo

    def get_amputee_status(self, name):
        return self.patient.amputee

    def get_amputee_date(self, name):
        return self.patient.amputee_since
        
    @staticmethod
    def default_assessment_date():
        return date.today()


    @staticmethod
    def default_healthprof():
        pool = Pool()
        HealthProf= pool.get('gnuhealth.healthprofessional')
        hp = HealthProf.get_health_professional()
        return hp

class PatientBodyFunctionAssessment(ModelSQL, ModelView):
    'Body Functions Assessment'
    __name__ = 'gnuhealth.body_function.assessment'

    assessment = fields.Many2One('gnuhealth.patient.disability_assessment',
        'Assessment', required=True)
    body_function = fields.Many2One('gnuhealth.body_function', 'Body Function')
    qualifier = fields.Selection([
        (None, ''),
        ('0', 'No impairment'),
        ('1', 'Mild impairment'),
        ('2', 'Severe impairment'),
        ('3', 'Complete impairment'),
        ('8', 'Not specified'),
        ('9', 'Not applicable'),
        ], 'Qualifier', sort=False)

class PatientBodyStructureAssessment(ModelSQL, ModelView):
    'Body Functions Assessment'
    __name__ = 'gnuhealth.body_structure.assessment'

    assessment = fields.Many2One('gnuhealth.patient.disability_assessment',
        'Assessment', required=True)
    body_structure = fields.Many2One('gnuhealth.body_structure', 'Body Structure')
    qualifier1 = fields.Selection([
        (None, ''),
        ('0', 'No impairment'),
        ('1', 'Mild impairment'),
        ('2', 'Moderate impairment'),
        ('3', 'Severe impairment'),
        ('4', 'Complete impairment'),
        ('8', 'Not specified'),
        ('9', 'Not applicable'),
        ], 'Extent', help="Extent of the impairment", sort=False)

    qualifier2 = fields.Selection([
        (None, ''),
        ('0', 'No change in structure'),
        ('1', 'Total absence'),
        ('2', 'Partial absence'),
        ('3', 'Additional part'),
        ('4', 'Aberrant dimensions'),
        ('5', 'Discontinuity'),
        ('6', 'Deviating position'),
        ('7', 'Qualitative changes in structure, including accumulation of fluid'),
        ('8', '8 - Not specified'),
        ('9', '9 - Not applicable'),
        ], 'Nature', help="Nature of the change", sort=False)

    body_side = fields.Selection([
        (None, ''),
        ('left', 'Left'),
        ('right', 'Right'),
        ('both', 'Both'),
        ], 'Side', help="Side of the body, if applies", sort=False)


class PatientActivityAndParticipationAsssessment(ModelSQL, ModelView):
    'Activity and Participation Assessment'
    __name__ = 'gnuhealth.activity.assessment'

    assessment = fields.Many2One('gnuhealth.patient.disability_assessment',
        'Assessment', required=True)
    
    activity_and_participation = fields.Many2One(
        'gnuhealth.activity_and_participation','Activity')
    
    qualifier1 = fields.Selection([
        (None, ''),
        ('0', 'No difficulty'),
        ('1', 'Mild difficulty'),
        ('2', 'Moderate difficulty'),
        ('3', 'Severe difficulty'),
        ('4', 'Complete difficulty'),
        ('8', 'Not specified'),
        ('9', 'Not applicable'),
        ], 'Performance', help="Extent of the difficulty", sort=False)

    qualifier2 = fields.Selection([
        (None, ''),
        ('0', 'No difficulty'),
        ('1', 'Mild difficulty'),
        ('2', 'Moderate difficulty'),
        ('3', 'Severe difficulty'),
        ('4', 'Complete difficulty'),
        ('8', 'Not specified'),
        ('9', 'Not applicable'),
        ], 'Capacity', help="Extent of the dificulty", sort=False)

class PatientEnvironmentalFactorAssessment(ModelSQL, ModelView):
    'Environmental Factors Assessment'
    __name__ = 'gnuhealth.environment.assessment'

    assessment = fields.Many2One('gnuhealth.patient.disability_assessment',
        'Assessment', required=True)
    
    environmental_factor = fields.Many2One(
        'gnuhealth.environmental_factor','Environment')

    qualifier = fields.Selection([
        (None, ''),
        ('0', 'No barriers'),
        ('1', 'Mild barriers'),
        ('2', 'Moderate barriers'),
        ('3', 'Severe barriers'),
        ('4', 'Complete barriers'),
        ('00', 'No facilitator'),
        ('11', 'Mild facilitator'),
        ('22', 'Moderate facilitator'),
        ('33', 'Severe facilitator'),
        ('44', 'Complete facilitator'),
        ], 'Barriers', help="Extent of the barriers or facilitators", sort=False)


# Amputation Information
class PatientAmputation(ModelSQL, ModelView):
    'Amputation'
    __name__ = 'gnuhealth.patient.amputation'
    
    patient = fields.Many2One('gnuhealth.patient','Patient', required=True)

    amputation_date = fields.Date('Date')

    body_structure = fields.Many2One('gnuhealth.body_structure','Structure')

    etiology = fields.Selection([
        (None, ''),
        ('pvd', 'Peripherial Vascular Disease'),
        ('trauma', 'Trauma'),
        ('neoplasia', 'Neoplasia'),
        ('infection', 'Infection'),
        ('congenital', 'Congenital'),
        ], 'Etiology', sort=False)

    limb = fields.Selection([
        (None, ''),
        ('lower', 'lower limb'),
        ('upper', 'upper limb'),
        ], 'Limb', sort=False)

    side = fields.Selection([
        (None, ''),
        ('left', 'left'),
        ('right', 'right'),
        ('both', 'both'),
        ], 'Side', sort=False)

    amputation_level = fields.Selection([
        (None, ''),
        ('sd', 'SD - Shoulder disarticulation'),
        ('th', 'TH - Transhumeral'),
        ('ed', 'ED - Elbow disarticulation'),
        ('tr', 'TR - Transradial'),
        ('wd', 'WD - Wrist disarticulation'),
        ('ph', 'PH'),
        ('hp', 'HD - Hemipelvectomy'),
        ('tf', 'TF - Transfemoral'),
        ('tt', 'TT - Transtibial'),
        ('symes', 'Symes'),
        ('pffd', 'PFFD'),
        ], 'Level', sort=False)

    comments = fields.Char('Comments')

    healthprof = fields.Many2One(
        'gnuhealth.healthprofessional', 'Health Prof',
        help="Authorized health professional")

    @staticmethod
    def default_healthprof():
        pool = Pool()
        HealthProf= pool.get('gnuhealth.healthprofessional')
        hp = HealthProf.get_health_professional()
        return hp

# Patient Protheses Information
class PatientProthesis(ModelSQL, ModelView):
    'Amputation'
    __name__ = 'gnuhealth.patient.prothesis'
    
    patient = fields.Many2One('gnuhealth.patient','Patient', required=True)

    issue_date = fields.Date('Date')

    prothesis = fields.Many2One(
        'product.product', 'Prothesis', required=True,
        domain=[('is_prothesis', '=', True)],
        help='Prosthetic device')

    comments = fields.Char('Comments')

    healthprof = fields.Many2One(
        'gnuhealth.healthprofessional', 'Health Prof',
        help="Prosthetist or authorized health professional")
    
    @staticmethod
    def default_healthprof():
        pool = Pool()
        HealthProf= pool.get('gnuhealth.healthprofessional')
        hp = HealthProf.get_health_professional()
        return hp



class PatientData (ModelSQL, ModelView):
    __name__ = 'gnuhealth.patient'

    disability_assesments = fields.One2Many('gnuhealth.patient.disability_assessment',
        'patient', 'Assessment', readonly=True)
