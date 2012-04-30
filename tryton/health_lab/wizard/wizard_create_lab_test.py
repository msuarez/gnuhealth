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
from trytond.wizard import Wizard, StateTransition, StateView, StateTransition, \
    Button
from trytond.transaction import Transaction

from trytond.pool import Pool

class CreateLabTestOrderInit(ModelView):
    'Create Test Report Init'
    _name = 'gnuhealth.lab.test.create.init'
    _description = __doc__

CreateLabTestOrderInit()


class CreateLabTestOrder(Wizard):
    'Create Lab Test Report'
    _name = 'gnuhealth.lab.test.create'

    start = StateView('gnuhealth.lab.test.create.init',
        'health_lab.view_lab_make_test', [
            Button('Cancel', 'end', 'tryton-cancel'),
            Button('Create Test Order', 'create_lab_test', 'tryton-ok', True),
            ])
    
    create_lab_test = StateTransition()


    def transition_create_lab_test(self, session):
        test_request_obj = Pool().get('gnuhealth.patient.lab.test')
        lab_obj = Pool().get('gnuhealth.lab')

        test_report_data = {}
        test_cases = []
        
        test_obj = test_request_obj.browse(Transaction().context.get('active_ids'))
        
        for lab_test_order in test_obj:
                  
            if lab_test_order.state == 'ordered':
                raise Exception('The Lab test order is already created.')

            test_report_data['test'] = lab_test_order.name.id
            test_report_data['patient'] = lab_test_order.patient_id.id
            test_report_data['requestor'] = lab_test_order.doctor_id.id
            test_report_data['date_requested'] = lab_test_order.date

            for critearea in lab_test_order.name.critearea:
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
            test_request_obj.write(lab_test_order.id, {'state': 'ordered'})
                       
        return 'end'
        

CreateLabTestOrder()
