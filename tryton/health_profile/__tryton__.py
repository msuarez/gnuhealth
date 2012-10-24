# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    MODULE : Profile
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

    'name' : 'GNU Health : Installer',  
    'version': '1.6.4',
    'author' : 'GNU Solidario',
    'email' : 'health@gnusolidario.org',
    'website' : "http://health.gnu.org",
    'category' : 'Generic Modules/Others',
    'depends' : ['health','health_socioeconomics','health_lifestyle',
        'health_genetics','health_icd10','health_gyneco',
        'health_pediatrics','health_surgery','health_lab', 'health_inpatient'],
    'name_es_ES': 'GNU Health : Perfil de Instalación estándar',
   
    'description' : """


Profile for Main Modules.
- Core
- Socioeconomics
- Lifestyle
- Genetics
- Surgery
- Laboratory
- Pediatrics
- ICD-10 Coding
- Gynecology and Obstetrics
- Inpatient

We don't include in the main installation the following modules :
- ICD-10-PCS (Surgical Procedures)
- Invoicing (Billing)

You can install these two manually.


""",

    'description_es_ES': 
'''
Perfil de Instalación de la functionalidad estándar

- Núcleo
- Socioeconomía
- Estilos de vida
- Genetica
- Cirugía
- Laboratorio
- Pediatría 
- ICD-10 
- Ginecología y Obstetricia
- Hospitalización

Los módulos :

- ICD-10-PCS (Procedimientos quirúrgicos
- Facturación (Billing)

No están en el perfil de instalación estándar, pero sí en el sistema.
Si lo desea, los puede instalar a posteriori.
''',

    'xml': [],
    "active": False 
}
