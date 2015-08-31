# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2008-2015 Luis Falcon <lfalcon@gnusolidario.org>
#    Copyright (C) 2011-2015 GNU Solidario <health@gnusolidario.org>
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
from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta, date
from sql import Literal, Join, Table
from trytond.model import ModelView, ModelSingleton, ModelSQL, fields
from trytond.wizard import Wizard, StateAction, StateView, Button
from trytond.transaction import Transaction
from trytond import backend
from trytond.pyson import Eval, Not, Bool, PYSONEncoder, Equal, And, Or, If
from trytond.pool import Pool
import string
import pytz

__all__ = ['PatientDisability']

class PatientDisability(ModelSQL, ModelView):
    'Patient Disability Information'
    __name__ = 'gnuhealth.patient_disability'
    
    patient = fields.Many2One('gnuhealth.patient','Patient', required=True)
    
    crutches = fields.Boolean('Crutches')
    wheelchair = fields.Boolean('Wheelchair')
    

