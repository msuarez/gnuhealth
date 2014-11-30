# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2008-2014 Luis Falcon <falcon@gnu.org>
#    Copyright (C) 2011-2014 GNU Solidario <health@gnusolidario.org>
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
from trytond.model import ModelView, fields
from trytond.transaction import Transaction
from trytond.pool import Pool

__all__ = ['CheckImmunizationStatusInit','CheckImmunizationStatus']

class CheckImmunizationStatusInit(ModelView):
    'Check Immunization Status Init'
    __name__ = 'gnuhealth.check_immunization_status.init'
    immunization_schedule = \
        fields.Many2One("gnuhealth.immunization_schedule","Schedule",
        required=True)

class CheckImmunizationStatus(Wizard):
    'Check Immunization Status'
    __name__ = 'gnuhealth.check_immunization_status'

    start = StateView('gnuhealth.check_immunization_status.init',
            'health.view_check_immunization_status', [
            Button('Cancel', 'end', 'tryton-cancel'),
            Button('Check Immunization Status', 'check_immunization_status',
                'tryton-ok', True),
            ])
    check_immunization_status = StateTransition()

    def transition_check_immunization_status(self):
       
        immunization_schedule =  self.start.immunization_schedule
        
        return 'end'
