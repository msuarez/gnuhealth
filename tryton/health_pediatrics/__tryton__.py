# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    MODULE : Pediatrics
#    Copyright (C) 2008-2012  Luis Falcon <lfalcon@gnusolidario.org>
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
{
    'name': 'GNU Health: Pediatrics',
    'version': '1.6.4',
    'author': 'GNU Solidario',
    'email': 'health@gnusolidario.org',
    'website': 'http://health.gnu.org',
    'depends': [
        'health',
    ],

    'name_es_ES': 'GNU Health : Pediatría',
    'translation': [
    ],

    'description': '''
	
	This module takes has the functionality for pediatric patients :
	
	- Neonatal 
	- Infancy 
	- Toddler and early childhood 
	- Late childhood 
    - Adolescence
    
	This module focuses on the basic pediatric evaluation, making emphasis in the nutritional, growth and development of the infant and child.
''',

    'description_es_ES': '''

Cubre la funcionalidad principal para pacientes pediátricos :

- Neonatología 
- Infancia 
- Niñez 
- Adolescencia

Nos focalizamos en la evaluación pediátrica básica, haciendo énfasis en el desarrollo nutricional y crecimiento del niño.

''',
    'xml': [
        'health_pediatrics_view.xml',
        'health_pediatrics_report.xml',
        'security/access_rights.xml'
    ],
    'active': False,
}
