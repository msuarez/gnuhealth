# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    MODULE : Health Services
#    Copyright (C) 2008-2012  Luis Falcon <lfalcon@gnusolidario.org>
#    Copyright (C) 2011  Adrian Bernardi - Mario Puntin (health_invoice)
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
    'name': 'GNU Health : Health Services and orders',
    'name_es_ES': 'GNU Health : Servicios y órdenes',
    'version': '1.6.4',
    'author': 'GNU Solidario',
    'email': 'health@gnusolidario.org',
    'website': 'http://health.gnu.org',
    'category': 'Generic Modules/Others',
    'depends': [
        'health','account_invoice',	
    ],

    'description': '''

This module allows grouping the services and orders related to a patient
evaluation / encounter and or Hospitalization.
It also permits invoicing the selected orders.

''',
    'description_es_ES': '''

El módulo permite agrupar servicios y pruebas del paciente, realizadas
durante la consulta o durante la hospitalización.

Es posible factuar los servicios seleccionados.

''',

    'xml': [
        'health_services_view.xml',
        'wizard/create_health_service_invoice.xml',
        'data/health_service_sequences.xml',
        'security/access_rights.xml'
    ],
    'active': False,
}
