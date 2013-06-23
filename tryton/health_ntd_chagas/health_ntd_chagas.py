# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2008-2013  Luis Falcon <lfalcon@gnusolidario.org>
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
from trytond.model import ModelView, ModelSingleton, ModelSQL, fields
from trytond.pool import Pool


__all__ = ['ChagasDUSurvey']

class ChagasDUSurvey(ModelSQL, ModelView):
    'Chagas DU Entomological Survey'
    __name__ = 'gnuhealth.chagas_du_survey'

    name = fields.Char ('Survey Code', required=True)
    du = fields.Many2One('gnuhealth.du', 'DU', help="Domiciliary Unit")
    survey_date = fields.Date('Date')
    next_survey_date = fields.Date('Next survey')
    observations = fields.Text('Observations')
