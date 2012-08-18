# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2011-2012  Sebastián Marró <smarro@thymbra.com>
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
from datetime import timedelta

from trytond.model import ModelView, ModelSQL, fields
from trytond.pool import Pool


class Physician(ModelSQL, ModelView):
    "Add Calendar to Physician"
    _name = "gnuhealth.physician"
    _description = __doc__

    calendar = fields.Many2One('calendar.calendar', 'Calendar')

Physician()


class Appointment(ModelSQL, ModelView):
    'Add Calendar to the Appointment'
    _name = 'gnuhealth.appointment'
    _description = __doc__

    event = fields.Many2One('calendar.event', 'Calendar Event', readonly=True,
        help="Calendar Event")
    appointment_time = fields.Integer('Appointment Time',
        help='Appointment Time (Minutes)')

    def default_appointment_time(self):
        return 30

    def create(self, values):
        event_obj = Pool().get('calendar.event')
        patient_obj = Pool().get('gnuhealth.patient')
        physician_obj = Pool().get('gnuhealth.physician')

        if values['doctor']:
            doctor = physician_obj.browse(values['doctor'])
            if doctor.calendar:
                patient = patient_obj.browse(values['patient'])
                values['event'] = event_obj.create({
                    'dtstart': values['appointment_date'],
                    'dtend': values['appointment_date'] +
                        timedelta(minutes=values['appointment_time']),
                    'calendar': doctor.calendar.id,
                    'summary': patient.name.lastname + ', ' + patient.name.name,
                    })
        return super(Appointment, self).create(values)

    def write(self, ids, values):
        event_obj = Pool().get('calendar.event')
        patient_obj = Pool().get('gnuhealth.patient')
        physician_obj = Pool().get('gnuhealth.physician')

        if isinstance(ids, (int, long)):
            ids = [ids]
        for appointment_id in ids:
            appointment = self.browse(appointment_id)
            if appointment.event:
                if 'appointment_date' in values:
                    event_obj.write(appointment.event.id, {
                        'dtstart': values['appointment_date'],
                        'dtend': values['appointment_date'] +
                            timedelta(minutes=appointment.appointment_time),
                        })
                if 'appointment_time' in values:
                    event_obj.write(appointment.event.id, {
                        'dtend': appointment.appointment_date +
                            timedelta(minutes=values['appointment_time']),
                        })
                if 'doctor' in values:
                    doctor = physician_obj.browse(values['doctor'])
                    event_obj.write(appointment.event.id, {
                        'calendar': doctor.calendar.id,
                        })
                if 'patient' in values:
                    patient = patient_obj.browse(values['patient'])
                    event_obj.write(appointment.event.id, {
                        'summary': patient.name.name,
                        })
        return super(Appointment, self).write(ids, values)

    def delete(self, ids):
        event_obj = Pool().get('calendar.event')

        if isinstance(ids, (int, long)):
            ids = [ids]
        for appointment_id in ids:
            appointment = self.browse(appointment_id)
            if appointment.event:
                event_obj.delete(appointment.event.id)
        return super(Appointment, self).delete(ids)

Appointment()
