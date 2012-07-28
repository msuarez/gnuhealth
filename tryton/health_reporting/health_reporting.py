##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2008-2012  Sebastian Marro <smarro@gnusolidario.org>
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
from trytond.backend import FIELDS
from trytond.pyson import PYSONEncoder
from trytond.transaction import Transaction

class TopDiseases(ModelSQL, ModelView):
    'Top Diseases'
    _name = 'gnuhealth.top_diseases'
    _description = __doc__

    disease = fields.Many2One('gnuhealth.pathology', 'Disease', select=True)
    cases = fields.Integer('Cases')

    def __init__(self):
        super(TopDiseases, self).__init__()
        self._order.insert(0, ('cases', 'DESC'))

    def table_query(self):
        from_clause = ' '
        where_clause = ' '
        args = [True]
        if Transaction().context.get('start_date'):
            where_clause += 'AND gpe.evaluation_start >= %s '
            args.append(Transaction().context['start_date'])
        if Transaction().context.get('end_date'):
            where_clause += 'AND gpe.evaluation_start <= %s '
            args.append(Transaction().context['end_date'])
        if Transaction().context.get('group'):
            from_clause = ', gnuhealth_disease_group_members gdgm '
            where_clause += 'AND gdgm.name = gpe.diagnosis ' \
                'AND gdgm.disease_group = %s '
            args.append(Transaction().context['group'])
        number_records = '10'
        if Transaction().context.get('number_records'):
            number_records = Transaction().context['number_records']
        return ('SELECT DISTINCT(gpe.diagnosis) AS id, ' \
                    'MAX(gpe.create_uid) AS create_uid, ' \
                    'MAX(gpe.create_date) AS create_date, ' \
                    'MAX(gpe.write_uid) AS write_uid, ' \
                    'MAX(gpe.write_date) AS write_date, ' \
                    'gpe.diagnosis as disease, ' \
                    'COUNT(*) AS cases ' \
                'FROM gnuhealth_patient_evaluation gpe ' \
                + from_clause + \
                'WHERE gpe.diagnosis is not null ' \
                'AND %s ' \
                + where_clause + \
                'GROUP BY gpe.diagnosis ' \
                'ORDER BY cases DESC ' \
                'LIMIT ' + number_records, args)

TopDiseases()


class OpenTopDiseasesStart(ModelView):
    'Open Top Diseases'
    _name = 'gnuhealth.top_diseases.open.start'
    _description = __doc__
    start_date = fields.Date('Start Date')
    end_date = fields.Date('End Date')
    group = fields.Many2One('gnuhealth.pathology.group', 'Disease Group')
    number_records = fields.Char('Number of Records')

OpenTopDiseasesStart()


class OpenTopDiseases(Wizard):
    'Open Top Diseases'
    _name = 'gnuhealth.top_diseases.open'

    start = StateView('gnuhealth.top_diseases.open.start',
        'health_reporting.top_diseases_open_start_view_form', [
            Button('Cancel', 'end', 'tryton-cancel'),
            Button('Open', 'open_', 'tryton-ok', default=True),
            ])
    open_ = StateAction('health_reporting.act_top_diseases_form')

    def do_open_(self, session, action):
        action['pyson_context'] = PYSONEncoder().encode({
                'start_date': session.start.start_date,
                'end_date': session.start.end_date,
                'group': session.start.group.id,
                'number_records': session.start.number_records,
                })
        return action, {}

    def transition_open_(self, session):
        return 'end'

OpenTopDiseases()


