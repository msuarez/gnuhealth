# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2008-2017 Luis Falcon <falcon@gnu.org>
#    Copyright (C) 2011-2017 GNU Solidario <health@gnusolidario.org>
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

from trytond.wizard import Wizard, StateView, Button, StateAction
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
            Button('Immunization Status', 'check_immunization_status',
                'tryton-ok', True),
            ])
    check_immunization_status = StateAction('health.report_immunization_status')

    def do_check_immunization_status(self, action):
        return action, self.get_info()
        
    def get_info(self):
    
        return {
            'patient_id': Transaction().context.get('active_id'),
            'immunization_schedule_id': self.start.immunization_schedule.id
            }

    def transition_check_immunization_status(self):
        return 'end'
