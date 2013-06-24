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
    survey_date = fields.Date('Date', required=True)
    
    triatomines =  fields.Boolean('Triatomines', help="Check this box if triatomines were found")
    vector = fields.Selection([
        (None, ''),
        ('t_infestans', 'T. infestans'),
        ('t_brasilensis', 'T. brasilensis'),
        ('r_prolixus', 'R. prolixus'),
        ('t_dimidiata', 'T. dimidiata'),
        ('p_megistus', 'P. megistus'),
        ], 'Vector', help="Vector", sort=False)

    nymphs = fields.Boolean ('Nymphs', "Check this box if triatomine nymphs were found")
    t_in_house = fields.Boolean('Domiciliary', help="Check this box if triatomines were found inside the house")
    t_peri = fields.Boolean('Peri-Domiciliary', help="Check this box if triatomines were found in the peridomiciliary area")
    
    
    dfloor = fields.Boolean('Floor', help="Current floor can host triatomines")
    dwall = fields.Boolean('Walls', help="Wall materials or state can host triatomines")
    droof = fields.Boolean('Roof', help="Roof materials or state can host triatomines")
    dperi = fields.Boolean('Peri-domicilary', help="Peri domiciliary area can host triatomines")
    
    
    observations = fields.Text('Observations')
    next_survey_date = fields.Date('Next survey')
