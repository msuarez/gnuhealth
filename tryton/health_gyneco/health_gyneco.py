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
import datetime
from trytond.model import ModelView, ModelSQL, fields, Unique
from trytond.pyson import Eval, Not, Bool, Equal
from trytond.pool import Pool
from trytond import backend
from trytond.transaction import Transaction
from sql import *
from sql.aggregate import *


__all__ = ['PatientPregnancy', 'PrenatalEvaluation', 'PuerperiumMonitor',
    'Perinatal', 'PerinatalMonitor', 'GnuHealthPatient',
    'PatientMenstrualHistory', 'PatientMammographyHistory',
    'PatientPAPHistory', 'PatientColposcopyHistory']


class PatientPregnancy(ModelSQL, ModelView):
    'Patient Pregnancy'
    __name__ = 'gnuhealth.patient.pregnancy'

    name = fields.Many2One('gnuhealth.patient', 'Patient ID')
    gravida = fields.Integer('Pregnancy #', required=True)
    warning = fields.Boolean('Warn', help='Check this box if this is pregancy'
        ' is or was NOT normal')
    warning_icon = fields.Function(fields.Char('Pregnancy warning icon'), 'get_warn_icon')
    reverse = fields.Boolean ('Reverse', help="Use this method *only* when the \
        pregnancy information is referred by the patient, as a history taking \
        procedure. Please keep in mind that the reverse pregnancy data is \
        subjective",
        states={
            'invisible': Bool(Eval('current_pregnancy')),
            }
        )
    reverse_weeks = fields.Integer ("Pr. Weeks",help="Number of weeks at \
        the end of pregnancy. Used only with the reverse input method.",
        states={
        'invisible': Not(Bool(Eval('reverse'))),
        'required': Bool(Eval('reverse')),
            }
        )
    lmp = fields.Date('LMP', help="Last Menstrual Period", required=True)

    pdd = fields.Function(fields.Date('Pregnancy Due Date'),
        'get_pregnancy_data')
    prenatal_evaluations = fields.One2Many(
        'gnuhealth.patient.prenatal.evaluation', 'name',
        'Prenatal Evaluations')
    perinatal = fields.One2Many('gnuhealth.perinatal', 'name',
        'Perinatal Info')
    puerperium_monitor = fields.One2Many('gnuhealth.puerperium.monitor',
        'name', 'Puerperium monitor')
    current_pregnancy = fields.Boolean('Current Pregnancy', help='This field'
        ' marks the current pregnancy')
    fetuses = fields.Integer('Fetuses', required=True)
    monozygotic = fields.Boolean('Monozygotic')
    pregnancy_end_result = fields.Selection([
        (None, ''),
        ('live_birth', 'Live birth'),
        ('abortion', 'Abortion'),
        ('stillbirth', 'Stillbirth'),
        ('status_unknown', 'Status unknown'),
        ], 'Result', sort=False,
            states={
            'invisible': Bool(Eval('current_pregnancy')),
            'required': Not(Bool(Eval('current_pregnancy'))),
            })
    pregnancy_end_date = fields.DateTime('End of Pregnancy',
        states={
            'invisible': Bool(Eval('current_pregnancy')),
            'required': Not(Bool(Eval('current_pregnancy'))),
            })
    bba = fields.Boolean('BBA', help="Born Before Arrival",
        states={
            'invisible': Bool(Eval('current_pregnancy')),
            })
    home_birth = fields.Boolean('Home Birth', help="Home Birth",
        states={
            'invisible': Bool(Eval('current_pregnancy')),
            })

    pregnancy_end_age = fields.Function(fields.Char('Weeks', help='Weeks at'
        ' the end of pregnancy'), 'get_pregnancy_data')
    iugr = fields.Selection([
        (None, ''),
        ('symmetric', 'Symmetric'),
        ('assymetric', 'Asymmetric'),
        ], 'IUGR', sort=False)

    institution = fields.Many2One('gnuhealth.institution', 'Institution',
        help="Health center where this initial obstetric record was created")

    healthprof = fields.Many2One(
        'gnuhealth.healthprofessional', 'Health Prof', readonly=True,
        help="Health Professional who created this initial obstetric record")

    @classmethod
    def __setup__(cls):
        super(PatientPregnancy, cls).__setup__()
        t = cls.__table__()
        cls._sql_constraints += [
            ('gravida_uniq', Unique(t,t.name, t.gravida),
                'This pregnancy code for this patient already exists'),
        ]

        cls._error_messages.update({
            'patient_already_pregnant': 'Our records indicate that the patient'
                ' is already pregnant !'})

    @classmethod
    def validate(cls, pregnancies):
        super(PatientPregnancy, cls).validate(pregnancies)
        for pregnancy in pregnancies:
            pregnancy.check_patient_current_pregnancy()

    def check_patient_current_pregnancy(self):
        ''' Check for only one current pregnancy in the patient '''
        pregnancy = Table('gnuhealth_patient_pregnancy')
        cursor = Transaction().connection.cursor()
        patient_id = int(self.name.id)
        
        cursor.execute (*pregnancy.select(Count(pregnancy.name),
            where=(pregnancy.current_pregnancy == 'true') &
            (pregnancy.name == patient_id))) 
                                       
        records = cursor.fetchone()[0]
        if records > 1:
            self.raise_user_error('patient_already_pregnant')

    @staticmethod
    def default_current_pregnancy():
        return True

    @staticmethod
    def default_institution():
        HealthInst = Pool().get('gnuhealth.institution')
        institution = HealthInst.get_institution()
        return institution

    @staticmethod
    def default_healthprof():
        pool = Pool()
        HealthProf= pool.get('gnuhealth.healthprofessional')
        return HealthProf.get_health_professional()

    @fields.depends('reverse_weeks', 'pregnancy_end_date')
    def on_change_with_lmp(self):
        # Calculate the estimate on Last Menstrual Period
        # using the reverse input method, taking the
        # end of pregnancy date and number of weeks

        if (self.reverse_weeks and self.pregnancy_end_date):
            estimated_lmp = datetime.datetime.date(self.pregnancy_end_date - 
                datetime.timedelta(self.reverse_weeks*7))
                        
            return estimated_lmp 

    def get_pregnancy_data(self, name):
        """ Calculate the Pregnancy Due Date and the Number of
        weeks at the end of pregnancy when using the Last Menstrual
        Period parameter. 
        It's not calculated when using the reverse input method
        """
        if name == 'pdd':
                return self.lmp + datetime.timedelta(days=280)
                
        if name == 'pregnancy_end_age':
            if self.pregnancy_end_date:
                gestational_age = datetime.datetime.date(
                    self.pregnancy_end_date) - self.lmp
                return (gestational_age.days) / 7
            else:
                return 0

    def get_warn_icon(self, name):
        if self.warning:
            return 'gnuhealth-warning'

