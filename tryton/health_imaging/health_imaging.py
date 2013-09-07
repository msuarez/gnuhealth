# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2008-2013  Luis Falcon <lfalcon@gnu.org>
#    Copyright (C) 2013  Sebastián Marro <smarro@thymbra.com>
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
from trytond.model import Workflow, ModelView, ModelSingleton, ModelSQL, fields
from trytond.wizard import Wizard, StateAction, StateTransition, StateView, \
    Button
from trytond.pyson import PYSONEncoder, Eval
from trytond.transaction import Transaction
from trytond.pool import Pool


__all__ = ['GnuHealthSequences', 'ImagingTestType', 'ImagingTest',
    'ImagingTestRequest', 'ImagingTestResult', 'WizardGenerateResult',
    'RequestImagingTest', 'RequestPatientImagingTestStart',
    'RequestPatientImagingTest']


class GnuHealthSequences(ModelSingleton, ModelSQL, ModelView):
    "Standard Sequences for GNU Health"
    __name__ = "gnuhealth.sequences"

    imaging_request_sequence = fields.Property(fields.Many2One('ir.sequence',
        'Imaging Request Sequence',
        domain=[('code', '=', 'gnuhealth.imaging.test.request')],
        required=True))
    imaging_sequence = fields.Property(fields.Many2One('ir.sequence',
        'Imaging Sequence',
        domain=[('code', '=', 'gnuhealth.imaging.test.result')],
        required=True))


class ImagingTestType(ModelSQL, ModelView):
    'Imaging Test Type'
    __name__ = 'gnuhealth.imaging.test.type'

    code = fields.Char('Code', required=True)
    name = fields.Char('Name', required=True)


class ImagingTest(ModelSQL, ModelView):
    'Imaging Test'
    __name__ = 'gnuhealth.imaging.test'

    code = fields.Char('Code', required=True)
    name = fields.Char('Name', required=True)
    test_type = fields.Many2One('gnuhealth.imaging.test.type', 'Type',
        required=True)
    product = fields.Many2One('product.product', 'Service', required=True)


class ImagingTestRequest(Workflow, ModelSQL, ModelView):
    'Imaging Test Request'
    __name__ = 'gnuhealth.imaging.test.request'

    patient = fields.Many2One('gnuhealth.patient', 'Patient', required=True)
    date = fields.DateTime('Date', required=True)
    requested_test = fields.Many2One('gnuhealth.imaging.test', 'Test',
        required=True)
    doctor = fields.Many2One('gnuhealth.physician', 'Doctor', required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('requested', 'Requested'),
        ('done', 'Done'),
        ], 'State', readonly=True)
    comment = fields.Text('Comment')
    request = fields.Char('Request', readonly=True)
    urgent = fields.Boolean('Urgent')

    @classmethod
    def __setup__(cls):
        super(ImagingTestRequest, cls).__setup__()
        cls._transitions |= set((
            ('draft', 'requested'),
            ('requested', 'done')
        ))
        cls._buttons.update({
            'requested': {
                'invisible': ~Eval('state').in_(['draft']),
                },
             'generate_results': {
                 'invisible': ~Eval('state').in_(['requested'])
                 }
                 })
        cls._order.insert(0, ('date', 'DESC'))
        cls._order.insert(1, ('request', 'DESC'))

    @staticmethod
    def default_date():
        return datetime.now()

    @staticmethod
    def default_state():
        return 'draft'

    @staticmethod
    def default_doctor():
        cursor = Transaction().cursor
        User = Pool().get('res.user')
        user = User(Transaction().user)
        login_user_id = int(user.id)
        cursor.execute('SELECT id FROM party_party WHERE is_doctor=True AND \
            internal_user = %s LIMIT 1', (login_user_id,))
        partner_id = cursor.fetchone()
        if partner_id:
            cursor = Transaction().cursor
            cursor.execute('SELECT id FROM gnuhealth_physician WHERE \
                name = %s LIMIT 1', (partner_id[0],))
            doctor_id = cursor.fetchone()
            return int(doctor_id[0])

    @classmethod
    def create(cls, vlist):
        Sequence = Pool().get('ir.sequence')
        Config = Pool().get('gnuhealth.sequences')

        vlist = [x.copy() for x in vlist]
        for values in vlist:
            if not values.get('request'):
                config = Config(1)
                values['request'] = Sequence.get_id(
                    config.imaging_request_sequence.id)

        return super(ImagingTestRequest, cls).create(vlist)

    @classmethod
    def copy(cls, tests, default=None):
        if default is None:
            default = {}
        default = default.copy()
        default['request'] = None
        default['date'] = cls.default_date()
        return super(ImagingTestRequest, cls).copy(tests, default=default)

    @classmethod
    @ModelView.button
    @Workflow.transition('requested')
    def requested(cls, requests):
        pass

    @classmethod
    @ModelView.button_action('health_imaging.wizard_generate_result')
    def generate_results(cls, requests):
        pass

    @classmethod
    @Workflow.transition('done')
    def done(cls, requests):
        pass


