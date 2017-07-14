# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#                           
#                            CALENDAR PACKAGE
#
#    Copyright (C) 2008-2017  Luis Falcon <lfalcon@gnusolidario.org>
#    Copyright (C) 2011-2017  GNU Solidario <health@gnusolidario.org>
#    Copyright (C) 2011-2014  Sebastián Marró <smarro@thymbra.com>
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
from trytond.model import fields
from trytond.pyson import Eval, Not, Bool
from trytond.pool import Pool, PoolMeta


__all__ = ['User', 'Appointment']


class User(metaclass=PoolMeta):
    __name__ = "res.user"

    use_caldav = fields.Boolean('CalDAV', help="The user has a CalDav account")
    calendar = fields.Many2One('calendar.calendar', 'Calendar',
        states={
            'invisible': Not(Bool(Eval('use_caldav'))),
            'required': Bool(Eval('use_caldav')),
            })


class Appointment(metaclass=PoolMeta):
    __name__ = 'gnuhealth.appointment'

    event = fields.Many2One(
        'calendar.event', 'CalDAV Event', readonly=True,
        help="Calendar Event",
        states={'invisible': Not(Bool(Eval('event')))})
    appointment_date_end = fields.DateTime('End Date and Time')

    @classmethod
    def create(cls, vlist):
        pool = Pool()
        Event = pool.get('calendar.event')
        Patient = pool.get('gnuhealth.patient')
        Healthprof = pool.get('gnuhealth.healthprofessional')

        vlist = [x.copy() for x in vlist]
        for values in vlist:
            if values['state'] == 'confirmed':
                if values['healthprof']:
                    healthprof = Healthprof(values['healthprof'])
                    if (healthprof.name.internal_user and
                            healthprof.name.internal_user.calendar):
                        patient = Patient(values['patient'])
                        appointment_date_end = None
                        if values.get('appointment_date_end'):
                            appointment_date_end = \
                                values['appointment_date_end']
                        events = Event.create([{
                            'dtstart': values['appointment_date'],
                            'dtend': appointment_date_end,
                            'calendar':
                                healthprof.name.internal_user.calendar.id,
                            'summary': patient.name.rec_name,
                            'description': values['comments'],
                            }])
                        values['event'] = events[0].id
        return super(Appointment, cls).create(vlist)

    @classmethod
    def write(cls, appointments, values):
        pool = Pool()
        Event = pool.get('calendar.event')
        Patient = pool.get('gnuhealth.patient')
        Healtprof = pool.get('gnuhealth.healthprofessional')

        for appointment in appointments:
            if values.get('patient'):
                if appointment.event:
                    if 'appointment_date' in values:
                        Event.write([appointment.event], {
                            'dtstart': values['appointment_date'],
                            })
                    if 'appointment_date_end' in values:
                        Event.write([appointment.event], {
                            'dtend': values['appointment_date_end'],
                            })
                    if 'healthprof' in values:
                        healthprof = Healtprof(values['healthprof'])
                        Event.write([appointment.event], {
                            'calendar': healthprof.calendar.id,
                            })
                    if 'patient' in values:
                        patient = Patient(values['patient'])
                        Event.write([appointment.event], {
                            'summary': patient.name.rec_name,
                            })
                else:
                    if appointment.healthprof:
                        if appointment.healthprof.name.internal_user.calendar:
                            patient = Patient(values['patient'])
                            events = Event.create([{
                                'dtstart': appointment.appointment_date,
                                'dtend': appointment.appointment_date_end,
                                'calendar':
                                    appointment.healthprof.name.internal_user.calendar.id,
                                'summary':
                                    patient.name.rec_name,
                                'description': values['comments'],
                                }])
                            values['event'] = events[0].id
        return super(Appointment, cls).write(appointments, values)

    @classmethod
    def delete(cls, appointments):
        Event = Pool().get('calendar.event')

        for appointment in appointments:
            if appointment.event:
                Event.delete([appointment.event])
        return super(Appointment, cls).delete(appointments)
