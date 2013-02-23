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
from trytond.pool import Pool
from trytond.transaction import Transaction
from trytond.pyson import Eval, Not, Bool


__all__ = ['InpatientRegistration','InpatientIcu']


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
        admission = datetime.strptime(str(icu_admission_date), '%Y-%m-%d %H:%M:%S')

        if discharged_from_icu:
            discharge = datetime.strptime(icu_discharge_date, '%Y-%m-%d %H:%M:%S')
            delta = relativedelta(discharge, admission)
            msg = "Discharged"
        else:
            delta = relativedelta(now, admission)
            msg = ''
        years_months_days = str(delta.years) + 'y ' \
                + str(delta.months) + 'm ' \
                + str(delta.days) + 'd' + msg

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

    
