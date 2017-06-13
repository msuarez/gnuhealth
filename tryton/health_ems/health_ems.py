# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2008-2017 Luis Falcon <falcon@gnu.org>
#    Copyright (C) 2011-2017 GNU Solidario <health@gnusolidario.org>
#
#    MODULE : Emergency Management
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
from trytond.model import ModelView, ModelSingleton, ModelSQL, fields, Unique
from trytond.pool import Pool


__all__ = [
    'GnuHealthSequences','Ambulance','SupportRequest', 'AmbulanceSupport',
    'AmbulanceHealthProfessional','SupportRequestLog']

class GnuHealthSequences(ModelSingleton, ModelSQL, ModelView):
    "Standard Sequences for GNU Health"
    __name__ = "gnuhealth.sequences"

    support_request_code_sequence = fields.Property(fields.Many2One('ir.sequence',
        'Support Request Sequence', 
        domain=[('code', '=', 'gnuhealth.support_request')],
        required=True))

class Ambulance (ModelSQL, ModelView):
    'Ambulance'
    __name__ = 'gnuhealth.ambulance'

    vehicle_identifier = fields.Char('ID', required=True,
        help="Ambulance license number or other type of ID")

    vehicle_brand = fields.Char('Brand', help="Ambulance maker")
    vehicle_model = fields.Char('Model', help="Ambulance model")

    vehicle_odometer = fields.Integer('Odometer',
        help="Current odometer reading")

    vehicle_type = fields.Selection([
        (None, ''),
        ('van', 'Van'),
        ('car', 'Car'),
        ('boat', 'Boat'),
        ('helicopter', 'Helicopter'),
        ('airplane', 'Airplane'),
        ('motorcycle', 'Motorcycle'),
        ('bicycle', 'Bicycle'),
        ('drone', 'Drone'),
        ], 'Type', required=True,
        help="Type of vehicle",sort=False)

    vehicle_function = fields.Selection([
        (None, ''),
        ('patient_transport', 'Type A - Patient Transport'),
        ('emergency', 'Type B - Emergency'),
        ('icu', 'Type C - Mobile ICU'),
        ], 'Function',sort=False, required=True, 
        help="Vehicle main functionality")
    
    vehicle_station = fields.Many2One(
        'gnuhealth.institution', 'Station',
        help="Station / Base of the vehicle")

    state = fields.Selection([
        (None, ''),
        ('available', 'Available / At Station'),
        ('dispatched', 'Dispatched'),
        ('en_route', 'En Route'),
        ('on_location', 'On Location'),
        ('to_hospital', 'To Hospital'),
        ('at_hospital', 'At Hospital'),
        ('returning', 'Returning'),
        ('out_of_service', 'Out of service'),
        ], 'Status',sort=False, readonly=True, help="Vehicle status")

    vehicle_remarks = fields.Text('Remarks')

    active = fields.Boolean('Active', select=True)

    @staticmethod
    def default_active():
        return True

    @staticmethod
    def default_state():
        return 'available'

    @classmethod
    def __setup__(cls):
        super(Ambulance, cls).__setup__()
        t = cls.__table__()
        cls._sql_constraints = [
            ('vehicle_uniq', Unique(t,t.vehicle_identifier), 
            'This vehicle ID already exists'),
        ]

    def get_rec_name(self, name):
        return (self.vehicle_identifier + ' : ' + self.vehicle_type)