class EvaluationsDoctor(ModelSQL, ModelView):
    'Evaluations per Doctor'
    _name = 'gnuhealth.evaluations_doctor'
    _description = __doc__

    doctor = fields.Many2One('gnuhealth.physician', 'Doctor', select=True)
    evaluations = fields.Integer('Evaluations')

    def table_query(self):
        clause = ' '
        args = [True]
        if Transaction().context.get('start_date'):
            clause += 'AND evaluation_start >= %s '
            args.append(Transaction().context['start_date'])
        if Transaction().context.get('end_date'):
            clause += 'AND evaluation_start <= %s '
            args.append(Transaction().context['end_date'])
        return ('SELECT DISTINCT(doctor) AS id, ' \
                    'MAX(create_uid) AS create_uid, ' \
                    'MAX(create_date) AS create_date, ' \
                    'MAX(write_uid) AS write_uid, ' \
                    'MAX(write_date) AS write_date, ' \
                    'doctor, COUNT(*) AS evaluations ' \
                'FROM gnuhealth_patient_evaluation ' \
                'WHERE %s ' \
                + clause + \
                'GROUP BY doctor', args)

EvaluationsDoctor()


class OpenEvaluationsDoctorStart(ModelView):
    'Open Evaluations per Doctor'
    _name = 'gnuhealth.evaluations_doctor.open.start'
    _description = __doc__
    start_date = fields.Date('Start Date')
    end_date = fields.Date('End Date')

OpenEvaluationsDoctorStart()


class OpenEvaluationsDoctor(Wizard):
    'Open Evaluations per Doctor'
    _name = 'gnuhealth.evaluations_doctor.open'

    start = StateView('gnuhealth.evaluations_doctor.open.start',
        'health_reporting.evaluations_doctor_open_start_view_form', [
            Button('Cancel', 'end', 'tryton-cancel'),
            Button('Open', 'open_', 'tryton-ok', default=True),
            ])
    open_ = StateAction('health_reporting.act_evaluations_doctor_form')

    def do_open_(self, session, action):
        action['pyson_context'] = PYSONEncoder().encode({
                'start_date': session.start.start_date,
                'end_date': session.start.end_date,
                })
        return action, {}

    def transition_open_(self, session):
        return 'end'

OpenEvaluationsDoctor()


class EvaluationsDoctorWeekly(ModelSQL, ModelView):
    'Evaluations per Doctor per Week'
    _name = 'gnuhealth.evaluations_doctor_weekly'
    _description = __doc__

    year = fields.Char('Year', select=True)
    week = fields.Integer('Week', select=True)
    doctor = fields.Many2One('gnuhealth.physician', 'Doctor', select=True)
    evaluations = fields.Integer('Evaluations')

    def __init__(self):
        super(EvaluationsDoctorWeekly, self).__init__()
        self._order.insert(0, ('year', 'DESC'))
        self._order.insert(1, ('week', 'DESC'))
        #self._order.insert(2, ('doctor', 'ASC')) /// wait for trytond-2.4.2

    def table_query(self):
        type_name = FIELDS[self.year._type].sql_type(self.year)[0]
        return ('SELECT id, create_uid, create_date, write_uid, write_date, ' \
                    'CAST(year AS ' + type_name + ') AS year, week, ' \
                    'doctor, evaluations ' \
                    'FROM ('
                        'SELECT EXTRACT(WEEK FROM evaluation_start) + ' \
                            'EXTRACT(YEAR FROM evaluation_start) * 100 + ' \
                            'doctor * 1000000 AS id, ' \
                        'MAX(create_uid) AS create_uid, ' \
                        'MAX(create_date) AS create_date, ' \
                        'MAX(write_uid) AS write_uid, ' \
                        'MAX(write_date) AS write_date, ' \
                        'EXTRACT(YEAR FROM evaluation_start) AS year, ' \
                        'EXTRACT(WEEK FROM evaluation_start) AS week, ' \
                        'doctor, COUNT(*) AS evaluations ' \
                        'FROM gnuhealth_patient_evaluation ' \
                        'GROUP BY year, week, doctor) AS ' + self._table, [])

EvaluationsDoctorWeekly()


