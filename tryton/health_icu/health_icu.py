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


__all__ = ['InpatientRegistration','InpatientIcu','ApacheII']


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


class ApacheII(ModelSQL, ModelView):
    'Apache II scoring'
    __name__ = 'gnuhealth.icu.apache2'
    
    name = fields.Many2One('gnuhealth.inpatient.registration',
        'Registration Code', required=True)
    score_date = fields.DateTime('Date', help="Date of the score",required=True)

    age = fields.Integer ('Age', help='Patient age in years',required=True)
    temperature = fields.Float ('Temperature', help='Rectal temperature')
    mean_ap = fields.Integer ('MAP',help = 'Mean Arterial Pressure')
    heart_rate = fields.Integer ('Heart Rate')
    respiratory_rate = fields.Integer ('Respiratory Rate')
    fio2 = fields.Integer ('FiO2')
    pao2 = fields.Integer ('PaO2')
    ph = fields.Float ('pH')
    serum_sodium = fields.Integer ('Sodium')
    serum_potassium = fields.Integer ('Potassium')
    serum_creatinine = fields.Integer ('Creatinine')
    arf = fields.Integer ('ARF', help='Acute Renal Failure')
    wbc = fields.Integer ('WBC')
    hematocrit = fields.Float ('Hematocrit')
    gcs = fields.Integer ('GSC', help='Last Glasgow Coma Scale'
        ' You can use the GSC calculator from the Patient Evaluation Form.')
    chronic_condition = fields.Boolean ('Chronic condition', help='Organ Failure '
        'or immunocompromised patient')
    apache_score = fields.Integer ('Score', on_change_with = 
        ['age', 'temperature', 'mean_ap', 'heart_rate', 'respiratory_rate',
        'fio2','pao2','ph','serum_sodium','serum_potassium','serum_creatinine',
        'arf','wbc','hematocrit','gcs','chronic_condition'])
    


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
            if ((self.heart_rate >= 40 and self.heart_rate < 55) or
                (self.heart_rate >= 140 and self.heart_rate < 180)):
                    total = total + 3
            elif (self.heart_rate >= 180 or self.heart_rate < 40):
                total = total + 4
            
        return total

