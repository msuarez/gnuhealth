# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2008-2017 Luis Falcon <lfalcon@gnusolidario.org>
#    Copyright (C) 2011-2017 GNU Solidario <health@gnusolidario.org>
#
#    Copyright (C) 2013  Sebastian Marro <smarro@gnusolidario.org>
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

from trytond.wizard import Wizard, StateView, Button, StateTransition
from trytond.model import ModelView
from trytond.transaction import Transaction
from trytond.pool import Pool

__all__ = ['CreatePrescriptionStockMoveInit','CreatePrescriptionStockMove']

class CreatePrescriptionStockMoveInit(ModelView):
    'Create Prescription Stock Move Init'
    __name__ = 'gnuhealth.prescription.stock.move.init'


class CreatePrescriptionStockMove(Wizard):
    'Create Prescription Stock Move'
    __name__ = 'gnuhealth.prescription.stock.move.create'

    start = StateView('gnuhealth.prescription.stock.move.init',
            'health_stock.view_create_prescription_stock_move', [
            Button('Cancel', 'end', 'tryton-cancel'),
            Button('Create Stock Move', 'create_stock_move',
                'tryton-ok', True),
            ])
    create_stock_move = StateTransition()

    def transition_create_stock_move(self):
        pool = Pool()
        StockMove = pool.get('stock.move')
        Prescription = pool.get('gnuhealth.prescription.order')

        moves = []
        prescriptions = Prescription.browse(Transaction().context.get(
            'active_ids'))
        for prescription in prescriptions:

            if prescription.moves:
                self.raise_user_error('stock_move_exists')

            if not prescription.pharmacy:
                self.raise_user_error('no_pharmacy_selected')

            from_location = prescription.pharmacy.warehouse
            if from_location.type == 'warehouse':
                from_location = from_location.storage_location
            to_location = prescription.patient.name.customer_location

            for line in prescription.prescription_line:
                move = StockMove()
                move.origin = prescription
                move.from_location = from_location
                move.to_location = to_location
                move.product = line.medicament.name
                move.unit_price = line.medicament.name.list_price
                move.quantity = line.quantity
                move.uom = line.medicament.name.default_uom
                moves.append(move)
        StockMove.save(moves)
        StockMove.do(moves)
        return 'end'

    @classmethod
    def __setup__(cls):
        super(CreatePrescriptionStockMove, cls).__setup__()
        cls._error_messages.update({
            'stock_move_exists':
                'Stock moves already exists!.',
            'no_pharmacy_selected':
                'You need to select a pharmacy.',
            })

