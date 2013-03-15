# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2008-2013  Luis Falcon <lfalcon@gnusolidario.org>
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
from trytond.model import ModelView, fields
from trytond.wizard import Wizard, StateView, Button, StateTransition
from trytond.pyson import Eval, Not, Bool
from trytond.transaction import Transaction
from trytond.pool import Pool, PoolMeta

__all__ = ['Medicament', 'Party', 'ShipmentOut',
    'CreatePrescriptionShipmentInit', 'CreatePrescriptionShipment']
__metaclass__ = PoolMeta


class Medicament:
    __name__ = 'gnuhealth.medicament'
    quantity = fields.Function(fields.Float('Quantity'), 'get_quantity')

    def get_quantity(self, name):
        pool = Pool()
        Date = pool.get('ir.date')
        Location = pool.get('stock.location')
        Product = pool.get('product.product')

        locations = Location.search([('type', '=', 'storage')])
        Transaction().set_context({'locations': [l.id for l in locations]})
        context = {}
        context['stock_date_end'] = Date.today()
        Transaction().set_context(context)

        pbl = Product.products_by_location(
                location_ids=Transaction().context['locations'],
                product_ids=[self.name.id], with_childs=True)
        quantity = 0.00
        if pbl.values():
            quantity = reduce(lambda x, y: x + y, pbl.values())
        return quantity


class Party:
    __name__ = 'party.party'
    warehouse = fields.Many2One('stock.location', 'Warehouse',
        domain=[('type', '=', 'warehouse')],
        states={
            'invisible': Not(Bool(Eval('is_pharmacy'))),
            'required': Bool(Eval('is_pharmacy')),
            },
        depends=['is_pharmacy'])

    @classmethod
    def default_warehouse(cls):
        Location = Pool().get('stock.location')
        locations = Location.search(cls.warehouse.domain)
        if len(locations) == 1:
            return locations[0].id


class ShipmentOut:
    __name__ = 'stock.shipment.out'
    prescription_order = fields.Many2One('gnuhealth.prescription.order',
        'Source Prescription')


class CreatePrescriptionShipmentInit(ModelView):
    'Create Prescription Shipment'
    __name__ = 'gnuhealth.prescription.shipment.init'


class CreatePrescriptionShipment(Wizard):
    'Create Prescription Shipment'
    __name__ = 'gnuhealth.prescription.shipment.create'

    start = StateView('gnuhealth.prescription.shipment.init',
            'health_stock.view_create_prescription_shipment', [
            Button('Cancel', 'end', 'tryton-cancel'),
            Button('Create Shipment', 'create_shipment',
                'tryton-ok', True),
            ])
    create_shipment = StateTransition()

    def transition_create_shipment(self):
        pool = Pool()
        Shipment = pool.get('stock.shipment.out')
        ShipmentLine = pool.get('stock.move')
        StockLocation = Pool().get('stock.location')
        Prescription = pool.get('gnuhealth.prescription.order')

        prescriptions = Prescription.browse(Transaction().context.get(
            'active_ids'))
        shipment_data = {}
        for prescription in prescriptions:
            shipment_data['customer'] = prescription.patient.name.id
            shipment_data['company'] = Transaction().context['company']
            shipment_data['warehouse'] = prescription.pharmacy.warehouse
            shipment_data['prescription_order'] = prescription.id
            if prescription.patient.name.addresses:
                shipment_data['delivery_address'] = \
                    prescription.patient.name.addresses[0]
            else:
                raise Exception('You need to define an address in the party \
                    form.')

            shipment = Shipment.create(shipment_data)

            #Create Shipment Lines
            warehouse = StockLocation(prescription.pharmacy.warehouse)
            Shipment.wait([shipment])
            for line in prescription.prescription_line:
                shipment_line_data = {}
                shipment_line_data['shipment_out'] = shipment.id
                shipment_line_data['from_location'] = \
                    warehouse.storage_location.id
                shipment_line_data['to_location'] = \
                    warehouse.output_location.id
                shipment_line_data['product'] = \
                    line.template.medicament.name.id
                shipment_line_data['quantity'] = line.quantity
                shipment_line_data['uom'] = \
                    line.template.medicament.name.default_uom.id
                shipment_line_data['state'] = 'assigned'
                ShipmentLine.create(shipment_line_data)

        return 'end'
