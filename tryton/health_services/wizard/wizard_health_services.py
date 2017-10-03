# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2008-2017 Luis Falcon <lfalcon@gnusolidario.org>
#    Copyright (C) 2011-2017 GNU Solidario <health@gnusolidario.org>
#
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
import datetime
from trytond.model import ModelView
from trytond.wizard import Wizard, StateTransition, StateView, Button
from trytond.transaction import Transaction
from trytond.pool import Pool


__all__ = ['CreateServiceInvoiceInit', 'CreateServiceInvoice']


class CreateServiceInvoiceInit(ModelView):
    'Create Service Invoice Init'
    __name__ = 'gnuhealth.service.invoice.init'


class CreateServiceInvoice(Wizard):
    'Create Service Invoice'
    __name__ = 'gnuhealth.service.invoice.create'

    start = StateView('gnuhealth.service.invoice.init',
        'health_services.view_health_service_invoice', [
            Button('Cancel', 'end', 'tryton-cancel'),
            Button('Create Invoice', 'create_service_invoice', 'tryton-ok',
                True),
            ])
    create_service_invoice = StateTransition()

    @classmethod
    def __setup__(cls):
        super(CreateServiceInvoice, cls).__setup__()
        cls._error_messages.update({
            'duplicate_invoice': 'Service already invoiced', \
            'no_invoice_address': 'No invoice address associated', \
            'no_payment_term': 'No Payment Term associated to the Patient'
            })

    def transition_create_service_invoice(self):
        pool = Pool()
        HealthService = pool.get('gnuhealth.health_service')
        Invoice = pool.get('account.invoice')
        Party = pool.get('party.party')
        Journal = pool.get('account.journal')

        currency_id = Transaction().context.get('currency')

        services = HealthService.browse(Transaction().context.get(
            'active_ids'))
        invoices = []

        #Invoice Header
        for service in services:
            if service.state == 'invoiced':
                self.raise_user_error('duplicate_invoice')
            if service.invoice_to:
                party = service.invoice_to
            else:
                party = service.patient.name
            invoice_data = {}
            invoice_data['description'] = service.desc
            invoice_data['party'] = party.id
            invoice_data['type'] = 'out'
            invoice_data['invoice_date'] = datetime.date.today()
            invoice_data['account'] = party.account_receivable.id
            invoice_data['company'] = service.company.id

            ctx = {}
            sale_price_list = None
            if hasattr(party, 'sale_price_list'):
                sale_price_list = party.sale_price_list

            if sale_price_list:
                ctx['price_list'] = sale_price_list.id
                ctx['sale_date'] = datetime.date.today()
                ctx['currency'] = currency_id
                ctx['customer'] = party.id

            journals = Journal.search([
                ('type', '=', 'revenue'),
                ], limit=1)

            if journals:
                journal, = journals
            else:
                journal = None

            invoice_data['journal'] = journal.id

            party_address = Party.address_get(party, type='invoice')
            if not party_address:
                self.raise_user_error('no_invoice_address')
            invoice_data['invoice_address'] = party_address.id
            invoice_data['reference'] = service.name

            if not party.customer_payment_term:
                self.raise_user_error('no_payment_term')

            invoice_data['payment_term'] = party.customer_payment_term.id

            #Invoice Lines
            seq = 0
            invoice_lines = []
            for line in service.service_line:
                seq = seq + 1
                account = line.product.template.account_revenue_used.id

                if sale_price_list:
                    with Transaction().set_context(ctx):
                        unit_price = sale_price_list.compute(party,
                            line.product, line.product.list_price,
                            line.qty, line.product.default_uom)
                else:
                    unit_price = line.product.list_price

                if line.to_invoice:
                    taxes = []
                    #Include taxes related to the product on the invoice line
                    for product_tax_line in line.product.customer_taxes_used:
                        taxes.append(product_tax_line.id)
                        
                    invoice_lines.append(('create', [{
                            'origin': str(line),
                            'product': line.product.id,
                            'description': line.desc,
                            'quantity': line.qty,
                            'account': account,
                            'unit': line.product.default_uom.id,
                            'unit_price': unit_price,
                            'sequence': seq,
                            'taxes': [('add',taxes)],
                        }]))
                invoice_data['lines'] = invoice_lines

            invoices.append(invoice_data)

        Invoice.update_taxes(Invoice.create(invoices))

        # Change to invoiced the status on the service document.
        HealthService.write(services, {'state': 'invoiced'})

        return 'end'
