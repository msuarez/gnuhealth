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
from trytond.model import ModelView, ModelSQL, ModelSingleton, fields
from datetime import datetime
from dateutil.relativedelta import relativedelta
from trytond.pool import Pool
from trytond.transaction import Transaction
from trytond.pyson import Eval, Not, Bool


__all__ = ['InpatientRegistration','InpatientIcu','Glasgow','ApacheII',
            'PatientRounding']


class InpatientRegistration(ModelSQL, ModelView):
    'Patient admission History'
    __name__ = 'gnuhealth.inpatient.registration'
    icu = fields.Boolean('ICU',help='Shows if patient was admitted to'
        ' the Intensive Care Unit during the hospitalization period')
    icu_admissions = fields.One2Many('gnuhealth.inpatient.icu',
        'name', "ICU Admissions")

class InpatientIcu(ModelSQL, ModelView):
    'Patient ICU Information'
    __name__ = 'gnuhealth.inpatient.icu'
    
    
    def icu_duration(self, name):

        now = datetime.now()
        admission = datetime.strptime(str(self.icu_admission_date), '%Y-%m-%d %H:%M:%S')

        if self.discharged_from_icu:
            discharge = datetime.strptime(str(self.icu_discharge_date), '%Y-%m-%d %H:%M:%S')
            delta = relativedelta(discharge, admission)
        else:
            delta = relativedelta(now, admission)
            msg = ''
        years_months_days = str(delta.years) + 'y ' \
                + str(delta.months) + 'm ' \
                + str(delta.days) + 'd'
        return years_months_days

    
    name = fields.Many2One('gnuhealth.inpatient.registration',
        'Registration Code', required=True)
    icu_admission_date = fields.DateTime('ICU Admission', help="ICU Admission Date",required=True)
    discharged_from_icu = fields.Boolean('Discharged')
    icu_discharge_date = fields.DateTime('Discharge', states={
            'invisible': Not(Bool(Eval('discharged_from_icu'))),
            'required': Bool(Eval('discharged_from_icu')),
            },
        depends=['discharged_from_icu'])
    icu_stay = fields.Function(fields.Char('Duration'), 'icu_duration')


class Glasgow(ModelSQL, ModelView):
    'Glasgow Coma Scale'
    __name__ = 'gnuhealth.icu.glasgow'


    name = fields.Many2One('gnuhealth.inpatient.registration',
        'Registration Code', required=True)

    evaluation_date = fields.DateTime('Date', help="Date / Time",required=True)

    glasgow = fields.Integer('Glasgow',
        on_change_with=['glasgow_verbal', 'glasgow_motor', 'glasgow_eyes'],
        help='Level of Consciousness - on Glasgow Coma Scale :  < 9 severe -'
        ' 9-12 Moderate, > 13 minor')
    glasgow_eyes = fields.Selection([
        ('1', '1 : Does not Open Eyes'),
        ('2', '2 : Opens eyes in response to painful stimuli'),
        ('3', '3 : Opens eyes in response to voice'),
        ('4', '4 : Opens eyes spontaneously'),
        ], 'Eyes', sort=False)
    glasgow_verbal = fields.Selection([
        ('1', '1 : Makes no sounds'),
        ('2', '2 : Incomprehensible sounds'),
        ('3', '3 : Utters inappropriate words'),
        ('4', '4 : Confused, disoriented'),
        ('5', '5 : Oriented, converses normally'),
        ], 'Verbal', sort=False)
    glasgow_motor = fields.Selection([
        ('1', '1 : Makes no movement'),
        ('2', '2 : Extension to painful stimuli - decerebrate response -'),
        ('3', '3 : Abnormal flexion to painful stimuli (decorticate response)'),
        ('4', '4 : Flexion / Withdrawal to painful stimuli'),
        ('5', '5 : localizes painful stimuli'),
        ('6', '6 : Obeys commands'),
        ], 'Motor', sort=False)

    @staticmethod
    def default_glasgow_eyes():
        return '4'

    @staticmethod
    def default_glasgow_verbal():
        return '5'

    @staticmethod
    def default_glasgow_motor():
        return '6'

    @staticmethod
    def default_glasgow():
        return 15

    # Default evaluation date
    @staticmethod
    def default_evaluation_date():
        return datetime.now()

    def on_change_with_glasgow(self):
        return int(self.glasgow_motor) + int(self.glasgow_eyes) + int(self.glasgow_verbal)

    # Return the Glasgow Score with each component
    def get_rec_name(self, name):
        if self.name:
            res = str(self.glasgow) + ': ' + 'E' + self.glasgow_eyes + ' V' + \
                self.glasgow_verbal + ' M' + self.glasgow_motor 
        return res



