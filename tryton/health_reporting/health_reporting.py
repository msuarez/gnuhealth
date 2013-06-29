##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2008-2013  Sebastian Marro <smarro@gnusolidario.org>
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


__all__ = ['TopDiseases', 'OpenTopDiseasesStart', 'OpenTopDiseases',
    'EvaluationsDoctor', 'OpenEvaluationsDoctorStart', 'OpenEvaluationsDoctor',
    'EvaluationsDoctorWeekly', 'EvaluationsDoctorMonthly',
    'EvaluationsSpecialty', 'OpenEvaluationsSpecialtyStart',
    'OpenEvaluationsSpecialty', 'EvaluationsSpecialtyWeekly',
    'EvaluationsSpecialtyMonthly', 'EvaluationsSector',
    'OpenEvaluationsSectorStart', 'OpenEvaluationsSector',
    'EvaluationsSectorWeekly', 'EvaluationsSectorMonthly']


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
        return ('SELECT DISTINCT(gpe.diagnosis) AS id, '
                    'MAX(gpe.create_uid) AS create_uid, '
                    'MAX(gpe.create_date) AS create_date, '
                    'MAX(gpe.write_uid) AS write_uid, '
                    'MAX(gpe.write_date) AS write_date, '
                    'gpe.diagnosis as disease, '
                    'COUNT(*) AS cases '
                'FROM gnuhealth_patient_evaluation gpe '
                + from_clause +
                'WHERE gpe.diagnosis is not null '
                'AND %s '
                + where_clause +
                'GROUP BY gpe.diagnosis '
                'ORDER BY cases DESC '
                'LIMIT ' + number_records, args)


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


class EvaluationsDoctor(ModelSQL, ModelView):
    'Evaluations per Doctor'
    __name__ = 'gnuhealth.evaluations_doctor'

    doctor = fields.Many2One('gnuhealth.physician', 'Doctor', select=True)
    evaluations = fields.Integer('Evaluations')

    @staticmethod
    def table_query():
        clause = ' '
        args = [True]
        if Transaction().context.get('start_date'):
            clause += 'AND evaluation_start >= %s '
            args.append(Transaction().context['start_date'])
        if Transaction().context.get('end_date'):
            clause += 'AND evaluation_start <= %s '
            args.append(Transaction().context['end_date'])
        return ('SELECT DISTINCT(doctor) AS id, '
                    'MAX(create_uid) AS create_uid, '
                    'MAX(create_date) AS create_date, '
                    'MAX(write_uid) AS write_uid, '
                    'MAX(write_date) AS write_date, '
                    'doctor, COUNT(*) AS evaluations '
                'FROM gnuhealth_patient_evaluation '
                'WHERE %s '
                + clause +
                'GROUP BY doctor', args)


class OpenEvaluationsDoctorStart(ModelView):
    'Open Evaluations per Doctor'
    __name__ = 'gnuhealth.evaluations_doctor.open.start'

    start_date = fields.Date('Start Date')
    end_date = fields.Date('End Date')


class OpenEvaluationsDoctor(Wizard):
    'Open Evaluations per Doctor'
    __name__ = 'gnuhealth.evaluations_doctor.open'

    start = StateView('gnuhealth.evaluations_doctor.open.start',
        'health_reporting.evaluations_doctor_open_start_view_form', [
            Button('Cancel', 'end', 'tryton-cancel'),
            Button('Open', 'open_', 'tryton-ok', default=True),
            ])
    open_ = StateAction('health_reporting.act_evaluations_doctor_form')

    def do_open_(self, action):
        action['pyson_context'] = PYSONEncoder().encode({
                'start_date': self.start.start_date,
                'end_date': self.start.end_date,
                })
        return action, {}

    def transition_open_(self):
        return 'end'


