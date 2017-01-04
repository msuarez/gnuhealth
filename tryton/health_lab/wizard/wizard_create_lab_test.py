# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2008-2017 Luis Falcon <lfalcon@gnusolidario.org>
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
from datetime import datetime
from trytond.model import ModelView, fields
from trytond.wizard import Wizard, StateTransition, StateView, Button
from trytond.transaction import Transaction
from trytond.pool import Pool


__all__ = ['CreateLabTestOrderInit', 'CreateLabTestOrder', 'RequestTest',
    'RequestPatientLabTestStart', 'RequestPatientLabTest']


class CreateLabTestOrderInit(ModelView):
    'Create Test Report Init'
    __name__ = 'gnuhealth.lab.test.create.init'


class CreateLabTestOrder(Wizard):
    'Create Lab Test Report'
    __name__ = 'gnuhealth.lab.test.create'

    start = StateView('gnuhealth.lab.test.create.init',
        'health_lab.view_lab_make_test', [
            Button('Cancel', 'end', 'tryton-cancel'),
            Button('Create Test Order', 'create_lab_test', 'tryton-ok', True),
            ])

    create_lab_test = StateTransition()

    def transition_create_lab_test(self):
        TestRequest = Pool().get('gnuhealth.patient.lab.test')
        Lab = Pool().get('gnuhealth.lab')

        tests_report_data = []

        tests = TestRequest.browse(Transaction().context.get('active_ids'))

        for lab_test_order in tests:

            test_cases = []
            test_report_data = {}

            if lab_test_order.state == 'ordered':
                self.raise_user_error(
                    "The Lab test order is already created")

            test_report_data['test'] = lab_test_order.name.id
            test_report_data['patient'] = lab_test_order.patient_id.id
            if lab_test_order.doctor_id:
                test_report_data['requestor'] = lab_test_order.doctor_id.id
            test_report_data['date_requested'] = lab_test_order.date
            test_report_data['request_order'] = lab_test_order.request

            for critearea in lab_test_order.name.critearea:
                test_cases.append(('create', [{
                        'name': critearea.name,
                        'sequence': critearea.sequence,
                        'lower_limit': critearea.lower_limit,
                        'upper_limit': critearea.upper_limit,
                        'normal_range': critearea.normal_range,
                        'units': critearea.units and critearea.units.id,
                    }]))
            test_report_data['critearea'] = test_cases

            tests_report_data.append(test_report_data)

        Lab.create(tests_report_data)
        TestRequest.write(tests, {'state': 'ordered'})

        return 'end'


class RequestTest(ModelView):
    'Request - Test'
    __name__ = 'gnuhealth.request-test'
    _table = 'gnuhealth_request_test'

    request = fields.Many2One('gnuhealth.patient.lab.test.request.start',
        'Request', required=True)
    test = fields.Many2One('gnuhealth.lab.test_type', 'Test', required=True)


class RequestPatientLabTestStart(ModelView):
    'Request Patient Lab Test Start'
    __name__ = 'gnuhealth.patient.lab.test.request.start'

    date = fields.DateTime('Date')
    patient = fields.Many2One('gnuhealth.patient', 'Patient', required=True)
    doctor = fields.Many2One('gnuhealth.healthprofessional', 'Doctor',
        help="Doctor who Request the lab tests.")
    tests = fields.Many2Many('gnuhealth.request-test', 'request', 'test',
        'Tests', required=True)
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
        pool = Pool()
        HealthProf= pool.get('gnuhealth.healthprofessional')
        hp = HealthProf.get_health_professional()
        if not hp:
            RequestPatientLabTestStart.raise_user_error(
                "No health professional associated to this user !")
        return hp

class RequestPatientLabTest(Wizard):
    'Request Patient Lab Test'
    __name__ = 'gnuhealth.patient.lab.test.request'

    start = StateView('gnuhealth.patient.lab.test.request.start',
        'health_lab.patient_lab_test_request_start_view_form', [
            Button('Cancel', 'end', 'tryton-cancel'),
            Button('Request', 'request', 'tryton-ok', default=True),
            ])
    request = StateTransition()

    def transition_request(self):
        PatientLabTest = Pool().get('gnuhealth.patient.lab.test')
        Sequence = Pool().get('ir.sequence')
        Config = Pool().get('gnuhealth.sequences')

        config = Config(1)
        request_number = Sequence.get_id(config.lab_request_sequence.id)
        lab_tests = []
        for test in self.start.tests:
            lab_test = {}
            lab_test['request'] = request_number
            lab_test['name'] = test.id
            lab_test['patient_id'] = self.start.patient.id
            if self.start.doctor:
                lab_test['doctor_id'] = self.start.doctor.id
            lab_test['date'] = self.start.date
            lab_test['urgent'] = self.start.urgent
            lab_tests.append(lab_test)
        PatientLabTest.create(lab_tests)

        return 'end'
