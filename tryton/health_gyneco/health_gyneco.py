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
from trytond.pool import Pool
import datetime


class PatientPregnancy(ModelSQL, ModelView):
    'Patient Pregnancy'
    _name = 'gnuhealth.patient.pregnancy'
    _description = __doc__

    def get_pregnancy_due_date(self, ids, name):
        result = {}
        
        for pregnancy_data in self.browse(ids):
            result[pregnancy_data.id] = pregnancy_data.lmp + datetime.timedelta(days=280)

        return result

    name = fields.Many2One('gnuhealth.patient', 'Patient ID')
    gravida = fields.Integer ('Gravida #', required=True)
    warning = fields.Boolean ('Anomalous', help="Check this box if this is pregancy is or was NOT normal")
    lmp = fields.Date ('LMP', help="Last Menstrual Period", required=True)
    pdd = fields.Function (fields.Date('Pregnancy Due Date'), 'get_pregnancy_due_date')

    prenatal_evaluations = fields.One2Many('gnuhealth.patient.prenatal.evaluation', 'name', 'Prenatal Evaluations')

    perinatal = fields.One2Many('gnuhealth.perinatal', 'name', 'Perinatal Info')

    puerperium_monitor = fields.One2Many('gnuhealth.puerperium.monitor', 'name', 'Puerperium monitor')


    def __init__(self):
        super(PatientPregnancy, self).__init__()
        self._sql_constraints = [
            ('gravida_uniq', 'UNIQUE(gravida)', 'The pregancy must be unique !'),
        ]

PatientPregnancy()


class PrenatalEvaluation(ModelSQL, ModelView):
    'Prenatal Evaluation'
    _name = 'gnuhealth.patient.prenatal.evaluation'
    _description = __doc__

    def get_patient_evaluation_data(self, ids, name):
        result = {}
        
        for evaluation_data in self.browse(ids):
            if name == 'systolic':
                result[evaluation_data.id] = evaluation_data.evaluation.systolic
            if name == 'diastolic':
                result[evaluation_data.id] = evaluation_data.evaluation.diastolic
            if name == 'mother_frequency':
                result[evaluation_data.id] = evaluation_data.evaluation.bpm

            if name == 'mother_weight':
                result[evaluation_data.id] = evaluation_data.evaluation.weight

            if name == 'evaluation_date':
                result[evaluation_data.id] = evaluation_data.evaluation.evaluation_start

            if name == 'gestational_weeks':
                gestational_age = datetime.datetime.date(evaluation_data.evaluation.evaluation_start) - evaluation_data.name.lmp

                result[evaluation_data.id] = (gestational_age.days)/7

            if name == 'gestational_days':
                gestational_age = datetime.datetime.date(evaluation_data.evaluation.evaluation_start) - evaluation_data.name.lmp

                result[evaluation_data.id] = gestational_age.days
                
            if name == 'evaluation_summary':
                result[evaluation_data.id] = evaluation_data.evaluation.evaluation_summary

        return result


    name = fields.Many2One('gnuhealth.patient.pregnancy', 'Patient Pregnancy')    

    evaluation = fields.Many2One('gnuhealth.patient.evaluation', 'Evaluation', required=True)

    evaluation_date = fields.Function(fields.DateTime('Date'),
        'get_patient_evaluation_data')

    systolic = fields.Function(fields.Integer('Systolic'),
        'get_patient_evaluation_data')

    diastolic = fields.Function(fields.Integer('Diastolic'),
        'get_patient_evaluation_data')

    mother_frequency = fields.Function(fields.Integer('Mother\'s Freq', help="Mother heart frequency"),
        'get_patient_evaluation_data')
    
    fetus_frequency = fields.Integer('Fetus Freq', help="Fetus heart frequency")

    mother_weight = fields.Function(fields.Float('Mother\'s weight'),
        'get_patient_evaluation_data')

    gestational_weeks = fields.Function(fields.Integer('Gestational wks'),
        'get_patient_evaluation_data')

    gestational_days = fields.Function(fields.Integer('Gestational days'),
        'get_patient_evaluation_data')

    fundal_height = fields.Integer('Fundal Height',
        help="Distance between the symphysis pubis and the uterine fundus " \
        "(S-FD) in cm")
        
    evaluation_summary = fields.Function(fields.Text('Summary'),
        'get_patient_evaluation_data')

PrenatalEvaluation()


