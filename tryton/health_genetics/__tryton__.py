# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    MODULE : Genetics
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
    'name': 'GNU Health : Genetics',
    'version': '1.6.4',
    'author': 'GNU Solidario',
    'email': 'health@gnusolidario.org',
    'website': 'http://health.gnu.org',
    'category': 'Generic Modules/Others',
    'depends': [
        'health',
    ],
    'name_es_ES': 'GNU Health : Genética',
    'translation': [
    ],
    'description': '''

Family history and genetic risks

The module includes hereditary risks, family history and genetic disorders.

In this module we include the NCBI and GeneCards information, more than 4200 genes associated to diseases


''',
    'description_es_ES': '''

Riesgos genéticos e historial familiar
Family history and genetic risks
Incluye desórdenes genéticos y genes patológicos ("disease genes"), con una base de más de 4200 de la NCBI y GeneCards.

''',

    'xml': [
        'health_genetics_view.xml',
        'data/disease_genes.xml','security/access_rights.xml'
    ],
    'active': False,
}
