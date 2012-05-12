# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2008-2012  Luis Falcon <lfalcon@gnusolidario.org>
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
from trytond.model import ModelView
from trytond.wizard import Wizard, StateTransition, StateView, StateTransition, \
    Button
from trytond.transaction import Transaction

from trytond.pool import Pool


class CreateServiceInvoiceInit(ModelView):
    'Create Service Invoice Init'
    _name = 'gnuhealth.service.invoice.init'
    _description = __doc__

CreateServiceInvoiceInit()


class CreateServiceInvoice(Wizard):
    'Create Service Invoice'
    _name = 'gnuhealth.service.invoice.create'

    start = StateView('gnuhealth.service.invoice.init',
        'health_services.view_health_service_invoice', [
            Button('Cancel', 'end', 'tryton-cancel'),
            Button('Create Invoice', 'create_service_invoice', 'tryton-ok', True),
            ])
    
    create_service_invoice = StateTransition()


    def transition_create_service_invoice(self, session):
        health_service_obj = Pool().get('gnuhealth.health_service')
        invoice_obj = Pool().get('account.invoice')
        party_obj = Pool().get('party.party')
        
        selected_services = health_service_obj.browse(Transaction().context.get('active_ids'))
        
        #Invoice Header
        for service in selected_services:

            if service.state == 'invoiced':
                    self.raise_user_error('duplicate_invoice')
                    
            invoice_data = {}

            invoice_data['description'] = service.desc
            invoice_data['party'] = service.patient.name.id  
            invoice_data['account'] = service.patient.name.account_receivable.id
            invoice_data['invoice_address'] = party_obj.address_get(service.patient.name.id, type='invoice')
            invoice_data['reference'] = service.name
           
            invoice_data['payment_term'] = \
                    service.patient.name.customer_payment_term and \
                    service.patient.name.customer_payment_term.id or \
                    False
            

        
            #Invoice Lines
            seq = 0
            invoice_lines = []
            
            for line in service.service_line:
                seq = seq + 1
                account = line['product'].template.account_revenue_used.id

                if line['to_invoice'] :                  
                    invoice_lines.append(('create', {
                            'product': line['product'].id,
                            'description': line['desc'],
                            'quantity': line['qty'],
                            'account': account,
                            'unit' : line['product'].default_uom.id,
                            'unit_price' : line['product'].list_price,
                            'sequence': seq
                        }))

                invoice_data['lines'] = invoice_lines
                                
            invoice_document = invoice_obj.create(invoice_data)
            
            
            # Change to invoiced the status on the service document.
            health_service_obj.write(service.id, {'state': 'invoiced'})
        
        return 'end'
        
    def __init__(self):
        super(CreateServiceInvoice, self).__init__()
        self._error_messages.update({
            'duplicate_invoice': 'Service already invoiced'})
            


CreateServiceInvoice()

