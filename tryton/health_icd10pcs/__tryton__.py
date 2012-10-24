# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    MODULE : Procedure Coding System .- ICD10-PCS
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

	'name' : 'GNU Health : Procedure Coding System .- ICD10-PCS',  
    'version': '1.6.4',
	'author' : 'GNU Solidario',
	'email' : 'health@gnusolidario.org',
	'depends' : ['health'],
	'website' : "http://health.gnu.org",
    'name_es_ES': 'GNU Health : Facturación',
    
	'description' : """

Procedure Coding System for Medical : ICD-10-PCS

The ICD-10 Procedure Coding System (ICD-10-PCS) is system of medical classification used for procedural codes. The National Center for Health Statistics (NCHS) received permission from the World Health Organization (WHO) (the body responsible for publishing the International Classification of Diseases [ICD]) to create the ICD-10-PCS as a successor to Volume 3 of ICD-9-CM and a clinical modification of the original ICD-10.

Each code consists of seven alphanumeric characters. The second through seventh characters mean the same thing within each section, but may mean different things in other sections. Each character can be any of 34 possible values the ten digits 0-9 and the 24 letters A-H,J-N and P-Z may be used in each character. The letters O and I excluded to avoid confusion with the numbers 0 and 1. There are no decimals in ICD-10-PCS

Check http://en.wikipedia.org/wiki/ICD-10_Procedure_Coding_System

""",
    'description_es_ES' : '''

ICD-10-PCS es el acrónimo del International Classification of Diseases 10th Revision Procedure Classification System, en español Sistema de Codificación de Procedimientos anexo a la Codificación Internacional de enfermedades, 10 edición, un sistema de clasificación propuesto por los Centros de Servicios Medicare y Medicaid (CMS) de los Estados Unidos como anexo a la CIE-10,
 que estipula reglas de codificación especializadas para todos los procedimientos relacionados con la salud, usando un código alfanumérico de siete caracteres que provee una clave única para cada uno de ellos. El sistema estuvo en una fase de desarrollo durante más de cinco años y comenzó a utilizarse en 1998.
Reemplaza el volumen 3 de la CIE-9-MC.

Ver : http://es.wikipedia.org/wiki/ICD-10-PCS
''',

	"xml" : ["data/icd_10_pcs_2009_part1.xml","data/icd_10_pcs_2009_part2.xml","data/icd_10_pcs_2009_part3.xml"],

	"active": False 
}
