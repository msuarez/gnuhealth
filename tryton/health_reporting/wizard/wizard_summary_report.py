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

from datetime import datetime, timedelta, date
from trytond.model import ModelView, fields
from trytond.wizard import Wizard, StateView, StateAction, StateTransition, \
    Button
from trytond.transaction import Transaction

__all__ = ['SummaryReportStart','SummaryReport']


class SummaryReportStart(ModelView):
    'Summary Report Start'
    __name__ = 'gnuhealth.summary.report.open.start'

    institution = fields.Many2One(
        'gnuhealth.institution', 'Institution',)

    start_date = fields.Date("Start")
    end_date = fields.Date("End")

    demographics = fields.Boolean("Demographics")
    patient_evaluations = fields.Boolean("Evaluations")

    @staticmethod
    def default_start_date():
        return date.today()

    @staticmethod
    def default_end_date():
        return date.today()

    @staticmethod
    def default_demographics():
        return True

class SummaryReport(Wizard):
    'Open Institution Summary Report'
    __name__ = 'gnuhealth.summary.report.open'

    start = StateView('gnuhealth.summary.report.open.start',
        'health_reporting.summary_report_open_start_view_form', [
            Button('Cancel', 'end', 'tryton-cancel'),
            Button('Open', 'open_', 'tryton-ok', default=True),
            ])
    
    open_ = StateAction('health_reporting.report_summary_information')

    def fill_data(self):
        return {
            'institution': (self.start.institution.id
                    if self.start.institution else None),
            'start_date': self.start.start_date,
            'end_date': self.start.end_date,
            'demographics': self.start.demographics,
            'patient_evaluations': self.start.patient_evaluations,
        }
    
    def do_open_(self, action):
        return action, self.fill_data()
            
    def transition_open_(self):
        return 'end'