class PrenatalEvaluation(ModelSQL, ModelView):
    'Prenatal and Antenatal Evaluations'
    __name__ = 'gnuhealth.patient.prenatal.evaluation'

    name = fields.Many2One('gnuhealth.patient.pregnancy', 'Patient Pregnancy')
    evaluation = fields.Many2One('gnuhealth.patient.evaluation',
        'Patient Evaluation', readonly=True)
    evaluation_date = fields.DateTime('Date', required=True)
    gestational_weeks = fields.Function(fields.Integer('Gestational Weeks'),
        'get_patient_evaluation_data')
    gestational_days = fields.Function(fields.Integer('Gestational days'),
        'get_patient_evaluation_data')
    hypertension = fields.Boolean('Hypertension', help='Check this box if the'
        ' mother has hypertension')
    preeclampsia = fields.Boolean('Preeclampsia', help='Check this box if the'
        ' mother has pre-eclampsia')
    overweight = fields.Boolean('Overweight', help='Check this box if the'
        ' mother is overweight or obesity')
    diabetes = fields.Boolean('Diabetes', help='Check this box if the mother'
        ' has glucose intolerance or diabetes')
    invasive_placentation = fields.Selection([
        (None, ''),
        ('normal', 'Normal decidua'),
        ('accreta', 'Accreta'),
        ('increta', 'Increta'),
        ('percreta', 'Percreta'),
        ], 'Placentation', sort=False)
    placenta_previa = fields.Boolean('Placenta Previa')
    vasa_previa = fields.Boolean('Vasa Previa')
    fundal_height = fields.Integer('Fundal Height',
        help="Distance between the symphysis pubis and the uterine fundus "
        "(S-FD) in cm")
    fetus_heart_rate = fields.Integer('Fetus heart rate', help='Fetus heart'
        ' rate')
    efw = fields.Integer('EFW', help="Estimated Fetal Weight")
    fetal_bpd = fields.Integer('BPD', help="Fetal Biparietal Diameter")
    fetal_ac = fields.Integer('AC', help="Fetal Abdominal Circumference")
    fetal_hc = fields.Integer('HC', help="Fetal Head Circumference")
    fetal_fl = fields.Integer('FL', help="Fetal Femur Length")
    oligohydramnios = fields.Boolean('Oligohydramnios')
    polihydramnios = fields.Boolean('Polihydramnios')
    iugr = fields.Boolean('IUGR', help="Intra Uterine Growth Restriction")

    institution = fields.Many2One('gnuhealth.institution', 'Institution')

    healthprof = fields.Many2One(
        'gnuhealth.healthprofessional', 'Health Prof', readonly=True,
        help="Health Professional in charge, or that who entered the \
            information in the system")

    @staticmethod
    def default_institution():
        HealthInst = Pool().get('gnuhealth.institution')
        institution = HealthInst.get_institution()
        return institution

    @staticmethod
    def default_healthprof():
        pool = Pool()
        HealthProf= pool.get('gnuhealth.healthprofessional')
        return HealthProf.get_health_professional()


    def get_patient_evaluation_data(self, name):
        if name == 'gestational_weeks':
            gestational_age = datetime.datetime.date(self.evaluation_date) - \
                self.name.lmp
            return (gestational_age.days) / 7
        if name == 'gestational_days':
            gestational_age = datetime.datetime.date(self.evaluation_date) - \
                self.name.lmp
            return gestational_age.days


