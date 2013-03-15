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
from datetime import datetime
from trytond.model import Workflow, ModelView, ModelSQL, fields
from trytond.wizard import Wizard, StateView, Button, StateTransition
from trytond.pyson import Eval, Not, Bool
from trytond.exceptions import UserError
from trytond.transaction import Transaction
from trytond.pool import Pool, PoolMeta

__all__ = ['Medicament', 'Party', 'ShipmentOut', 'Move',
    'PatientAmbulatoryCare', 'PatientAmbulatoryCareLineMedicament',
    'PatientAmbulatoryCareLineSupply', 'PatientAmbulatoryCareLineVaccine',
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


class Move:
    __name__ = 'stock.move'
    ambulatory_care = fields.Many2One('gnuhealth.patient.ambulatory_care',
        'Source Ambulatory Care')
    rounding = fields.Many2One('gnuhealth.patient.rounding',
        'Source Rounding')


class PatientAmbulatoryCare(Workflow, ModelSQL, ModelView):
    'Patient Ambulatory Care'
    __name__ = 'gnuhealth.patient.ambulatory_care'

    medication_line = fields.One2Many(
        'gnuhealth.patient.ambulatory_care.line.medicament', 'name',
        'Medication')
    medical_supply_line = fields.One2Many(
        'gnuhealth.patient.ambulatory_care.line.supply', 'name',
        'Medical Supplies')
    vaccine_line = fields.One2Many(
        'gnuhealth.patient.ambulatory_care.line.vaccine', 'name', "Vaccines")
    moves = fields.One2Many('stock.move', 'ambulatory_care', 'Stock Moves',
        readonly=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('done', 'Done'),
        ], 'State', readonly=True)
    care_location = fields.Many2One('stock.location', 'Care Location',
        required=True)

    @classmethod
    def __setup__(cls):
        super(PatientAmbulatoryCare, cls).__setup__()
        cls._transitions |= set((
            ('draft', 'done'),
        ))
        cls._buttons.update({
            'done': {
                'invisible': ~Eval('state').in_(['draft']),
            }})

    @staticmethod
    def default_state():
        return 'draft'

    @classmethod
    @ModelView.button
    @Workflow.transition('done')
    def done(cls, ambulatory_cares):
        pool = Pool()
        Patient = pool.get('gnuhealth.patient')
        Vaccination = pool.get('gnuhealth.vaccination')

        lines_to_ship = {}
        medicaments_to_ship = []
        supplies_to_ship = []
        vaccines_to_ship = []

        for ambulatory in ambulatory_cares:
            patient = Patient(ambulatory.patient.id)
            for medicament in ambulatory.medication_line:
                medicaments_to_ship.append(medicament)

            for medical_supply in ambulatory.medical_supply_line:
                supplies_to_ship.append(medical_supply)

            for vaccine in ambulatory.vaccine_line:
                if vaccine.lot:
                    if vaccine.lot.number:
                        lot_number = vaccine.lot.number
                    if vaccine.lot.due_date:
                        due_date = vaccine.lot.due_date
                else:
                    lot_number = ''
                    due_date = ''
                vaccination_data = {
                    'name': patient.id,
                    'vaccine': vaccine.vaccine.id,
                    'vaccine_lot': lot_number,
                    'institution': Transaction().context.get('company')
                        or None,
                    'date': datetime.now(),
                    'dose': vaccine.dose,
                    'next_dose_date': vaccine.next_dose_date,
                    'vaccine_expiration_date': due_date
                    }
                Vaccination.create(vaccination_data)
                vaccines_to_ship.append(vaccine)

        lines_to_ship['medicaments'] = medicaments_to_ship
        lines_to_ship['supplies'] = supplies_to_ship
        lines_to_ship['vaccines'] = vaccines_to_ship

        cls.create_stock_moves(ambulatory_cares, lines_to_ship)

    @classmethod
    def create_stock_moves(cls, ambulatory_cares, lines):
        pool = Pool()
        Move = pool.get('stock.move')
        Date = pool.get('ir.date')
        for ambulatory in ambulatory_cares:
            for medicament in lines['medicaments']:
                move_info = {}
                move_info['product'] = medicament.medicament.name.id
                move_info['uom'] = medicament.medicament.name.default_uom.id
                move_info['quantity'] = medicament.quantity
                move_info['from_location'] = ambulatory.care_location.id
                move_info['to_location'] = \
                    ambulatory.patient.name.customer_location.id
                move_info['unit_price'] = 1
                move_info['ambulatory_care'] = ambulatory.id
                if medicament.lot:
                    if  medicament.lot.due_date \
                    and medicament.lot.due_date < Date.today():
                        raise UserError('Expired medicaments')
                    move_info['lot'] = medicament.lot.id

                new_move = Move.create(move_info)
                Move.write([new_move], {
                    'state': 'done',
                    'effective_date': Date.today(),
                })

            for medical_supply in lines['supplies']:
                move_info = {}
                move_info['product'] = medical_supply.product.id
                move_info['uom'] = medical_supply.product.default_uom.id
                move_info['quantity'] = medical_supply.quantity
                move_info['from_location'] = ambulatory.care_location.id
                move_info['to_location'] = \
                    ambulatory.patient.name.customer_location.id
                move_info['unit_price'] = 1
                move_info['ambulatory_care'] = ambulatory.id
                if medical_supply.lot:
                    if  medical_supply.lot.due_date \
                    and medical_supply.lot.due_date < Date.today():
                        raise UserError('Expired supplies')
                    move_info['lot'] = medical_supply.lot.id

                new_move = Move.create(move_info)
                Move.write([new_move], {
                    'state': 'done',
                    'effective_date': Date.today(),
                })

            for vaccine in lines['vaccines']:
                move_info = {}
                move_info['product'] = vaccine.vaccine.id
                move_info['uom'] = vaccine.vaccine.default_uom.id
                move_info['quantity'] = vaccine.quantity
                move_info['from_location'] = ambulatory.care_location.id
                move_info['to_location'] = \
                    ambulatory.patient.name.customer_location.id
                move_info['unit_price'] = 1
                move_info['ambulatory_care'] = ambulatory.id
                if vaccine.lot:
                    if  vaccine.lot.due_date \
                    and vaccine.lot.due_date < Date.today():
                        raise UserError('Expired vaccines')
                    move_info['lot'] = vaccine.lot.id
                new_move = Move.create(move_info)
                Move.write([new_move], {
                    'state': 'done',
                    'effective_date': Date.today(),
                })

        return True


