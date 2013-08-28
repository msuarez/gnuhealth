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


__all__ = ['Physician', 'Appointment']


class Physician(ModelSQL, ModelView):
    "Add Calendar to Physician"
    __name__ = "gnuhealth.physician"

    calendar = fields.Many2One('calendar.calendar', 'Calendar')


class Appointment(ModelSQL, ModelView):
    'Add Calendar to the Appointment'
    __name__ = 'gnuhealth.appointment'

    event = fields.Many2One(
        'calendar.event', 'Calendar Event', readonly=True,
        help="Calendar Event")
    appointment_time = fields.Integer(
        'Appointment Time',
        help='Appointment Time (Minutes)')

    @staticmethod
    def default_appointment_time():
        return 30

    @classmethod
    def create(cls, vlist):
        Event = Pool().get('calendar.event')
        Patient = Pool().get('gnuhealth.patient')
        Physician = Pool().get('gnuhealth.physician')

        vlist = [x.copy() for x in vlist]
        for values in vlist:
            if values['doctor']:
                doctor = Physician(values['doctor'])
                if doctor.calendar:
                    patient = Patient(values['patient'])
                    events = Event.create([{
                        'dtstart': values['appointment_date'],
                        'dtend': values['appointment_date'] +
                        timedelta(minutes=values['appointment_time']),
                        'calendar': doctor.calendar.id,
                        'summary': patient.name.lastname + ', ' +
                        patient.name.name,
                        }])
                    values['event'] = events[0].id
        return super(Appointment, cls).create(vlist)

    @classmethod
    def write(cls, appointments, values):
        Event = Pool().get('calendar.event')
        Patient = Pool().get('gnuhealth.patient')
        Physician = Pool().get('gnuhealth.physician')

        for appointment in appointments:
            if appointment.event:
                if 'appointment_date' in values:
                    Event.write([appointment.event], {
                        'dtstart': values['appointment_date'],
                        'dtend': values['appointment_date'] +
                        timedelta(minutes=appointment.appointment_time),
                        })
                if 'appointment_time' in values:
                    Event.write([appointment.event], {
                        'dtend': appointment.appointment_date +
                        timedelta(minutes=values['appointment_time']),
                        })
                if 'doctor' in values:
                    doctor = Physician(values['doctor'])
                    Event.write([appointment.event], {
                        'calendar': doctor.calendar.id,
                        })
                if 'patient' in values:
                    patient = Patient(values['patient'])
                    Event.write([appointment.event], {
                        'summary': patient.name.name,
                        })
        return super(Appointment, cls).write(appointments, values)

    @classmethod
    def delete(cls, appointments):
        Event = Pool().get('calendar.event')

        for appointment in appointments:
            if appointment.event:
                Event.delete([appointment.event])
        return super(Appointment, cls).delete(appointments)