class EvaluationsDoctorWeekly(ModelSQL, ModelView):
    'Evaluations per Doctor per Week'
    __name__ = 'gnuhealth.evaluations_doctor_weekly'

    year = fields.Char('Year', select=True)
    week = fields.Integer('Week', select=True)
    doctor = fields.Many2One('gnuhealth.physician', 'Doctor', select=True)
    evaluations = fields.Integer('Evaluations')

    @classmethod
    def __setup__(cls):
        super(EvaluationsDoctorWeekly, cls).__setup__()
        cls._order.insert(0, ('year', 'DESC'))
        cls._order.insert(1, ('week', 'DESC'))
        cls._order.insert(2, ('doctor', 'ASC'))

    @classmethod
    def table_query(cls):
        type_name = FIELDS[cls.year._type].sql_type(cls.year)[0]
        return ('SELECT id, create_uid, create_date, write_uid, write_date, '
                    'CAST(year AS ' + type_name + ') AS year, week, '
                    'doctor, evaluations '
                    'FROM ('
                        'SELECT EXTRACT(WEEK FROM evaluation_start) + '
                            'EXTRACT(YEAR FROM evaluation_start) * 100 + '
                            'doctor * 1000000 AS id, '
                        'MAX(create_uid) AS create_uid, '
                        'MAX(create_date) AS create_date, '
                        'MAX(write_uid) AS write_uid, '
                        'MAX(write_date) AS write_date, '
                        'EXTRACT(YEAR FROM evaluation_start) AS year, '
                        'EXTRACT(WEEK FROM evaluation_start) AS week, '
                        'doctor, COUNT(*) AS evaluations '
                        'FROM gnuhealth_patient_evaluation '
                        'GROUP BY year, week, doctor) AS ' + cls._table, [])


class EvaluationsDoctorMonthly(ModelSQL, ModelView):
    'Evaluations per Doctor per Month'
    __name__ = 'gnuhealth.evaluations_doctor_monthly'

    year = fields.Char('Year', select=True)
    month = fields.Integer('Month', select=True)
    doctor = fields.Many2One('gnuhealth.physician', 'Doctor', select=True)
    evaluations = fields.Integer('Evaluations')

    @classmethod
    def __setup__(cls):
        super(EvaluationsDoctorMonthly, cls).__setup__()
        cls._order.insert(0, ('year', 'DESC'))
        cls._order.insert(1, ('month', 'DESC'))
        cls._order.insert(2, ('doctor', 'ASC'))

    @classmethod
    def table_query(cls):
        type_name = FIELDS[cls.year._type].sql_type(cls.year)[0]
        return ('SELECT id, create_uid, create_date, write_uid, write_date, '
                    'CAST(year AS ' + type_name + ') AS year, month, '
                    'doctor, evaluations '
                    'FROM ('
                        'SELECT EXTRACT(MONTH FROM evaluation_start) + '
                            'EXTRACT(YEAR FROM evaluation_start) * 100 + '
                            'doctor * 1000000 AS id, '
                        'MAX(create_uid) AS create_uid, '
                        'MAX(create_date) AS create_date, '
                        'MAX(write_uid) AS write_uid, '
                        'MAX(write_date) AS write_date, '
                        'EXTRACT(YEAR FROM evaluation_start) AS year, '
                        'EXTRACT(MONTH FROM evaluation_start) AS month, '
                        'doctor, COUNT(*) AS evaluations '
                        'FROM gnuhealth_patient_evaluation '
                        'GROUP BY year, month, doctor) AS ' + cls._table, [])


class EvaluationsSpecialty(ModelSQL, ModelView):
    'Evaluations per Specialty'
    __name__ = 'gnuhealth.evaluations_specialty'

    specialty = fields.Many2One('gnuhealth.specialty', 'Specialty',
        select=True)
    evaluations = fields.Integer('Evaluations')

    @staticmethod
    def table_query():
        clause = ' '
        args = []
        if Transaction().context.get('start_date'):
            clause += 'AND evaluation_start >= %s '
            args.append(Transaction().context['start_date'])
        if Transaction().context.get('end_date'):
            clause += 'AND evaluation_start <= %s '
            args.append(Transaction().context['end_date'])
        return ('SELECT DISTINCT(specialty) AS id, '
                    'MAX(create_uid) AS create_uid, '
                    'MAX(create_date) AS create_date, '
                    'MAX(write_uid) AS write_uid, '
                    'MAX(write_date) AS write_date, '
                    'specialty, COUNT(*) AS evaluations '
                'FROM gnuhealth_patient_evaluation '
                'WHERE specialty is not null '
                + clause +
                'GROUP BY specialty', args)


