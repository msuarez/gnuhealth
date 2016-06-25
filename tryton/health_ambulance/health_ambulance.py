# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2008-2016 Luis Falcon <falcon@gnu.org>
#    Copyright (C) 2011-2016 GNU Solidario <health@gnusolidario.org>
#
#    MODULE : INJURY SURVEILLANCE SYSTEM
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
#
#
# The documentation of the module goes in the "doc" directory.

from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta, date

from trytond.pyson import Eval, Not, Bool, PYSONEncoder, Equal
from trytond.model import ModelView, ModelSQL, fields, Unique
from trytond.pool import Pool


__all__ = ['SupportRequest']


class SupportRequest (ModelSQL, ModelView):
    'Support Request Registration'
    __name__ = 'gnuhealth.support_request'

    code = fields.Char('Code',help='Request Code', required=True)

    operator = fields.Many2One(
        'gnuhealth.healthprofessional', 'Operator',
        help="Operator who took the call / support request")

    requestor = fields.Many2One('party.party', 'Requestor',
    domain=[('is_person', '=', True)], help="Related party (person)")

    patient = fields.Many2One('gnuhealth.patient', 'Patient')

    evaluation = fields.Many2One('gnuhealth.patient.evaluation',
        'Evaluation', 
        domain=[('patient', '=', Eval('patient'))], depends=['patient'],
        help='Related Patient Evaluation')

    request_date = fields.DateTime('Date', required=True,
        help="Date and time of the call for help")
    
    operational_sector = fields.Many2One('gnuhealth.operational_sector',
        'O. Sector',help="Operational Sector")

    latitude = fields.Numeric('Latidude', digits=(3, 14))
    longitude = fields.Numeric('Longitude', digits=(4, 14))

    urladdr = fields.Char(
        'OSM Map',
        help="Maps the location on Open Street Map")

    healthcenter = fields.Many2One('gnuhealth.institution','Calling Institution')

    patient_sex = fields.Function(
        fields.Char('Sex'),
        'get_patient_sex')

    patient_age = fields.Function(
        fields.Char('Age'),
        'get_patient_age')

    complaint = fields.Function(
        fields.Char('Chief Complaint'),
        'get_patient_complaint')

    request_extra_info = fields.Text('Details')
       
    place_occurrance = fields.Selection([
        (None, ''),
        ('home', 'Home'),
        ('street', 'Street'),
        ('institution', 'Institution'),
        ('school', 'School'),
        ('commerce', 'Commercial Area'),
        ('publicbuilding', 'Public Building'),
        ('recreational', 'Recreational Area'),
        ('transportation', 'Public transportation'),
        ('sports', 'Sports event'),
        ('unknown', 'Unknown'),
        ], 'Origin', help="Place of occurrance",sort=False)

    
    def get_patient_sex(self, name):
        if self.patient:
            return self.patient.gender

    def get_patient_age(self, name):
        if self.patient:
            return self.patient.name.age

    def get_patient_complaint(self, name):
        if self.evaluation:
            if self.evaluation.chief_complaint:
                return self.evaluation.chief_complaint

    @staticmethod
    def default_operator():
        pool = Pool()
        HealthProf= pool.get('gnuhealth.healthprofessional')
        operator = HealthProf.get_health_professional()
        return operator

    @staticmethod
    def default_request_date():
        return datetime.now()


    @fields.depends('latitude', 'longitude')
    def on_change_with_urladdr(self):
        # Generates the URL to be used in OpenStreetMap
        # The address will be mapped to the URL in the following way
        # If the latitud and longitude of the Accident / Injury 
        # are given, then those parameters will be used.

        ret_url = ''
        if (self.latitude and self.longitude):
            ret_url = 'http://openstreetmap.org/?mlat=' + \
                str(self.latitude) + '&mlon=' + str(self.longitude)

        return ret_url

    @classmethod
    def __setup__(cls):
        super(SupportRequest, cls).__setup__()
        t = cls.__table__()
        cls._sql_constraints = [
            ('code_uniq', Unique(t,t.code), 
            'This Request Code already exists'),
        ]

