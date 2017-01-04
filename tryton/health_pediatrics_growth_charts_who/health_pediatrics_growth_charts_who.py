# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2008-2017 Luis Falcon <lfalcon@gnusolidario.org>
#    Copyright (C) 2013 Sebastián Marro <smarro@gnusolidario.org>
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

__all__ = ['PediatricsGrowthChartsWHO']


class PediatricsGrowthChartsWHO(ModelSQL, ModelView):
    'Pediatrics Growth Chart WHO'
    __name__ = 'gnuhealth.pediatrics.growth.charts.who'

    indicator = fields.Selection([
        ('l/h-f-a', 'Length/height for age'),
        ('w-f-a', 'Weight for age'),
        ('bmi-f-a', 'Body mass index for age (BMI for age)'),
        ], 'Indicator', sort=False, required=True)
    measure = fields.Selection([
        ('p', 'percentiles'),
        ('z', 'z-scores'),
        ], 'Measure')
    sex = fields.Selection([
        ('m', 'Male'),
        ('f', 'Female'),
        ], 'Sex')
    month = fields.Integer('Month')
    type = fields.Char('Type')
    value = fields.Float('Value')
