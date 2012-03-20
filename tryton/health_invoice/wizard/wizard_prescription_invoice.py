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


class MakeMedicalPrescriptionInvoiceInit(ModelView):
    'Make Medical Prescription Invoice Init'
    _name = 'gnuhealth.prescription.invoice.init'
    _description = __doc__

MakeMedicalPrescriptionInvoiceInit()


class MakeMedicalPrescriptionInvoice(Wizard):
    _name = 'gnuhealth.prescription.invoice'

    states = {
        'init': {
            'result': {
                'type': 'form',
                'object': 'gnuhealth.prescription.invoice.init',
                'state': [
                    ('end', 'Cancel', 'tryton-cancel'),
                    ('create', 'Create Prescription Invoices', 'tryton-ok',
                            True),
                ],
            }
        },
        'create': {
            'result': {
                'type': 'action',
                'action': '_create_prescription_invoice',
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

    def _create_prescription_invoice(self, data):
        __logger = logging.getLogger(
                'gnuhealth_invoice.wizard.prescription_invoice')
        invoice_obj = Pool().get('account.invoice')
        pres_request_obj = Pool().get('gnuhealth.prescription.order')

#       prescriptions = ids
# Don't use this. It will be 1 (and it would go to the invoice status of the
# first prescription )

# To get the IDs of the prescriptions, use the context value array for
# active_ids

        prescriptions = data['ids']

        pats = []
        for pres_id in prescriptions:
            pres = pres_request_obj.browse(pres_id)
            pats.append(pres.patient)  # TODO: _rec_name = 'patient' in 
                                       # gnuhealth.prescription.order
            __logger.debug('pres = %s; pats = %s', repr(pres), repr(pats))

        if pats.count(pats[0]) == len(pats):
            invoice_data = {}
            for pres_id in prescriptions:
                pres = pres_request_obj.browse(pres_id)

# Check if the prescription is invoice exempt, and stop the invoicing process
                if pres.no_invoice:
                    raise Exception('The prescription is invoice exempt')

                if pres.invoice_status == 'invoiced':
                    __logger.debug('pres.invoice_status = %s',
                            repr(pres.invoice_status))
                    if len(prescriptions) > 1:
                        raise Exception('At least one of the selected ' \
                                        'prescriptions is already invoiced')
                    else:
                        raise Exception('Prescription already invoiced')
                if pres.invoice_status == 'no':
                    if len(prescriptions) > 1:
                        raise Exception('At least one of the selected ' \
                                        'prescriptions can not be invoiced')
                    else:
                        raise Exception('You can not invoice this ' \
                                        'prescription')

            # TODO: _rec_name = 'patient' in gnuhealth.prescription.order
            __logger.debug('pres.patient = %s', repr(pres.patient))
            if pres.patient.name.id:
                invoice_data['party'] = pres.patient.name.id
                res = Pool().get('party.party').address_get(
                        pres.patient.name.id, None)
                invoice_data['invoice_address'] = res
                invoice_data['account'] = \
                        pres.patient.name.account_receivable.id
                invoice_data['payment_term'] = pres.patient.name.payment_term \
                        and pres.patient.name.payment_term.id or False

            prods_data = {}
            for pres_id in prescriptions:
                pres = pres_request_obj.browse(pres_id)
                __logger.debug('pres.patient = %s; ' \
                        'pres.prescription_line = %s', pres.patient,
                        pres.prescription_line)

# Check for empty prescription lines

                if not pres.prescription_line:
                    raise Exception('You need to have at least one ' \
                                    'prescription item in your invoice')

                for pres_line in pres.prescription_line:
                    __logger.debug('pres_line = %s; ' \
                            'pres_line.medicament.name = %s; ' \
                            'pres_line.quantity = %s', pres_line,
                            pres_line.medicament.name, pres_line.quantity)

                    if prods_data.has_key(pres_line.medicament.name):
                        prods_data[pres_line.medicament.name]['quantity'] \
                                += pres_line.quantity
                    else:
                        a = pres_line.medicament.name.template.account_revenue_used.id
                        #if not a:
                            #a = pres_line.medicament.name.categ_id.property_account_income_categ.id  # TODO

                        taxes_ids = []

                        taxes = \
                            pres_line.medicament.name.template.customer_taxes

                        for taxes_id in taxes:
                            taxes_ids.append(taxes_id.id)
                            __logger.debug('taxes_id = %s; taxes_ids = %s;',
                                    taxes_id, taxes_ids)

                        prods_data[pres_line.medicament.name] = {
                            'product': pres_line.medicament.name.id,
                            'description': pres_line.medicament.name.name,
                            'quantity': pres_line.quantity,
                            'unit': pres_line.medicament.name.default_uom.id,
                            'account': a,
                            'taxes': [('set', taxes_ids)],
                            'unit_price': pres_line.medicament.name.list_price,
                        }
                        __logger.debug('prods_data[%s] = %s;',
                                pres_line.medicament.name,
                                prods_data[pres_line.medicament.name])

            product_lines = []
            for prod_id, prod_data in prods_data.items():
                __logger.debug('product = %s', repr(prod_data['product']))
                product_lines.append(('create', {
                        'product': prod_data['product'],
                        'description': prod_data['description'],
                        'quantity': prod_data['quantity'],
                        'unit': prod_data['unit'],
                        'account': prod_data['account'],
                        'taxes': prod_data['taxes'],
                        'unit_price': prod_data['unit_price'],
                    }))

            invoice_data['lines'] = product_lines
            invoice_id = invoice_obj.create(invoice_data)

            pres_request_obj.write(prescriptions, {
                    'invoice_status': 'invoiced'})

            return self._action_open_invoice(invoice_id)

        else:
            raise Exception('When multiple prescriptions are selected, ' \
                            'patient must be the same')

MakeMedicalPrescriptionInvoice()