class PuerperiumMonitor(ModelSQL, ModelView):
    'Puerperium Monitor'
    __name__ = 'gnuhealth.puerperium.monitor'

    name = fields.Many2One('gnuhealth.patient.pregnancy', 'Patient Pregnancy')
    date = fields.DateTime('Date and Time', required=True)
    # Deprecated in 1.6.4 All the clinical information will be taken at the
    # main evaluation.
    # systolic / diastolic / frequency / temperature
    systolic = fields.Integer('Systolic Pressure')
    diastolic = fields.Integer('Diastolic Pressure')
    frequency = fields.Integer('Heart Frequency')
    temperature = fields.Float('Temperature')
    lochia_amount = fields.Selection([
        (None, ''),
        ('n', 'normal'),
        ('e', 'abundant'),
        ('h', 'hemorrhage'),
        ], 'Lochia amount', sort=False)
    lochia_color = fields.Selection([
        (None, ''),
        ('r', 'rubra'),
        ('s', 'serosa'),
        ('a', 'alba'),
        ], 'Lochia color', sort=False)
    lochia_odor = fields.Selection([
        (None, ''),
        ('n', 'normal'),
        ('o', 'offensive'),
        ], 'Lochia odor', sort=False)
    uterus_involution = fields.Integer('Fundal Height',
        help="Distance between the symphysis pubis and the uterine fundus "
        "(S-FD) in cm")

    institution = fields.Many2One('gnuhealth.institution', 'Institution')

    healthprof = fields.Many2One(
        'gnuhealth.healthprofessional', 'Health Prof', readonly=True,
        help="Health Professional in charge, or that who entered the \
            information in the system")

    @staticmethod
    def default_institution():
        HealthInst = Pool().get('gnuhealth.institution')
        institution = HealthInst.get_institution()
        return institution

    @staticmethod
    def default_healthprof():
        pool = Pool()
        HealthProf= pool.get('gnuhealth.healthprofessional')
        return HealthProf.get_health_professional()


