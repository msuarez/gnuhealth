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
from trytond.model import ModelView, fields
from trytond.wizard import Wizard, StateView, StateAction, StateTransition, \
    Button
from trytond.transaction import Transaction

__all__ = ['OpenPediatricsGrowthChartsWHOReportStart',
    'OpenPediatricsGrowthChartsWHOReport']


class OpenPediatricsGrowthChartsWHOReportStart(ModelView):
    'Open Pediatrics Growth Charts WHO Report Start'
    __name__ = 'gnuhealth.pediatrics.growth.charts.who.report.open.start'

    indicator = fields.Selection([
        ('l/h-f-a', 'Length/height for age'),
        ('w-f-a', 'Weight for age'),
        ('bmi-f-a', 'Body mass index for age (BMI for age)'),
        ], 'Indicator', sort=False, required=True)
    measure = fields.Selection([
        ('p', 'percentiles'),
        ('z', 'z-scores'),
        ], 'Measure', required=True)


class OpenPediatricsGrowthChartsWHOReport(Wizard):
    'Open Pediatrics Growth Charts WHO Report'
    __name__ = 'gnuhealth.pediatrics.growth.charts.who.report.open'

    start = StateView('gnuhealth.pediatrics.growth.charts.who.report.open.start',
        'health_pediatrics_growth_charts_who.growth_charts_who_open_start_view_form', [
            Button('Cancel', 'end', 'tryton-cancel'),
            Button('Open', 'choose', 'tryton-ok', default=True),
            ])
    choose = StateTransition()
    print_wfa = StateAction('health_pediatrics_growth_charts_who.report_pediatrics_growth_charts_who_wfa')
    print_lhfa = StateAction('health_pediatrics_growth_charts_who.report_pediatrics_growth_charts_who_lhfa')
    print_bmifa = StateAction('health_pediatrics_growth_charts_who.report_pediatrics_growth_charts_who_bmifa')

    def transition_choose(self):
        if self.start.indicator == 'w-f-a':
            return 'print_wfa'
        elif self.start.indicator == 'l/h-f-a':
            return 'print_lhfa'
        else:
            return 'print_bmifa'

    def fill_data(self):
        return {
            'patient': Transaction().context.get('active_id'),
            'indicator': self.start.indicator,
            'measure': self.start.measure,
            }

    def do_print_wfa(self, action):
        return action, self.fill_data()

    def do_print_lhfa(self, action):
        return action, self.fill_data()

    def do_print_bmifa(self, action):
        return action, self.fill_data()
