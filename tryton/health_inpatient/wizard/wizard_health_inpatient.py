# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2008-2017 Luis Falcon <lfalcon@gnusolidario.org>
#    Copyright (C) 2011-2017 GNU Solidario <health@gnusolidario.org>
#
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
from datetime import datetime
from trytond.model import ModelView, fields
from trytond.wizard import Wizard, StateTransition, StateView, Button
from trytond.transaction import Transaction
from trytond.pool import Pool


__all__ = ['CreateBedTransferInit', 'CreateBedTransfer']


class CreateBedTransferInit(ModelView):
    'Create Bed Transfer Init'
    __name__ = 'gnuhealth.bed.transfer.init'
    newbed = fields.Many2One('gnuhealth.hospital.bed', 'New Bed',
        required=True, select=True)
    reason = fields.Char('Reason', required=True)

    orig_bed_state = fields.Selection((
        (None,''),
        ('free', 'Free'),
        ('reserved', 'Reserved'),
        ('occupied', 'Occupied'),
        ('to_clean', 'Needs cleaning'),
        ('na', 'Not available'),
        ), 'Bed of origin Status', sort=False, required=True)

    @staticmethod
    def default_orig_bed_state():
        return 'to_clean'

class CreateBedTransfer(Wizard):
    'Create Bed Transfer'
    __name__ = 'gnuhealth.bed.transfer.create'


    start = StateView('gnuhealth.bed.transfer.init',
        'health_inpatient.view_patient_bed_transfer', [
            Button('Cancel', 'end', 'tryton-cancel'),
            Button('Transfer Patient', 'create_bed_transfer', 'tryton-ok',
                True),
            ])
    create_bed_transfer = StateTransition()


    @classmethod
    def __setup__(cls):
        super(CreateBedTransfer, cls).__setup__()
        cls._error_messages.update({
            'bed_unavailable': 'Destination bed is unavailable',
            'choose_one': 'You have chosen more than 1 records. Please choose only one'})

    def transition_create_bed_transfer(self):
        inpatient_registrations = Pool().get('gnuhealth.inpatient.registration')
        bed = Pool().get('gnuhealth.hospital.bed')

        registrations = inpatient_registrations.browse(Transaction().context.get(
            'active_ids'))

        # Don't allow mass changes. Work on a single record
        if len(registrations) > 1 :
            self.raise_user_error('choose_one')

        registration = registrations[0]
        current_bed = registration.bed
        destination_bed = self.start.newbed
        reason = self.start.reason
        orig_bed_state = self.start.orig_bed_state


        # Check that the new bed is free
        if (destination_bed.state == 'free'):

            # Update bed status with the one given in the transfer
            bed.write([current_bed], {'state': orig_bed_state})

            # Set as occupied the new bed
            bed.write([destination_bed], {'state': 'occupied'})
            # Update the hospitalization record
            hospitalization_info = {}

            hospitalization_info['bed'] = destination_bed

            # Update the hospitalization data
            transfers = []
            transfers.append(('create', [{
                            'transfer_date' : datetime.now(),
                            'bed_from' : current_bed,
                            'bed_to' : destination_bed,
                            'reason': reason,
                        }]))
            hospitalization_info['bed_transfers'] = transfers

            inpatient_registrations.write([registration],hospitalization_info)



        else:
            self.raise_user_error('bed_unavailable')

        return 'end'