class Perinatal(ModelSQL, ModelView):
    'Perinatal Information'
    __name__ = 'gnuhealth.perinatal'

    name = fields.Many2One('gnuhealth.patient.pregnancy', 'Patient Pregnancy')
    admission_code = fields.Char('Code')
    # 1.6.4 Gravida number and abortion information go now in the pregnancy
    # header. It will be calculated as a function if needed
    gravida_number = fields.Integer('Gravida #')
    # Deprecated. Use End of Pregnancy as a general concept in the pregnancy
    # model
    # Abortion / Stillbirth / Live Birth
    abortion = fields.Boolean('Abortion')
    stillbirth = fields.Boolean('Stillbirth')
    admission_date = fields.DateTime('Admission',
        help="Date when she was admitted to give birth", required=True)
    # Prenatal evaluations deprecated in 1.6.4. Will be computed automatically
    prenatal_evaluations = fields.Integer('Prenatal evaluations',
        help="Number of visits to the doctor during pregnancy")
    start_labor_mode = fields.Selection([
        (None, ''),
        ('v', 'Vaginal - Spontaneous'),
        ('ve', 'Vaginal - Vacuum Extraction'),
        ('vf', 'Vaginal - Forceps Extraction'),
        ('c', 'C-section'),
        ], 'Delivery mode', sort=False)
    gestational_weeks = fields.Function(fields.Integer('Gestational wks'),
        'get_perinatal_information')
    gestational_days = fields.Integer('Days')
    fetus_presentation = fields.Selection([
        (None, ''),
        ('cephalic', 'Cephalic'),
        ('breech', 'Breech'),
        ('shoulder', 'Shoulder'),
        ], 'Fetus Presentation', sort=False)
    dystocia = fields.Boolean('Dystocia')
    placenta_incomplete = fields.Boolean('Incomplete',
        help='Incomplete Placenta')
    placenta_retained = fields.Boolean('Retained', help='Retained Placenta')
    abruptio_placentae = fields.Boolean('Abruptio Placentae',
        help='Abruptio Placentae')
    episiotomy = fields.Boolean('Episiotomy')
    #Vaginal tearing and forceps variables are deprecated in 1.6.4.
    #They are included in laceration and delivery mode respectively
    vaginal_tearing = fields.Boolean('Vaginal tearing')
    forceps = fields.Boolean('Forceps')
    monitoring = fields.One2Many('gnuhealth.perinatal.monitor', 'name',
        'Monitors')
    laceration = fields.Selection([
        (None, ''),
        ('perineal', 'Perineal'),
        ('vaginal', 'Vaginal'),
        ('cervical', 'Cervical'),
        ('broad_ligament', 'Broad Ligament'),
        ('vulvar', 'Vulvar'),
        ('rectal', 'Rectal'),
        ('bladder', 'Bladder'),
        ('urethral', 'Urethral'),
        ], 'Lacerations', sort=False)
    hematoma = fields.Selection([
        (None, ''),
        ('vaginal', 'Vaginal'),
        ('vulvar', 'Vulvar'),
        ('retroperitoneal', 'Retroperitoneal'),
        ], 'Hematoma', sort=False)
    notes = fields.Text('Notes')

    institution = fields.Many2One('gnuhealth.institution', 'Institution')

    healthprof = fields.Many2One(
        'gnuhealth.healthprofessional', 'Health Prof', readonly=True,
        help="Health Professional in charge, or that who entered the \
            information in the system")

    @staticmethod
    def default_institution():
        HealthInst = Pool().get('gnuhealth.institution')
        institution = HealthInst.get_institution()
        return institution

    @staticmethod
    def default_healthprof():
        pool = Pool()
        HealthProf= pool.get('gnuhealth.healthprofessional')
        return HealthProf.get_health_professional()




    def get_perinatal_information(self, name):
        if name == 'gestational_weeks':
            gestational_age = datetime.datetime.date(self.admission_date) - \
                self.name.lmp
            return (gestational_age.days) / 7


