# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    MODULE : Millennium Development Goal #6 HIV/AIDS, Malaria and Tuberculosis
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

    'name': 'GNU Health : MDG 6. HIV/AIDS, Malaria and Tuberculosis',
    'version': '1.6.4',
    'author': 'GNU Solidario',
    'email': 'health@gnusolidario.org',
    'website': "http://health.gnu.org",
    'depends': ['health','health_lab'],
    'name_es_ES': 'GNU Health: MDG 6. VIH/SIDA, Malaria y Tuberculosis',

    "xml": ["data/lab_test_data.xml"],

    'description': """

Millennium Development Goal # 6
--------------------------------

health_mdg6 is a GNU Health module that incorporates the Millennium Development Goal # 6, to combat HIV/AIDS, malaria and Tuberculosis

The United Nations signed in September 2000 the Millennium Declaration, to fight poverty, hunger, disease, illiteracy, environmental degradation, and discrimination against women .


The Millennium Development Goals (MDG) has derived from the Millennium declaration and it has 8 goals. MDG 6 focuses on HIV/AIDS, Malaria and Tuberculosis.

GNU Solidario believes that Free Software is a key factor to accomplish these goals. GNU Health, the Free Health and Hospital Information System will help the health centers, researches, NGOs and professionals and volunteers to eradicate these devastating diseases.

GNU Health will incorporate the specific functionality to help prevent, diagnose, treat and control each of these devastating diseases.

The health_mdg6 module will maintain the multi-disciplinary approach, providing tools to the social worker, nurse, biochemist, laboratory , pharmacist, epidemiologist and physician, integrating the health professional into the community.

So, for example, upon a new possible case of active Tuberculosis (TB), GNU Health will execute the following actions : Detect and notify the contacts of the patient; Start profilaxis treatment on contacts ; Create a new laboratory order for culture and antibiogram and check for the strain resistance ; verify the DOTS (Direct Observed Treatment Short) on the patient ; Check the stock for the PPD test-kits and do a forecast for the existing anti-tuberculosis medicaments; Check for availability of special rooms if there is need for hospitalization; inform the health authorities of a new case; start a new prevention campaign.

""",

    'description_es_ES': '''
Acerca de GNU Health
---------------------------------

GNU Health es un sistema libre de Gestión Hospitalaria y de Información de salud que ofrece las siguientes funciones :

    * Expediente Médico Electrónico (EMR)

    * Sistema de Gestión Hospitalaria (HIS)

    * Sistema de Información de Salud

Nuestro objetivo es contribuir con los profesionales de la salud alrededor del mundo para mejorar la calidad de vida de los más necesitados, ofreciendo un sistema libre que optimice la promoción de la salud y la prevención de la enfermedad.


Características de GNU Health :


    - Focalizado en medicina familiar y APS (Atención Primaria de la Salud)

    - Interés en condiciones Socio-economicas (estilos de vida, ámbito familiar, educación...)

    - Enfermedades y Procedimientos Médicos standard (ICD-10 / ICD-10-PCS)

    - Gestión de Internación (Hospitalización)

    - Marcadores genéticos y riesgos hereditarios: Más de 4200 genes relacionados con enfermedades

    - Epidemiología y otros registros estadísticos

    - Registro Electrónico. Sin necesidad de papel

    - Recetas

    - Facturación

    - Administración del Paciente (creación, evaluación / consultas, historia ...)

    - Administración de Laboratorio

    - Vademécum

    - Gestión de Stock y de cadena de abastecimiento

    - Administración Financiera y gestión Hospitalaria

    - Diseñado con los estándares de la industria en mente

    - Software Libre:  License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>

** Para mayor información, visite la página del proyecto en http://health.gnu.org

** Puede escribirnos a health@gnusolidario.org

''',


}