class ApacheII(ModelSQL, ModelView):
    'Apache II scoring'
    __name__ = 'gnuhealth.icu.apache2'
    
    name = fields.Many2One('gnuhealth.inpatient.registration',
        'Registration Code', required=True)
    score_date = fields.DateTime('Date', help="Date of the score",required=True)

    age = fields.Integer ('Age', help='Patient age in years')
    temperature = fields.Float ('Temperature', help='Rectal temperature')
    mean_ap = fields.Integer ('MAP',help = 'Mean Arterial Pressure')
    heart_rate = fields.Integer ('Heart Rate')
    respiratory_rate = fields.Integer ('Respiratory Rate')
    fio2 = fields.Float ('FiO2')
    pao2 = fields.Integer ('PaO2')
    paco2 = fields.Integer ('PaCO2')
    aado2 = fields.Integer ('A-a DO2', on_change_with =
        ['fio2','pao2','paco2'])

    ph = fields.Float ('pH')
    serum_sodium = fields.Integer ('Sodium')
    serum_potassium = fields.Float ('Potassium')
    serum_creatinine = fields.Float ('Creatinine')
    arf = fields.Boolean ('ARF', help='Acute Renal Failure')
    wbc = fields.Float ('WBC', help="White blood cells x 1000 - if you"
        " want to input 4500 wbc / ml, type in 4.5")
    hematocrit = fields.Float ('Hematocrit')
    gcs = fields.Integer ('GSC', help='Last Glasgow Coma Scale'
        ' You can use the GSC calculator from the Patient Evaluation Form.')
    chronic_condition = fields.Boolean ('Chronic condition', help='Organ Failure '
        'or immunocompromised patient')
    hospital_admission_type = fields.Selection([
        ('me', 'Medical or emergency postoperative'),
        ('el', 'elective postoperative')],
        'Hospital Admission Type', states={
            'invisible': Not(Bool(Eval('chronic_condition'))),
            'required': Bool(Eval('chronic_condition'))})

    apache_score = fields.Integer ('Score', on_change_with = 
        ['age', 'temperature', 'mean_ap', 'heart_rate', 'respiratory_rate',
        'fio2','pao2','aado2','ph','serum_sodium','serum_potassium',
        'serum_creatinine','arf','wbc','hematocrit','gcs','chronic_condition',
        'hospital_admission_type'])
    

    #Default FiO2 PaO2 and PaCO2 so we do the A-a gradient 
    #calculation with non-null values


    def on_change_with_aado2(self):
    # Calculates the Alveolar-arterial difference
    # based on FiO2, PaCO2 and PaO2 values
        if ( self.fio2 and self.paco2 and self.pao2 ):
            return (713 * self.fio2) - (self.paco2 / 0.8) - self.pao2
     
    def on_change_with_apache_score(self):
    # Calculate the APACHE SCORE from the variables in the    
        
        total = 0
        # Age 
        if (self.age):
            if (self.age > 44 and self.age < 55):
                total = total + 2
            elif (self.age > 54 and self.age < 65):
                total = total + 3
            elif (self.age > 64 and self.age < 75):
                total = total + 5
            elif (self.age > 74):
                total = total + 6

        # Temperature 
        if (self.temperature):
            if ((self.temperature >= 38.5 and self.temperature < 39) or
                (self.temperature >= 34 and self.temperature < 36)):
                    total = total + 1
            elif (self.temperature >= 32 and self.temperature < 34):
                total = total + 2
            elif ((self.temperature >= 30 and self.temperature < 32) or
                (self.temperature >= 39 and self.temperature < 41)):
                total = total + 3
            elif (self.temperature >= 41 or self.temperature < 30):
                total = total + 4

        # Mean Arterial Pressure (MAP) 
        if (self.mean_ap):
            if ((self.mean_ap >= 110 and self.mean_ap < 130) or
                (self.mean_ap >= 50 and self.mean_ap < 70)):
                    total = total + 2
            elif (self.mean_ap >= 130 and self.mean_ap < 160):
                total = total + 3
            elif (self.mean_ap >= 160 or self.mean_ap < 50):
                total = total + 4

        # Heart Rate 
        if (self.heart_rate):
            if ((self.heart_rate >= 55 and self.heart_rate < 70) or
                (self.heart_rate >= 110 and self.heart_rate < 140)):
                    total = total + 2
            elif ((self.heart_rate >= 40 and self.heart_rate < 55) or
                (self.heart_rate >= 140 and self.heart_rate < 180)):
                    total = total + 3
            elif (self.heart_rate >= 180 or self.heart_rate < 40):
                total = total + 4

        # Respiratory Rate 
        if (self.respiratory_rate):
            if ((self.respiratory_rate >= 10 and self.respiratory_rate < 12) or
                (self.respiratory_rate >= 25 and self.respiratory_rate < 35)):
                    total = total + 1
            elif (self.respiratory_rate >= 6 and self.respiratory_rate < 10):
                    total = total + 2
            elif (self.respiratory_rate >= 35 and self.respiratory_rate < 50):
                    total = total + 3
            elif (self.respiratory_rate >= 50 or self.respiratory_rate < 6):
                total = total + 4

        # FIO2 
        if (self.fio2):
            # If Fi02 is greater than 0.5, we measure the AaDO2 gradient
            # Otherwise, we take into account the Pa02 value 
 
            if (self.fio2 >= 0.5):
                if (self.aado2 >= 200 and self.aado2 < 350):
                    total = total + 2

                elif (self.aado2 >= 350 and self.aado2 < 500):
                    total = total + 3

                elif (self.aado2 >= 500):
                    total = total + 4
            
            else:
                if (self.pao2 >= 61 and self.pao2 < 71):
                    total = total + 1
                
                elif (self.pao2 >= 55 and self.pao2 < 61):
                    total = total + 3

                elif (self.pao2 < 55):
                    total = total + 4
                

        # Arterial pH 
        if (self.ph):
            if (self.ph >= 7.5 and self.ph < 7.6):
                    total = total + 1
            elif (self.ph >= 7.25 and self.ph < 7.33):
                    total = total + 2
            elif ((self.ph >= 7.15 and self.ph < 7.25) or
                (self.ph >= 7.6 and self.ph < 7.7)):
                    total = total + 3
            elif (self.ph >= 7.7 or self.ph < 7.15):
                total = total + 4

        # Serum Sodium 
        if (self.serum_sodium):
            if (self.serum_sodium >= 150 and self.serum_sodium < 155):
                    total = total + 1
            elif ((self.serum_sodium >= 155 and self.serum_sodium < 160) or
                (self.serum_sodium >= 120 and self.serum_sodium < 130)):
                    total = total + 2
            elif ((self.serum_sodium >= 160 and self.serum_sodium < 180) or
                (self.serum_sodium >= 111 and self.serum_sodium < 120)):
                    total = total + 3
            elif (self.serum_sodium >= 180 or self.serum_sodium < 111):
                total = total + 4

        # Serum Potassium 
        if (self.serum_potassium):
            if ((self.serum_potassium >= 3 and self.serum_potassium < 3.5) or
                (self.serum_potassium >= 5.5 and self.serum_potassium < 6)):
                    total = total + 1
            elif (self.serum_potassium >= 2.5 and self.serum_potassium < 3):
                total = total + 2
            elif (self.serum_potassium >= 6 and self.serum_potassium < 7):
                total = total + 3
            elif (self.serum_potassium >= 7 or self.serum_potassium < 2.5):
                total = total + 4

        # Serum Creatinine 
        if (self.serum_creatinine):
            arf_factor=1
            if (self.arf):
            # We multiply by 2 the score if there is concomitant ARF
                arf_factor=2
            if ((self.serum_creatinine < 0.6) or
                (self.serum_creatinine >= 1.5 and self.serum_creatinine < 2)):
                    total = total + 2*arf_factor
            elif (self.serum_creatinine >= 2 and self.serum_creatinine < 3.5):
                total = total + 3*arf_factor
            elif (self.serum_creatinine >= 3.5):
                total = total + 4*arf_factor

        # Hematocrit 
        if (self.hematocrit):
            if (self.hematocrit >= 46 and self.hematocrit < 50):
                total = total + 1
            elif ((self.hematocrit >= 50 and self.hematocrit < 60) or
                (self.hematocrit >= 20 and self.hematocrit < 30)):
                    total = total + 2
            elif (self.hematocrit >= 60 or self.hematocrit < 20):
                total = total + 4

        # WBC ( x 1000 )
        if (self.wbc):
            if (self.wbc >= 15 and self.wbc < 20):
                total = total + 1
            elif ((self.wbc >= 20 and self.wbc < 40) or
                (self.wbc >= 1 and self.wbc < 3)):
                    total = total + 2
            elif (self.wbc >= 40 or self.wbc < 1):
                total = total + 4

        # Immnunocompromised or severe organ failure
        if (self.chronic_condition):
            if (self.hospital_admission_type == 'me'):
                total = total + 5
            else:
                total = total + 2
                
        return total