class PerinatalMonitor(ModelSQL, ModelView):
    'Perinatal Monitor'
    __name__ = 'gnuhealth.perinatal.monitor'

    name = fields.Many2One('gnuhealth.perinatal',
        'Patient Perinatal Evaluation')
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
        (None, ''),
        ('o', 'Occiput / Cephalic Posterior'),
        ('fb', 'Frank Breech'),
        ('cb', 'Complete Breech'),
        ('t', 'Transverse Lie'),
        ('t', 'Footling Breech'),
        ], 'Fetus Position', sort=False)


class GnuHealthPatient(ModelSQL, ModelView):
    'Add to the Medical patient_data class (gnuhealth.patient) the ' \
    'gynecological and obstetric fields.'
    __name__ = 'gnuhealth.patient'

    currently_pregnant = fields.Function(fields.Boolean('Pregnant'),
        'get_pregnancy_info')
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
    #From version 2.6 Gravida, premature, abortions and stillbirths are now
    # functional fields, computed from the obstetric information
    gravida = fields.Function(fields.Integer('Pregnancies',
        help="Number of pregnancies, computed from Obstetric history"),
        'patient_obstetric_info')
    premature = fields.Function(fields.Integer('Premature',
     help="Preterm < 37 wks live births"),'patient_obstetric_info')
     
    abortions = fields.Function(fields.Integer('Abortions'),
        'patient_obstetric_info')
    stillbirths = fields.Function(fields.Integer('Stillbirths'),
        'patient_obstetric_info')

    full_term = fields.Integer('Full Term', help="Full term pregnancies")
    # GPA Deprecated in 1.6.4. It will be used as a function or report from the
    # other fields
    #    gpa = fields.Char('GPA',
    #        help="Gravida, Para, Abortus Notation. For example G4P3A1 : 4 " \
    #        "Pregnancies, 3 viable and 1 abortion")
    # Deprecated. The born alive number will be calculated from pregnancies -
    # abortions - stillbirths
    #    born_alive = fields.Integer('Born Alive')
    # Deceased in 1st week or after 2nd weeks are deprecated since 1.6.4 .
    # The information will be retrieved from the neonatal or infant record
    #    deaths_1st_week = fields.Integer('Deceased during 1st week',
    #        help="Number of babies that die in the first week")
    #    deaths_2nd_week = fields.Integer('Deceased after 2nd week',
    #        help="Number of babies that die after the second week")
    # Perinatal Deprecated since 1.6.4 - Included in the obstetric history
    #    perinatal = fields.One2Many('gnuhealth.perinatal', 'name',
    #        'Perinatal Info')
    menstrual_history = fields.One2Many('gnuhealth.patient.menstrual_history',
        'name', 'Menstrual History')
    mammography_history = fields.One2Many(
        'gnuhealth.patient.mammography_history', 'name', 'Mammography History',
         states={'invisible': Not(Bool(Eval('mammography')))},
        )
    pap_history = fields.One2Many('gnuhealth.patient.pap_history', 'name',
        'PAP smear History',
         states={'invisible': Not(Bool(Eval('pap_test')))},
        )
    colposcopy_history = fields.One2Many(
        'gnuhealth.patient.colposcopy_history', 'name', 'Colposcopy History',
         states={'invisible': Not(Bool(Eval('colposcopy')))},
        )
    pregnancy_history = fields.One2Many('gnuhealth.patient.pregnancy', 'name',
        'Pregnancies')

    def get_pregnancy_info(self, name):
        if name == 'currently_pregnant':
            for pregnancy_history in self.pregnancy_history:
                if pregnancy_history.current_pregnancy:
                    return True
        return False

    def patient_obstetric_info(self,name):
        ''' Return the number of pregnancies, perterm, 
        abortion and stillbirths '''

        counter=0
        pregnancies = len(self.pregnancy_history)
         
        if (name == "gravida"):
            return pregnancies 

        if (name == "premature"):
            prematures=0
            while counter < pregnancies:
                result = self.pregnancy_history[counter].pregnancy_end_result
                preg_weeks = self.pregnancy_history[counter].pregnancy_end_age
                if (result == "live_birth" and
                    preg_weeks < 37):
                        prematures=prematures+1
                counter=counter+1
            return prematures

        if (name == "abortions"):
            abortions=0
            while counter < pregnancies:
                result = self.pregnancy_history[counter].pregnancy_end_result
                preg_weeks = self.pregnancy_history[counter].pregnancy_end_age
                if (result == "abortion"):
                    abortions=abortions+1
                counter=counter+1

            return abortions

        if (name == "stillbirths"):
            stillbirths=0
            while counter < pregnancies:
                result = self.pregnancy_history[counter].pregnancy_end_result
                preg_weeks = self.pregnancy_history[counter].pregnancy_end_age
                if (result == "stillbirth"):
                    stillbirths=stillbirths+1
                counter=counter+1
            return stillbirths


    @classmethod
    def view_attributes(cls):
        return [('//page[@id="page_gyneco_obs"]', 'states', {
                'invisible': Equal(Eval('biological_sex'), 'm'),
                })]

