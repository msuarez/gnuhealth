# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    MODULE = Nursing
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
    'name': 'GNU Health: Nursing',
    'version': '1.6.4',
    'author': 'GNU Solidario',
    'email': 'health@gnusolidario.org',
    'website': 'http://health.gnu.org',
    'depends': ['health', 'health_inpatient'],
    'name_es_ES': 'GNU Health : Enfermería',
    'translation': [],
    'description': '''

This module includes nursing functionality, both for inpatient and outpatient settings



''',
    'description_es_ES': '''

Este módulo incluye la funcionalidad de enfermería, tanto para hospitalizaciones o ambulatorias

''',

    'xml': [
        'health_nursing_view.xml',
        'data/health_nursing_sequences.xml',        
        'security/access_rights.xml'
    ],
    'active': False,
}
