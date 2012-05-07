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

from trytond.wizard import Wizard, StateTransition, StateView, StateTransition, \
    Button

from trytond.transaction import Transaction


from trytond.pool import Pool

class MakeMedicalAppointmentInvoiceInit(ModelView):
    'Make Medical Appointment Invoice Init'
    _name = 'gnuhealth.appointment.invoice.init'
    _description = __doc__

MakeMedicalAppointmentInvoiceInit()


class MakeMedicalAppointmentInvoice(Wizard):
    _name = 'gnuhealth.appointment.invoice'


    start = StateView('gnuhealth.appointment.invoice.init',
        'health_lab.view_lab_make_test', [
            Button('Cancel', 'end', 'tryton-cancel'),
            Button('Create Invoices', 'create_invoices', 'tryton-ok', True),
            ])
    
    create_invoices = StateTransition()


    def transition_create_invoice(self, session):

        invoice_obj = Pool().get('account.invoice')
        appointment_obj = Pool().get('gnuhealth.appointment')

        invoices = invoice_obj.browse(Transaction().context.get('active_ids'))
        
        for invoice in invoices:
        apps = data['ids']
        pats = []

        for app_id in apps:
            pats.append(appointment_obj.browse(app_id).patient.name.id)

        if pats.count(pats[0]) == len(pats):
            invoice_data = {}
            for app_id in apps:
                appointment = appointment_obj.browse(app_id)

                # Check if the appointment is invoice exempt, and stop the invoicing process
                if appointment.no_invoice:
                    raise Exception('The appointment is invoice exempt')

                if appointment.validity_status == 'invoiced':
                    if len(apps) > 1:
                        raise Exception('At least one of the selected ' \
                                        'appointments is already invoiced')
                    else:
                        raise Exception('Appointment already invoiced')
                if appointment.validity_status == 'no':
                    if len(apps) > 1:
                        raise Exception('At least one of the selected ' \
                                        'appointments can not be invoiced')
                    else:
                        raise Exception('You can not invoice this appointment')

            if appointment.patient.name.id:
                invoice_data['party'] = appointment.patient.name.id
                res = Pool().get('party.party').address_get(
                        appointment.patient.name.id, None)
                invoice_data['invoice_address'] = res
                invoice_data['account'] = \
                        appointment.patient.name.account_receivable.id
                invoice_data['payment_term'] = \
                        appointment.patient.name.customer_payment_term and \
                        appointment.patient.name.customer_payment_term.id or \
                        False

            prods_data = {}
            for app_id in apps:
                appointment = appointment_obj.browse(app_id)
                __logger.debug('appointment = %s; ' \
                        'appointment.consultations = %s', appointment,
                        appointment.consultations)
                if appointment.consultations:
                    __logger.debug('appointment.consultations = %s; ' \
                            'appointment.consultations.id = %s',
                            appointment.consultations,
                            appointment.consultations.id)
                    if prods_data.has_key(appointment.consultations.id):
                        prods_data[
                                appointment.consultations.id]['quantity'] += 1
                    else:
                        a = appointment.consultations.template.account_revenue_used.id
                        #if not a:
                            #a = appointment.consultations.categ_id.property_account_income_categ.id  # TODO
                        prods_data[appointment.consultations.id] = {
                            'product': appointment.consultations.id,
                            'description': appointment.consultations.name,
                            'unit': appointment.consultations.default_uom.id,
                            'quantity': 1,
                            'account': a,
                            'unit_price': appointment.consultations.list_price,
                        }
                else:
                    raise Exception('No consultation service is connected ' \
                                    'with the selected appointments')

            product_lines = []
            for prod_id, prod_data in prods_data.items():
                product_lines.append(('create', {
                        'product': prod_data['product'],
                        'description': prod_data['description'],
                        'unit': prod_data['unit'],
                        'quantity': prod_data['quantity'],
                        'account': prod_data['account'],
                        'unit_price': prod_data['unit_price'],
                    }))

            __logger.debug('product_lines = %s', product_lines)
            invoice_data['lines'] = product_lines
            __logger.debug('invoice_data = %s', invoice_data)
            invoice_id = invoice_obj.create(invoice_data)

            appointment_obj.write(apps, {'validity_status': 'invoiced'})

            return 'end'

        else:
            raise Exception('When multiple appointments are selected, ' \
                            'patient must be the same')

MakeMedicalAppointmentInvoice()
