# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2011  Adrián Bernardi, Mario Puntin
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
    'name': 'GNU Health: Invoice',
    'version': '1.4.5',
    'author': 'Silix',
    'website': 'http://health.gnu.org',
    'depends': [
        'health',
        'health_lab',
        'account_invoice',
        'party',
    ],
    'xml': [
        'health_invoice_view.xml',
        'wizard/appointment_invoice.xml',
        'wizard/prescription_invoice.xml',
        'wizard/create_lab_invoice.xml',
        'security/access_rights.xml'
    ],
    'name_es_ES': 'GNU Health : Facturación',
    'translation': ['locale/es_ES.po', 'locale/fr_FR.po', 'locale/el.po',
        'locale/fa.po','locale/it.po'],

    'description': ''' 
        This module add functionality to create invoices for doctor's consulting charge.

        Features:
        -Invoice of multiple appointments at a time.
        ''',
    'description_es_ES': ''' 
        Este módulo añade funcionalidad para crear facturas por servicios de evaluaciones, 
        recetas o pruebas de laboratorio.
        
        - Permite facturar múltples evaluaciones de una vez
        ''',


}
