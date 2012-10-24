# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    MODULE : Lifestyle
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
    'name': 'GNU Health: Lifestyle',
    'version': '1.6.4',
    'author': 'GNU Solidario',
    'email': 'health@gnusolidario.org',
    'website': 'http://health.gnu.org',
    'depends': [
        'health',
    ],
    'name_es_ES': 'GNU Health : Estilos de vida',
    'translation': [
    ],
    'description': '''

Gathers information about the habits and sexuality of the patient

- Eating habits and diets
- Sleep patterns
- Recreational drugs database from NIDA
- Henningfield drug ratings
- Drug / alcohol addictions
- Physical activity (workout / excercise )
- Sexuality and sexual behaviour
- Home and child safety




''',
    'description_es_ES': '''
Guarda información de los hábitos y sexualidad del paciente

- Dietas y hábitos alimenticios
- Ejercicio físico
- Adicciones
- Drogras recreacionales (Base de datos de NIDA)
- Score de Henningfield de drogas
- Patrones del sueño
- Sexualidad y hábitos sexuales
- Seguridad en el hogar y vial

''',



    'xml': [
        'health_lifestyle_view.xml',
        'data/recreational_drugs.xml',
        'security/access_rights.xml'
    ],
    'active': False,
}
