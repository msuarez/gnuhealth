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
from trytond.transaction import Transaction

__all__ = ['InstitutionSummaryReport']

class InstitutionSummaryReport(Report):
    __name__ = 'gnuhealth.summary.report'

    @classmethod
    def get_new_patients(cls, start_date, end_date):
        """ Return Total Number of new registered patients """
        cursor = Transaction().cursor
        cursor.execute("SELECT COUNT(activation_date) \
            FROM party_party \
            WHERE activation_date BETWEEN \
            %s AND %s and is_patient=True",(start_date, end_date))
       
        res = cursor.fetchone()
        return(res)

    @classmethod
    def get_total_patients(cls):
        """ Return Total Number of registered patients in the system """
        cursor = Transaction().cursor
        cursor.execute("SELECT COUNT(activation_date) \
            FROM party_party \
            WHERE is_patient=True")
       
        res = cursor.fetchone()
        return(res)

    @classmethod
    def parse(cls, report, objects, data, localcontext):
        Patient = Pool().get('gnuhealth.patient')
        Evaluation = Pool().get('gnuhealth.patient.evaluation')

        start_date = data['start_date']
        end_date = data['end_date']

        localcontext['start_date'] = data['start_date']
        localcontext['end_date'] = data['end_date']

        localcontext['new_patients'] = \
            InstitutionSummaryReport().get_new_patients(start_date, end_date)
        localcontext['total_patients'] = \
            InstitutionSummaryReport().get_total_patients()

        return super(InstitutionSummaryReport, cls).parse(report,
            objects, data, localcontext)