class PuerperiumMonitor(ModelSQL, ModelView):
    'Puerperium Monitor'
    _name = 'gnuhealth.puerperium.monitor'
    _description = __doc__

    name = fields.Many2One('gnuhealth.patient.pregnancy', 'Patient Pregnancy')
    date = fields.DateTime('Date and Time', required=True)
    systolic = fields.Integer('Systolic Pressure')
    diastolic = fields.Integer('Diastolic Pressure')
    frequency = fields.Integer('Heart Frequency')

    lochia_amount = fields.Selection([
        ('n', 'normal'),
        ('e', 'abundant'),
        ('h', 'hemorrhage'),
        ], 'Lochia amount', select=True)

    lochia_color = fields.Selection([
        ('r', 'rubra'),
        ('s', 'serosa'),
        ('a', 'alba'),
        ], 'Lochia color', select=True)

    lochia_odor = fields.Selection([
        ('n', 'normal'),
        ('o', 'offensive'),
        ], 'Lochia odor', select=True)

    uterus_involution = fields.Integer('Fundal Height',
        help="Distance between the symphysis pubis and the uterine fundus " \
        "(S-FD) in cm")
    temperature = fields.Float('Temperature')

PuerperiumMonitor()


class PerinatalMonitor(ModelSQL, ModelView):
    'Perinatal and monitor'
    _name = 'gnuhealth.perinatal.monitor'
    _description = __doc__

    name = fields.Many2One('gnuhealth.patient.pregnancy', 'Patient Pregnancy')
    date = fields.DateTime('Date and Time')
    systolic = fields.Integer('Systolic Pressure')
    diastolic = fields.Integer('Diastolic Pressure')
    contractions = fields.Integer('Contractions')
    frequency = fields.Integer('Mother\'s Heart Frequency')
    dilation = fields.Integer('Cervix dilation')
    f_frequency = fields.Integer('Fetus Heart Frequency')
    meconium = fields.Boolean('Meconium')
    bleeding = fields.Boolean('Bleeding')
    fundal_height = fields.Integer('Fundal Height')
    fetus_position = fields.Selection([
        ('n', 'Correct'),
        ('o', 'Occiput / Cephalic Posterior'),
        ('fb', 'Frank Breech'),
        ('cb', 'Complete Breech'),
        ('t', 'Transverse Lie'),
        ('t', 'Footling Breech'),
        ], 'Fetus Position', select=True)

PerinatalMonitor()


class Perinatal(ModelSQL, ModelView):
    'Perinatal Information'
    _name = 'gnuhealth.perinatal'
    _description = __doc__

    def get_perinatal_information(self, ids, name):
        result = {}
        
        for perinatal_data in self.browse(ids):
            if name == 'gestational_weeks':
                gestational_age = datetime.datetime.date(perinatal_data.admission_date) - perinatal_data.name.lmp
                result[perinatal_data.id] = (gestational_age.days)/7

        return result

    name = fields.Many2One('gnuhealth.patient.pregnancy', 'Patient Pregnancy')
    admission_code = fields.Char('Code')

# 1.6.4 Gravida number and abortion information go now in the pregnancy header
# It will be calculated as a function if needed
    gravida_number = fields.Integer('Gravida #')
    abortion = fields.Boolean('Abortion')

    admission_date = fields.DateTime('Admission',
        help="Date when she was admitted to give birth", required=True)

# Deprecated in 1.6.4
    prenatal_evaluations = fields.Integer('Prenatal evaluations', \
        help="Number of visits to the doctor during pregnancy")

    start_labor_mode = fields.Selection([
        ('n', 'Normal'),
        ('i', 'Induced'),
        ('c', 'c-section'),
        ], 'Labor mode', select=True)

    gestational_weeks = fields.Function(fields.Integer('Gestational wks'),
        'get_perinatal_information')

    gestational_days = fields.Integer('Days')
    fetus_presentation = fields.Selection([
        ('n', 'Correct'),
        ('o', 'Occiput / Cephalic Posterior'),
        ('fb', 'Frank Breech'),
        ('cb', 'Complete Breech'),
        ('t', 'Transverse Lie'),
        ('t', 'Footling Breech'),
        ], 'Fetus Presentation', select=True)
    dystocia = fields.Boolean('Dystocia')
    placenta_incomplete = fields.Boolean('Incomplete Placenta')
    placenta_retained = fields.Boolean('Retained Placenta')
    episiotomy = fields.Boolean('Episiotomy')
    vaginal_tearing = fields.Boolean('Vaginal tearing')
    forceps = fields.Boolean('Use of forceps')
    monitoring = fields.One2Many('gnuhealth.perinatal.monitor', 'name',
        'Monitors')
