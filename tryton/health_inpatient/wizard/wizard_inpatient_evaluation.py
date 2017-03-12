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
from trytond.model import ModelView
from trytond.wizard import Wizard, StateTransition, StateAction, StateView, Button
from trytond.transaction import Transaction
from trytond.pool import Pool
from trytond.pyson import PYSONEncoder


__all__ = ['CreateInpatientEvaluation']

class CreateInpatientEvaluation(Wizard):
    'Create Inpatient Evaluation'
    __name__ = 'wizard.gnuhealth.inpatient.evaluation'
  
    start_state = 'inpatient_evaluation'
    inpatient_evaluation = StateAction('health_inpatient.act_inpatient_evaluation')

    def do_inpatient_evaluation(self, action):
      
        inpatient_registration = Transaction().context.get('active_id')

        try:
            reg_id = \
                Pool().get('gnuhealth.inpatient.registration').browse([inpatient_registration])[0]
        except:
            self.raise_user_error('no_record_selected')
            
        patient = reg_id.patient.id

        
        action['pyson_domain'] = PYSONEncoder().encode([
            ('patient', '=', patient),
            ('inpatient_registration_code', '=', reg_id.id),
            ('evaluation_type', '=', 'inpatient'),
            ])
        action['pyson_context'] = PYSONEncoder().encode({
            'patient': patient,
            'inpatient_registration_code': reg_id.id,
            'evaluation_type': 'inpatient',
            })
            
        return action, {}
        
    @classmethod
    def __setup__(cls):
        super(CreateInpatientEvaluation, cls).__setup__()
        cls._error_messages.update({
            'no_record_selected':
                'You need to select an inpatient registration record',
        })