class ImagingTestResult(ModelSQL, ModelView):
    'Imaging Test Result'
    __name__ = 'gnuhealth.imaging.test.result'

    patient = fields.Many2One('gnuhealth.patient', 'Patient', readonly=True)
    number = fields.Char('Number', readonly=True)
    date = fields.DateTime('Date', required=True)
    request_date = fields.DateTime('Requested Date', readonly=True)
    requested_test = fields.Many2One('gnuhealth.imaging.test', 'Test',
        required=True)
    request = fields.Many2One('gnuhealth.imaging.test.request', 'Request',
        readonly=True)
    doctor = fields.Many2One('gnuhealth.physician', 'Doctor', required=True)
    comment = fields.Text('Comment')
    images = fields.One2Many('ir.attachment', 'resource', 'Images')

    @classmethod
    def create(cls, vlist):
        Sequence = Pool().get('ir.sequence')
        Config = Pool().get('gnuhealth.sequences')

        vlist = [x.copy() for x in vlist]
        for values in vlist:
            if not values.get('name'):
                config = Config(1)
                values['number'] = Sequence.get_id(
                    config.imaging_sequence.id)

        return super(ImagingTestResult, cls).create(vlist)


class WizardGenerateResult(Wizard):
    'Open Suppliers'
    __name__ = 'wizard.generate.result'
    start_state = 'open_'
    open_ = StateAction('health_imaging.act_imaging_test_result_view')

    def do_open_(self, action):
        pool = Pool()
        Request = pool.get('gnuhealth.imaging.test.request')
        Result = pool.get('gnuhealth.imaging.test.result')
        ModelData = pool.get('ir.model.data')
        ActionActWindow = pool.get('ir.action.act_window')

        request_data = []
        requests = Request.browse(Transaction().context.get('active_ids'))
        for request in requests:
            request_data.append({
                'patient': request.patient.id,
                'date': datetime.now(),
                'request_date': request.date,
                'requested_test': request.requested_test,
                'request': request.id,
                'doctor': request.doctor})
        results = Result.create(request_data)

        action['pyson_domain'] = PYSONEncoder().encode(
            [('id', 'in', [r.id for r in results])])

        model_data, = ModelData.search([
            ('fs_id', '=', 'act_imaging_test_result_view'),
            ('module', '=', 'health_imaging'),
            ], limit=1)
        action_window = ActionActWindow(model_data.db_id)

        action['name'] = action_window.name
        Request.requested(requests)
        Request.done(requests)
        return action, {}


class RequestImagingTest(ModelView):
    'Request - Test'
    __name__ = 'gnuhealth.request-imaging-test'
    _table = 'gnuhealth_request_imaging_test'

    request = fields.Many2One('gnuhealth.patient.imaging.test.request.start',
        'Request', required=True)
    test = fields.Many2One('gnuhealth.imaging.test', 'Test', required=True)


class RequestPatientImagingTestStart(ModelView):
    'Request Patient Imaging Test Start'
    __name__ = 'gnuhealth.patient.imaging.test.request.start'

    date = fields.DateTime('Date')
    patient = fields.Many2One('gnuhealth.patient', 'Patient', required=True)
    doctor = fields.Many2One('gnuhealth.physician', 'Doctor', required=True,
        help="Doctor who Request the lab tests.")
    tests = fields.Many2Many('gnuhealth.request-imaging-test', 'request',
        'test', 'Tests', required=True)
    urgent = fields.Boolean('Urgent')

    @staticmethod
    def default_date():
        return datetime.now()

    @staticmethod
    def default_patient():
        if Transaction().context.get('active_model') == 'gnuhealth.patient':
            return Transaction().context.get('active_id')

    @staticmethod
    def default_doctor():
        cursor = Transaction().cursor
        User = Pool().get('res.user')
        user = User(Transaction().user)
        login_user_id = int(user.id)
        cursor.execute('SELECT id FROM party_party WHERE is_doctor=True AND \
            internal_user = %s LIMIT 1', (login_user_id,))
        partner_id = cursor.fetchone()
        if partner_id:
            cursor = Transaction().cursor
            cursor.execute('SELECT id FROM gnuhealth_physician WHERE \
                name = %s LIMIT 1', (partner_id[0],))
            doctor_id = cursor.fetchone()
            return int(doctor_id[0])


class RequestPatientImagingTest(Wizard):
    'Request Patient Imaging Test'
    __name__ = 'gnuhealth.patient.imaging.test.request'

    start = StateView('gnuhealth.patient.imaging.test.request.start',
        'health_imaging.patient_imaging_test_request_start_view_form', [
            Button('Cancel', 'end', 'tryton-cancel'),
            Button('Request', 'request', 'tryton-ok', default=True),
            ])
    request = StateTransition()

    def transition_request(self):
        ImagingTestRequest = Pool().get('gnuhealth.imaging.test.request')
        Sequence = Pool().get('ir.sequence')
        Config = Pool().get('gnuhealth.sequences')

        config = Config(1)
        request_number = Sequence.get_id(config.imaging_request_sequence.id)
        imaging_tests = []
        for test in self.start.tests:
            imaging_test = {}
            imaging_test['request'] = request_number
            imaging_test['requested_test'] = test.id
            imaging_test['patient'] = self.start.patient.id
            if self.start.doctor:
                imaging_test['doctor'] = self.start.doctor.id
            imaging_test['date'] = self.start.date
            imaging_test['urgent'] = self.start.urgent
            imaging_tests.append(imaging_test)
        ImagingTestRequest.create(imaging_tests)

        return 'end'