class EvaluationsDoctorMonthly(ModelSQL, ModelView):
    'Evaluations per Doctor per Month'
    _name = 'gnuhealth.evaluations_doctor_monthly'
    _description = __doc__

    year = fields.Char('Year', select=True)
    month = fields.Integer('Month', select=True)
    doctor = fields.Many2One('gnuhealth.physician', 'Doctor', select=True)
    evaluations = fields.Integer('Evaluations')

    def __init__(self):
        super(EvaluationsDoctorMonthly, self).__init__()
        self._order.insert(0, ('year', 'DESC'))
        self._order.insert(1, ('month', 'DESC'))
        #self._order.insert(2, ('doctor', 'ASC')) /// wait for trytond-2.4.2

    def table_query(self):
        type_name = FIELDS[self.year._type].sql_type(self.year)[0]
        return ('SELECT id, create_uid, create_date, write_uid, write_date, ' \
                    'CAST(year AS ' + type_name + ') AS year, month, ' \
                    'doctor, evaluations ' \
                    'FROM ('
                        'SELECT EXTRACT(MONTH FROM evaluation_start) + ' \
                            'EXTRACT(YEAR FROM evaluation_start) * 100 + ' \
                            'doctor * 1000000 AS id, ' \
                        'MAX(create_uid) AS create_uid, ' \
                        'MAX(create_date) AS create_date, ' \
                        'MAX(write_uid) AS write_uid, ' \
                        'MAX(write_date) AS write_date, ' \
                        'EXTRACT(YEAR FROM evaluation_start) AS year, ' \
                        'EXTRACT(MONTH FROM evaluation_start) AS month, ' \
                        'doctor, COUNT(*) AS evaluations ' \
                        'FROM gnuhealth_patient_evaluation ' \
                        'GROUP BY year, month, doctor) AS ' + self._table, [])

EvaluationsDoctorMonthly()


class EvaluationsSpecialty(ModelSQL, ModelView):
    'Evaluations per Specialty'
    _name = 'gnuhealth.evaluations_specialty'
    _description = __doc__

    specialty = fields.Many2One('gnuhealth.specialty', 'Specialty', select=True)
    evaluations = fields.Integer('Evaluations')

    def table_query(self):
        clause = ' '
        args = [True]
        if Transaction().context.get('start_date'):
            clause += 'AND evaluation_start >= %s '
            args.append(Transaction().context['start_date'])
        if Transaction().context.get('end_date'):
            clause += 'AND evaluation_start <= %s '
            args.append(Transaction().context['end_date'])
        return ('SELECT DISTINCT(specialty) AS id, ' \
                    'MAX(create_uid) AS create_uid, ' \
                    'MAX(create_date) AS create_date, ' \
                    'MAX(write_uid) AS write_uid, ' \
                    'MAX(write_date) AS write_date, ' \
                    'specialty, COUNT(*) AS evaluations ' \
                'FROM gnuhealth_patient_evaluation ' \
                'WHERE %s ' \
                + clause + \
                'GROUP BY specialty', args)

EvaluationsSpecialty()


class OpenEvaluationsSpecialtyStart(ModelView):
    'Open Evaluations per Specialty'
    _name = 'gnuhealth.evaluations_specialty.open.start'
    _description = __doc__
    start_date = fields.Date('Start Date')
    end_date = fields.Date('End Date')

OpenEvaluationsSpecialtyStart()


class OpenEvaluationsSpecialty(Wizard):
    'Open Evaluations per Specialty'
    _name = 'gnuhealth.evaluations_specialty.open'

    start = StateView('gnuhealth.evaluations_specialty.open.start',
        'health_reporting.evaluations_specialty_open_start_view_form', [
            Button('Cancel', 'end', 'tryton-cancel'),
            Button('Open', 'open_', 'tryton-ok', default=True),
            ])
    open_ = StateAction('health_reporting.act_evaluations_specialty_form')

    def do_open_(self, session, action):
        action['pyson_context'] = PYSONEncoder().encode({
                'start_date': session.start.start_date,
                'end_date': session.start.end_date,
                })
        return action, {}

    def transition_open_(self, session):
        return 'end'