class PatientMenstrualHistory(ModelSQL, ModelView):
    'Menstrual History'
    __name__ = 'gnuhealth.patient.menstrual_history'

    name = fields.Many2One('gnuhealth.patient', 'Patient', readonly=True,
        required=True)
    evaluation = fields.Many2One('gnuhealth.patient.evaluation', 'Evaluation',
        domain=[('patient', '=', Eval('name'))],
        depends=['name'])
    evaluation_date = fields.Date('Date', help="Evaluation Date",
        required=True)
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

    institution = fields.Many2One('gnuhealth.institution', 'Institution')

    healthprof = fields.Many2One(
        'gnuhealth.healthprofessional', 'Reviewed', readonly=True,
        help="Health Professional who reviewed the information")

    @staticmethod
    def default_institution():
        HealthInst = Pool().get('gnuhealth.institution')
        institution = HealthInst.get_institution()
        return institution

    @staticmethod
    def default_healthprof():
        pool = Pool()
        HealthProf= pool.get('gnuhealth.healthprofessional')
        return HealthProf.get_health_professional()


    @staticmethod
    def default_evaluation_date():
        return Pool().get('ir.date').today()

    @staticmethod
    def default_evaluation_date():
        return Pool().get('ir.date').today()

    @staticmethod
    def default_frequency():
        return 'eumenorrhea'

    @staticmethod
    def default_volume():
        return 'normal'