class OpenEvaluationsSpecialtyStart(ModelView):
    'Open Evaluations per Specialty'
    __name__ = 'gnuhealth.evaluations_specialty.open.start'

    start_date = fields.Date('Start Date')
    end_date = fields.Date('End Date')


class OpenEvaluationsSpecialty(Wizard):
    'Open Evaluations per Specialty'
    __name__ = 'gnuhealth.evaluations_specialty.open'

    start = StateView('gnuhealth.evaluations_specialty.open.start',
        'health_reporting.evaluations_specialty_open_start_view_form', [
            Button('Cancel', 'end', 'tryton-cancel'),
            Button('Open', 'open_', 'tryton-ok', default=True),
            ])
    open_ = StateAction('health_reporting.act_evaluations_specialty_form')

    def do_open_(self, action):
        action['pyson_context'] = PYSONEncoder().encode({
                'start_date': self.start.start_date,
                'end_date': self.start.end_date,
                })
        return action, {}

    def transition_open_(self):
        return 'end'


class EvaluationsSpecialtyWeekly(ModelSQL, ModelView):
    'Evaluations per Specialty per Week'
    __name__ = 'gnuhealth.evaluations_specialty_weekly'

    year = fields.Char('Year', select=True)
    week = fields.Integer('Week', select=True)
    specialty = fields.Many2One('gnuhealth.specialty', 'Specialty',
        select=True)
    evaluations = fields.Integer('Evaluations')

    @classmethod
    def __setup__(cls):
        super(EvaluationsSpecialtyWeekly, cls).__setup__()
        cls._order.insert(0, ('year', 'DESC'))
        cls._order.insert(1, ('week', 'DESC'))
        cls._order.insert(2, ('specialty', 'ASC'))

    @classmethod
    def table_query(cls):
        type_name = FIELDS[cls.year._type].sql_type(cls.year)[0]
        return ('SELECT id, create_uid, create_date, write_uid, write_date, '
                    'CAST(year AS ' + type_name + ') AS year, week, '
                    'specialty, evaluations '
                    'FROM ('
                        'SELECT EXTRACT(WEEK FROM evaluation_start) + '
                            'EXTRACT(YEAR FROM evaluation_start) * 100 + '
                            'specialty * 1000000 AS id, '
                        'MAX(create_uid) AS create_uid, '
                        'MAX(create_date) AS create_date, '
                        'MAX(write_uid) AS write_uid, '
                        'MAX(write_date) AS write_date, '
                        'EXTRACT(YEAR FROM evaluation_start) AS year, '
                        'EXTRACT(WEEK FROM evaluation_start) AS week, '
                        'specialty, COUNT(*) AS evaluations '
                        'FROM gnuhealth_patient_evaluation '
                        'WHERE specialty is not null '
                        'GROUP BY year, week, specialty) AS ' + cls._table, [])


