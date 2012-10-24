# coding=utf-8
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    MODULE : International Classification of Diseases .- ICD-10
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

	'name' : 'GNU Health: International Classification of Diseases .- ICD-10',  
    'version': '1.6.4',
	'author' : 'GNU Solidario',
	"website" : "http://health.gnu.org",
	'email' : 'health@gnusolidario.org',
	'depends' : ['health'],
    'name_es_ES': 'GNU Health : Clasificación Internacional de Enfermedades .- CIE-10',
	'description' : '''
World Health Organization - International Classification of Diseases for GNU HEALTH - 10th revision
''',

	'description_es_ES' : '''
Organización Mundial de la Salud - Clasificación Internacional de Enfermedades - Revisión 10' 
''',
	"xml" : ["data/disease_categories.xml","data/diseases.xml"],

    'translation': [],

	"active": False 
}