# Deprecated in 1.6.4. Puerperium is now a separate entity from perinatal
# and is included in the obstetric evaluation history

#    puerperium_monitor = fields.One2Many('gnuhealth.puerperium.monitor', 'name',
#        'Puerperium monitor')

    medication = fields.One2Many('gnuhealth.patient.medication', 'name',
        'Medication and anesthesics')
    dismissed = fields.DateTime('Discharged')
    place_of_death = fields.Selection([
        ('ho', 'Hospital'),
        ('dr', 'At the delivery room'),
        ('hh', 'in transit to the hospital'),
        ('th', 'Being transferred to other hospital'),
        ], 'Place of Death', help="Place where the mother died",
        states={'invisible': Not(Bool(Eval('mother_deceased')))},
        depends=['mother_deceased'])

    mother_deceased = fields.Boolean('Maternal death',
        help="Mother died in the process")

    notes = fields.Text('Notes')

Perinatal()



class GnuHealthPatient(ModelSQL, ModelView):
    'Add to the Medical patient_data class (gnuhealth.patient) the ' \
    'gynecological and obstetric fields.'
    _name = 'gnuhealth.patient'
    _description = __doc__

    currently_pregnant = fields.Boolean('Currently Pregnant')
    fertile = fields.Boolean('Fertile',
        help="Check if patient is in fertile age")
    menarche = fields.Integer('Menarche age')
    menopausal = fields.Boolean('Menopausal')
    menopause = fields.Integer('Menopause age')
    mammography = fields.Boolean('Mammography',
        help="Check if the patient does periodic mammographys")
    mammography_last = fields.Date('Last mammography',
        help="Enter the date of the last mammography")
    breast_self_examination = fields.Boolean('Breast self-examination',
        help="Check if patient does and knows how to self examine her breasts")
    pap_test = fields.Boolean('PAP test',
        help="Check if patient does periodic cytologic pelvic smear screening")
    pap_test_last = fields.Date('Last PAP test',
        help="Enter the date of the last Papanicolau test")
    colposcopy = fields.Boolean('Colposcopy',
        help="Check if the patient has done a colposcopy exam")
    colposcopy_last = fields.Date('Last colposcopy',
        help="Enter the date of the last colposcopy")

    gravida = fields.Integer('Pregnancies', help="Number of pregnancies")
    premature = fields.Integer('Premature', help="Premature Deliveries")
    abortions = fields.Integer('Abortions')
    stillbirths = fields.Integer('Stillbirths')
    full_term = fields.Integer('Full Term', help="Full term pregnancies")

# GPA Deprecated in 1.6.4. It will be used as a function or report from the other fields 
#    gpa = fields.Char('GPA',
#        help="Gravida, Para, Abortus Notation. For example G4P3A1 : 4 " \
#        "Pregnancies, 3 viable and 1 abortion")

# Deprecated. The born alive number will be calculated from pregnancies - abortions - stillbirths
#    born_alive = fields.Integer('Born Alive')
# Deceased in 1st week or after 2nd weeks are deprecated since 1.6.4 . The information will
# be retrieved from the neonatal or infant record

#    deaths_1st_week = fields.Integer('Deceased during 1st week',
#        help="Number of babies that die in the first week")
#    deaths_2nd_week = fields.Integer('Deceased after 2nd week',
#        help="Number of babies that die after the second week")

# Perinatal Deprecated since 1.6.4 - Included in the obstetric history
#    perinatal = fields.One2Many('gnuhealth.perinatal', 'name', 'Perinatal Info')

    menstrual_history = fields.One2Many('gnuhealth.patient.menstrual_history',
        'name', 'Menstrual History')

    mammography_history = fields.One2Many( \
        'gnuhealth.patient.mammography_history', 'name', 'Mammography History')

    pap_history = fields.One2Many('gnuhealth.patient.pap_history', 'name',
        'PAP smear History')

    colposcopy_history = fields.One2Many('gnuhealth.patient.colposcopy_history',
        'name', 'Colposcopy History')

    pregnancy_history = fields.One2Many('gnuhealth.patient.pregnancy', 'name', 'Pregnancies')

GnuHealthPatient()