class PatientMammographyHistory(ModelSQL, ModelView):
    'Mammography History'
    __name__ = 'gnuhealth.patient.mammography_history'

    name = fields.Many2One('gnuhealth.patient', 'Patient', readonly=True,
        required=True)
    evaluation = fields.Many2One('gnuhealth.patient.evaluation', 'Evaluation',
        domain=[('patient', '=', Eval('name'))],
        depends=['name'])
    evaluation_date = fields.Date('Date', help="Date", required=True)
    last_mammography = fields.Date('Previous', help="Last Mammography")
    result = fields.Selection([
        (None, ''),
        ('normal', 'normal'),
        ('abnormal', 'abnormal'),
        ], 'result', help="Please check the lab test results if the module is \
            installed", sort=False)
    comments = fields.Char('Remarks')

    institution = fields.Many2One('gnuhealth.institution', 'Institution')

    healthprof = fields.Many2One(
        'gnuhealth.healthprofessional', 'Reviewed', readonly=True,
        help="Health Professional who last reviewed the test")

    @staticmethod
    def default_institution():
        HealthInst = Pool().get('gnuhealth.institution')
        institution = HealthInst.get_institution()
        return institution

    @staticmethod
    def default_healthprof():
        pool = Pool()
        HealthProf= pool.get('gnuhealth.healthprofessional')
        return HealthProf.get_health_professional()


    @staticmethod
    def default_evaluation_date():
        return Pool().get('ir.date').today()

    @staticmethod
    def default_last_mammography():
        return Pool().get('ir.date').today()


class PatientPAPHistory(ModelSQL, ModelView):
    'PAP Test History'
    __name__ = 'gnuhealth.patient.pap_history'

    name = fields.Many2One('gnuhealth.patient', 'Patient', readonly=True,
        required=True)
    evaluation = fields.Many2One('gnuhealth.patient.evaluation', 'Evaluation',
        domain=[('patient', '=', Eval('name'))],
        depends=['name'])
    evaluation_date = fields.Date('Date', help="Date", required=True)
    last_pap = fields.Date('Previous', help="Last Papanicolau")
    result = fields.Selection([
        (None, ''),
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

    institution = fields.Many2One('gnuhealth.institution', 'Institution')

    healthprof = fields.Many2One(
        'gnuhealth.healthprofessional', 'Reviewed', readonly=True,
        help="Health Professional who last reviewed the test")

    @staticmethod
    def default_institution():
        HealthInst = Pool().get('gnuhealth.institution')
        institution = HealthInst.get_institution()
        return institution

    @staticmethod
    def default_healthprof():
        pool = Pool()
        HealthProf= pool.get('gnuhealth.healthprofessional')
        return HealthProf.get_health_professional()


    @staticmethod
    def default_evaluation_date():
        return Pool().get('ir.date').today()

    @staticmethod
    def default_last_pap():
        return Pool().get('ir.date').today()


class PatientColposcopyHistory(ModelSQL, ModelView):
    'Colposcopy History'
    __name__ = 'gnuhealth.patient.colposcopy_history'

    name = fields.Many2One('gnuhealth.patient', 'Patient', readonly=True,
        required=True)
    evaluation = fields.Many2One('gnuhealth.patient.evaluation', 'Evaluation',
        domain=[('patient', '=', Eval('name'))],
        depends=['name'])
    evaluation_date = fields.Date('Date', help="Date", required=True)
    last_colposcopy = fields.Date('Previous', help="Last colposcopy")
    result = fields.Selection([
        (None, ''),
        ('normal', 'normal'),
        ('abnormal', 'abnormal'),
        ], 'result', help="Please check the lab test results if the module is \
            installed", sort=False)
    comments = fields.Char('Remarks')

    institution = fields.Many2One('gnuhealth.institution', 'Institution')

    healthprof = fields.Many2One(
        'gnuhealth.healthprofessional', 'Reviewed', readonly=True,
        help="Health Professional who last reviewed the test")

    @staticmethod
    def default_institution():
        HealthInst = Pool().get('gnuhealth.institution')
        institution = HealthInst.get_institution()
        return institution

    @staticmethod
    def default_healthprof():
        pool = Pool()
        HealthProf= pool.get('gnuhealth.healthprofessional')
        return HealthProf.get_health_professional()


    @staticmethod
    def default_evaluation_date():
        return Pool().get('ir.date').today()

    @staticmethod
    def default_last_colposcopy():
        return Pool().get('ir.date').today()
