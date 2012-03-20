# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2008-2012  Luis Falcon <lfalcon@gnusolidario.org>
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
from trytond.model import ModelView
from trytond.wizard import Wizard
from trytond.pool import Pool


class CreateTestReportInit(ModelView):
    'Create Test Report Init'
    _name = 'gnuhealth.lab.test.create.init'
    _description = __doc__

CreateTestReportInit()


class CreateTestReport(Wizard):
    'Create Test Report'
    _name = 'gnuhealth.lab.test.create'

    states = {
        'init': {
            'result': {
                'type': 'form',
                'object': 'gnuhealth.lab.test.create.init',
                'state': [
                    ('end', 'Cancel', 'tryton-cancel'),
                    ('create', 'Create Lab Test', 'tryton-ok', True),
                ],
            }
        },
        'create': {
            'result': {
                'type': 'action',
                'action': '_create_lab_test',
                'state': 'end',
            },
        },
    }

    def _action_open_gnuhealth_lab(self, ids):
        model_data_obj = Pool().get('ir.model.data')
        act_window_obj = Pool().get('ir.action.act_window')

        act_window_id = model_data_obj.get_id('health_lab',
                'gnuhealth_action_tree_lab')
        res = act_window_obj.read(act_window_id)
        res['res_id'] = ids
        return res

    def _create_lab_test(self, data):
        test_request_obj = Pool().get('gnuhealth.patient.lab.test')
        lab_obj = Pool().get('gnuhealth.lab')

        test_report_data = {}
        test_cases = []
        test_obj = test_request_obj.browse([data['id']])[0]
        if test_obj.state == 'tested':
            raise Exception('Test Report already created.')
        test_report_data['test'] = test_obj.name.id
        test_report_data['patient'] = test_obj.patient_id.id
        test_report_data['requestor'] = test_obj.doctor_id.id
        test_report_data['date_requested'] = test_obj.date

        for critearea in test_obj.name.critearea:
            test_cases.append(('create', {
                    'name': critearea.name,
                    'sequence': critearea.sequence,
                    'lower_limit': critearea.lower_limit,
                    'upper_limit': critearea.upper_limit,                    
                    'normal_range': critearea.normal_range,
                    'units': critearea.units.id,
                }))
        test_report_data['critearea'] = test_cases
        lab_id = lab_obj.create(test_report_data)
        test_request_obj.write([data['id']], {'state': 'tested'})
        return self._action_open_gnuhealth_lab(lab_id)

CreateTestReport()
