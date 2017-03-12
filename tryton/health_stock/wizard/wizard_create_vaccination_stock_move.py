# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2008-2017 Luis Falcon <falcon@gnu.org>
#    Copyright (C) 2011-2017 GNU Solidario <health@gnusolidario.org>
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

__all__ = ['CreateVaccinationStockMoveInit','CreateVaccinationStockMove']

class CreateVaccinationStockMoveInit(ModelView):
    'Create Vaccination Stock Move Init'
    __name__ = 'gnuhealth.vaccination.stock.move.init'


class CreateVaccinationStockMove(Wizard):
    'Create Vaccination Stock Move'
    __name__ = 'gnuhealth.vaccination.stock.move.create'

    start = StateView('gnuhealth.vaccination.stock.move.init',
            'health_stock.view_create_vaccination_stock_move', [
            Button('Cancel', 'end', 'tryton-cancel'),
            Button('Create Stock Move', 'create_stock_move',
                'tryton-ok', True),
            ])
    create_stock_move = StateTransition()

    def transition_create_stock_move(self):
        pool = Pool()
        StockMove = pool.get('stock.move')
        Vaccination = pool.get('gnuhealth.vaccination')

        vaccinations = Vaccination.browse(Transaction().context.get(
            'active_ids'))
        for vaccination in vaccinations:

            if vaccination.moves:
                self.raise_user_error('stock_move_exists')
                 
            lines = []
            
            line_data = {}
            line_data['origin'] = str(vaccination)
            line_data['from_location'] = \
                vaccination.location.id
            line_data['to_location'] = \
                vaccination.name.name.customer_location.id
            line_data['product'] = \
                vaccination.vaccine.name.id
            line_data['unit_price'] = \
                vaccination.vaccine.name.list_price
            line_data['quantity'] = 1
            line_data['uom'] = \
                vaccination.vaccine.name.default_uom.id
            line_data['state'] = 'draft'
            lines.append(line_data)
            
            moves = StockMove.create(lines)

            StockMove.assign(moves)
            StockMove.do(moves)
            
            
        return 'end'

    @classmethod
    def __setup__(cls):
        super(CreateVaccinationStockMove, cls).__setup__()
        cls._error_messages.update({
            'stock_move_exists':
                'Stock moves already exists!.',})

