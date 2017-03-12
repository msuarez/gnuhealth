# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2008-2017 Luis Falcon <falcon@gnu.org>
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
import pytz
from datetime import datetime
from trytond.pool import Pool
from trytond.transaction import Transaction
from trytond.report import Report

__all__ = ['PatientDiseaseReport', 'PatientMedicationReport', 
    'PatientVaccinationReport']

def get_print_date():
    Company = Pool().get('company.company')

    timezone = None
    company_id = Transaction().context.get('company')
    if company_id:
        company = Company(company_id)
        if company.timezone:
            timezone = pytz.timezone(company.timezone)

    dt = datetime.now()
    return datetime.astimezone(dt.replace(tzinfo=pytz.utc), timezone)


class PatientDiseaseReport(Report):
    __name__ = 'patient.disease'

    @classmethod
    def parse(cls, report, objects, data, localcontext):
        localcontext['print_date'] = get_print_date()
        localcontext['print_time'] = localcontext['print_date'].time()

        return super(PatientDiseaseReport, cls).parse(report, objects, data, 
            localcontext)


class PatientMedicationReport(Report):
    __name__ = 'patient.medication'

    @classmethod
    def parse(cls, report, objects, data, localcontext):
        localcontext['print_date'] = get_print_date()
        localcontext['print_time'] = localcontext['print_date'].time()

        return super(PatientMedicationReport, cls).parse(report, objects, data, 
            localcontext)


class PatientVaccinationReport(Report):
    __name__ = 'patient.vaccination'

    @classmethod
    def parse(cls, report, objects, data, localcontext):
        localcontext['print_date'] = get_print_date()
        localcontext['print_time'] = localcontext['print_date'].time()

        return super(PatientVaccinationReport, cls).parse(report, objects, data, 
            localcontext)
