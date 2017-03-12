# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2008-2017 Luis Falcon <lfalcon@gnusolidario.org>
#    Copyright (C) 2013 Sebastián Marro <smarro@thymbra.com>
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
from trytond.pool import Pool
from .health_pediatrics_growth_charts_who import *
from .wizard import *
from .report import *


def register():
    Pool.register(
        PediatricsGrowthChartsWHO,
        OpenPediatricsGrowthChartsWHOReportStart,
        module='health_pediatrics_growth_charts_who', type_='model')
    Pool.register(
        OpenPediatricsGrowthChartsWHOReport,
        module='health_pediatrics_growth_charts_who', type_='wizard')
    Pool.register(
        PediatricsGrowthChartsWHOReport,
        WeightForAge,
        LengthHeightForAge,
        BMIForAge,
        module='health_pediatrics_growth_charts_who', type_='report')