class EvaluationsSpecialtyMonthly(ModelSQL, ModelView):
    'Evaluations per Specialty per Month'
    __name__ = 'gnuhealth.evaluations_specialty_monthly'

    year = fields.Char('Year', select=True)
    month = fields.Integer('Month', select=True)
    specialty = fields.Many2One('gnuhealth.specialty', 'Specialty',
        select=True)
    evaluations = fields.Integer('Evaluations')

    @classmethod
    def __setup__(cls):
        super(EvaluationsSpecialtyMonthly, cls).__setup__()
        cls._order.insert(0, ('year', 'DESC'))
        cls._order.insert(1, ('month', 'DESC'))
        cls._order.insert(2, ('specialty', 'ASC'))

    @classmethod
    def table_query(cls):
        type_name = FIELDS[cls.year._type].sql_type(cls.year)[0]
        return ('SELECT id, create_uid, create_date, write_uid, write_date, '
                    'CAST(year AS ' + type_name + ') AS year, month, '
                    'specialty, evaluations '
                    'FROM ('
                        'SELECT EXTRACT(MONTH FROM evaluation_start) + '
                            'EXTRACT(YEAR FROM evaluation_start) * 100 + '
                            'specialty * 1000000 AS id, '
                        'MAX(create_uid) AS create_uid, '
                        'MAX(create_date) AS create_date, '
                        'MAX(write_uid) AS write_uid, '
                        'MAX(write_date) AS write_date, '
                        'EXTRACT(YEAR FROM evaluation_start) AS year, '
                        'EXTRACT(MONTH FROM evaluation_start) AS month, '
                        'specialty, COUNT(*) AS evaluations '
                        'FROM gnuhealth_patient_evaluation '
                        'WHERE specialty is not null '
                        'GROUP BY year, month, specialty) AS ' + cls._table,
                        [])


class EvaluationsSector(ModelSQL, ModelView):
    'Evaluations per Sector'
    __name__ = 'gnuhealth.evaluations_sector'

    sector = fields.Many2One('gnuhealth.operational_sector', 'Sector',
        select=True)
    evaluations = fields.Integer('Evaluations')

    @staticmethod
    def table_query():
        clause = ' '
        args = [True]
        if Transaction().context.get('start_date'):
            clause += 'AND gpe.evaluation_start >= %s '
            args.append(Transaction().context['start_date'])
        if Transaction().context.get('end_date'):
            clause += 'AND gpe.evaluation_start <= %s '
            args.append(Transaction().context['end_date'])
        return ('SELECT DISTINCT(gos.id) AS id, '
                    'MAX(gpe.create_uid) AS create_uid, '
                    'MAX(gpe.create_date) AS create_date, '
                    'MAX(gpe.write_uid) AS write_uid, '
                    'MAX(gpe.write_date) AS write_date, '
                    'gos.id as sector, '
                    'COUNT(*) AS evaluations '
                'FROM party_party pp, '
                    'gnuhealth_patient_evaluation gpe, '
                    'gnuhealth_patient gp, '
                    'gnuhealth_du gdu, '
                    'gnuhealth_operational_sector gos '
                'WHERE gpe.patient = gp.id '
                    'AND gp.name = pp.id '
                    'AND pp.du = gdu.id '
                    'AND gdu.operational_sector = gos.id '
                    'AND %s '
                + clause +
                'GROUP BY gos.id', args)


class OpenEvaluationsSectorStart(ModelView):
    'Open Evaluations per Sector'
    __name__ = 'gnuhealth.evaluations_sector.open.start'

    start_date = fields.Date('Start Date')
    end_date = fields.Date('End Date')


class OpenEvaluationsSector(Wizard):
    'Open Evaluations per Sector'
    __name__ = 'gnuhealth.evaluations_sector.open'

    start = StateView('gnuhealth.evaluations_sector.open.start',
        'health_reporting.evaluations_sector_open_start_view_form', [
            Button('Cancel', 'end', 'tryton-cancel'),
            Button('Open', 'open_', 'tryton-ok', default=True),
            ])
    open_ = StateAction('health_reporting.act_evaluations_sector_form')

    def do_open_(self, action):
        action['pyson_context'] = PYSONEncoder().encode({
                'start_date': self.start.start_date,
                'end_date': self.start.end_date,
                })
        return action, {}

    def transition_open_(self):
        return 'end'