class PatientAmbulatoryCareLineMedicament(ModelSQL, ModelView):
    'Patient Ambulatory Care Line'
    __name__ = 'gnuhealth.patient.ambulatory_care.line.medicament'

    name = fields.Many2One('gnuhealth.patient.ambulatory_care',
        'Ambulatory ID')
    medicament = fields.Many2One('gnuhealth.medicament', 'Medicament',
        required=True, on_change=['medicament', 'product'])
    product = fields.Many2One('product.product', 'Product')
    quantity = fields.Integer('Quantity')
    short_comment = fields.Char('Comment',
        help='Short comment on the specific drug')
    lot = fields.Many2One('stock.lot', 'Lot',
        domain=[('product', '=', Eval('product'))])

    @staticmethod
    def default_quantity():
        return 1

    def on_change_medicament(self):
        res = {}
        if self.medicament:
            res = {'product': self.medicament.name.id}
        else:
            res = {'product': None}
        return res


class PatientAmbulatoryCareLineSupply(ModelSQL, ModelView):
    'Patient Ambulatory Care Line Medical Supply'
    __name__ = 'gnuhealth.patient.ambulatory_care.line.supply'

    name = fields.Many2One('gnuhealth.patient.ambulatory_care',
        'Ambulatory ID')
    product = fields.Many2One('product.product', 'Medical Supply',
        domain=[('is_medical_supply', '=', True)], required=True)
    quantity = fields.Integer('Quantity')
    short_comment = fields.Char('Comment',
        help='Short comment on the specific drug')
    lot = fields.Many2One('stock.lot', 'Lot',
        domain=[
            ('product', '=', Eval('product')),
            ])

    @staticmethod
    def default_quantity():
        return 1


class PatientAmbulatoryCareLineVaccine(ModelSQL, ModelView):
    'Patient Ambulatory Care Line Vaccine'
    __name__ = 'gnuhealth.patient.ambulatory_care.line.vaccine'

    name = fields.Many2One('gnuhealth.patient.ambulatory_care',
        'Ambulatory ID')
    vaccine = fields.Many2One('product.product', 'Name', required=True,
        domain=[('is_vaccine', '=', True)])
    quantity = fields.Integer('Quantity')
    dose = fields.Integer('Dose')
    next_dose_date = fields.DateTime('Next Dose', required=True)
    short_comment = fields.Char('Comment',
        help='Short comment on the specific drug')
    lot = fields.Many2One('stock.lot', 'Lot',
        domain=[
            ('product', '=', Eval('vaccine')),
            ])

    @staticmethod
    def default_quantity():
        return 1


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