# Nursing Rounding for ICU
# Append to the existing model the new functionality for ICU

class PatientRounding(ModelSQL, ModelView):
    'Patient Rounding'
    __name__ = 'gnuhealth.patient.rounding'

    icu_patient = fields.Boolean('ICU', help='Check this box if this is'
    'an Intensive Care Unit rounding.')
    # Neurological assesment
    gsc = fields.Many2One ('gnuhealth.icu.glasgow','GSC',domain = [('name', '=', Eval('name'))])

    pupil_dilation = fields.Selection([
        ('normal', 'Normal'),
        ('miosis', 'Miosis'),
        ('mydriasis', 'Mydriasis')],
        'Pupil Dilation')
    
    left_pupil = fields.Integer ('L', help="size in mm of left pupil")
    right_pupil = fields.Integer ('R', help="size in mm of right pupil")
    
    anisocoria = fields.Boolean ('Anisocoria') 
 
    # Respiratory assesment
    
    ventilation = fields.Selection([
        ('own', 'Maintains Own'),
        ('nppv', 'Non-Invasive'),
        ('ett', 'ETT'),
        ('tracheostomy', 'Traqcheostomy')],
        'Ventilation', help="NPPV = Non-Invasive Positive " 
            "Pressure Ventilation, BiPAP-CPAP \n"
            "ETT - Endotracheal Tube")
    
    respiration_type = fields.Selection([
        ('regular', 'Regular'),
        ('deep', 'Deep'),
        ('shallow', 'Shallow'),
        ('labored', 'Labored'),
        ('intercostal', 'Intercostal')],
        'Respiration')


    @staticmethod
    def default_pupil_dilation():
        return 'normal'
