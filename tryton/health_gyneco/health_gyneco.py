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


class PuerperiumMonitor(ModelSQL, ModelView):
    'Puerperium Monitor'
    _name = 'gnuhealth.puerperium.monitor'
    _description = __doc__

    name = fields.Many2One('gnuhealth.patient', 'Patient ID')
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
    'Perinatal monitor'
    _name = 'gnuhealth.perinatal.monitor'
    _description = __doc__

    name = fields.Many2One('gnuhealth.patient', 'Patient ID')
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

    name = fields.Many2One('gnuhealth.patient', 'Patient ID')
    admission_code = fields.Char('Code')
    gravida_number = fields.Integer('Gravida #')
    abortion = fields.Boolean('Abortion')
    admission_date = fields.DateTime('Admission',
        help="Date when she was admitted to give birth", required=True)
    prenatal_evaluations = fields.Integer('Prenatal evaluations',
        help="Number of visits to the doctor during pregnancy")
    start_labor_mode = fields.Selection([
        ('n', 'Normal'),
        ('i', 'Induced'),
        ('c', 'c-section'),
        ], 'Labor mode', select=True)
    gestational_weeks = fields.Integer('Weeks')
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
    puerperium_monitor = fields.One2Many('gnuhealth.puerperium.monitor', 'name',
        'Puerperium monitor')
    medication = fields.One2Many('gnuhealth.patient.medication', 'name',
        'Medication and anesthesics')
    dismissed = fields.DateTime('Dismissed')
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

    gravida = fields.Integer('Gravida', help="Number of pregnancies")
    premature = fields.Integer('Premature', help="Premature Deliveries")
    abortions = fields.Integer('Abortions')
    full_term = fields.Integer('Full Term', help="Full term pregnancies")
    gpa = fields.Char('GPA',
        help="Gravida, Para, Abortus Notation. For example G4P3A1 : 4 " \
        "Pregnancies, 3 viable and 1 abortion")
    born_alive = fields.Integer('Born Alive')
    deaths_1st_week = fields.Integer('Deceased during 1st week',
        help="Number of babies that die in the first week")
    deaths_2nd_week = fields.Integer('Deceased after 2nd week',
        help="Number of babies that die after the second week")

    perinatal = fields.One2Many('gnuhealth.perinatal', 'name', 'Perinatal Info')

    menstrual_history = fields.One2Many('gnuhealth.patient.menstrual_history', 'name', 'Menstrual History')

    mammography_history = fields.One2Many('gnuhealth.patient.mammography_history', 'name', 'Mammography History')

    pap_history = fields.One2Many('gnuhealth.patient.pap_history', 'name', 'PAP smear History')

    colposcopy_history = fields.One2Many('gnuhealth.patient.colposcopy_history', 'name', 'Colposcopy History')

GnuHealthPatient()

class PatientMenstrualHistory(ModelSQL, ModelView):
    'Menstrual History'
    _name = 'gnuhealth.patient.menstrual_history'
    _description = __doc__
    
    name = fields.Many2One('gnuhealth.patient', 'Patient', readonly=True, required=True)
    evaluation = fields.Many2One('gnuhealth.patient.evaluation', 'Evaluation', readonly=True)
    evaluation_date = fields.Date('Date', help="Evaluation Date", required=True)
    lmp = fields.Date('LMP', help="Last Menstrual Period", required=True)
    lmp_length = fields.Integer('Length',required=True)
    is_regular = fields.Boolean('Regular')
    dysmenorrhea = fields.Boolean ('Dysmenorrhea')
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
    
    name = fields.Many2One('gnuhealth.patient', 'Patient', readonly=True, required=True)
    evaluation = fields.Many2One('gnuhealth.patient.evaluation', 'Evaluation', readonly=True)
    evaluation_date = fields.Date('Date', help=" Date")
    last_mammography = fields.Date('Date', help="Last Mammography", required=True)
    result = fields.Selection([
        ('normal', 'normal'),
        ('abnormal', 'abnormal'),
        ], 'result', help="Please check the lab test results if the module is installed", sort=False)
 
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
    
    name = fields.Many2One('gnuhealth.patient', 'Patient', readonly=True, required=True)
    evaluation = fields.Many2One('gnuhealth.patient.evaluation', 'Evaluation', readonly=True)
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
        ], 'result', help="Please check the lab results if the module is installed", sort=False)
 
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
    
    name = fields.Many2One('gnuhealth.patient', 'Patient', readonly=True, required=True)
    evaluation = fields.Many2One('gnuhealth.patient.evaluation', 'Evaluation', readonly=True)
    evaluation_date = fields.Date('Date', help=" Date")
    last_colposcopy = fields.Date('Date', help="Last colposcopy", required=True)
    result = fields.Selection([
        ('normal', 'normal'),
        ('abnormal', 'abnormal'),
        ], 'result', help="Please check the lab test results if the module is installed", sort=False)
 
    comments = fields.Char('Remarks')
    
    def default_evaluation_date(self):
        return Pool().get('ir.date').today()

    def default_last_colposcopy(self):
        return Pool().get('ir.date').today()

PatientColposcopyHistory()
