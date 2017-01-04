##############################################################################
#
#    GNU Health: Reporting Module
#
#
#    Copyright (C) 2012-2014  Sebastian Marro <smarro@gnusolidario.org>
#    Copyright (C) 2013-2017 Luis Falcon <lfalcon@gnusolidario.org>
#    Copyright (C) 2011-2017 GNU Solidario <health@gnusolidario.org>
#
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
from sql import Literal, Join
from sql.aggregate import Max, Count
from trytond.model import ModelView, ModelSQL, fields
from trytond.wizard import Wizard, StateView, StateAction, StateTransition, \
    Button
from trytond.pyson import PYSONEncoder
from trytond.pool import Pool
from trytond.transaction import Transaction


__all__ = ['TopDiseases', 'OpenTopDiseasesStart', 'OpenTopDiseases']


class TopDiseases(ModelSQL, ModelView):
    'Top Diseases'
    __name__ = 'gnuhealth.top_diseases'

    disease = fields.Many2One('gnuhealth.pathology', 'Disease', select=True)
    cases = fields.Integer('Cases')

    @classmethod
    def __setup__(cls):
        super(TopDiseases, cls).__setup__()
        cls._order.insert(0, ('cases', 'DESC'))

    @staticmethod
    def table_query():
        pool = Pool()
        Evaluation = pool.get('gnuhealth.patient.evaluation')
        evaluation = Evaluation.__table__()
        source = evaluation
        where = evaluation.diagnosis != None
        if Transaction().context.get('start_date'):
            where &= evaluation.evaluation_start >= \
                Transaction().context['start_date']
        if Transaction().context.get('end_date'):
            where &= evaluation.evaluation_start <= \
                Transaction().context['end_date']
        if Transaction().context.get('group'):
            DiseaseGroupMembers = pool.get('gnuhealth.disease_group.members')
            diseasegroupmembers = DiseaseGroupMembers.__table__()
            join = Join(evaluation, diseasegroupmembers)
            join.condition = join.right.name == evaluation.diagnosis
            where &= join.right.disease_group == Transaction().context['group']
            source = join

        select = source.select(
            evaluation.diagnosis.as_('id'),
            Max(evaluation.create_uid).as_('create_uid'),
            Max(evaluation.create_date).as_('create_date'),
            Max(evaluation.write_uid).as_('write_uid'),
            Max(evaluation.write_date).as_('write_date'),
            evaluation.diagnosis.as_('disease'),
            Count(evaluation.diagnosis).as_('cases'),
            where=where,
            group_by=evaluation.diagnosis)

        if Transaction().context.get('number_records'):
            select.limit = Transaction().context['number_records']

        return select


class OpenTopDiseasesStart(ModelView):
    'Open Top Diseases'
    __name__ = 'gnuhealth.top_diseases.open.start'

    start_date = fields.Date('Start Date')
    end_date = fields.Date('End Date')
    group = fields.Many2One('gnuhealth.pathology.group', 'Disease Group')
    number_records = fields.Integer('Number of Records', required=True)

    @staticmethod
    def default_number_records():
        return 10


class OpenTopDiseases(Wizard):
    'Open Top Diseases'
    __name__ = 'gnuhealth.top_diseases.open'

    start = StateView('gnuhealth.top_diseases.open.start',
        'health_reporting.top_diseases_open_start_view_form', [
            Button('Cancel', 'end', 'tryton-cancel'),
            Button('Open', 'open_', 'tryton-ok', default=True),
            ])
    open_ = StateAction('health_reporting.act_top_diseases_form')

    def do_open_(self, action):
        action['pyson_context'] = PYSONEncoder().encode({
                'start_date': self.start.start_date,
                'end_date': self.start.end_date,
                'group': self.start.group.id if self.start.group else None,
                'number_records': self.start.number_records,
                })
        return action, {}

    def transition_open_(self):
        return 'end'