class SupportRequest (ModelSQL, ModelView):
    'Support Request Registration'
    __name__ = 'gnuhealth.support_request'
    _rec_name = 'code'

    code = fields.Char('Code',help='Request Code', readonly=True)

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

    address = fields.Text("Address", help="Free text address / location")
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

    urgency = fields.Selection([
        (None, ''),
        ('low', 'Low'),
        ('urgent', 'Urgent'),
        ('emergency', 'Emergency'),
        ], 'Urgency', sort=False)
       
    place_occurrance = fields.Selection([
        (None, ''),
        ('home', 'Home'),
        ('street', 'Street'),
        ('institution', 'Institution'),
        ('school', 'School'),
        ('commerce', 'Commercial Area'),
        ('recreational', 'Recreational Area'),
        ('transportation', 'Public transportation'),
        ('sports', 'Sports event'),
        ('publicbuilding', 'Public Building'),
        ('unknown', 'Unknown'),
        ], 'Origin', help="Place of occurrance",sort=False)

    event_type = fields.Selection([
        (None, ''),
        ('event1', 'Acute Coronary Syndrome'),
        ('event2', 'Acute pain'),
        ('event3', 'Acute illness'),
        ('event4', 'Allergic reaction'),
        ('event5', 'Bullying, battering'),
        ('event6', 'Gastrointestinal event'),
        ('event7', 'Endocrine event (diabetes, adrenal crisis, ..)'),
        ('event8', 'Choke'),
        ('event9', 'Domestic violence'),
        ('event10', 'Environmental event (weather, animals, ...)'),
        ('event11', 'Sexual assault'),
        ('event12', 'Drug intoxication'),
        ('event13', 'Robbery, violent assault'),
        ('event14', 'Respiratory distress'),
        ('event15', 'Pregnancy related event'),
        ('event16', 'Gas intoxication'),
        ('event17', 'Food intoxication'),
        ('event18', 'Neurological event (stroke, TIA, seizure, ...)'),
        ('event19', 'Chronic illness'),
        ('event20', 'Near drowning'),
        ('event21', 'Eye, Ear and Nose event'),
        ('event22', 'Fall'),
        ('event23', 'Deceased person'),
        ('event24', 'Psychiatric event'),
        ('event25', 'Suicide attempt'),
        ('event26', 'Fire'),
        ('event27', 'Transportation accident'),
        ('event28', 'Traumatic Injuries'),
        ('event29', 'Explosion'),
        ('event30', 'Other specified'),
        ], 'Event type')

    event_specific = fields.Many2One ('gnuhealth.pathology','Incident')

    multiple_casualties = fields.Boolean('Multiple Casualties')

    request_actions = fields.One2Many(
        'gnuhealth.support_request.log', 'sr',
        'Activities', help='Support request activity log')

    ambulances = fields.One2Many(
        'gnuhealth.ambulance.support', 'sr',
        'Ambulances', help='Ambulances requested in this Support Request')

    request_extra_info = fields.Text('Details')

    state = fields.Selection([
        (None, ''),
        ('open', 'Open'),
        ('closed', 'Closed'),
        ], 'State', sort=False, readonly=True)
 
    @staticmethod
    def default_request_date():
        return datetime.now()

    
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
    def default_state():
        return 'open'


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
    def create(cls, vlist):
        Sequence = Pool().get('ir.sequence')
        Config = Pool().get('gnuhealth.sequences')

        vlist = [x.copy() for x in vlist]
        for values in vlist:
            if not values.get('code'):
                config = Config(1)
                values['code'] = Sequence.get_id(
                    config.support_request_code_sequence.id)

        return super(SupportRequest, cls).create(vlist)


    @classmethod
    def __setup__(cls):
        super(SupportRequest, cls).__setup__()
        t = cls.__table__()
        cls._sql_constraints = [
            ('code_uniq', Unique(t,t.code), 
            'This Request Code already exists'),
        ]

        cls._buttons.update({
            'open_support': {'invisible': Equal(Eval('state'), 'open')},
            'close_support': {'invisible': Equal(Eval('state'), 'closed')},
            })


    @classmethod
    @ModelView.button
    def open_support(cls, srs):
        cls.write(srs, {
            'state': 'open'})

    @classmethod
    @ModelView.button
    def close_support(cls, srs):
        cls.write(srs, {
            'state': 'closed'})