OpenEvaluationsSpecialty()


class EvaluationsSpecialtyWeekly(ModelSQL, ModelView):
    'Evaluations per Specialty per Week'
    _name = 'gnuhealth.evaluations_specialty_weekly'
    _description = __doc__

    year = fields.Char('Year', select=True)
    week = fields.Integer('Week', select=True)
    specialty = fields.Many2One('gnuhealth.specialty', 'Specialty', select=True)
    evaluations = fields.Integer('Evaluations')

    def __init__(self):
        super(EvaluationsSpecialtyWeekly, self).__init__()
        self._order.insert(0, ('year', 'DESC'))
        self._order.insert(1, ('week', 'DESC'))
        #self._order.insert(2, ('specialty', 'ASC')) /// wait for trytond-2.4.2

    def table_query(self):
        type_name = FIELDS[self.year._type].sql_type(self.year)[0]
        return ('SELECT id, create_uid, create_date, write_uid, write_date, ' \
                    'CAST(year AS ' + type_name + ') AS year, week, ' \
                    'specialty, evaluations ' \
                    'FROM ('
                        'SELECT EXTRACT(WEEK FROM evaluation_start) + ' \
                            'EXTRACT(YEAR FROM evaluation_start) * 100 + ' \
                            'specialty * 1000000 AS id, ' \
                        'MAX(create_uid) AS create_uid, ' \
                        'MAX(create_date) AS create_date, ' \
                        'MAX(write_uid) AS write_uid, ' \
                        'MAX(write_date) AS write_date, ' \
                        'EXTRACT(YEAR FROM evaluation_start) AS year, ' \
                        'EXTRACT(WEEK FROM evaluation_start) AS week, ' \
                        'specialty, COUNT(*) AS evaluations ' \
                        'FROM gnuhealth_patient_evaluation ' \
                        'GROUP BY year, week, specialty) AS ' + self._table, [])

EvaluationsSpecialtyWeekly()


class EvaluationsSpecialtyMonthly(ModelSQL, ModelView):
    'Evaluations per Specialty per Month'
    _name = 'gnuhealth.evaluations_specialty_monthly'
    _description = __doc__

    year = fields.Char('Year', select=True)
    month = fields.Integer('Month', select=True)
    specialty = fields.Many2One('gnuhealth.specialty', 'Specialty', select=True)
    evaluations = fields.Integer('Evaluations')

    def __init__(self):
        super(EvaluationsSpecialtyMonthly, self).__init__()
        self._order.insert(0, ('year', 'DESC'))
        self._order.insert(1, ('month', 'DESC'))
        #self._order.insert(2, ('specialty', 'ASC')) /// wait for trytond-2.4.2

    def table_query(self):
        type_name = FIELDS[self.year._type].sql_type(self.year)[0]
        return ('SELECT id, create_uid, create_date, write_uid, write_date, ' \
                    'CAST(year AS ' + type_name + ') AS year, month, ' \
                    'specialty, evaluations ' \
                    'FROM ('
                        'SELECT EXTRACT(MONTH FROM evaluation_start) + ' \
                            'EXTRACT(YEAR FROM evaluation_start) * 100 + ' \
                            'specialty * 1000000 AS id, ' \
                        'MAX(create_uid) AS create_uid, ' \
                        'MAX(create_date) AS create_date, ' \
                        'MAX(write_uid) AS write_uid, ' \
                        'MAX(write_date) AS write_date, ' \
                        'EXTRACT(YEAR FROM evaluation_start) AS year, ' \
                        'EXTRACT(MONTH FROM evaluation_start) AS month, ' \
                        'specialty, COUNT(*) AS evaluations ' \
                        'FROM gnuhealth_patient_evaluation ' \
                        'GROUP BY year, month, specialty) AS ' + self._table, [])