class PatientMenstrualHistory(ModelSQL, ModelView):
    'Menstrual History'
    _name = 'gnuhealth.patient.menstrual_history'
    _description = __doc__

    name = fields.Many2One('gnuhealth.patient', 'Patient', readonly=True,
        required=True)
    evaluation = fields.Many2One('gnuhealth.patient.evaluation', 'Evaluation',
        readonly=True)
    evaluation_date = fields.Date('Date', help="Evaluation Date", required=True)
    lmp = fields.Date('LMP', help="Last Menstrual Period", required=True)
    lmp_length = fields.Integer('Length', required=True)
    is_regular = fields.Boolean('Regular')
    dysmenorrhea = fields.Boolean('Dysmenorrhea')
    frequency = fields.Selection([
        ('amenorrhea', 'amenorrhea'),
        ('oligomenorrhea', 'oligomenorrhea'),
        ('eumenorrhea', 'eumenorrhea'),
        ('polymenorrhea', 'polymenorrhea'),
        ], 'frequency', sort=False)

    volume = fields.Selection([
        ('hypomenorrhea', 'hypomenorrhea'),
        ('normal', 'normal'),
        ('menorrhagia', 'menorrhagia'),
        ], 'volume', sort=False)

    def default_evaluation_date(self):
        return Pool().get('ir.date').today()

    def default_frequency(self):
        return 'eumenorrhea'

    def default_volume(self):
        return 'normal'

PatientMenstrualHistory()


class PatientMammographyHistory(ModelSQL, ModelView):
    'Mammography History'
    _name = 'gnuhealth.patient.mammography_history'
    _description = __doc__

    name = fields.Many2One('gnuhealth.patient', 'Patient', readonly=True,
        required=True)
    evaluation = fields.Many2One('gnuhealth.patient.evaluation', 'Evaluation',
        readonly=True)
    evaluation_date = fields.Date('Date', help=" Date")
    last_mammography = fields.Date('Date', help="Last Mammography",
        required=True)
    result = fields.Selection([
        ('normal', 'normal'),
        ('abnormal', 'abnormal'),
        ], 'result', help="Please check the lab test results if the module is \
            installed", sort=False)

    comments = fields.Char('Remarks')

    def default_evaluation_date(self):
        return Pool().get('ir.date').today()

    def default_last_mammography(self):
        return Pool().get('ir.date').today()


PatientMammographyHistory()


class PatientPAPHistory(ModelSQL, ModelView):
    'PAP Test History'
    _name = 'gnuhealth.patient.pap_history'
    _description = __doc__

    name = fields.Many2One('gnuhealth.patient', 'Patient', readonly=True,
        required=True)
    evaluation = fields.Many2One('gnuhealth.patient.evaluation', 'Evaluation',
        readonly=True)
    evaluation_date = fields.Date('Date', help=" Date")
    last_pap = fields.Date('Date', help="Last Papanicolau", required=True)
    result = fields.Selection([
        ('negative', 'Negative'),
        ('c1', 'ASC-US'),
        ('c2', 'ASC-H'),
        ('g1', 'ASG'),
        ('c3', 'LSIL'),
        ('c4', 'HSIL'),
        ('g4', 'AIS'),
        ], 'result', help="Please check the lab results if the module is \
            installed", sort=False)

    comments = fields.Char('Remarks')

    def default_evaluation_date(self):
        return Pool().get('ir.date').today()

    def default_last_pap(self):
        return Pool().get('ir.date').today()

PatientPAPHistory()


class PatientColposcopyHistory(ModelSQL, ModelView):
    'Colposcopy History'
    _name = 'gnuhealth.patient.colposcopy_history'
    _description = __doc__

    name = fields.Many2One('gnuhealth.patient', 'Patient', readonly=True,
        required=True)
    evaluation = fields.Many2One('gnuhealth.patient.evaluation', 'Evaluation',
        readonly=True)
    evaluation_date = fields.Date('Date', help=" Date")
    last_colposcopy = fields.Date('Date', help="Last colposcopy", required=True)
    result = fields.Selection([
        ('normal', 'normal'),
        ('abnormal', 'abnormal'),
        ], 'result', help="Please check the lab test results if the module is \
            installed", sort=False)

    comments = fields.Char('Remarks')

    def default_evaluation_date(self):
        return Pool().get('ir.date').today()

    def default_last_colposcopy(self):
        return Pool().get('ir.date').today()

PatientColposcopyHistory()
