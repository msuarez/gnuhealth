# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    MODULE : Laboratory
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
    'name': 'GNU Health: Laboratory',
    'version': '1.6.4',
    'author': 'GNU Solidario',
    'email': 'health@gnusolidario.org',
    'website': 'http://health.gnu.org',
    'depends': [
        'health',
    ],

    'name_es_ES': 'GNU Health : Laboratorio',
    'translation': [
    ],

    'description': '''

This modules includes lab tests: Values, reports and PoS.


''',

    'description_es_ES': '''

Módulo con la funcionalidad de laboratorio.

''',

    'xml': [
        'health_lab_view.xml',
        'health_lab_report.xml',
        'data/health_lab_sequences.xml',
        'data/lab_test_data.xml',
        'wizard/create_lab_test.xml',
        'security/access_rights.xml',
    ],
}