EvaluationsSpecialtyMonthly()


class EvaluationsSector(ModelSQL, ModelView):
    'Evaluations per Sector'
    _name = 'gnuhealth.evaluations_sector'
    _description = __doc__

    sector = fields.Many2One('gnuhealth.operational_sector', 'Sector', select=True)
    evaluations = fields.Integer('Evaluations')

    def table_query(self):
        clause = ' '
        args = [True]
        if Transaction().context.get('start_date'):
            clause += 'AND gpe.evaluation_start >= %s '
            args.append(Transaction().context['start_date'])
        if Transaction().context.get('end_date'):
            clause += 'AND gpe.evaluation_start <= %s '
            args.append(Transaction().context['end_date'])
        return ('SELECT DISTINCT(gos.id) AS id, ' \
                    'MAX(gpe.create_uid) AS create_uid, ' \
                    'MAX(gpe.create_date) AS create_date, ' \
                    'MAX(gpe.write_uid) AS write_uid, ' \
                    'MAX(gpe.write_date) AS write_date, ' \
                    'gos.id as sector, ' \
                    'COUNT(*) AS evaluations ' \
                'FROM party_party pp, ' \
                    'gnuhealth_patient_evaluation gpe, ' \
                    'gnuhealth_patient gp, ' \
                    'gnuhealth_family_member gfm, ' \
                    'gnuhealth_family gf, ' \
                    'gnuhealth_operational_sector gos ' \
                'WHERE gpe.patient = gp.id ' \
                    'AND gp.name = pp.id ' \
                    'AND gfm.party = pp.id ' \
                    'AND gfm.name = gf.id ' \
                    'AND gf.operational_sector = gos.id ' \
                    'AND %s ' \
                + clause + \
                'GROUP BY gos.id', args)

EvaluationsSector()


class OpenEvaluationsSectorStart(ModelView):
    'Open Evaluations per Sector'
    _name = 'gnuhealth.evaluations_sector.open.start'
    _description = __doc__
    start_date = fields.Date('Start Date')
    end_date = fields.Date('End Date')

OpenEvaluationsSectorStart()


class OpenEvaluationsSector(Wizard):
    'Open Evaluations per Sector'
    _name = 'gnuhealth.evaluations_sector.open'

    start = StateView('gnuhealth.evaluations_sector.open.start',
        'health_reporting.evaluations_sector_open_start_view_form', [
            Button('Cancel', 'end', 'tryton-cancel'),
            Button('Open', 'open_', 'tryton-ok', default=True),
            ])
    open_ = StateAction('health_reporting.act_evaluations_sector_form')

    def do_open_(self, session, action):
        action['pyson_context'] = PYSONEncoder().encode({
                'start_date': session.start.start_date,
                'end_date': session.start.end_date,
                })
        return action, {}

    def transition_open_(self, session):
        return 'end'

OpenEvaluationsSector()


