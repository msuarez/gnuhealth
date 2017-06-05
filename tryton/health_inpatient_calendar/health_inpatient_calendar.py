# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    # Package : Health Inpatient Calendar
#    Copyright (C) 2008-2017  Luis Falcon <falcon@gnu.org>
#    Copyright (C) 2011-2012  Sebastián Marró <smarro@thymbra.com>
#    Copyright (C) 2011-2017  GNU Solidario <health@gnusolidario.org>
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
from trytond.model import ModelView, ModelSQL, fields
from trytond.pool import Pool


__all__ = ['HospitalBed', 'InpatientRegistration']


class HospitalBed(ModelSQL, ModelView):
    "Add Calendar to Hospital Bed"
    __name__ = "gnuhealth.hospital.bed"

    calendar = fields.Many2One('calendar.calendar', 'Calendar')


class InpatientRegistration(ModelSQL, ModelView):
    'Add Calendar to the Inpatient Registration'
    __name__ = 'gnuhealth.inpatient.registration'

    event = fields.Many2One('calendar.event', 'Calendar Event', readonly=True,
        help="Calendar Event")

    @classmethod
    def confirmed(cls, registrations):
        super(InpatientRegistration, cls).confirmed(registrations)

        Event = Pool().get('calendar.event')

        for inpatient_registration in registrations:
            if inpatient_registration.bed.calendar:
                if not inpatient_registration.event:
                    bed = inpatient_registration.bed.name.code + ": "
                    events = Event.create([{
                        'dtstart': inpatient_registration.hospitalization_date,
                        'dtend': inpatient_registration.discharge_date,
                        'calendar': inpatient_registration.bed.calendar.id,
                        'summary': bed + inpatient_registration.patient.name.rec_name
                        }])
                    cls.write([inpatient_registration],
                        {'event': events[0].id})

    @classmethod
    def discharge(cls, registrations):
        super(InpatientRegistration, cls).discharge(registrations)

        Event = Pool().get('calendar.event')

        for inpatient_registration in registrations:
            if inpatient_registration.event:
                Event.delete([inpatient_registration.event])

    @classmethod
    def write(cls, registrations, values):
        Event = Pool().get('calendar.event')
        Patient = Pool().get('gnuhealth.patient')
        HospitalBed = Pool().get('gnuhealth.hospital.bed')

        for inpatient_registration in registrations:
            if inpatient_registration.event:
                if 'hospitalization_date' in values:
                    Event.write([inpatient_registration.event], {
                        'dtstart': values['hospitalization_date'],
                        })
                if 'discharge_date' in values:
                    Event.write([inpatient_registration.event], {
                        'dtend': values['discharge_date'],
                        })
                if 'bed' in values:
                    bed = HospitalBed(values['bed'])
                    Event.write([inpatient_registration.event], {
                        'calendar': bed.calendar.id,
                        })
                if 'patient' in values:
                    patient = Patient(values['patient'])
                    bed = inpatient_registration.bed.name.code + ": "
                    Event.write([inpatient_registration.event], {
                        'summary': bed + patient.name.rec_name,
                        })

        return super(InpatientRegistration, cls).write(registrations, values)

    @classmethod
    def delete(cls, registrations):
        Event = Pool().get('calendar.event')

        for inpatient_registration in registrations:
            if inpatient_registration.event:
                Event.delete([inpatient_registration.event])
        return super(InpatientRegistration, cls).delete(registrations)
