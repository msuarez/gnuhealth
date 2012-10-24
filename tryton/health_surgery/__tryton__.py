# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    MODULE : Surgery
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
    'name': 'GNU Health: Surgery',
    'version': '1.6.4',
    'author': 'GNU Solidario',
    'email': 'health@gnusolidario.org',
    'website': 'http://health.gnu.org',
    'depends': [
        'health',
    ],
    'name_es_ES': 'GNU Health : Cirugía',
    'translation': [
    ],

    'description': '''

Basic Surgery Module for GNU Health

If you want to include standard codings for procedures, please install
corresponding module, like ICD10-PCS

''',

    'description_es_ES': '''
Módulo básico que cirugía para GNU Health

Si quiere incluir códigos de procedimientos, por favor instale algún módulo
con la funcionalidad específica, como gnuhealth_ICD10-PCS
''',

    'xml': [
        'health_surgery_view.xml',
        'security/access_rights.xml'
    ],
    'active': False,
}