class EvaluationsSectorWeekly(ModelSQL, ModelView):
    'Evaluations per Sector per Week'
    _name = 'gnuhealth.evaluations_sector_weekly'
    _description = __doc__

    year = fields.Char('Year', select=True)
    week = fields.Integer('Week', select=True)
    sector = fields.Many2One('gnuhealth.operational_sector', 'Sector', select=True)
    evaluations = fields.Integer('Evaluations')

    def __init__(self):
        super(EvaluationsSectorWeekly, self).__init__()
        self._order.insert(0, ('year', 'DESC'))
        self._order.insert(1, ('week', 'DESC'))
        self._order.insert(2, ('sector', 'ASC'))

    def table_query(self):
        type_name = FIELDS[self.year._type].sql_type(self.year)[0]
        return ('SELECT id, create_uid, create_date, write_uid, write_date, ' \
                    'CAST(year AS ' + type_name + ') AS year, week, ' \
                    'sector, evaluations ' \
                    'FROM ('
                        'SELECT EXTRACT(WEEK FROM gpe.evaluation_start) + ' \
                            'EXTRACT(YEAR FROM gpe.evaluation_start) * 100 + ' \
                            'gos.id * 1000000 AS id, ' \
                        'MAX(gpe.create_uid) AS create_uid, ' \
                        'MAX(gpe.create_date) AS create_date, ' \
                        'MAX(gpe.write_uid) AS write_uid, ' \
                        'MAX(gpe.write_date) AS write_date, ' \
                        'EXTRACT(YEAR FROM gpe.evaluation_start) AS year, ' \
                        'EXTRACT(WEEK FROM gpe.evaluation_start) AS week, ' \
                        'gos.id as sector, COUNT(*) AS evaluations ' \
                        'FROM party_party pp, ' \
                            'gnuhealth_patient_evaluation gpe, ' \
                            'gnuhealth_patient gp, ' \
                            'gnuhealth_family_member gfm, ' \
                            'gnuhealth_family gf, ' \
                            'gnuhealth_operational_sector gos ' \
                        'WHERE gpe.patient = gp.id ' \
                            'AND gp.name = pp.id ' \
                            'AND gfm.party = pp.id ' \
                            'AND gfm.name = gf.id ' \
                            'AND gf.operational_sector = gos.id ' \
                        'GROUP BY year, week, gos.id) AS ' + self._table, [])

EvaluationsSectorWeekly()


class EvaluationsSectorMonthly(ModelSQL, ModelView):
    'Evaluations per Sector per Month'
    _name = 'gnuhealth.evaluations_sector_monthly'
    _description = __doc__

    year = fields.Char('Year', select=True)
    month = fields.Integer('Month', select=True)
    sector = fields.Many2One('gnuhealth.operational_sector', 'Sector', select=True)
    evaluations = fields.Integer('Evaluations')

    def __init__(self):
        super(EvaluationsSectorMonthly, self).__init__()
        self._order.insert(0, ('year', 'DESC'))
        self._order.insert(1, ('month', 'DESC'))
        self._order.insert(2, ('sector', 'ASC'))

    def table_query(self):
        type_name = FIELDS[self.year._type].sql_type(self.year)[0]
        return ('SELECT id, create_uid, create_date, write_uid, write_date, ' \
                    'CAST(year AS ' + type_name + ') AS year, month, ' \
                    'sector, evaluations ' \
                    'FROM ('
                        'SELECT EXTRACT(MONTH FROM gpe.evaluation_start) + ' \
                            'EXTRACT(YEAR FROM gpe.evaluation_start) * 100 + ' \
                            'gos.id * 1000000 AS id, ' \
                        'MAX(gpe.create_uid) AS create_uid, ' \
                        'MAX(gpe.create_date) AS create_date, ' \
                        'MAX(gpe.write_uid) AS write_uid, ' \
                        'MAX(gpe.write_date) AS write_date, ' \
                        'EXTRACT(YEAR FROM gpe.evaluation_start) AS year, ' \
                        'EXTRACT(MONTH FROM gpe.evaluation_start) AS month, ' \
                        'gos.id as sector, COUNT(*) AS evaluations ' \
                        'FROM party_party pp, ' \
                            'gnuhealth_patient_evaluation gpe, ' \
                            'gnuhealth_patient gp, ' \
                            'gnuhealth_family_member gfm, ' \
                            'gnuhealth_family gf, ' \
                            'gnuhealth_operational_sector gos ' \
                        'WHERE gpe.patient = gp.id ' \
                            'AND gp.name = pp.id ' \
                            'AND gfm.party = pp.id ' \
                            'AND gfm.name = gf.id ' \
                            'AND gf.operational_sector = gos.id ' \
                        'GROUP BY year, month, gos.id) AS ' + self._table, [])

EvaluationsSectorMonthly()
