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


from trytond.model import ModelView, ModelSingleton, ModelSQL, fields
from trytond.transaction import Transaction
from trytond.pool import Pool


class InpatientSequences(ModelSingleton, ModelSQL, ModelView):
    "Inpatient Registration Sequences for GNU Health"

    _name = "gnuhealth.sequences"

    inpatient_registration_sequence = fields.Property(fields.Many2One('ir.sequence',
        'Inpatient Sequence', domain=[('code', '=', 'gnuhealth.inpatient.registration')],
        required=True))

InpatientSequences()


class InpatientRegistration(ModelSQL, ModelView):
    'Patient admission History'
    _name = 'gnuhealth.inpatient.registration'
    _description = __doc__

    name = fields.Char('Registration Code', readonly=True, select=True)
    patient = fields.Many2One('gnuhealth.patient', 'Patient',
     required=True, select=True)
    admission_type = fields.Selection([
        ('routine', 'Routine'),
        ('maternity', 'Maternity'),
        ('elective', 'Elective'),
        ('urgent', 'Urgent'),
        ('emergency', 'Emergency'),
        ], 'Admission type', required=True, select=True)
    hospitalization_date = fields.DateTime('Hospitalization date',
        required=True, select=True)
    discharge_date = fields.DateTime('Discharge date', required=True,
     select=True)
    attending_physician = fields.Many2One('gnuhealth.physician',
        'Attending Physician',select=True)
    operating_physician = fields.Many2One('gnuhealth.physician',
        'Operating Physician')
    admission_reason = fields.Many2One('gnuhealth.pathology',
        'Reason for Admission', help="Reason for Admission", select=True)
    bed = fields.Many2One('gnuhealth.hospital.bed', 'Hospital Bed',
     required=True, select=True)
    nursing_plan = fields.Text('Nursing Plan')
    discharge_plan = fields.Text('Discharge Plan')

    info = fields.Text('Extra Info')
    state = fields.Selection((
        ('free', 'free'),
        ('cancelled', 'cancelled'),
        ('confirmed', 'confirmed'),
        ('hospitalized', 'hospitalized'),
        ), 'Status', select=True)

# Method to check for availability and make the hospital bed reservation

    def button_registration_confirm(self, ids):
        cursor = Transaction().cursor

        for reservation in self.browse(ids):
            bed_id = str(reservation.bed.id)

            cursor.execute("SELECT COUNT(*) \
                FROM gnuhealth_inpatient_registration \
                WHERE (hospitalization_date::timestamp,discharge_date::timestamp) \
                    OVERLAPS (timestamp %s, timestamp %s) \
                  AND state = %s \
                  AND bed = CAST(%s AS INTEGER) ",
                (reservation.hospitalization_date, reservation.discharge_date,
                'confirmed', bed_id))

            res = cursor.fetchone()

        if res[0] > 0:
            self.raise_user_error('bed_is_not_available')
        else:
            self.write(ids, {'state': 'confirmed'})

        return True

    def button_patient_discharge(self, ids):
        self.write(ids, {'state': 'free'})
        return True

    def button_registration_cancel(self, ids):
        self.write(ids, {'state': 'cancelled'})
        return True

    def button_registration_admission(self, ids):
        self.write(ids, {'state': 'hospitalized'})
        return True

    def create(self, values):
        sequence_obj = Pool().get('ir.sequence')
        config_obj = Pool().get('gnuhealth.sequences')

        values = values.copy()
        if not values.get('name'):
            config = config_obj.browse(1)
            values['name'] = sequence_obj.get_id(
            config.inpatient_registration_sequence.id)

        return super(InpatientRegistration, self).create(values)

    def default_state(self):
        return 'free'

    def __init__(self):
        super(InpatientRegistration, self).__init__()

        self._rpc.update({
            'button_registration_confirm': True,
            'button_patient_discharge': True,
            'button_registration_cancel': True,
            'button_registration_admission': True,
        })

        self._sql_constraints = [
            ('name_uniq', 'unique(name)',
             'The Registration code already exists')
        ]

        self._error_messages.update({
                'bed_is_not_available': 'Bed is not available'})

InpatientRegistration()


class Appointment(ModelSQL, ModelView):
    'Add Inpatient Registration field to the Appointment model.'
    _name = 'gnuhealth.appointment'
    _description = __doc__

    inpatient_registration_code = fields.Many2One(
        'gnuhealth.inpatient.registration', 'Inpatient Registration',
        help="Enter the patient hospitalization code")

Appointment()


class PatientData(ModelSQL, ModelView):
    'Inherit patient model and add the patient status to the patient.'
    _name = 'gnuhealth.patient'
    _description = __doc__

    def get_patient_status(self, ids, name):
        cursor = Transaction().cursor

        def get_hospitalization_status(patient_dbid):
            cursor.execute('SELECT state ' \
                'FROM gnuhealth_inpatient_registration ' \
                'WHERE patient = %s ' \
                  'AND state = \'hospitalized\' ', (str(patient_dbid),))

            try:
                patient_status = str(cursor.fetchone()[0])
            except:
                patient_status = 'outpatient'

            return patient_status

        result = {}

# Get the patient (DB) id to be used in the search on the medical inpatient
# registration table lookup

        for patient_data in self.browse(ids):
            patient_dbid = patient_data.id

            if patient_dbid:
                result[patient_data.id] = \
                        get_hospitalization_status(patient_dbid)

        return result

    patient_status = fields.Function(fields.Char('Hospitalization Status'),
        'get_patient_status')

PatientData()
