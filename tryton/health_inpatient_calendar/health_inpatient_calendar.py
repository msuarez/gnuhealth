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
from trytond.model import ModelView, ModelSQL, fields
from trytond.pool import Pool


class HospitalBed(ModelSQL, ModelView):
    "Add Calendar to Hospital Bed"
    _name = "gnuhealth.hospital.bed"
    _description = __doc__

    calendar = fields.Many2One('calendar.calendar', 'Calendar')

HospitalBed()


class InpatientRegistration(ModelSQL, ModelView):
    'Add Calendar to the Inpatient Registration'
    _name = 'gnuhealth.inpatient.registration'
    _description = __doc__

    event = fields.Many2One('calendar.event', 'Calendar Event', readonly=True,
        help="Calendar Event")

    def button_registration_confirm(self, ids):
        super(InpatientRegistration, self).button_registration_confirm(ids)

        event_obj = Pool().get('calendar.event')

        for inpatient_registration_id in ids:
            inpatient_registration = self.browse(inpatient_registration_id)
            if inpatient_registration.bed.calendar:
                if not inpatient_registration.event:
                    event_id = event_obj.create({
                        'dtstart': inpatient_registration.hospitalization_date,
                        'dtend': inpatient_registration.discharge_date,
                        'calendar': inpatient_registration.bed.calendar.id,
                        'summary': inpatient_registration.patient.name.name
                        })
                    self.write(inpatient_registration_id, {'event': event_id})

        return True

    def button_patient_discharge(self, ids):
        super(InpatientRegistration, self).button_patient_discharge(ids)

        event_obj = Pool().get('calendar.event')

        for inpatient_registration_id in ids:
            inpatient_registration = self.browse(inpatient_registration_id)
            if inpatient_registration.event:
                event_obj.delete(inpatient_registration.event.id)

        return True

    def write(self, ids, values):
        event_obj = Pool().get('calendar.event')
        patient_obj = Pool().get('gnuhealth.patient')
        hospital_bed_obj = Pool().get('gnuhealth.hospital.bed')

        if isinstance(ids, (int, long)):
            ids = [ids]
        for inpatient_registration_id in ids:
            inpatient_registration = self.browse(inpatient_registration_id)
            if inpatient_registration.event:
                if 'hospitalization_date' in values:
                    event_obj.write(inpatient_registration.event.id, {
                        'dtstart': values['hospitalization_date'],
                        })
                if 'discharge_date' in values:
                    event_obj.write(inpatient_registration.event.id, {
                        'dtend': values['discharge_date'],
                        })
                if 'bed' in values:
                    bed = hospital_bed_obj.browse(values['bed'])
                    event_obj.write(inpatient_registration.event.id, {
                        'calendar': bed.calendar.id,
                        })
                if 'patient' in values:
                    patient = patient_obj.browse(values['patient'])
                    event_obj.write(inpatient_registration.event.id, {
                        'summary': patient.name.name,
                        })
        return super(InpatientRegistration, self).write(ids, values)

    def delete(self, ids):
        event_obj = Pool().get('calendar.event')

        if isinstance(ids, (int, long)):
            ids = [ids]
        for inpatient_registration_id in ids:
            inpatient_registration = self.browse(inpatient_registration_id)
            if inpatient_registration.event:
                event_obj.delete(inpatient_registration.event.id)
        return super(InpatientRegistration, self).delete(ids)

InpatientRegistration()
