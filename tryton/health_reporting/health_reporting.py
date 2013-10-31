##############################################################################
#
#    GNU Health: Reporting Module
#    
#    
#    Copyright (C) 2012-2013  Sebastian Marro <smarro@gnusolidario.org>
#    Copyright (C) 2013  Luis Falcon <falcon@gnu.org>
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
from trytond.wizard import Wizard, StateView, StateAction, Button
from trytond.pyson import PYSONEncoder
from trytond.pool import Pool
from sql import *
from sql.functions import Now
from sql.aggregate import *
from sql.conditionals import *

from trytond.transaction import Transaction


__all__ = ['TopDiseases', 'OpenTopDiseasesStart', 'OpenTopDiseases',
    'Evaluations', 'OpenEvaluations', 'OpenEvaluationsStart']


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
        
        select = evaluation.select (
            evaluation.diagnosis.as_('id'),
            Literal(0).as_('create_uid'),
            Now().as_('create_date'),
            Literal(None).as_('write_uid'),
            Literal(None).as_('write_date'),
            Count(evaluation.diagnosis).as_('cases'),
            group_by = [evaluation.diagnosis]
        )
        
        return (select)

        
class OpenTopDiseasesStart(ModelView):
    'Open Top Diseases'
    __name__ = 'gnuhealth.top_diseases.open.start'

    start_date = fields.Date('Start Date')
    end_date = fields.Date('End Date')
    group = fields.Many2One('gnuhealth.pathology.group', 'Disease Group')
    number_records = fields.Char('Number of Records')


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


class OpenEvaluationsStart(ModelView):
    'Open Evaluations'
    __name__ = 'gnuhealth.evaluations.open.start'

    start_date = fields.Date('Start Date')
    end_date = fields.Date('End Date')


class OpenEvaluations(Wizard):
    'Open Evaluations'
    __name__ = 'gnuhealth.evaluations.open'

    start = StateView('gnuhealth.evaluations.open.start',
        'health_reporting.evaluations_open_start_view_form', [
            Button('Cancel', 'end', 'tryton-cancel'),
            Button('Open', 'open_', 'tryton-ok', default=True),
            ])
    open_ = StateAction('health_reporting.act_evaluations_form')

    def do_open_(self, action):
        action['pyson_context'] = PYSONEncoder().encode({
                'start_date': self.start.start_date,
                'end_date': self.start.end_date,
                })
        return action, {}

    def transition_open_(self):
        return 'end'


class Evaluations(ModelSQL, ModelView):
    'Evaluations'
    __name__ = 'gnuhealth.evaluations'

    doctor = fields.Many2One('gnuhealth.physician',
     'Health Professional', select=True)
    evaluations = fields.Integer('Evaluations')

    @classmethod
    def table_query(cls):
        return True
