# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2011  Adrián Bernardi, Mario Puntin
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
import logging

from trytond.model import ModelView
from trytond.wizard import Wizard

from trytond.pool import Pool

logging.basicConfig(level=logging.DEBUG)


class CreateTestInvoiceInit(ModelView):
    'Create Test Invoice Init'
    _name = 'gnuhealth.lab.test.invoice.init'
    _description = __doc__

CreateTestInvoiceInit()


class CreateTestInvoice(Wizard):
    _name = 'gnuhealth.lab.test.invoice'

    states = {
        'init': {
            'result': {
                'type': 'form',
                'object': 'gnuhealth.lab.test.invoice.init',
                'state': [
                    ('end', 'Cancel', 'tryton-cancel'),
                    ('create', 'Create Lab Invoice', 'tryton-ok', True),
                ],
            }
        },
        'create': {
            'result': {
                'type': 'action',
                'action': '_create_lab_invoice',
                'state': 'end',
            },
        },
    }

    def _action_open_invoice(self, ids):
        model_data_obj = Pool().get('ir.model.data')
        act_window_obj = Pool().get('ir.action.act_window')

        act_window_id = model_data_obj.get_id('account_invoice',
                'act_invoice_out_invoice_form3')
        res = act_window_obj.read(act_window_id)
        res['res_id'] = ids
        return res

    def _journal_id(self):
        journal_obj = Pool().get('account.journal')
        journal_id = journal_obj.search([
            ('type', '=', 'revenue'),
            ], limit=1)
        if journal_id:
            journal_id = journal_id[0]
        return journal_id

    def _create_lab_invoice(self, data):
        __logger = logging.getLogger('gnuhealth_invoice.wizard.test_invoice')

        invoice_obj = Pool().get('account.invoice')
        test_request_obj = Pool().get('gnuhealth.patient.lab.test')

        tests = data['ids']
        __logger.debug('tests = %s', repr(tests))

        pats = []
        for test_id in tests:
            #pats.append(test_request_obj.browse(test_id).patient_id)
            cur_test = test_request_obj.browse(test_id)
            __logger.debug('cur_test = %s; pats = %s', repr(cur_test),
                    repr(pats))
            pats.append(cur_test.patient_id)

        __logger.debug('pats = %s', repr(pats))

        if pats.count(pats[0]) == len(pats):
            invoice_data = {}
            for test_id in tests:
                test = test_request_obj.browse(test_id)
                __logger.debug('test = %s', repr(test))
                __logger.debug('test.patient_id = %s; test.patient_id.id = %s',
                        test.patient_id, test.patient_id.id)
                if test.invoice_status == 'invoiced':
                    if len(tests) > 1:
                        raise Exception('At least one of the selected lab ' \
                                        'tests is already invoiced')
                    else:
                        raise Exception('Lab test already invoiced')
                if test.invoice_status == 'no':
                    if len(tests) > 1:
                        raise Exception('At least one of the selected lab ' \
                                        'tests can not be invoiced')
                    else:
                        raise Exception('You can not invoice this lab test')

            __logger.debug('test.patient_id = %s; test.patient_id.id = %s',
                    test.patient_id, test.patient_id.id)
            if test.patient_id.name.id:
                invoice_data['state'] = 'draft'
                invoice_data['type'] = 'out_invoice'
                invoice_data['party'] = test.patient_id.name.id
                res = Pool().get('party.party').address_get(
                        test.patient_id.name.id, None)
                invoice_data['invoice_address'] = res
                invoice_data['account'] = \
                        test.patient_id.name.account_receivable.id
                invoice_data['payment_term'] = \
                        test.patient_id.name.payment_term and \
                        test.patient_id.name.payment_term.id or False
                invoice_data['journal'] = self._journal_id()

            prods_data = {}

            tests = data['ids']
            __logger.debug('tests = %s', repr(tests))

            for test_id in tests:
                test = test_request_obj.browse(test_id)
                __logger.debug('test.name = %s; test.name.product_id = %s; ' \
                        'test.name.product_id.id = %s', test.name,
                        test.name.product_id, test.name.product_id.id)

                if prods_data.has_key(test.name.product_id.id):
                    prods_data[test.name.product_id.id]['quantity'] += 1
                    __logger.debug('prods_data = %s; ' \
                            'test.name.product_id.id = %s', prods_data,
                            test.name.product_id.id)
                else:
                    __logger.debug('test.name.product_id.id = %s',
                            test.name.product_id.id)
                    a = test.name.product_id.template.account_revenue_used.id
                    #if not a:
                        #a = test.name.product_id.categ_id.property_account_income_categ.id # TODO
                    prods_data[test.name.product_id.id] = {
                        'product': test.name.product_id.id,
                        'description': test.name.product_id.name,
                        'quantity': 1,
                        'unit': test.name.product_id.default_uom.id,
                        'account': a,
                        'unit_price': test.name.product_id.list_price,
                    }
                    __logger.debug('prods_data[%s] = %s',
                            test.name.product_id.id,
                            prods_data[test.name.product_id.id])

            product_lines = []
            for prod_id, prod_data in prods_data.items():
                product_lines.append(('create', {
                        'product': prod_data['product'],
                        'description': prod_data['description'],
                        'quantity': prod_data['quantity'],
                        'unit': prod_data['unit'],
                        'account': prod_data['account'],
                        'unit_price': prod_data['unit_price'],
                    }))

            invoice_data['lines'] = product_lines
            invoice_id = invoice_obj.create(invoice_data)

            test_request_obj.write(tests, {'invoice_status': 'invoiced'})

            return self._action_open_invoice(invoice_id)

        else:
            raise Exception('When multiple lab tests are selected, patient ' \
                            'must be the same')

CreateTestInvoice()
