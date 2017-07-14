# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2011-2014 Sebastian Marro <smarro@gnusolidario.org>
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
from .wizard import *
from .report import *

def register():
    Pool.register(
        TopDiseases,
        OpenTopDiseasesStart,
        OpenEvaluationsStart,
        SummaryReportStart,
        EvaluationsDoctor,
        EvaluationsSpecialty,
        EvaluationsSector,
        module='health_reporting', type_='model')
    Pool.register(
        OpenTopDiseases,
        OpenEvaluations,
        SummaryReport,
        module='health_reporting', type_='wizard')

    Pool.register(
        InstitutionSummaryReport,
        module='health_reporting', type_='report')

