# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2008-2017 Luis Falcon <lfalcon@gnusolidario.org>
#    Copyright (C) 2013  Sebastián Marro <smarro@gnusolidario.org>
#    Copyright (C) 2011-2017 GNU Solidario <health@gnusolidario.org>
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
from trytond.model import fields
from trytond.pool import PoolMeta

__all__ = ['PatientEvaluation']
__metaclass__ = PoolMeta


class PatientEvaluation(metaclass=PoolMeta):
    __name__ = 'gnuhealth.patient.evaluation'

    age_months = fields.Function(fields.Integer('Patient Age in Months'),
        'get_patient_age_months')

    def get_patient_age_months(self, name):
        if self.patient:
            if self.patient.dob:
                delta = relativedelta(self.evaluation_start, self.patient.dob)
                return delta.years * 12 + delta.months
        return None
