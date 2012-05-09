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
        
        selected_services = health_service_obj.browse(Transaction().context.get('active_ids'))
        
        for service in selected_services:
                print service.desc
        
        return 'end'
        

CreateServiceInvoice()

