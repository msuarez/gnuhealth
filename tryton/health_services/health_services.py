# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2008-2013  Luis Falcon <falcon@gnu.org>
#    Copyright (C) 2011  Adrián Bernardi, Mario Puntin (health_invoice)
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
from trytond.model import ModelView, ModelSQL, fields, ModelSingleton
from trytond.pyson import Eval, Equal
from trytond.pool import Pool


__all__ = ['GnuHealthSequences', 'HealthService', 'HealthServiceLine']


class GnuHealthSequences(ModelSingleton, ModelSQL, ModelView):
    "Standard Sequences for GNU Health"
    __name__ = "gnuhealth.sequences"

    health_service_sequence = fields.Property(fields.Many2One('ir.sequence',
        'Health Service Sequence', domain=[
            ('code', '=', 'gnuhealth.health_service')
        ], required=True))


class HealthService(ModelSQL, ModelView):
    'Health Service'
    __name__ = 'gnuhealth.health_service'

    name = fields.Char('ID', readonly=True)
    desc = fields.Char('Description', required=True)
    patient = fields.Many2One('gnuhealth.patient', 'Patient', required=True)
    service_date = fields.Date('Date')
    service_line = fields.One2Many('gnuhealth.health_service.line',
        'name', 'Service Line', help="Service Line")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('invoiced', 'Invoiced'),
        ], 'State', readonly=True)

    @classmethod
    def __setup__(cls):
        super(HealthService, cls).__setup__()
        cls._sql_constraints += [
            ('name_uniq', 'UNIQUE(name)', 'The Service ID must be unique')]
        cls._buttons.update({
            'button_set_to_draft': {'invisible': Equal(Eval('state'),
                'draft')}
            })

    @staticmethod
    def default_state():
        return 'draft'

    @classmethod
    @ModelView.button
    def button_set_to_draft(cls, services):
        cls.write(services, {'state': 'draft'})

    @classmethod
    def create(cls, vlist):
        Sequence = Pool().get('ir.sequence')
        Config = Pool().get('gnuhealth.sequences')

        vlist = [x.copy() for x in vlist]
        for values in vlist:
            if not values.get('name'):
                config = Config(1)
                values['name'] = Sequence.get_id(
                    config.health_service_sequence.id)
        return super(HealthService, cls).create(vlist)


class HealthServiceLine(ModelSQL, ModelView):
    'Health Service'
    __name__ = 'gnuhealth.health_service.line'

    name = fields.Many2One('gnuhealth.health_service', 'Service',
        readonly=True)
    desc = fields.Char('Description', required=True)
    appointment = fields.Many2One('gnuhealth.appointment', 'Appointment',
        help='Enter or select the date / ID of the appointment related to'
        ' this evaluation')
    to_invoice = fields.Boolean('Invoice')
    product = fields.Many2One('product.product', 'Product', required=True)
    qty = fields.Integer('Qty')
    from_date = fields.Date('From')
    to_date = fields.Date('To')

    @staticmethod
    def default_qty():
        return 1