class AmbulanceSupport (ModelSQL, ModelView):
    'Ambulance associated to a Support Request'
    __name__ = 'gnuhealth.ambulance.support'

    sr = fields.Many2One('gnuhealth.support_request',
        'SR', help="Support Request", required=True)

    ambulance = fields.Many2One('gnuhealth.ambulance','Ambulance',
        domain=[('state', '=', 'available')],)
    
    healthprofs = fields.One2Many('gnuhealth.ambulance_hp','name',
        'Health Professionals')

    state = fields.Selection([
        (None, ''),
        ('available', 'Available / At Station'),
        ('dispatched', 'Dispatched'),
        ('en_route', 'En Route'),
        ('on_location', 'On Location'),
        ('to_hospital', 'To Hospital'),
        ('at_hospital', 'At Hospital'),
        ('returning', 'Returning'),
        ('out_of_service', 'Out of service'),
        ], 'Status',sort=False, readonly=True, help="Vehicle status")

    @staticmethod
    def default_state():
        return 'available'


    @classmethod
    def __setup__(cls):
        super(AmbulanceSupport, cls).__setup__()
        cls._buttons.update({
            'available': {'invisible': Equal(Eval('state'), 'available')},
            'dispatched': {'invisible': Equal(Eval('state'), 'dispatched')},
            'en_route': {'invisible': Equal(Eval('state'), 'en_route')},
            'on_location': {'invisible': Equal(Eval('state'), 'on_location')},
            'to_hospital': {'invisible': Equal(Eval('state'), 'to_hospital')},
            'at_hospital': {'invisible': Equal(Eval('state'), 'at_hospital')},
            'returning': {'invisible': Equal(Eval('state'), 'returning')},
            'out_of_service': {'invisible': Equal(Eval('state'),
            'out_of_service')},
            })


    @classmethod
    @ModelView.button
    def available(cls, ambulances):
        cls.update_ambulance_status(ambulances, status='available')

    @classmethod
    @ModelView.button
    def dispatched(cls, ambulances):
        cls.update_ambulance_status(ambulances, status='dispatched')

    @classmethod
    @ModelView.button
    def en_route(cls, ambulances):
         cls.update_ambulance_status(ambulances, status='en_route')

    @classmethod
    @ModelView.button
    def on_location(cls, ambulances):
        cls.update_ambulance_status(ambulances, status='on_location')

    @classmethod
    @ModelView.button
    def to_hospital(cls, ambulances):
        cls.update_ambulance_status(ambulances, status='to_hospital')

    @classmethod
    @ModelView.button
    def at_hospital(cls, ambulances):
        cls.update_ambulance_status(ambulances, status='at_hospital')

    @classmethod
    @ModelView.button
    def returning(cls, ambulances):
        cls.update_ambulance_status(ambulances, status='returning')

    @classmethod
    @ModelView.button
    def out_of_service(cls, ambulances):
        cls.update_ambulance_status(ambulances, status='out_of_service')


    @classmethod
    def update_ambulance_status(cls, ambulances, status):
        # Update status on local support model for this ambulance
        cls.write(ambulances, {
            'state': status})
            
        # Write current status on ambulance model
        Ambulance = Pool().get('gnuhealth.ambulance')
        vehicle = []
        
        vehicle.append(ambulances[0].ambulance)
        
        Ambulance.write(vehicle, {
            'state': status })

        # Create a new current ambulance status on support request log
        Activity = Pool().get('gnuhealth.support_request.log')
        log = []
        timestamp = datetime.now()
        values = {
            'sr': 'ambulance',
            'action': 'ambulance',
            'remarks': status,
            'timestamp': timestamp,
            }
        values['sr'] = ambulances[0].sr
        
        log.append(values)
        Activity.create(log)


class AmbulanceHealthProfessional(ModelSQL, ModelView):
    'Ambulance Health Professionals'
    __name__ = 'gnuhealth.ambulance_hp'

    name = fields.Many2One('gnuhealth.ambulance.support', 'SR')

    healthprof = fields.Many2One(
        'gnuhealth.healthprofessional', 'Health Prof',
        help='Health Professional for this ambulance and support request')

class SupportRequestLog (ModelSQL, ModelView):
    'Ambulance associated to a Support Request'
    __name__ = 'gnuhealth.support_request.log'

    sr = fields.Many2One('gnuhealth.support_request',
        'SR', help="Support Request", required=True)

    timestamp = fields.DateTime('Time', required=True,
        help="Date and time of activity")

    action = fields.Selection([
        (None, ''),
        ('ambulance', 'Ambulance'),
        ('general', 'General'),
        ], 'Activity',sort=False, help="Activity log")

    remarks = fields.Char('Remarks', help="Remarks for this item")
    

    @staticmethod
    def default_timestamp():
        return datetime.now()

    @staticmethod
    def default_action():
        return 'general'
