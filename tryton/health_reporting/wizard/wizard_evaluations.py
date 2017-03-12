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


__all__ = ['OpenEvaluationsStart', 'OpenEvaluations', 'EvaluationsDoctor',
    'EvaluationsSpecialty', 'EvaluationsSector']


class OpenEvaluationsStart(ModelView):
    'Open Evaluations'
    __name__ = 'gnuhealth.evaluations.open.start'

    start_date = fields.Date('Start Date')
    end_date = fields.Date('End Date')
    group_by = fields.Selection([
        ('doctor', 'Doctor'),
        ('specialty', 'Specialty'),
        ('sector', 'Sector'),
        ], 'Group By', sort=False, required=True)


class OpenEvaluations(Wizard):
    'Open Evaluations'
    __name__ = 'gnuhealth.evaluations.open'

    start = StateView('gnuhealth.evaluations.open.start',
        'health_reporting.evaluations_open_start_view_form', [
            Button('Cancel', 'end', 'tryton-cancel'),
            Button('Open', 'select', 'tryton-ok', default=True),
            ])
    select = StateTransition()
    open_doctor = StateAction('health_reporting.act_evaluations_doctor')
    open_specialty = StateAction('health_reporting.act_evaluations_specialty')
    open_sector = StateAction('health_reporting.act_evaluations_sector')

    def transition_select(self):
        return 'open_' + self.start.group_by

    def do_open_doctor(self, action):
        action['pyson_context'] = PYSONEncoder().encode({
                'start_date': self.start.start_date,
                'end_date': self.start.end_date,
                })
        return action, {}

    def do_open_specialty(self, action):
        action['pyson_context'] = PYSONEncoder().encode({
                'start_date': self.start.start_date,
                'end_date': self.start.end_date,
                })
        return action, {}

    def do_open_sector(self, action):
        action['pyson_context'] = PYSONEncoder().encode({
                'start_date': self.start.start_date,
                'end_date': self.start.end_date,
                })
        return action, {}

    def transition_open_doctor(self):
        return 'end'

    def transition_open_specialty(self):
        return 'end'

    def transition_open_sector(self):
        return 'end'


class EvaluationsDoctor(ModelSQL, ModelView):
    'Evaluations per Doctor'
    __name__ = 'gnuhealth.evaluations_doctor'

    doctor = fields.Many2One('gnuhealth.healthprofessional', 'Doctor')
    evaluations = fields.Integer('Evaluations')

    @staticmethod
    def table_query():
        pool = Pool()
        Evaluation = pool.get('gnuhealth.patient.evaluation')
        evaluation = Evaluation.__table__()
        where = Literal(True)
        if Transaction().context.get('start_date'):
            where &= evaluation.evaluation_start >= \
                Transaction().context['start_date']
        if Transaction().context.get('end_date'):
            where &= evaluation.evaluation_start <= \
                Transaction().context['end_date']

        return evaluation.select(
            evaluation.healthprof.as_('id'),
            Max(evaluation.create_uid).as_('create_uid'),
            Max(evaluation.create_date).as_('create_date'),
            Max(evaluation.write_uid).as_('write_uid'),
            Max(evaluation.write_date).as_('write_date'),
            evaluation.healthprof.as_('doctor'),
            Count(evaluation.id).as_('evaluations'),
            where=where,
            group_by=evaluation.healthprof)


class EvaluationsSpecialty(ModelSQL, ModelView):
    'Evaluations per Specialty'
    __name__ = 'gnuhealth.evaluations_specialty'

    specialty = fields.Many2One('gnuhealth.specialty', 'Specialty')
    evaluations = fields.Integer('Evaluations')

    @staticmethod
    def table_query():
        pool = Pool()
        Evaluation = pool.get('gnuhealth.patient.evaluation')
        evaluation = Evaluation.__table__()
        where = evaluation.specialty != None
        if Transaction().context.get('start_date'):
            where &= evaluation.evaluation_start >= \
                Transaction().context['start_date']
        if Transaction().context.get('end_date'):
            where &= evaluation.evaluation_start <= \
                Transaction().context['end_date']

        return evaluation.select(
            evaluation.specialty.as_('id'),
            Max(evaluation.create_uid).as_('create_uid'),
            Max(evaluation.create_date).as_('create_date'),
            Max(evaluation.write_uid).as_('write_uid'),
            Max(evaluation.write_date).as_('write_date'),
            evaluation.specialty,
            Count(evaluation.specialty).as_('evaluations'),
            where=where,
            group_by=evaluation.specialty)


class EvaluationsSector(ModelSQL, ModelView):
    'Evaluations per Sector'
    __name__ = 'gnuhealth.evaluations_sector'

    sector = fields.Many2One('gnuhealth.operational_sector', 'Sector')
    evaluations = fields.Integer('Evaluations')

    @staticmethod
    def table_query():
        pool = Pool()
        evaluation = pool.get('gnuhealth.patient.evaluation').__table__()
        party = pool.get('party.party').__table__()
        patient = pool.get('gnuhealth.patient').__table__()
        du = pool.get('gnuhealth.du').__table__()
        sector = pool.get('gnuhealth.operational_sector').__table__()
        join1 = Join(evaluation, patient)
        join1.condition = join1.right.id == evaluation.patient
        join2 = Join(join1, party)
        join2.condition = join2.right.id == join1.right.name
        join3 = Join(join2, du)
        join3.condition = join3.right.id == join2.right.du
        join4 = Join(join3, sector)
        join4.condition = join4.right.id == join3.right.operational_sector
        where = Literal(True)
        if Transaction().context.get('start_date'):
            where &= evaluation.evaluation_start >= \
                Transaction().context['start_date']
        if Transaction().context.get('end_date'):
            where &= evaluation.evaluation_start <= \
                Transaction().context['end_date']

        return join4.select(
            join4.right.id,
            Max(evaluation.create_uid).as_('create_uid'),
            Max(evaluation.create_date).as_('create_date'),
            Max(evaluation.write_uid).as_('write_uid'),
            Max(evaluation.write_date).as_('write_date'),
            join4.right.id.as_('sector'),
            Count(join4.right.id).as_('evaluations'),
            where=where,
            group_by=join4.right.id)

