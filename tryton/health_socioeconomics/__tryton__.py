# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    MODULE : Socioeconomics
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
    'name': 'GNU Health : Socioeconomics',
    'version': '1.6.4',
    'author': 'GNU Solidario',
    'email': 'health@gnusolidario.org',
    'website': 'http://health.gnu.org',
    'depends': [
        'health',
    ],
    'name_es_ES': 'GNU Health : Socioeconomía',
    'translation': [
    ],

    'description': '''


This module takes care of the input of all the socio-economic factors that influence the health of the individual / family and society.

Among others, we include the following factors :

- Living conditions
- Educational level
- Infrastructure (electricity, sewers, ... )
- Family affection ( APGAR )
- Drug addiction
- Hostile environment
- Teenage Pregnancy
- Working children


''',
    'description_es_ES': '''
Este módulo se encarge de ingresar y procesar los factores socio-económicos que influyen en la salud del individuo, su familia y sociedad.

Algunos aspectos que abarca :

- Condiciones de vida
- Nivel educativo
- Infraestructura (electricidad, gas, alcantarillas... )
- Afectividad familiar
- Trabajo Infantil
- Entornos hostiles
- Embarazos adolescentes
- Profesiones
- Violencia doméstica

''',

    'xml': [
        'health_socioeconomics_view.xml',
    ],
    'active': False,
}
