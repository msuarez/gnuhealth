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
            from_clause = ', gnuhealth_pathology_group gpg '
            where_clause += 'AND gpg.name = gpe.diagnosis AND gpg.id = %s '
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
