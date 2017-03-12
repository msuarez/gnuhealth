# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2008-2017 Luis Falcon <falcon@gnu.org>
#    Copyright (C) 2011-2017 GNU Solidario <health@gnusolidario.org>
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

from trytond.pyson import Eval, Not, Bool, PYSONEncoder, Equal
from trytond.model import ModelView, ModelSQL, fields, Unique

__all__ = ['Iss']


class Iss (ModelSQL, ModelView):
    'Injury Surveillance System Registration'
    __name__ = 'gnuhealth.iss'

    name = fields.Many2One('gnuhealth.patient.evaluation',
        'Evaluation', required=True, help='Related Patient Evaluation')

    injury_date = fields.Date('Injury Date',
        help="Usually the same as the Evaluation")
    
    registration_date = fields.Date('Registration Date')
    
    code = fields.Char('Code',help='Injury Code', required=True)

    operational_sector = fields.Many2One('gnuhealth.operational_sector',
        'O. Sector',help="Operational Sector in which happened the injury")

    latitude = fields.Numeric('Latidude', digits=(3, 14))
    longitude = fields.Numeric('Longitude', digits=(4, 14))

    urladdr = fields.Char(
        'OSM Map',
        help="Maps the Accident / Injury location on Open Street Map")

    healthcenter = fields.Many2One('gnuhealth.institution','Institution')

    patient = fields.Function(
        fields.Char('Patient'),
        'get_patient', searcher='search_patient')

    patient_sex = fields.Function(
        fields.Char('Gender'),
        'get_patient_sex')

    patient_age = fields.Function(fields.Char('Age'), 'get_patient_age')


    complaint = fields.Function(
        fields.Char('Chief Complaint'),
        'get_patient_complaint')

    injury_type = fields.Selection([
        (None, ''),
        ('accidental', 'Accidental / Unintentional'),
        ('violence', 'Violence'),
        ('attempt_suicide', 'Suicide Attempt'),
        ('motor_vehicle', 'Motor Vehicle'),
        ], 'Injury Type', required=True, sort=False)

    mva_mode = fields.Selection([
        (None, ''),
        ('pedestrian', 'Pedestrian'),
        ('bicycle', 'Bicycle'),
        ('motorbike', 'Motorbike'),
        ('car', 'Car'),
        ('van', 'Van / Pickup / Jeep'),
        ('truck', 'Truck / Heavy vehicle'),
        ('bus', 'Bus'),
        ('train', 'Train'),
        ('taxi', 'Taxi'),
        ('boat', 'Boat / Ship'),
        ('aircraft', 'Aircraft'),
        ('other', 'Other'),
        ('unknown', 'Unknown'),
        ], 'Mode', help="Motor Vehicle Accident Mode",sort=False,
           states={'required': Equal(Eval('injury_type'), 'motor_vehicle')})

    mva_position = fields.Selection([
        (None, ''),
        ('driver', 'Driver'),
        ('passenger', 'Passenger'),
        ('outside', 'Outside / on the back'),
        ('bystander', 'Bystander'),
        ('unspecified_vehicle', 'Unspecified vehicle'),
        ('unknown', 'Unknown'),
        ], 'User Position', help="Motor Vehicle Accident user position",sort=False,
           states={'required': Equal(Eval('injury_type'), 'motor_vehicle')})
 

    mva_counterpart = fields.Selection([
        (None, ''),
        ('pedestrian', 'Pedestrian'),
        ('bicycle', 'Bicycle'),
        ('motorbike', 'Motorbike'),
        ('car', 'Car'),
        ('van', 'Van / Pickup / Jeep'),
        ('truck', 'Truck / Heavy vehicle'),
        ('bus', 'Bus'),
        ('train', 'Train'),
        ('taxi', 'Taxi'),
        ('boat', 'Boat / Ship'),
        ('aircraft', 'Aircraft'),
        ('other', 'Other'),
        ('unknown', 'Unknown'),
        ], 'Counterpart', help="Motor Vehicle Accident Counterpart",sort=False,
            states={'required': Equal(Eval('injury_type'), 'motor_vehicle')})
         

    safety_gear = fields.Selection([
        (None, ''),
        ('yes', 'Yes'),
        ('no', 'No'),
        ('unknown', 'Unknown'),
        ], 'Safety Gear', help="Use of Safety Gear - Helmet, safety belt...",sort=False,
           states={'required': Equal(Eval('injury_type'), 'motor_vehicle')})


    alcohol = fields.Selection([
        (None, ''),
        ('yes', 'Yes'),
        ('no', 'No'),
        ('suspected','Suspected'),
        ('unknown', 'Unknown'),
        ], 'Alcohol', required=True,
            help="Is there evidence of alcohol use by the injured person"
                " in the 6 hours before the accident ?",sort=False)

    drugs = fields.Selection([
        (None, ''),
        ('yes', 'Yes'),
        ('no', 'No'),
        ('suspected','Suspected'),
        ('unknown', 'Unknown'),
        ], 'Other Drugs', required=True,
            help="Is there evidence of drug use by the injured person"
                " in the 6 hours before the accident ?",sort=False)

    injury_details = fields.Text('Details')
    
    # Add victim-perpretator relationship for violence-related injuries
    victim_perpetrator = fields.Selection([
        (None, ''),
        ('parent', 'Parent'),
        ('spouse', 'Wife / Husband'),
        ('girlboyfriend', 'Girl / Boyfriend'),
        ('relative', 'Other relative'),
        ('acquaintance', 'Acquaintance / Friend'),
        ('official', 'Official / Legal'),
        ('stranger', 'Stranger'),
        ('other', 'other'),
        ], 'Relationship', help="Victim - Perpetrator relationship",sort=False,
            states={'required': Equal(Eval('injury_type'), 'violence')})


    violence_circumstances = fields.Selection([
        (None, ''),
        ('fight', 'Fight'),
        ('robbery', 'Robbery'),
        ('drug', 'Drug Related'),
        ('sexual', 'Sexual Assault'),
        ('gang', 'Gang Activity'),
        ('other_crime', 'Committing a crime (other)'),
        ('other', 'Other'),
        ('unknown', 'Unknown'),
        ], 'Context', help="Precipitating Factor",sort=False,
            states={'required': Equal(Eval('injury_type'), 'violence')})

    injury_method = fields.Selection([
        (None, ''),
        ('blunt', 'Blunt object'),
        ('push', 'Push/bodily force'),
        ('sharp', 'Sharp objects'),
        ('gun', 'Gun shot'),
        ('sexual', 'Sexual Assault'),
        ('choking', 'Choking/strangulation'),
        ('other', 'Other'),
        ('unknown', 'Unknown'),
        ], 'Method', help="Method of Injury",sort=False,
            states={'required': Equal(Eval('injury_type'), 'violence')})


    # Place of occurrance . Not used in motor vehicle accidents
    
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
        ], 'Place', help="Place of occurrance",sort=False,
            states={'required': Not(Equal(Eval('injury_type'), 'motor_vehicle'))})

    disposition = fields.Selection([
        (None, ''),
        ('treated_sent', 'Treated and Sent Home'),
        ('admitted', 'Admitted to Ward'),
        ('observation', 'Admitted to Observation'),
        ('died', 'Died'),
        ('daa', 'Discharge Against Advise'),
        ('transferred', 'Transferred'),
        ('doa', 'Dead on Arrival'),
        ], 'Disposition', help="Place of occurrance",sort=False, required=True)
    
    def get_patient(self, name):
        return self.name.patient.rec_name

    def get_patient_sex(self, name):
        return self.name.patient.name.gender

    def get_patient_age(self, name):
        return self.name.patient.name.age

    def get_patient_complaint(self, name):
        return self.name.chief_complaint

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
    def search_patient(cls, name, clause):
        res = []
        value = clause[2]
        res.append(('name.patient', clause[1], value))
        return res

    @classmethod
    def __setup__(cls):
        super(Iss, cls).__setup__()
        t = cls.__table__()
        cls._sql_constraints = [
            ('code_uniq', Unique(t,t.code), 
            'This ISS registration Code already exists'),
        ]

    @classmethod
    def view_attributes(cls):
        return [('//group[@id="motor_vehicle_accident"]', 'states', {
                'invisible': Not(Equal(Eval('injury_type'), 'motor_vehicle')),
                }),
                ('//group[@id="violent_injury"]', 'states', {
                'invisible': Not(Equal(Eval('injury_type'), 'violence')),
                }),
                ('//group[@id="iss_place"]', 'states', {
                'invisible': Equal(Eval('injury_type'), 'motor_vehicle'),
                }),
                ]

