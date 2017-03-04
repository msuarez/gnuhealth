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
from datetime import datetime
from trytond.report import Report
from trytond.pool import Pool

__all__ = ['PediatricsGrowthChartsWHOReport', 'WeightForAge',
    'LengthHeightForAge', 'BMIForAge']

_TYPES = {
    '-3': 'p3',
    '-2': 'p15',
    '0': 'p50',
    '2': 'p85',
    '3': 'p97',
    }
_INDICATORS = {
    'l/h-f-a': 'Length/height for age',
    'w-f-a': 'Weight for age',
    'bmi-f-a': 'Body mass index for age (BMI for age)',
    }
_MEASURES = {
    'p': 'percentiles',
    'z': 'z-scores',
    }
_GENDERS = {
    'f': 'Girls',
    'm': 'Boys',
    }


class PediatricsGrowthChartsWHOReport(Report):
    __name__ = 'gnuhealth.pediatrics.growth.charts.who.report'

    @classmethod
    def get_context(cls, records, data):
        pool = Pool()
        GrowthChartsWHO = pool.get('gnuhealth.pediatrics.growth.charts.who')
        Patient = pool.get('gnuhealth.patient')
        Evaluation = pool.get('gnuhealth.patient.evaluation')

        context = super(PediatricsGrowthChartsWHOReport, cls).get_context(records, data)

        patient = Patient(data['patient'])

        growthchartswho = GrowthChartsWHO.search([
                ('indicator', '=', data['indicator']),
                ('measure', '=', data['measure']),
                ('sex', '=', patient.name.gender),
                ], order=[('month', 'ASC')],
                )

        context['title'] = _INDICATORS[data['indicator']] + ' ' + \
            _GENDERS[patient.name.gender]
        context['subtitle'] = 'Birth to 5 years (%s)' % \
            _MEASURES[data['measure']]
        context['name'] = patient.name.rec_name
        context['puid'] = patient.puid
        context['date'] = datetime.now().date()
        context['age'] = patient.age
        context['measure'] = data['measure']

        if data['measure'] == 'p':
            context['p3'] = '3rd'
            context['p15'] = '15th'
            context['p50'] = '50th'
            context['p85'] = '85th'
            context['p97'] = '97th'
        else:
            context['p3'] = '-3'
            context['p15'] = '-2'
            context['p50'] = '0'
            context['p85'] = '2'
            context['p97'] = '3'

        for value in growthchartswho:
            if data['measure'] == 'p':
                context[value.type.lower() + '_' + str(value.month)] = \
                    value.value
            else:
                context[_TYPES[value.type] + '_' + str(value.month)] = \
                    value.value

        evaluations = Evaluation.search([
                ('patient', '=', data['patient']),
                ])

        for month in range(61):
            context['v' + str(month)] = ''

        for evaluation in evaluations:
            if evaluation.age_months is not None:
                con = ''.join(['v', str(evaluation.age_months)])
                if data['indicator'] == 'l/h-f-a':
                    context[con] = evaluation.height
                elif data['indicator'] == 'w-f-a':
                    context[con] = evaluation.weight
                else:
                    context[con] = evaluation.bmi

        return context

class WeightForAge(PediatricsGrowthChartsWHOReport):
    __name__ = 'gnuhealth.pediatrics.growth.charts.who.wfa.report'


class LengthHeightForAge(PediatricsGrowthChartsWHOReport):
    __name__ = 'gnuhealth.pediatrics.growth.charts.who.lhfa.report'


class BMIForAge(PediatricsGrowthChartsWHOReport):
    __name__ = 'gnuhealth.pediatrics.growth.charts.who.bmifa.report'
