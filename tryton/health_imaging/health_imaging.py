# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2008-2013  Luis Falcon <lfalcon@gnusolidario.org>
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
from trytond.wizard import Wizard, StateAction
from trytond.pyson import PYSONEncoder, Eval
from trytond.transaction import Transaction
from trytond.pool import Pool


__all__ = ['GnuHealthSequences', 'ImagingTestType', 'ImagingTest',
    'ImagingTestRequest', 'ImagingTestResult', 'WizardGenerateResult']


class GnuHealthSequences(ModelSingleton, ModelSQL, ModelView):
    "Standard Sequences for GNU Health"
    __name__ = "gnuhealth.sequences"

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
        Request.done(requests)
        return action, {}
