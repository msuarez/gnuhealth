# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2008-2014 Luis Falcon <lfalcon@gnusolidario.org>
#    Copyright (C) 2011-2014 GNU Solidario <health@gnusolidario.org>
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
from trytond.model import ModelView
from trytond.wizard import Wizard, StateTransition, StateAction, StateView, Button
from trytond.transaction import Transaction
from trytond.pool import Pool
from trytond.pyson import PYSONEncoder


__all__ = ['CreateAppointmentEvaluation']

class CreateAppointmentEvaluation(Wizard):
    'Create Appointment Evaluation'
    __name__ = 'wizard.gnuhealth.appointment.evaluation'
  
    start_state = 'appointment_evaluation'
    appointment_evaluation = StateAction('health.act_app_evaluation')

    def do_appointment_evaluation(self, action):
      
        appointment = Transaction().context.get('active_id')

        app_id = Pool().get('gnuhealth.appointment').browse([appointment])[0]

        patient = app_id.patient.id
        if (app_id.speciality):
            specialty = app_id.speciality.id
        else:
            specialty = None
        urgency = str(app_id.urgency)
        evaluation_type = str(app_id.appointment_type)
        visit_type = str(app_id.visit_type)

        action['pyson_domain'] = PYSONEncoder().encode([
            ('evaluation_date', '=', appointment),
            ('patient', '=', patient),
            ('specialty', '=', specialty),
            ('urgency', '=', urgency),
            ('evaluation_type', '=', evaluation_type),
            ('visit_type', '=', visit_type),
            ])
        action['pyson_context'] = PYSONEncoder().encode({
            'evaluation_date': appointment,
            'patient': patient,
            'specialty': specialty,
            'urgency': urgency,
            'evaluation_type': evaluation_type,
            'visit_type': visit_type,
            })
            
        return action, {}
        