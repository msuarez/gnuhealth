# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    MODULE : Hospitalization / Inpatient
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
    'name': 'GNU Health: Inpatient administration',
    'version': '1.6.4',
    'author': 'GNU Solidario',
    'email': 'health@gnusolidario.org',
    'website': 'http://health.gnu.org',
    'depends': [
        'health',
    ],
    'name_es_ES': 'GNU Health : Hospitalización',
    'translation': [
    ],

    'description': '''
This module will hold all the processes related to Inpatient (Patient hospitalization and bed assignment )

- Patient Registration
- Bed reservation
- Hospitalization
- Nursing Plan
- Discharge Plan
- Reporting

''',

    'description_es_ES': '''
Contiene los procesos relacionados a la internación (Hospitalización y asignación de camas )

- Registro del paciente
- Reserva de camas
- Hospitalización
- Plan de enfermería
- Plan para después del alta
- Reportes

''',

    'xml': [
        'health_inpatient_view.xml','data/health_inpatient_sequence.xml',
        'data/inpatient_diets.xml','data/diets_beliefs.xml',
        'security/access_rights.xml'
    ],
    'active': False,
}