class EvaluationsSectorWeekly(ModelSQL, ModelView):
    'Evaluations per Sector per Week'
    __name__ = 'gnuhealth.evaluations_sector_weekly'

    year = fields.Char('Year', select=True)
    week = fields.Integer('Week', select=True)
    sector = fields.Many2One('gnuhealth.operational_sector', 'Sector',
        select=True)
    evaluations = fields.Integer('Evaluations')

    @classmethod
    def __setup__(cls):
        super(EvaluationsSectorWeekly, cls).__setup__()
        cls._order.insert(0, ('year', 'DESC'))
        cls._order.insert(1, ('week', 'DESC'))
        cls._order.insert(2, ('sector', 'ASC'))

    @classmethod
    def table_query(cls):
        type_name = FIELDS[cls.year._type].sql_type(cls.year)[0]
        return ('SELECT id, create_uid, create_date, write_uid, write_date, '
                    'CAST(year AS ' + type_name + ') AS year, week, '
                    'sector, evaluations '
                    'FROM ('
                        'SELECT EXTRACT(WEEK FROM gpe.evaluation_start) + '
                            'EXTRACT(YEAR FROM gpe.evaluation_start) * 100 + '
                            'gos.id * 1000000 AS id, '
                        'MAX(gpe.create_uid) AS create_uid, '
                        'MAX(gpe.create_date) AS create_date, '
                        'MAX(gpe.write_uid) AS write_uid, '
                        'MAX(gpe.write_date) AS write_date, '
                        'EXTRACT(YEAR FROM gpe.evaluation_start) AS year, '
                        'EXTRACT(WEEK FROM gpe.evaluation_start) AS week, '
                        'gos.id as sector, COUNT(*) AS evaluations '
                        'FROM party_party pp, '
                            'gnuhealth_patient_evaluation gpe, '
                            'gnuhealth_patient gp, '
                            'gnuhealth_du gdu, '
                            'gnuhealth_operational_sector gos '
                        'WHERE gpe.patient = gp.id '
                            'AND gp.name = pp.id '
                            'AND pp.du = gdu.id '
                            'AND gdu.operational_sector = gos.id '
                        'GROUP BY year, week, gos.id) AS ' + cls._table, [])


class EvaluationsSectorMonthly(ModelSQL, ModelView):
    'Evaluations per Sector per Month'
    __name__ = 'gnuhealth.evaluations_sector_monthly'

    year = fields.Char('Year', select=True)
    month = fields.Integer('Month', select=True)
    sector = fields.Many2One('gnuhealth.operational_sector', 'Sector',
        select=True)
    evaluations = fields.Integer('Evaluations')

    @classmethod
    def __setup__(cls):
        super(EvaluationsSectorMonthly, cls).__setup__()
        cls._order.insert(0, ('year', 'DESC'))
        cls._order.insert(1, ('month', 'DESC'))
        cls._order.insert(2, ('sector', 'ASC'))

    @classmethod
    def table_query(cls):
        type_name = FIELDS[cls.year._type].sql_type(cls.year)[0]
        return ('SELECT id, create_uid, create_date, write_uid, write_date, '
                    'CAST(year AS ' + type_name + ') AS year, month, '
                    'sector, evaluations '
                    'FROM ('
                        'SELECT EXTRACT(MONTH FROM gpe.evaluation_start) + '
                            'EXTRACT(YEAR FROM gpe.evaluation_start) * 100 + '
                            'gos.id * 1000000 AS id, '
                        'MAX(gpe.create_uid) AS create_uid, '
                        'MAX(gpe.create_date) AS create_date, '
                        'MAX(gpe.write_uid) AS write_uid, '
                        'MAX(gpe.write_date) AS write_date, '
                        'EXTRACT(YEAR FROM gpe.evaluation_start) AS year, '
                        'EXTRACT(MONTH FROM gpe.evaluation_start) AS month, '
                        'gos.id as sector, COUNT(*) AS evaluations '
                        'FROM party_party pp, '
                            'gnuhealth_patient_evaluation gpe, '
                            'gnuhealth_patient gp, '
                            'gnuhealth_du gdu, '
                            'gnuhealth_operational_sector gos '
                        'WHERE gpe.patient = gp.id '
                            'AND gp.name = pp.id '
                            'AND pp.du = gdu.id '
                            'AND gdu.operational_sector = gos.id '
                        'GROUP BY year, month, gos.id) AS ' + cls._table, [])

