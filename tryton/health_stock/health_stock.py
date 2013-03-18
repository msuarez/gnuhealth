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
from trytond.pyson import If, Or, Eval, Not, Bool
from trytond.exceptions import UserError
from trytond.transaction import Transaction
from trytond.pool import Pool, PoolMeta

__all__ = ['Medicament', 'Party', 'Lot', 'ShipmentOut', 'Move',
    'PatientAmbulatoryCare', 'PatientAmbulatoryCareMedicament',
    'PatientAmbulatoryCareMedicalSupply', 'PatientAmbulatoryCareVaccine',
    'PatientRounding', 'PatientRoundingMedicament',
    'PatientRoundingMedicalSupply', 'PatientRoundingVaccine',
    'CreatePrescriptionShipmentInit', 'CreatePrescriptionShipment']
__metaclass__ = PoolMeta

_STATES = {
    'readonly': Eval('state') == 'done',
    }
_DEPENDS = ['state']


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


class Lot:
    __name__ = 'stock.lot'
    expiration_date = fields.Date('Expiration Date')
    quantity = fields.Function(fields.Float('Quantity'), 'sum_lot_quantity')

    def sum_lot_quantity(self, name):
        Move = Pool().get('stock.move')

        moves = Move.search([
            ('lot', '=', self.id),
            ('product', '=', self.product.id)
        ])
        quantity = 0
        for move in moves:
            if move.to_location.type == 'storage':
                quantity += move.quantity
            if move.from_location.type == 'storage':
                quantity -= move.quantity
        return quantity


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

    care_location = fields.Many2One('stock.location', 'Care Location',
        states={
            'required': If(Or(Bool(Eval('medicaments')),
                Bool(Eval('medical_supplies')),
                Bool(Eval('vaccines'))), True, False),
            'readonly': Eval('state') == 'done',
        }, depends=['state', 'medicaments'])
    medicaments = fields.One2Many(
        'gnuhealth.patient.ambulatory_care.medicament', 'name',
        'Medicaments', states=_STATES, depends=_DEPENDS)
    medical_supplies = fields.One2Many(
        'gnuhealth.patient.ambulatory_care.medical_supply', 'name',
        'Medical Supplies', states=_STATES, depends=_DEPENDS)
    vaccines = fields.One2Many(
        'gnuhealth.patient.ambulatory_care.vaccine', 'name', 'Vaccines',
        states=_STATES, depends=_DEPENDS)
    moves = fields.One2Many('stock.move', 'ambulatory_care', 'Stock Moves',
        readonly=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('done', 'Done'),
        ], 'State', readonly=True)

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
            for medicament in ambulatory.medicaments:
                medicaments_to_ship.append(medicament)

            for medical_supply in ambulatory.medical_supplies:
                supplies_to_ship.append(medical_supply)

            for vaccine in ambulatory.vaccines:
                lot_number = ''
                expiration_date = ''
                if vaccine.lot:
                    if vaccine.lot.number:
                        lot_number = vaccine.lot.number
                    if vaccine.lot.expiration_date:
                        expiration_date = vaccine.lot.expiration_date
                vaccination_data = {
                    'name': patient.id,
                    'vaccine': vaccine.vaccine.id,
                    'vaccine_lot': lot_number,
                    'institution': Transaction().context.get('company')
                        or None,
                    'date': datetime.now(),
                    'dose': vaccine.dose,
                    'next_dose_date': vaccine.next_dose_date,
                    'vaccine_expiration_date': expiration_date
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
                    if  medicament.lot.expiration_date \
                    and medicament.lot.expiration_date < Date.today():
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
                    if  medical_supply.lot.expiration_date \
                    and medical_supply.lot.expiration_date < Date.today():
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
                    if  vaccine.lot.expiration_date \
                    and vaccine.lot.expiration_date < Date.today():
                        raise UserError('Expired vaccines')
                    move_info['lot'] = vaccine.lot.id
                new_move = Move.create(move_info)
                Move.write([new_move], {
                    'state': 'done',
                    'effective_date': Date.today(),
                })

        return True


class PatientAmbulatoryCareMedicament(ModelSQL, ModelView):
    'Patient Ambulatory Care Medicament'
    __name__ = 'gnuhealth.patient.ambulatory_care.medicament'

    name = fields.Many2One('gnuhealth.patient.ambulatory_care',
        'Ambulatory ID')
    medicament = fields.Many2One('gnuhealth.medicament', 'Medicament',
        required=True, on_change=['medicament', 'product'])
    product = fields.Many2One('product.product', 'Product')
    quantity = fields.Integer('Quantity')
    short_comment = fields.Char('Comment',
        help='Short comment on the specific drug')
    lot = fields.Many2One('stock.lot', 'Lot', depends=['product'],
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


class PatientAmbulatoryCareMedicalSupply(ModelSQL, ModelView):
    'Patient Ambulatory Care Medical Supply'
    __name__ = 'gnuhealth.patient.ambulatory_care.medical_supply'

    name = fields.Many2One('gnuhealth.patient.ambulatory_care',
        'Ambulatory ID')
    product = fields.Many2One('product.product', 'Medical Supply',
        domain=[('is_medical_supply', '=', True)], required=True)
    quantity = fields.Integer('Quantity')
    short_comment = fields.Char('Comment',
        help='Short comment on the specific drug')
    lot = fields.Many2One('stock.lot', 'Lot', depends=['product'],
        domain=[
            ('product', '=', Eval('product')),
            ])

    @staticmethod
    def default_quantity():
        return 1


class PatientAmbulatoryCareVaccine(ModelSQL, ModelView):
    'Patient Ambulatory Care Vaccine'
    __name__ = 'gnuhealth.patient.ambulatory_care.vaccine'

    name = fields.Many2One('gnuhealth.patient.ambulatory_care',
        'Ambulatory ID')
    vaccine = fields.Many2One('product.product', 'Name', required=True,
        domain=[('is_vaccine', '=', True)])
    quantity = fields.Integer('Quantity')
    dose = fields.Integer('Dose')
    next_dose_date = fields.DateTime('Next Dose')
    short_comment = fields.Char('Comment',
        help='Short comment on the specific drug')
    lot = fields.Many2One('stock.lot', 'Lot', depends=['vaccine'],
        domain=[
            ('product', '=', Eval('vaccine')),
            ])

    @staticmethod
    def default_quantity():
        return 1


class PatientRounding(Workflow, ModelSQL, ModelView):
    'Patient Ambulatory Care'
    __name__ = 'gnuhealth.patient.rounding'

    hospitalization_location = fields.Many2One('stock.location',
        'Hospitalization Location',
        states={
            'required': If(Or(Bool(Eval('medicaments')),
                Bool(Eval('medical_supplies')),
                Bool(Eval('vaccines'))), True, False),
            'readonly': Eval('state') == 'done',
        }, depends=_DEPENDS)
    medicaments = fields.One2Many(
        'gnuhealth.patient.rounding.medicament', 'name', 'Medicaments',
        states=_STATES, depends=_DEPENDS)
    medical_supplies = fields.One2Many(
        'gnuhealth.patient.rounding.medical_supply', 'name', 'Medical Supplies',
        states=_STATES, depends=_DEPENDS)
    vaccines = fields.One2Many(
        'gnuhealth.patient.rounding.vaccine', 'name', 'Vaccines',
        states=_STATES, depends=_DEPENDS,)
    moves = fields.One2Many('stock.move', 'rounding', 'Stock Moves',
        readonly=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('done', 'Done'),
        ], 'State', readonly=True)

    @classmethod
    def __setup__(cls):
        super(PatientRounding, cls).__setup__()
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
    def done(cls, roundings):
        pool = Pool()
        Patient = pool.get('gnuhealth.patient')
        Vaccination = pool.get('gnuhealth.vaccination')

        lines_to_ship = {}
        medicaments_to_ship = []
        supplies_to_ship = []
        vaccines_to_ship = []

        for rounding in roundings:
            patient = Patient(rounding.name.patient.id)

            for medicament in rounding.medicaments:
                medicaments_to_ship.append(medicament)

            for medical_supply in rounding.medical_supplies:
                supplies_to_ship.append(medical_supply)

            for vaccine in rounding.vaccines:
                lot_number = ''
                expiration_date = ''
                if vaccine.lot:
                    if vaccine.lot.number:
                        lot_number = vaccine.lot.number
                    if vaccine.lot.expiration_date:
                        expiration_date = vaccine.lot.expiration_date
                vaccination_data = {
                    'name': patient.id,
                    'vaccine': vaccine.vaccine.id,
                    'vaccine_lot': lot_number,
                    'institution': Transaction().context.get('company')
                        or None,
                    'date': datetime.now(),
                    'dose': vaccine.dose,
                    'next_dose_date': vaccine.next_dose_date,
                    'vaccine_expiration_date': expiration_date
                    }
                Vaccination.create(vaccination_data)
                vaccines_to_ship.append(vaccine)


        lines_to_ship['medicaments'] = medicaments_to_ship
        lines_to_ship['supplies'] = supplies_to_ship
        lines_to_ship['vaccines'] = vaccines_to_ship

        cls.create_stock_moves(roundings, lines_to_ship)

    @classmethod
    def create_stock_moves(cls, roundings, lines):
        pool = Pool()
        Move = pool.get('stock.move')
        Date = pool.get('ir.date')
        for rounding in roundings:
            for medicament in lines['medicaments']:
                move_info = {}
                move_info['product'] = medicament.medicament.name.id
                move_info['uom'] = medicament.medicament.name.default_uom.id
                move_info['quantity'] = medicament.quantity
                move_info['from_location'] = \
                    rounding.hospitalization_location.id
                move_info['to_location'] = \
                rounding.name.patient.name.customer_location.id
                move_info['unit_price'] = 1
                move_info['rounding'] = rounding.id
                if medicament.lot:
                    if  medicament.lot.expiration_date \
                    and medicament.lot.expiration_date < Date.today():
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
                    move_info['from_location'] = \
                        rounding.hospitalization_location.id
                    move_info['to_location'] = \
                    rounding.name.patient.name.customer_location.id
                    move_info['unit_price'] = 1
                    move_info['rounding'] = rounding.id
                    if medical_supply.lot:
                        if  medical_supply.lot.expiration_date \
                        and medical_supply.lot.expiration_date < Date.today():
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
                move_info['from_location'] = \
                    rounding.hospitalization_location.id
                move_info['to_location'] = \
                rounding.name.patient.name.customer_location.id
                move_info['unit_price'] = 1
                move_info['rounding'] = rounding.id
                if vaccine.lot:
                    if  vaccine.lot.expiration_date \
                    and vaccine.lot.expiration_date < Date.today():
                        raise UserError('Expired vaccines')
                    move_info['lot'] = vaccine.lot.id
                new_move = Move.create(move_info)
                Move.write([new_move], {
                    'state': 'done',
                    'effective_date': Date.today(),
                })

        return True


class PatientRoundingMedicament(ModelSQL, ModelView):
    'Patient Rounding Medicament'
    __name__ = 'gnuhealth.patient.rounding.medicament'

    name = fields.Many2One('gnuhealth.patient.rounding', 'Ambulatory ID')
    medicament = fields.Many2One('gnuhealth.medicament', 'Medicament',
        required=True, on_change=['medicament', 'product'])
    product = fields.Many2One('product.product', 'Product')
    quantity = fields.Integer('Quantity')
    short_comment = fields.Char('Comment',
        help='Short comment on the specific drug')
    lot = fields.Many2One('stock.lot', 'Lot', depends=['product'],
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


class PatientRoundingMedicalSupply(ModelSQL, ModelView):
    'Patient Rounding Medical Supply'
    __name__ = 'gnuhealth.patient.rounding.medical_supply'

    name = fields.Many2One('gnuhealth.patient.rounding', 'Ambulatory ID')
    product = fields.Many2One('product.product', 'Medical Supply',
        domain=[('is_medical_supply', '=', True)], required=True)
    quantity = fields.Integer('Quantity')
    short_comment = fields.Char('Comment',
        help='Short comment on the specific drug')
    lot = fields.Many2One('stock.lot', 'Lot', depends=['product'],
        domain=[
            ('product', '=', Eval('product')),
            ])

    @staticmethod
    def default_quantity():
        return 1


class PatientRoundingVaccine(ModelSQL, ModelView):
    'Patient Ambulatory Care Vaccine'
    __name__ = 'gnuhealth.patient.rounding.vaccine'

    name = fields.Many2One('gnuhealth.patient.rounding', 'Rounding ID')
    vaccine = fields.Many2One('product.product', 'Name', required=True,
        domain=[('is_vaccine', '=', True)])
    quantity = fields.Integer('Quantity')
    dose = fields.Integer('Dose')
    next_dose_date = fields.DateTime('Next Dose')
    short_comment = fields.Char('Comment',
        help='Short comment on the specific drug')
    lot = fields.Many2One('stock.lot', 'Lot', depends=['vaccine'],
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


