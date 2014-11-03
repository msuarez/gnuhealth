# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2008-2014 Luis Falcon <falcon@gnu.org>
#    Copyright (C) 2011-2014 GNU Solidario <health@gnusolidario.org>
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
from datetime import datetime
from trytond.report import Report
from trytond.pool import Pool

__all__ = ['SummaryReport']


class SummaryReport(Report):
    __name__ = 'gnuhealth.summary.report'

    @classmethod
    def parse(cls, report, objects, data, localcontext):
        Patient = Pool.get('gnuhealth.patient')
        Evaluation = Pool.get('gnuhealth.patient.evaluation')

        localcontext['new_patients'] = 10
        
        return super(SummaryReport, cls).parse(report,
            objects, data, localcontext)


