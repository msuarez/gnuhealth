# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2008-2017 Luis Falcon <lfalcon@gnusolidario.org>
#    Copyright (C) 2011-2017 GNU Solidario <health@gnusolidario.org>
#    Copyright (C) 2015 Cédric Krier
#    Copyright (C) 2014-2015 Chris Zimmerman <siv@riseup.net>
#
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
from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta, date
from urllib.parse import urlencode
from urllib.parse import urlunparse
from collections import OrderedDict
from io import BytesIO

try:
    from PIL import Image
except ImportError:
    Image = None
from sql import Literal, Join, Table, Null
from sql.functions import Overlay, Position

from trytond.model import ModelView, ModelSingleton, ModelSQL, fields, Unique
from trytond.wizard import Wizard, StateAction, StateView, Button
from trytond.transaction import Transaction
from trytond import backend
from trytond.pyson import Eval, Not, Bool, PYSONEncoder, Equal, And, Or, If
from trytond.pool import Pool
from trytond.tools import grouped_slice, reduce_ids
from trytond.backend import name as backend_name

from uuid import uuid4
import string
import random
import pytz

__all__ = [
    'OperationalArea', 'OperationalSector', 'Occupation',
    'Ethnicity','DomiciliaryUnit','BirthCertificate','DeathCertificate',
    'Party','ContactMechanism', 'PersonName','PartyAddress',
    'DrugDoseUnits', 'MedicationFrequency', 'DrugForm', 'DrugRoute', 
    'MedicalSpecialty','HealthInstitution', 'HealthInstitutionSpecialties',
    'HealthInstitutionOperationalSector','HealthInstitutionO2M',
    'HospitalBuilding', 'HospitalUnit','HospitalOR', 'HospitalWard',
    'HospitalBed', 'HealthProfessional','HealthProfessionalSpecialties',
    'PhysicianSP', 'Family', 'FamilyMember', 'MedicamentCategory',
    'Medicament', 'ImmunizationSchedule', 'ImmunizationScheduleLine',
    'ImmunizationScheduleDose', 'PathologyCategory', 'PathologyGroup',
    'Pathology', 'DiseaseMembers', 'ProcedureCode', 
    'BirthCertExtraInfo','DeathCertExtraInfo', 'DeathUnderlyingCondition',
    'InsurancePlan', 'Insurance', 'AlternativePersonID',
    'Product', 'GnuHealthSequences', 'PatientData', 
    'PatientDiseaseInfo','Appointment', 'AppointmentReport',
    'OpenAppointmentReportStart', 'OpenAppointmentReport',
    'PatientPrescriptionOrder', 'PrescriptionLine', 'PatientMedication', 
    'PatientVaccination','PatientEvaluation',
    'Directions', 'SecondaryCondition', 'DiagnosticHypothesis',
    'SignsAndSymptoms', 'PatientECG', 'ProductTemplate']


def compute_age_from_dates(dob, deceased, dod, gender, caller, extra_date):
    """ Get the person's age.

    Calculate the current age of the patient or age at time of death.

    Returns:
    If caller == 'age': str in Y-M-D,
       caller == 'childbearing_age': boolean,
       caller == 'raw_age': [Y, M, D]
    
    """
    today = datetime.today().date()
           
    if dob:
        start = datetime.strptime(str(dob), '%Y-%m-%d')
        end = datetime.strptime(str(today),'%Y-%m-%d')
            
        if extra_date:
            end = datetime.strptime(str(extra_date), '%Y-%m-%d')
            
        if deceased:
            end = datetime.strptime(
                        str(dod), '%Y-%m-%d %H:%M:%S')

        rdelta = relativedelta(end, start)
        
            
        years_months_days = str(rdelta.years) + 'y ' \
            + str(rdelta.months) + 'm ' \
            + str(rdelta.days) + 'd'
        
    else:
        return None

    if caller == 'age':
        return years_months_days

    elif caller == 'childbearing_age':
        if (rdelta.years >= 11
           and rdelta.years <= 55 and gender == 'f'):
            return True
        else:
            return False

    elif caller == 'raw_age':
        return [rdelta.years, rdelta.months, rdelta.days]

    else:
        return None
        

class DomiciliaryUnit(ModelSQL, ModelView):
    'Domiciliary Unit'
    __name__ = 'gnuhealth.du'

    def get_parent(self, subdivision):
        # Recursively get the parent subdivisions
        if (subdivision.parent):
            return str(subdivision.rec_name) +'\n'+ \
                str(self.get_parent(subdivision.parent))
        else:
            return subdivision.rec_name
        
    def get_du_address(self, name):
        du_addr=''
        # Street
        if (self.address_street):
            du_addr = str(self.address_street) + ' ' + \
                str(self.address_street_number) + "\n"
            
        # Grab the parent subdivisions
        if (self.address_subdivision):
            du_addr = du_addr + \
                str(self.get_parent(subdivision=self.address_subdivision))
        
        # Zip Code
        if (self.address_zip):
            du_addr = du_addr +" - "+ self.address_zip

        # Country
        if (self.address_country):
            du_addr = du_addr +"\n"+ self.address_country.rec_name

        return du_addr

    name = fields.Char('Code', required=True)
    desc = fields.Char('Desc')
    address_street = fields.Char('Street')
    address_street_number = fields.Integer('Number')
    address_street_bis = fields.Char('Apartment')

    address_district = fields.Char(
        'District', help="Neighborhood, Village, Barrio....")

    address_municipality = fields.Char(
        'Municipality', help="Municipality, Township, county ..")
    address_city = fields.Char('City')
    address_zip = fields.Char('Zip Code')
    address_country = fields.Many2One(
        'country.country', 'Country', help='Country')

    address_subdivision = fields.Many2One(
        'country.subdivision', 'Subdivision',
        domain=[('country', '=', Eval('address_country'))],
        depends=['address_country'])

    operational_sector = fields.Many2One(
        'gnuhealth.operational_sector', 'Operational Sector')

    picture = fields.Binary('Picture')

    latitude = fields.Numeric('Latitude', digits=(3, 14))
    longitude = fields.Numeric('Longitude', digits=(4, 14))
    altitude = fields.Integer('Altitude', help="Altitude in meters")

    urladdr = fields.Char(
        'OSM Map',
        help="Locates the DU on the Open Street Map by default")

    # Text Representation
    address_repr = fields.Function(fields.Text("DU Address"),
        'get_du_address')
        
    # Infrastructure

    dwelling = fields.Selection([
        (None, ''),
        ('single_house', 'Single / Detached House'),
        ('apartment', 'Apartment'),
        ('townhouse', 'Townhouse'),
        ('factory', 'Factory'),
        ('building', 'Building'),
        ('mobilehome', 'Mobile House'),
        ], 'Type', sort=False)

    materials = fields.Selection([
        (None, ''),
        ('concrete', 'Concrete'),
        ('adobe', 'Adobe'),
        ('wood', 'Wood'),
        ('mud', 'Mud / Straw'),
        ('stone', 'Stone'),
        ], 'Material', sort=False)

    roof_type = fields.Selection([
        (None, ''),
        ('concrete', 'Concrete'),
        ('adobe', 'Adobe'),
        ('wood', 'Wood'),
        ('mud', 'Mud'),
        ('thatch', 'Thatched'),
        ('stone', 'Stone'),
        ], 'Roof', sort=False)

    total_surface = fields.Integer('Surface', help="Surface in sq. meters")
    bedrooms = fields.Integer('Bedrooms')
    bathrooms = fields.Integer('Bathrooms')

    housing = fields.Selection([
        (None, ''),
        ('0', 'Shanty, deficient sanitary conditions'),
        ('1', 'Small, crowded but with good sanitary conditions'),
        ('2', 'Comfortable and good sanitary conditions'),
        ('3', 'Roomy and excellent sanitary conditions'),
        ('4', 'Luxury and excellent sanitary conditions'),
        ], 'Conditions',
        help="Housing and sanitary living conditions", sort=False)

    sewers = fields.Boolean('Sanitary Sewers')
    water = fields.Boolean('Running Water')
    trash = fields.Boolean('Trash recollection')
    electricity = fields.Boolean('Electrical supply')
    gas = fields.Boolean('Gas supply')
    telephone = fields.Boolean('Telephone')
    television = fields.Boolean('Television')
    internet = fields.Boolean('Internet')

    members = fields.One2Many('party.party', 'du', 'Members', readonly=True)

    @fields.depends('latitude', 'longitude', 'address_street',
        'address_street_number', 'address_district', 'address_municipality',
        'address_city', 'address_zip', 'address_subdivision',
        'address_country')
    def on_change_with_urladdr(self):
        # Generates the URL to be used in OpenStreetMap
        #   If latitude and longitude are known, use them.
        #   Otherwise, use street, municipality, city, and so on.


        parts = OrderedDict()
        parts['scheme'] = 'http'
        parts['netloc'] = ''
        parts['path'] = ''
        parts['params'] = ''
        parts['query'] = ''
        parts['fragment'] = ''

        if (self.latitude and self.longitude):
            parts['netloc'] = 'openstreetmap.org'
            parts['path'] = '/'
            parts['query'] = urlencode({'mlat': self.latitude,
                                        'mlon': self.longitude})

        else:
            state = country = postalcode = city = municipality = street = number = ''
            if self.address_street_number is not None:
                number = str(self.address_street_number)
            if self.address_street:
                street = self.address_street
            if self.address_municipality:
                municipality = self.address_municipality
            if self.address_city:
                city = self.address_city
            if self.address_zip:
                postalcode = self.address_zip
            if self.address_subdivision:
                state = self.address_subdivision.name
            if self.address_country:
                country = self.address_country.code

            parts['netloc'] = 'nominatim.openstreetmap.org'
            parts['path'] = 'search'
            parts['query'] = urlencode({'street': ' '.join([number, street]).strip(),
                                        'county': municipality,
                                        'city': city,
                                        'state': state,
                                        'postalcode': postalcode,
                                        'country': country})

        return urlunparse(list(parts.values()))

    # Show the resulting Address representation in realtime
    @fields.depends('address_street', 'address_subdivision', 
        'address_street_number', 'address_country')
    def on_change_with_address_repr(self):
        return self.get_du_address(name=None)

    @classmethod
    def __setup__(cls):
        super(DomiciliaryUnit, cls).__setup__()
        t = cls.__table__()
        cls._sql_constraints = [
            ('code_uniq', Unique(t, t.name),
             'The Domiciliary Unit must be unique !')
        ]
 
class Party(ModelSQL, ModelView):
    __name__ = 'party.party'

    def person_age(self, name):
        return compute_age_from_dates(self.dob, self.deceased,
                              self.dod, self.gender, name, None)


    def get_du_address(self, name):
        if (self.du):
            return self.du.address_repr

    person_names = fields.One2Many('gnuhealth.person_name','party',
        'Person Names',
        states={'invisible': Not(Bool(Eval('is_person')))})

    name_representation = fields.Selection([
        (None, ''),
        ('pgfs', 'Prefix Given Family, Suffix'),
        ('gf', 'Given Family'),
        ('fg', 'Family, Given'),
        ], 'Name Representation',
        states={'invisible': Not(Bool(Eval('is_person')))})


    activation_date = fields.Date(
        'Activation date', help='Date of activation of the party')

    federation_account = fields.Char('Federation ID')

    ref = fields.Char(
        'PUID',
        help='Person Unique Identifier',
        states={'invisible': Not(Bool(Eval('is_person')))})

    unidentified = fields.Boolean(
        'Unidentified',
        help='Patient is currently unidentified',
        states={'invisible': Not(Bool(Eval('is_person')))})

    is_person = fields.Boolean(
        'Person',
        help='Check if the party is a person.')

    is_patient = fields.Boolean(
        'Patient',
        states={'invisible': Not(Bool(Eval('is_person')))},
        help='Check if the party is a patient')

    is_healthprof = fields.Boolean(
        'Health Prof',
        states={'invisible': Not(Bool(Eval('is_person')))},
        help='Check if the party is a health professional')

    is_institution = fields.Boolean(
        'Institution', help='Check if the party is a Health Care Institution')
    is_insurance_company = fields.Boolean(
        'Insurance Company', help='Check if the party is an Insurance Company')
    is_pharmacy = fields.Boolean(
        'Pharmacy', help='Check if the party is a Pharmacy')

    lastname = fields.Char('Family names', help='Family or last names',
        states={'invisible': Not(Bool(Eval('is_person')))})
    dob = fields.Date('DoB', help='Date of Birth')

    age = fields.Function(fields.Char('Age'), 'person_age')

    gender = fields.Selection([
        (None, ''),
        ('m', 'Male'),
        ('f', 'Female'),
        ], 'Gender', states={'required': Bool(Eval('is_person'))})

    photo = fields.Binary('Picture')
    ethnic_group = fields.Many2One('gnuhealth.ethnicity', 'Ethnicity')

    marital_status = fields.Selection([
        (None, ''),
        ('s', 'Single'),
        ('m', 'Married'),
        ('c', 'Concubinage'),
        ('w', 'Widowed'),
        ('d', 'Divorced'),
        ('x', 'Separated'),
        ], 'Marital Status', sort=False)

    citizenship = fields.Many2One(
        'country.country', 'Citizenship', help='Country of Citizenship')
    residence = fields.Many2One(
        'country.country', 'Residence', help='Country of Residence')
    alternative_identification = fields.Boolean(
        'Alternative IDs', help='Other types of '
        'identification, not the official PUID . '
        'Examples : Passport, foreign ID,..')

    alternative_ids = fields.One2Many(
        'gnuhealth.person_alternative_identification',
        'name', 'Alternative IDs',
        states={'invisible': Not(Bool(Eval('alternative_identification')))})

    insurance = fields.One2Many('gnuhealth.insurance', 'name', 'Insurances',
        help="Insurance Plans associated to this party")

    internal_user = fields.Many2One(
        'res.user', 'Internal User',
        help='In GNU Health is the user (person) '
        'that logins. When the'
        ' party is a person, it will be the user'
        ' that maps the party.',
        states={
            'invisible': Not(Bool(Eval('is_person'))),
            })

    insurance_company_type = fields.Selection([
        (None, ''),
        ('state', 'State'),
        ('labour_union', 'Labour Union / Syndical'),
        ('private', 'Private'),
        ], 'Insurance Type', select=True)
    insurance_plan_ids = fields.One2Many(
        'gnuhealth.insurance.plan', 'company', 'Insurance Plans')

    du = fields.Many2One('gnuhealth.du', 'DU', help="Domiciliary Unit")

    du_address = fields.Function(
        fields.Text('Main address', 
        help="Main Address, based on the associated DU"),'get_du_address')

    birth_certificate = fields.Many2One('gnuhealth.birth_certificate',
        'Birth Certificate', readonly=True)

    deceased = fields.Boolean('Deceased', readonly=True,
        help='The information is updated from the Death Certificate',
        states={'invisible': Not(Bool(Eval('deceased')))})

    dod = fields.Function(fields.DateTime(
        'Date of Death',
        states={
            'invisible': Not(Bool(Eval('deceased'))),
            },
        depends=['deceased']),'get_dod')

    death_certificate = fields.Many2One('gnuhealth.death_certificate',
        'Death Certificate', readonly=True)

    mother = fields.Function(
        fields.Many2One('party.party','Mother', 
        help="Mother from the Birth Certificate"),'get_mother')

    father = fields.Function(
        fields.Many2One('party.party','Father', 
        help="Father from the Birth Certificate"),'get_father')

    def get_mother(self, name):
        if (self.birth_certificate and self.birth_certificate.mother):
            return self.birth_certificate.mother.id

    def get_father(self, name):
        if (self.birth_certificate and self.birth_certificate.father):
            return self.birth_certificate.father.id

    def get_dod(self, name):
        if (self.deceased):
            return self.death_certificate.dod

    @staticmethod
    def default_activation_date():
        return date.today()

    @classmethod
    def generate_puid(cls):
        # Add a default random string in the ref field.
        # The STRSIZE constant provides the length of the PUID
        # The format of the PUID is XXXNNNXXX
        # By default, this field will be used only if nothing is entered
        
        STRSIZE = 9
        puid = ''
        for x in range(STRSIZE): 
            if ( x < 3 or x > 5 ):
                puid = puid + random.choice(string.ascii_uppercase)
            else:
                puid = puid + random.choice(string.digits)
        return puid

    @classmethod
    def convert_photo(cls, data):
        if data and Image:
            image = Image.open(BytesIO(data))
            image.thumbnail((200, 200), Image.ANTIALIAS)
            data = BytesIO()
            image.save(data, image.format)
            data = fields.Binary.cast(data.getvalue())
        return data

    @classmethod
    def write(cls, *args):
        actions = iter(args)
        args = []
        for parties, vals in zip(actions, actions):
            given_name=family_name=''
            vals = vals.copy()
            person_id = parties[0].id
            # We use this method overwrite to make the fields that have a
            # unique constraint get the NULL value at PostgreSQL level, and not
            # the value '' coming from the client
            if vals.get('ref') == '':
                vals['ref'] = None

            if vals.get('federation_account') == '':
                vals['federation_account'] = None

            if 'photo' in vals:
                vals['photo'] = cls.convert_photo(vals['photo'])
            
            if ('name' in vals) or ('lastname' in vals):
                given_name=family_name=''
                if 'name' in vals:
                    given_name = vals['name']
                if 'lastname' in vals:
                    family_name=vals['lastname']

                if parties[0].is_person:
                    cls.update_person_official_name(person_id,given_name,
                        family_name)

            args.append(parties)
            args.append(vals)
        return super(Party, cls).write(*args)

    @classmethod
    def update_person_official_name(cls,person_id,given_name,family_name):
        # Create or update the official PersonName entry with the Given / Family
        # names from the main entry field.
        person=[]
        
        Pname = Pool().get('gnuhealth.person_name')
        officialnames = Pname.search(
            [("party", "=", person_id), ("use", "=", 'official')],)
            
        # If no official name found, create a new record
        if not (officialnames):
            values = {
                'party': person_id,
                'use': 'official',
                }

            if given_name:
                values['given'] = given_name
            if family_name:
                values['family'] = family_name

            person.append(values)
            Pname.create(person)

        #Found a related official name record, then 
        #update official Person Name(s) when modified in main form
        else:
            official_rec=[]
            official_rec.append(officialnames[0])

            values = {'use': 'official'}
            
            if given_name:
                values['given'] = given_name
            if family_name:
                values['family'] = family_name
            
            Pname.write(official_rec, values)

    
    @classmethod
    def create(cls, vlist):
        Configuration = Pool().get('party.configuration')

        vlist = [x.copy() for x in vlist]
        for values in vlist:

            if not 'ref' in values or values['ref'] == '':
                values['ref'] = cls.generate_puid()
                if 'unidentified' in values and values['unidentified']:
                    values['ref'] = 'NN-' + values.get('ref')
                if 'is_person' in values and not values['is_person']:
                    values['ref'] = 'NP-' + values['ref']
            if not values.get('code'):
                config = Configuration(1)
                # Use the company name . Initially, use the name
                # since the company hasn't been created yet.
                suffix = Transaction().context.get('company.rec_name') \
                    or values['name']
                # Generate the party code in the form of 
                # "UUID-" . Where company is the name of the Health
                # Institution.
                #
                # The field "code" is the one that is used in distributed
                # environments, with multiple GNU Health instances across
                # a country / region
                values['code'] = '%s-%s' % (uuid4(), suffix)

            if not 'federation_account' in values or \
                values['federation_account'] == '':
                    values['federation_account'] = None
            
            values.setdefault('addresses', None)

            if 'photo' in values:
                values['photo'] = cls.convert_photo(values['photo'])

            
            #If the party is a physical person, 
            #add new PersonName record with the given and family name
            #as the official name
            
            if (values.get('is_person')):
                if ('name' in values) or ('lastname' in values):
                    official_name = []
                    given_name = family_name= ''

                    if 'name' in values:
                        given_name = values['name']
                    if 'lastname' in values:
                        family_name=values['lastname']
                                        
                    official_name.append(('create', [{
                        'use': 'official',
                        'given': given_name,
                        'family': family_name,
                        }]))

                    values['person_names'] = official_name
                
        return super(Party, cls).create(vlist)

    @classmethod
    def __setup__(cls):
        super(Party, cls).__setup__()
        t = cls.__table__()
        cls._sql_constraints += [
            ('ref_uniq', Unique(t,t.ref), 'The PUID must be unique'),
            ('internal_user_uniq', Unique(t,t.internal_user),
                'This internal user is already assigned to a party'),
            ('federation_account_uniq', 
                Unique(t,t.federation_account),
                'The Federation Account must be unique'),]

        cls._order.insert(0, ('lastname', 'ASC'))
        cls._order.insert(1, ('name', 'ASC'))
        #Sort to be used when called from other models.
        cls._order_name = 'lastname'
        
    def get_rec_name(self, name):
        #Display name on the following sequence
        # 1 - Oficial Name from PersonName with the name representation
        # If not offficial name :
        # 2 - Last name, First name
        
        if self.person_names:            
            prefix = given = family = suffix = ''
            for pname in self.person_names:
                if pname.prefix:
                    prefix = pname.prefix + ' ' 
                if pname.suffix:
                    suffix = ', ' + pname.suffix

                given = pname.given or ''
                family = pname.family or ''

                res=''
                if pname.use == 'official':
                    if self.name_representation == 'pgfs':
                        res = prefix + given + ' ' + family + suffix
                    if self.name_representation == 'gf':
                        if pname.family:
                            family = ' ' + pname.family
                        res = given + family
                    if self.name_representation == 'fg':
                        if pname.family:
                            family = pname.family + ', '
                        res = family + given

                    if not self.name_representation:
                        # Default value
                        if family:
                            return family + ', ' + given
                        else:
                            return given
                return res
                    
        if self.lastname:
            return self.lastname + ', ' + self.name
        else:
            return self.name

    @classmethod
    def search_rec_name(cls, name, clause):
        """ Search for the name, lastname, PUID, any alternative IDs,
            and any family and / or given name from the person_names
        """
        if clause[1].startswith('!') or clause[1].startswith('not '):
            bool_op = 'AND'
        else:
            bool_op = 'OR'
        return [bool_op,
            ('ref',) + tuple(clause[1:]),
            ('alternative_ids.code',) + tuple(clause[1:]),
            ('federation_account',) + tuple(clause[1:]),
            ('contact_mechanisms.value',) + tuple(clause[1:]),
            ('person_names.family',) + tuple(clause[1:]),            
            ('person_names.given',) + tuple(clause[1:]),            
            ('name',) + tuple(clause[1:]),
            ('lastname',) + tuple(clause[1:]),
            ]

    @fields.depends('is_person', 'is_patient', 'is_healthprof')
    def on_change_with_is_person(self):
        # Set is_person if the party is a health professional or a patient
        if (self.is_healthprof or self.is_patient or self.is_person):
            return True

    @fields.depends('du')
    def on_change_with_du_address(self):
        if (self.du):
            return self.get_du_address(name=None)

    @classmethod
    def validate(cls, parties):
        super(Party, cls).validate(parties)
        for party in parties:
            party.check_person()
            party.validate_official_name()
            
    def check_person(self):
        # Verify that health professional and patient
        # are unchecked when is_person is False

        if not self.is_person and (self.is_patient or self.is_healthprof):
            self.raise_user_error(
                "The Person field must be set if the party is a health"
                " professional or a patient")


    def validate_official_name(self):
        # Only allow one official name on the party name
        Pname = Pool().get('gnuhealth.person_name')
        officialnames = Pname.search_count(
            [("party", "=", self.id), ("use", "=", 'official')],)
    
        if (officialnames > 1):
                        self.raise_user_error(
                "The person can have only one official name")
    
    
    @classmethod
    def view_attributes(cls):
        # Hide the group holding all the demographics when the party is not
        # a person
        return [('//group[@id="person_details"]', 'states', {
                'invisible': ~Eval('is_person'),
                })]
                
class ContactMechanism(ModelSQL, ModelView):
    __name__ = 'party.contact_mechanism'

    emergency = fields.Boolean('Emergency', select=True)
    remarks = fields.Char('Remarks',help="Enter the name of the contact"
        " or other remarks")


class PersonName(ModelSQL, ModelView):
    "Person Name"
    __name__ = 'gnuhealth.person_name'
    
    """ We are using the concept of HumanName on HL7 FHIR
    http://www.hl7.org/implement/standards/fhir/datatypes.html#HumanName
    """
    
    party = fields.Many2One('party.party','Person',  
        domain=[('is_person', '=', True)], help="Related party (person)")
        
    use = fields.Selection([
        (None, ''),
        ('official', 'Official'),
        ('usual', 'Usual'),
        ('nickname', 'Nickname'),
        ('maiden', 'Maiden'),
        ('anonymous', 'Anonymous'),
        ('temp', 'Temp'),
        ('old', 'old'),
        ], 'Use', sort=False, required=True)
    family = fields.Char('Family', 
        help="Family / Surname.")
    given = fields.Char('Given', 
        help="Given / First name. May include middle name", required=True)
    prefix = fields.Selection([
        (None, ''),
        ('Mr', 'Mr'),
        ('Mrs', 'Mrs'),
        ('Miss', 'Miss'),
        ('Dr', 'Dr'),
        ], 'Prefix', sort=False)
    suffix = fields.Char('Suffix')
    date_from = fields.Date('From')
    date_to = fields.Date('To')


class PartyAddress(ModelSQL, ModelView):
    'Party Address'
    __name__ = 'party.address'

    relationship = fields.Char(
        'Relationship',
        help='Include the relationship with the person - friend, co-worker,'
        ' brother,...')
    relative_id = fields.Many2One(
        'party.party', 'Contact', domain=[('is_person', '=', True)],
        help='Include link to the relative')

    is_school = fields.Boolean(
        "School", help="Check this box to mark the school address")
    is_work = fields.Boolean(
        "Work", help="Check this box to mark the work address")

class DrugDoseUnits(ModelSQL, ModelView):
    'Drug Dose Unit'
    __name__ = 'gnuhealth.dose.unit'

    name = fields.Char('Unit', required=True, select=True, translate=True)
    desc = fields.Char('Description', translate=True)

    @classmethod
    def __setup__(cls):
        super(DrugDoseUnits, cls).__setup__()
        t = cls.__table__()

        cls._sql_constraints = [
            ('name_uniq', Unique(t,t.name), 'The Unit must be unique !'),
        ]


class MedicationFrequency(ModelSQL, ModelView):
    'Medication Common Frequencies'
    __name__ = 'gnuhealth.medication.dosage'

    name = fields.Char(
        'Frequency', required=True, select=True, translate=True,
        help='Common frequency name')
    code = fields.Char(
        'Code', required=True,
        help='Dosage Code,for example: SNOMED 229798009 = 3 times per day.'
           'Please use CAPITAL LETTERS and no spaces')
    abbreviation = fields.Char(
        'Abbreviation',
        help='Dosage abbreviation, such as tid in the US or tds in the UK')

    @classmethod
    def __setup__(cls):
        super(MedicationFrequency, cls).__setup__()
        t = cls.__table__()
        cls._sql_constraints = [
            ('name_uniq', Unique(t,t.name), 'The Unit must be unique !'),
            ('code_uniq', Unique(t,t.code), 'The CODE must be unique !'),
        ]


class DrugForm(ModelSQL, ModelView):
    'Drug Form'
    __name__ = 'gnuhealth.drug.form'

    name = fields.Char('Form', required=True, select=True, translate=True)
    code = fields.Char('Code', required=True,
        help="Please use CAPITAL LETTERS and no spaces")

    @classmethod
    def __setup__(cls):
        super(DrugForm, cls).__setup__()
        t = cls.__table__()
        cls._sql_constraints = [
            ('name_uniq', Unique(t,t.name), 'The Unit must be unique !'),
            ('code_uniq', Unique(t,t.code), 'The CODE must be unique !'),
        ]


class DrugRoute(ModelSQL, ModelView):
    'Drug Administration Route'
    __name__ = 'gnuhealth.drug.route'

    name = fields.Char('Unit', required=True, select=True, translate=True)
    code = fields.Char('Code', required=True,
        help="Please use CAPITAL LETTERS and no spaces")

    @classmethod
    def __setup__(cls):
        super(DrugRoute, cls).__setup__()
        t = cls.__table__()

        cls._sql_constraints = [
            ('name_uniq', Unique(t,t.name), 'The Name must be unique !'),
            ('code_uniq', Unique(t,t.code), 'The CODE must be unique !'),
        ]


class Occupation(ModelSQL, ModelView):
    'Occupation'
    __name__ = 'gnuhealth.occupation'

    name = fields.Char('Name', required=True, translate=True)
    code = fields.Char('Code',  required=True, 
        help="Please use CAPITAL LETTERS and no spaces")

    @classmethod
    def __setup__(cls):
        super(Occupation, cls).__setup__()
        t = cls.__table__()
        cls._sql_constraints = [
            ('name_uniq', Unique(t,t.name), 'The Name must be unique !'),
            ('code_uniq', Unique(t,t.code), 'The CODE must be unique !'),
        ]


class Ethnicity(ModelSQL, ModelView):
    'Ethnicity'
    __name__ = 'gnuhealth.ethnicity'

    name = fields.Char('Name', required=True, translate=True)
    code = fields.Char('Code', required=True,
        help="Please use CAPITAL LETTERS and no spaces")
    notes = fields.Char('Notes')

    @classmethod
    def __setup__(cls):
        super(Ethnicity, cls).__setup__()
        t = cls.__table__()

        cls._sql_constraints = [
            ('name_uniq', Unique(t,t.name), 'The Name must be unique !'),
            ('code_uniq', Unique(t,t.code), 'The CODE must be unique !'),

        ]

class OperationalArea(ModelSQL, ModelView):
    'Operational Area'
    __name__ = 'gnuhealth.operational_area'

    name = fields.Char(
        'Name', required=True, help='Operational Area of the city or region')

    operational_sector = fields.One2Many(
        'gnuhealth.operational_sector', 'operational_area',
        'Operational Sector', readonly=True)

    info = fields.Text('Extra Information')

    @classmethod
    def __setup__(cls):
        super(OperationalArea, cls).__setup__()
        t = cls.__table__()
        cls._sql_constraints += [
            ('name_uniq', Unique(t,t.name),
                'The operational area must be unique !'),
        ]


class OperationalSector(ModelSQL, ModelView):
    'Operational Sector'
    __name__ = 'gnuhealth.operational_sector'

    name = fields.Char(
        'Op. Sector', required=True,
        help='Region included in an operational area')

    operational_area = fields.Many2One(
        'gnuhealth.operational_area', 'Operational Area')

    info = fields.Text('Extra Information')

    @classmethod
    def __setup__(cls):
        super(OperationalSector, cls).__setup__()
        t = cls.__table__()
        cls._sql_constraints += [
            ('name_uniq', Unique(t,t.name, t.operational_area),
                'The operational sector must be unique in each'
                ' operational area!'),
        ]



# HEALTH INSTITUTION
class HealthInstitution(ModelSQL, ModelView):
    'Health Institution'
    __name__ = 'gnuhealth.institution'

    @classmethod
    def get_institution(cls):
        # Retrieve the institution associated to this GNU Health instance
        # That is associated to the Company.
        
        company = Transaction().context.get('company')
        
        cursor = Transaction().connection.cursor()
        cursor.execute('SELECT party FROM company_company WHERE id=%s \
            LIMIT 1', (company,))
        party_id = cursor.fetchone()
        if party_id:
            cursor = Transaction().connection.cursor()
            cursor.execute('SELECT id FROM gnuhealth_institution WHERE \
                name = %s LIMIT 1', (party_id[0],))
            institution_id = cursor.fetchone()
            if (institution_id):
                return int(institution_id[0])
        

    name = fields.Many2One(
        'party.party', 'Institution',
        domain=[('is_institution', '=', True)],
        help='Party Associated to this Health Institution',
        required=True,
        states={'readonly': Bool(Eval('name'))})
        
    code = fields.Char('Code', required=True,
        help="Institution code")

    picture = fields.Binary('Picture')

    institution_type = fields.Selection((
        (None, ''),
        ('doctor_office', 'Doctor office'),
        ('primary_care', 'Primary Care Center'),
        ('clinic', 'Clinic'),
        ('hospital', 'General Hospital'),
        ('specialized', 'Specialized Hospital'),
        ('nursing_home', 'Nursing Home'),
        ('hospice', 'Hospice'),
        ('rural', 'Rural facility'),
        ), 'Type', required=True, sort=False)
   
    beds = fields.Integer("Beds")

    operating_room = fields.Boolean("Operating Room", 
        help="Check this box if the institution" \
        " has operating rooms",
        )
    or_number = fields.Integer("ORs",
        states={'invisible': Not(Bool(Eval('operating_room')))})
    
    public_level = fields.Selection((
        (None, ''),
        ('private', 'Private'),
        ('public', 'Public'),
        ('mixed', 'Private - State'),
        ), 'Public Level', required=True, sort=False)

    teaching = fields.Boolean("Teaching", help="Mark if this is a" \
        " teaching institution")
    heliport = fields.Boolean("Heliport")
    trauma_center = fields.Boolean("Trauma Center")
    trauma_level = fields.Selection((
        (None, ''),
        ('one', 'Level I'),
        ('two', 'Level II'),
        ('three', 'Level III'),
        ('four', 'Level IV'),
        ('five', 'Level V'),
        ), 'Trauma Level', sort=False,
        states={'invisible': Not(Bool(Eval('trauma_center')))})
    
    extra_info = fields.Text("Extra Info")

    def get_rec_name(self, name):
        if self.name:
            return self.name.name

    @classmethod
    def __setup__(cls):
        super(HealthInstitution, cls).__setup__()
        t = cls.__table__()
        cls._sql_constraints = [
            ('name_uniq', Unique(t,t.name), 'This Institution already exists !'),
            ('code_uniq', Unique(t,t.code), 'This CODE already exists !'),
        ]


class HealthInstitutionSpecialties(ModelSQL, ModelView):
    'Health Institution Specialties'
    __name__ = 'gnuhealth.institution.specialties'

    name = fields.Many2One('gnuhealth.institution', 'Institution',
        required=True)
    specialty = fields.Many2One('gnuhealth.specialty', 'Specialty',
        required=True)

    
    def get_rec_name(self, name):
        if self.specialty:
            return self.specialty.name

    @classmethod
    def __setup__(cls):
        super(HealthInstitutionSpecialties, cls).__setup__()
        t = cls.__table__()
        cls._sql_constraints = [
            ('name_sp_uniq', Unique(t,t.name, t.specialty),
                'The Specialty already exists for this institution'),
        ]

class HealthInstitutionOperationalSector(ModelSQL, ModelView):
    'Operational Sectors covered by Institution'
    __name__ = 'gnuhealth.institution.operationalsector'

    name = fields.Many2One('gnuhealth.institution', 'Institution',
        required=True)
    operational_sector = fields.Many2One('gnuhealth.operational_sector',
        'Operational Sector', required=True)

    @classmethod
    def __setup__(cls):
        super(HealthInstitutionOperationalSector, cls).__setup__()
        t = cls.__table__()
        cls._sql_constraints = [
            ('name_os_uniq', Unique(t,t.name, t.operational_sector),
                'The Operational Sector already exists for this institution'),
        ]

class HealthInstitutionO2M(ModelSQL, ModelView):
    'Health Institution'
    __name__ = 'gnuhealth.institution'

    # Add Specialties to the Health Institution
    specialties = fields.One2Many('gnuhealth.institution.specialties',
        'name','Specialties',
        help="Specialties Provided in this Health Institution")

    main_specialty = fields.Many2One('gnuhealth.institution.specialties',
        'Specialty',
        domain=[('name', '=', Eval('id'))],
        depends=['specialties', 'institution_type', 'id'],
        help="Choose the speciality in the case of Specialized Hospitals" \
            " or where this center excels", 
        
        # Allow to select the institution specialty only if the record already
        # exists
        states={'required': And(Eval('institution_type') == 'specialized',
            Eval('id', 0) > 0),
            'readonly': Eval('id', 0) < 0})

    # Add Specialties to the Health Institution
    operational_sectors = fields.One2Many('gnuhealth.institution.operationalsector',
        'name','Operational Sector',
        help="Operational Sectors covered by this institution")


# HEALTH CENTER / HOSPITAL INFRASTRUCTURE
class HospitalBuilding(ModelSQL, ModelView):
    'Hospital Building'
    __name__ = 'gnuhealth.hospital.building'

    name = fields.Char(
        'Name', required=True,
        help='Name of the building within the institution')

    institution = fields.Many2One(
        'gnuhealth.institution', 'Institution', required=True,
        help='Health Institution of this building')

    code = fields.Char('Code', required=True)
    extra_info = fields.Text('Extra Info')

    @staticmethod
    def default_institution():
        return HealthInstitution().get_institution()

    @classmethod
    def __setup__(cls):
        super(HospitalBuilding, cls).__setup__()
        t = cls.__table__()
        cls._sql_constraints = [
            ('name_uniq', Unique(t,t.name, t.institution),
                'The Building name must be unique per Health'
                ' Center'),
            ('code_uniq', Unique(t,t.code, t.institution),
                'The Building code must be unique per Health'
                ' Center'),
        ]


class HospitalUnit(ModelSQL, ModelView):
    'Hospital Unit'
    __name__ = 'gnuhealth.hospital.unit'

    name = fields.Char(
        'Name', required=True,
        help='Name of the unit, eg Neonatal, Intensive Care, ...')

    institution = fields.Many2One(
        'gnuhealth.institution', 'Institution',required=True,
        help='Health Institution')

    code = fields.Char('Code', required=True)
    extra_info = fields.Text('Extra Info')

    @staticmethod
    def default_institution():
        return HealthInstitution().get_institution()

    @classmethod
    def __setup__(cls):
        super(HospitalUnit, cls).__setup__()
        t = cls.__table__()
        cls._sql_constraints = [
            ('name_uniq', Unique(t,t.name, t.institution),
                'The Unit NAME must be unique per Health'
                ' Center'),
            ('code_uniq', Unique(t,t.code, t.institution),
                'The Unit CODE must be unique per Health'
                ' Center'),
        ]


class HospitalOR(ModelSQL, ModelView):
    'Operating Room'
    __name__ = 'gnuhealth.hospital.or'

    name = fields.Char(
        'Name', required=True, help='Name of the Operating Room')

    institution = fields.Many2One(
        'gnuhealth.institution', 'Institution', required=True,
        help='Health Institution')

    building = fields.Many2One(
        'gnuhealth.hospital.building', 'Building',
        domain=[('institution', '=', Eval('institution'))],
        depends=['institution'],
        select=True)

    unit = fields.Many2One('gnuhealth.hospital.unit', 'Unit',
        domain=[('institution', '=', Eval('institution'))],
        depends=['institution'])
    extra_info = fields.Text('Extra Info')

    state = fields.Selection((
        (None, ''),
        ('free', 'Free'),
        ('confirmed', 'Confirmed'),
        ('occupied', 'Occupied'),
        ('na', 'Not available'),
        ), 'Status', readonly=True, sort=False)

    @staticmethod
    def default_institution():
        return HealthInstitution().get_institution()

    @staticmethod
    def default_state():
        return 'free'

    @classmethod
    def __setup__(cls):
        super(HospitalOR, cls).__setup__()
        t = cls.__table__()
        cls._sql_constraints = [
            ('name_uniq', Unique(t,t.name, t.institution),
                'The Operating Room Name must be unique per Health'
                ' Center'),
        ]


class HospitalWard(ModelSQL, ModelView):
    'Hospital Ward'
    __name__ = 'gnuhealth.hospital.ward'

    name = fields.Char('Name', required=True, help='Ward / Room code')

    institution = fields.Many2One(
        'gnuhealth.institution', 'Institution',required=True,
        help='Health Institution')

    building = fields.Many2One('gnuhealth.hospital.building', 'Building',
        domain=[('institution', '=', Eval('institution'))],
        depends=['institution'])
    floor = fields.Integer('Floor Number')
    unit = fields.Many2One('gnuhealth.hospital.unit', 'Unit',
        domain=[('institution', '=', Eval('institution'))],
        depends=['institution'])

    private = fields.Boolean(
        'Private', help='Check this option for private room')

    bio_hazard = fields.Boolean(
        'Bio Hazard', help='Check this option if there is biological hazard')

    number_of_beds = fields.Integer(
        'Number of beds', help='Number of patients per ward')

    telephone = fields.Boolean('Telephone access')
    ac = fields.Boolean('Air Conditioning')
    private_bathroom = fields.Boolean('Private Bathroom')
    guest_sofa = fields.Boolean('Guest sofa-bed')
    tv = fields.Boolean('Television')
    internet = fields.Boolean('Internet Access')
    refrigerator = fields.Boolean('Refrigerator')
    microwave = fields.Boolean('Microwave')

    gender = fields.Selection((
        (None, ''),
        ('men', 'Men Ward'),
        ('women', 'Women Ward'),
        ('unisex', 'Unisex'),
        ), 'Gender', required=True, sort=False)

    state = fields.Selection((
        (None, ''),
        ('beds_available', 'Beds available'),
        ('full', 'Full'),
        ('na', 'Not available'),
        ), 'Status', sort=False)

    extra_info = fields.Text('Extra Info')

    @staticmethod
    def default_gender():
        return 'unisex'

    @staticmethod
    def default_number_of_beds():
        return 1

    @staticmethod
    def default_institution():
        return HealthInstitution().get_institution()

    @classmethod
    def __setup__(cls):
        super(HospitalWard, cls).__setup__()
        t = cls.__table__()
        cls._sql_constraints = [
            ('name_uniq', Unique(t,t.name, t.institution),
                'The Ward / Room Name must be unique per Health'
                ' Center'),
        ]


class HospitalBed(ModelSQL, ModelView):
    'Hospital Bed'
    __name__ = 'gnuhealth.hospital.bed'
    _rec_name = 'telephone_number'

    name = fields.Many2One(
        'product.product', 'Bed', required=True,
        domain=[('is_bed', '=', True)],
        help='Bed Number')

    institution = fields.Many2One(
        'gnuhealth.institution', 'Institution', required=True,
        help='Health Institution')

    ward = fields.Many2One(
        'gnuhealth.hospital.ward', 'Ward',
        domain=[('institution', '=', Eval('institution'))],
        depends=['institution'],
        help='Ward or room')

    bed_type = fields.Selection((
        (None, ''),
        ('gatch', 'Gatch Bed'),
        ('electric', 'Electric'),
        ('stretcher', 'Stretcher'),
        ('low', 'Low Bed'),
        ('low_air_loss', 'Low Air Loss'),
        ('circo_electric', 'Circo Electric'),
        ('clinitron', 'Clinitron'),
        ), 'Bed Type', required=True, sort=False)

    telephone_number = fields.Char(
        'Telephone Number', help='Telephone number / Extension')

    extra_info = fields.Text('Extra Info')

    state = fields.Selection((
        (None, ''),
        ('free', 'Free'),
        ('reserved', 'Reserved'),
        ('occupied', 'Occupied'),
        ('to_clean', 'Needs cleaning'),
        ('na', 'Not available'),
        ), 'Status', readonly=True, sort=False)

    @staticmethod
    def default_bed_type():
        return 'gatch'

    @staticmethod
    def default_state():
        return 'free'

    @staticmethod
    def default_institution():
        return HealthInstitution().get_institution()

    def get_rec_name(self, name):
        if self.name:
            return self.name.name

    @classmethod
    def search_rec_name(cls, name, clause):
        return [('name',) + tuple(clause[1:])]

    @classmethod
    def __setup__(cls):
        super(HospitalBed, cls).__setup__()
        t = cls.__table__()
        cls._sql_constraints = [
            ('name_uniq', Unique(t,t.name, t.institution),
                'The Bed must be unique per Health Center'),
        ]
        # Show fix button when is in state "needs cleaning" or "NA"
        cls._buttons.update({
                'fix_bed': {
                    'invisible': Or(Equal(Eval('state'), 'free'),
                        Equal(Eval('state'), 'occupied'),
                        Equal(Eval('state'), 'reserved')
                        )},
                    }),

    @classmethod
    @ModelView.button
    def fix_bed(cls, beds):
        cls.write(beds, {'state': 'free'})


class MedicalSpecialty(ModelSQL, ModelView):
    'Medical Specialty'
    __name__ = 'gnuhealth.specialty'

    name = fields.Char(
        'Specialty', required=True, translate=True,
        help='ie, Addiction Psychiatry')
    code = fields.Char('Code', required=True,
        help='ie, ADP. Please use CAPITAL LETTERS and no spaces')

    @classmethod
    def __setup__(cls):
        t = cls.__table__()
        cls._sql_constraints = [
            ('name_uniq', Unique(t,t.name), 'The Specialty must be unique !'),
            ('code_uniq', Unique(t,t.code), 'The CODE must be unique !'),
        ]
        super(MedicalSpecialty, cls).__setup__()

class HealthProfessional(ModelSQL, ModelView):
    'Health Professional'
    __name__ = 'gnuhealth.healthprofessional'

    @classmethod
    def get_health_professional(cls):
        # Get the professional associated to the internal user id
        # that logs into GNU Health
        cursor = Transaction().connection.cursor()
        User = Pool().get('res.user')
        user = User(Transaction().user)
        login_user_id = int(user.id)
        cursor.execute('SELECT id FROM party_party WHERE is_healthprof=True AND \
            internal_user = %s LIMIT 1', (login_user_id,))
        partner_id = cursor.fetchone()
        if partner_id:
            cursor = Transaction().connection.cursor()
            cursor.execute('SELECT id FROM gnuhealth_healthprofessional WHERE \
                name = %s LIMIT 1', (partner_id[0],))
            healthprof_id = cursor.fetchone()
            if (healthprof_id):
                return int(healthprof_id[0])
        else:
            cls.raise_user_error("No Health Professional associated to this user")

    name = fields.Many2One(
        'party.party', 'Health Professional', required=True,
        domain=[
            ('is_healthprof', '=', True),
            ('is_person', '=', True),
            ],
        help='Health Professional\'s Name, from the partner list')

    institution = fields.Many2One(
        'gnuhealth.institution', 'Institution',
        help='Main institution where she/he works')

    code = fields.Char('LICENSE ID', help='License ID')

    specialties = fields.One2Many(
        'gnuhealth.hp_specialty', 'name', 'Specialties')

    info = fields.Text('Extra info')

    puid = fields.Function(
        fields.Char('PUID', help="Person Unique Identifier"),
        'get_hp_puid', searcher='search_hp_puid')

    active = fields.Boolean('Active', select=True)

    @staticmethod
    def default_active():
        return True

    def get_hp_puid(self, name):
        return self.name.ref

    @staticmethod
    def default_institution():
        return HealthInstitution().get_institution()

    @classmethod
    def search_hp_puid(cls, name, clause):
        res = []
        value = clause[2]
        res.append(('name.ref', clause[1], value))
        return res

    @classmethod
    def __setup__(cls):
        super(HealthProfessional, cls).__setup__()
        t = cls.__table__()
        cls._sql_constraints = [
            ('hp_uniq', Unique(t,t.name),
                'The health professional must be unique'),
            ('code_uniq', Unique(t,t.code),
                'The LICENSE ID must be unique'),
        ]

    def get_rec_name(self, name):
        if self.name:
            res = self.name.name
            if self.name.lastname:
                res = self.name.lastname + ', ' + self.name.name
        return res

class HealthProfessionalSpecialties(ModelSQL, ModelView):
    'Health Professional Specialties'
    __name__ = 'gnuhealth.hp_specialty'

    name = fields.Many2One('gnuhealth.healthprofessional', 'Health Professional')

    specialty = fields.Many2One(
        'gnuhealth.specialty', 'Specialty', help='Specialty Code')

    def get_rec_name(self, name):
        return self.specialty.name


class PhysicianSP(ModelSQL, ModelView):
    # Add Main Specialty field after from the Health Professional Speciality
    'Health Professional'
    __name__ = 'gnuhealth.healthprofessional'

    main_specialty = fields.Many2One(
        'gnuhealth.hp_specialty', 'Main Specialty',
        domain=[('name', '=', Eval('id'))],
        states={'readonly': Eval('id', 0) < 0},
        depends=['id'])


class Family(ModelSQL, ModelView):
    'Family'
    __name__ = 'gnuhealth.family'

    name = fields.Char('Family', required=True, help='Family code')

    members = fields.One2Many(
        'gnuhealth.family_member', 'name', 'Family Members')

    info = fields.Text('Extra Information')

    @classmethod
    def __setup__(cls):
        super(Family, cls).__setup__()
        t = cls.__table__()
        cls._sql_constraints = [
            ('name_uniq', Unique(t,t.name), 'The Family Code must be unique !'),
        ]


class FamilyMember(ModelSQL, ModelView):
    'Family Member'
    __name__ = 'gnuhealth.family_member'

    name = fields.Many2One(
        'gnuhealth.family', 'Family', required=True, readonly=True,
        help='Family code')

    party = fields.Many2One(
        'party.party', 'Party', required=True,
        domain=[('is_person', '=', True)],
        help='Family Member')

    role = fields.Char('Role', help='Father, Mother, sibbling...')




# Use the template as in Product category.
class MedicamentCategory(ModelSQL, ModelView):
    'Medicament Category'
    __name__ = 'gnuhealth.medicament.category'

    name = fields.Char('Name', required=True, translate=True)

    parent = fields.Many2One(
        'gnuhealth.medicament.category', 'Parent', select=True)

    childs = fields.One2Many(
        'gnuhealth.medicament.category', 'parent', string='Children')


    @classmethod
    def __setup__(cls):
        super(MedicamentCategory, cls).__setup__()
        cls._order.insert(0, ('name', 'ASC'))

    @classmethod
    def validate(cls, categories):
        super(MedicamentCategory, cls).validate(categories)
        cls.check_recursion(categories, rec_name='name')

    def get_rec_name(self, name):
        if self.parent:
            return self.parent.get_rec_name(name) + ' / ' + self.name
        else:
            return self.name


class Medicament(ModelSQL, ModelView):
    'Medicament'
    __name__ = 'gnuhealth.medicament'
    
    name = fields.Many2One(
        'product.product', 'Product', required=True,
        domain=[('is_medicament', '=', True)],
        help='Product Name')

    active_component = fields.Char(
        'Active component', translate=True,
        help='Active Component')

    category = fields.Many2One(
        'gnuhealth.medicament.category', 'Category', select=True)

    therapeutic_action = fields.Char(
        'Therapeutic effect', help='Therapeutic action')

    composition = fields.Text('Composition', help='Components')
    indications = fields.Text('Indication', help='Indications')
    strength = fields.Float(
        'Strength',
        help='Amount of medication (eg, 250 mg) per dose')

    unit = fields.Many2One(
        'gnuhealth.dose.unit', 'dose unit',
        help='Unit of measure for the medication to be taken')

    route = fields.Many2One(
        'gnuhealth.drug.route', 'Administration Route',
        help='Drug administration route code.')

    form = fields.Many2One(
        'gnuhealth.drug.form', 'Form',
        help='Drug form, such as tablet, suspension, liquid ..')

    sol_conc = fields.Float(
        'Concentration',
        help='Solution drug concentration')

    sol_conc_unit = fields.Many2One(
        'gnuhealth.dose.unit', 'Unit',
        help='Unit of the drug concentration')
    
    sol_vol = fields.Float(
        'Volume',
        help='Solution concentration volume')

    sol_vol_unit = fields.Many2One(
        'gnuhealth.dose.unit', 'Unit',
        help='Unit of the solution volume')


    dosage = fields.Text('Dosage Instructions', help='Dosage / Indications')
    overdosage = fields.Text('Overdosage', help='Overdosage')
    pregnancy_warning = fields.Boolean(
        'Pregnancy Warning',
        help='The drug represents risk to pregnancy or lactancy')

    pregnancy = fields.Text(
        'Pregnancy and Lactancy', help='Warnings for Pregnant Women')

    pregnancy_category = fields.Selection([
        (None, ''),
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('X', 'X'),
        ('N', 'N'),
        ], 'Pregnancy Category',
        help='** FDA Pregnancy Categories ***\n'
        'CATEGORY A :Adequate and well-controlled human studies have failed'
        ' to demonstrate a risk to the fetus in the first trimester of'
        ' pregnancy (and there is no evidence of risk in later'
        ' trimesters).\n\n'
        'CATEGORY B : Animal reproduction studies have failed todemonstrate a'
        ' risk to the fetus and there are no adequate and well-controlled'
        ' studies in pregnant women OR Animal studies have shown an adverse'
        ' effect, but adequate and well-controlled studies in pregnant women'
        ' have failed to demonstrate a risk to the fetus in any'
        ' trimester.\n\n'
        'CATEGORY C : Animal reproduction studies have shown an adverse'
        ' effect on the fetus and there are no adequate and well-controlled'
        ' studies in humans, but potential benefits may warrant use of the'
        ' drug in pregnant women despite potential risks. \n\n '
        'CATEGORY D : There is positive evidence of human fetal  risk based'
        ' on adverse reaction data from investigational or marketing'
        ' experience or studies in humans, but potential benefits may warrant'
        ' use of the drug in pregnant women despite potential risks.\n\n'
        'CATEGORY X : Studies in animals or humans have demonstrated fetal'
        ' abnormalities and/or there is positive evidence of human fetal risk'
        ' based on adverse reaction data from investigational or marketing'
        ' experience, and the risks involved in use of the drug in pregnant'
        ' women clearly outweigh potential benefits.\n\n'
        'CATEGORY N : Not yet classified')

    presentation = fields.Text('Presentation', help='Packaging')
    adverse_reaction = fields.Text('Adverse Reactions')
    storage = fields.Text('Storage Conditions')
    is_vaccine = fields.Boolean('Vaccine')
    notes = fields.Text('Extra Info')

    active = fields.Boolean('Active', select=True)

    @staticmethod
    def default_active():
        return True
    
    # Show the icon depending on the pregnancy category
    pregnancy_cat_icon = \
        fields.Function(fields.Char('Preg. Cat. Icon'), 'get_preg_cat_icon')
    
    def get_preg_cat_icon(self, name):
        if (self.pregnancy_category == 'X'):
            return 'gnuhealth-stop'
        if (self.pregnancy_category == 'D' or self.pregnancy_category == "C"):
            return 'gnuhealth-warning'

      
    def get_rec_name(self, name):
        return self.name.name

    # Allow to search by name, active component or category
    @classmethod
    def search_rec_name(cls, name, clause):
        if clause[1].startswith('!') or clause[1].startswith('not '):
            bool_op = 'AND'
        else:
            bool_op = 'OR'
        return [bool_op,
            ('name',) + tuple(clause[1:]),
            ('active_component',) + tuple(clause[1:]),
            ('category',) + tuple(clause[1:]),
            ]

    @classmethod
    def check_xml_record(cls, records, values):
        return True

class ImmunizationScheduleDose(ModelSQL, ModelView):
    'Immunization Schedule Dose'
    __name__ = 'gnuhealth.immunization_schedule_dose'

    vaccine = fields.Many2One(
        'gnuhealth.immunization_schedule_line', 'Vaccine', required=True,
        help='Vaccine Name')
    dose_number = fields.Integer('Dose',required=True)
    age_dose = fields.Integer('Age',required=True)
    age_unit = fields.Selection([
        (None,''),
        ('days','days'),
        ('weeks','weeks'),
        ('months','months'),
        ('years','years'),
        ],'Time Unit',required=True)

    remarks = fields.Char('Remarks')

    sched = fields.Function(
        fields.Char('Schedule'), 'get_dose_schedule',
        searcher='search_dose_schedule')

    def get_dose_schedule(self, name):
        return self.vaccine.sched.sched

    @classmethod
    def search_dose_schedule(cls, name, clause):
        res = []
        value = clause[2]
        res.append(('vaccine.sched.sched', clause[1], value))
        return res

    @classmethod
    def __setup__(cls):
        super(ImmunizationScheduleDose, cls).__setup__()
        t = cls.__table__()
        cls._sql_constraints = [
            ('number_uniq', Unique(t,t.dose_number,t.vaccine),
                'The dose number must be unique for this vaccine'),
        ]
        cls._order.insert(0, ('vaccine', 'ASC'))
        cls._order.insert(1, ('dose_number', 'ASC'))

class ImmunizationScheduleLine(ModelSQL, ModelView):
    'Immunization Schedule Line'
    __name__ = 'gnuhealth.immunization_schedule_line'


    sched = fields.Many2One(
        'gnuhealth.immunization_schedule', 'Schedule', required=True,
        help='Schedule Name')

    vaccine = fields.Many2One(
        'gnuhealth.medicament', 'Vaccine', required=True,
        domain=[('is_vaccine', '=', True)],
        help='Vaccine Name')

    scope = fields.Selection([
        (None, ''),
        ('systematic','Systematic'),
        ('recommended','Recommended'),
        ('highrisk','Risk groups'), 
        ],'Scope', sort=False)

    remarks = fields.Char('Remarks')

    doses = fields.One2Many ('gnuhealth.immunization_schedule_dose',
        'vaccine','Doses')

    def get_rec_name(self, name):
        return (self.vaccine.name.name)

    @staticmethod
    def default_scope():
        return 'systematic'

class ImmunizationSchedule(ModelSQL, ModelView):
    'Immunization Schedule'
    __name__ = 'gnuhealth.immunization_schedule'

    sched = fields.Char('Code',
     help="Code for this immunization schedule", required=True)
    country = fields.Many2One('country.country','Country')
    year = fields.Integer('Year')
    active = fields.Boolean('Active')

    vaccines = fields.One2Many ('gnuhealth.immunization_schedule_line',
        'sched','Vaccines')

    desc = fields.Char('Description',
     help="Short Description for this immunization schedule", required=True)
     
    def get_rec_name(self, name):
        return (self.sched)

    @staticmethod
    def default_active():
        return True

    @classmethod
    def __setup__(cls):
        super(ImmunizationSchedule, cls).__setup__()
        t = cls.__table__()
        cls._sql_constraints = [
            ('sched_uniq', Unique(t,t.sched),
                'The schedule code must be unique'),
        ]
    
class PathologyCategory(ModelSQL, ModelView):
    'Disease Categories'
    __name__ = 'gnuhealth.pathology.category'

    name = fields.Char('Category Name', required=True, translate=True)
    parent = fields.Many2One(
        'gnuhealth.pathology.category', 'Parent Category', select=True)

    childs = fields.One2Many(
        'gnuhealth.pathology.category', 'parent', 'Children Category')

    @classmethod
    def __setup__(cls):
        super(PathologyCategory, cls).__setup__()
        cls._order.insert(0, ('name', 'ASC'))

    @classmethod
    def validate(cls, categories):
        super(PathologyCategory, cls).validate(categories)
        cls.check_recursion(categories, rec_name='name')

    def get_rec_name(self, name):
        if self.parent:
            return self.parent.get_rec_name(name) + ' / ' + self.name
        else:
            return self.name

    @classmethod
    def __setup__(cls):
        super(PathologyCategory, cls).__setup__()
        t = cls.__table__()
        cls._sql_constraints += [
            ('name_uniq', Unique(t,t.name),
            'The category name must be unique'),
        ]


class PathologyGroup(ModelSQL, ModelView):
    'Pathology Groups'
    __name__ = 'gnuhealth.pathology.group'

    name = fields.Char(
        'Name', required=True, translate=True, help='Group name')

    code = fields.Char(
        'Code', required=True,
        help='for example MDG6 code will contain the Millennium Development'
        ' Goals # 6 diseases : Tuberculosis, Malaria and HIV/AIDS')

    desc = fields.Char('Short Description', required=True)
    info = fields.Text('Detailed information')

    members = fields.One2Many ('gnuhealth.disease_group.members',
        'disease_group','Members', readonly=True)

    @classmethod
    def __setup__(cls):
        super(PathologyGroup, cls).__setup__()
        t = cls.__table__()
        cls._sql_constraints += [
            ('code_uniq', Unique(t,t.code),
            'The Pathology Group code must be unique'),
        ]


class Pathology(ModelSQL, ModelView):
    'Health Conditions'
    __name__ = 'gnuhealth.pathology'

    name = fields.Char(
        'Name', required=True, translate=True, help='Health condition name')
    code = fields.Char(
        'Code', required=True,
        help='Specific Code for the Disease (eg, ICD-10)')
    category = fields.Many2One(
        'gnuhealth.pathology.category', 'Main Category',
        help='Select the main category for this disease This is usually'
        ' associated to the standard. For instance, the chapter on the ICD-10'
        ' will be the main category for de disease')

    groups = fields.One2Many(
        'gnuhealth.disease_group.members', 'name',
        'Groups', help='Specify the groups this pathology belongs. Some'
        ' automated processes act upon the code of the group')

    chromosome = fields.Char('Affected Chromosome', help='chromosome number')
    protein = fields.Char(
        'Protein involved', help='Name of the protein(s) affected')
    gene = fields.Char('Gene', help='Name of the gene(s) affected')
    info = fields.Text('Extra Info')

    active = fields.Boolean('Active', select=True)

    @staticmethod
    def default_active():
        return True

    # Include code + description in result
    def get_rec_name(self, name):
        return (self.code + ' : ' + self.name)

    # Search by the health condition code or the description
    @classmethod
    def search_rec_name(cls, name, clause):
        if clause[1].startswith('!') or clause[1].startswith('not '):
            bool_op = 'AND'
        else:
            bool_op = 'OR'
        return [bool_op,
            ('code',) + tuple(clause[1:]),
            ('name',) + tuple(clause[1:]),
            ]

    @classmethod
    def __setup__(cls):
        super(Pathology, cls).__setup__()
        t = cls.__table__()
        cls._sql_constraints += [
            ('code_uniq', Unique(t,t.code), 'The disease code must be unique'),
        ]


# DISEASE GROUP MEMBERS
class DiseaseMembers(ModelSQL, ModelView):
    'Disease group members'
    __name__ = 'gnuhealth.disease_group.members'

    name = fields.Many2One('gnuhealth.pathology', 'Condition', readonly=True)
    disease_group = fields.Many2One(
        'gnuhealth.pathology.group', 'Group', required=True)


class ProcedureCode(ModelSQL, ModelView):
    'Medical Procedures'
    __name__ = 'gnuhealth.procedure'

    name = fields.Char('Code', required=True)
    description = fields.Char('Long Text', translate=True)

    # Include code + description in result
    def get_rec_name(self, name):
        return (self.name + ' : ' + self.description)

    # Search by the Procedure code or the description
    @classmethod
    def search_rec_name(cls, name, clause):
        if clause[1].startswith('!') or clause[1].startswith('not '):
            bool_op = 'AND'
        else:
            bool_op = 'OR'
        return [bool_op,
            ('name',) + tuple(clause[1:]),
            ('description',) + tuple(clause[1:]),
            ]

# Add institution attribute AFTER registering the Health Institution
# Health Professionals and underlying conditions

class BirthCertExtraInfo (ModelSQL, ModelView):
    'Birth Certificate'
    __name__ = 'gnuhealth.birth_certificate'

    STATES = {'readonly': Eval('state') == 'done'}
    
    institution = fields.Many2One(
        'gnuhealth.institution', 'Institution',
        states = STATES )

    signed_by = fields.Many2One(
        'gnuhealth.healthprofessional', 
        'Certifier', readonly=True, help='Person who certifies this'
        ' birth document',
        states = STATES )

    certification_date = fields.DateTime('Signed on', readonly=True,
        states = STATES )

    @staticmethod
    def default_institution():
        return HealthInstitution().get_institution()

    @fields.depends('institution')
    def on_change_institution(self):
        country=None
        subdivision=None
        if (self.institution and self.institution.name.addresses[0].country):
            country = self.institution.name.addresses[0].country.id
        
        if (self.institution and self.institution.name.addresses[0].subdivision):
            subdivision = self.institution.name.addresses[0].subdivision.id

        self.country = country
        self.country_subdivision = subdivision

    @classmethod
    @ModelView.button
    def sign(cls, certificates):
        pool = Pool()
        HealthProfessional = pool.get('gnuhealth.healthprofessional')
        Person = pool.get('party.party')
        party=[]

        # Change the state of the birth certificate to "Signed"
        # and write the name of the certifying health professional
        
        signing_hp = HealthProfessional.get_health_professional()
        if not signing_hp:
            cls.raise_user_error(
                "No health professional associated to this user !")

        cls.write(certificates, {
            'state': 'signed',
            'signed_by': signing_hp,
            'certification_date': datetime.now()})

        party.append(certificates[0].name)
        
        Person.write(party, {
            'birth_certificate': certificates[0].id })


class DeathCertExtraInfo (ModelSQL, ModelView):
    'Death Certificate'
    __name__ = 'gnuhealth.death_certificate'

    STATES = {'readonly': Eval('state') == 'done'}
    
    institution = fields.Many2One(
        'gnuhealth.institution', 'Institution',
        states = STATES)

    signed_by = fields.Many2One(
        'gnuhealth.healthprofessional', 'Signed by', readonly=True,
        states={'invisible': Equal(Eval('state'), 'draft')},
        help="Health Professional that signed the death certificate")

    certification_date = fields.DateTime('Certified on', readonly=True)

    cod = fields.Many2One(
        'gnuhealth.pathology', 'Cause',
        required=True, help="Immediate Cause of Death",
        states = STATES)

    underlying_conditions = fields.One2Many(
        'gnuhealth.death_underlying_condition',
        'death_certificate', 'Underlying Conditions', help='Underlying'
        ' conditions that initiated the events resulting in death.'
        ' Please code them in sequential, chronological order',
        states = STATES)

    @staticmethod
    def default_institution():
        return HealthInstitution().get_institution()

    @staticmethod
    def default_state():
        return 'draft'

    @fields.depends('institution')
    def on_change_institution(self):
        country=None
        subdivision=None
        if (self.institution and self.institution.name.addresses[0].country):
            country = self.institution.name.addresses[0].country.id
        
        if (self.institution and self.institution.name.addresses[0].subdivision):
            subdivision = self.institution.name.addresses[0].subdivision.id

        self.country = country
        self.country_subdivision = subdivision

    @classmethod
    @ModelView.button
    def sign(cls, certificates):
        pool = Pool()
        HealthProfessional = pool.get('gnuhealth.healthprofessional')
        Person = pool.get('party.party')

        # Change the state of the death certificate to "Signed"
        # and write the name of the certifying health professional
        
        # It also set the associated party attribute deceased to True.

        party=[]
        
        signing_hp = HealthProfessional.get_health_professional()
        if not signing_hp:
            cls.raise_user_error(
                "No health professional associated to this user !")

        cls.write(certificates, {
            'state': 'signed',
            'signed_by': signing_hp,
            'certification_date': datetime.now()})

        party.append(certificates[0].name)
        
        Person.write(party, {
            'deceased': True,
            'death_certificate': certificates[0].id
        })
        

# UNDERLYING CONDITIONS THAT RESULT IN DEATH INCLUDED IN DEATH CERT.
class DeathUnderlyingCondition(ModelSQL, ModelView):
    'Underlying Conditions'
    __name__ = 'gnuhealth.death_underlying_condition'

    death_certificate = fields.Many2One(
        'gnuhealth.death_certificate', 'Certificate', readonly=True)

    condition = fields.Many2One(
        'gnuhealth.pathology', 'Condition', required=True)

    interval = fields.Integer('Interval', help='Approx Interval'
        ' onset to death', required=True)

    unit_of_time = fields.Selection([
        (None, ''),
        ('minutes', 'minutes'),
        ('hours', 'hours'),
        ('days', 'days'),
        ('months', 'months'),
        ('years', 'years'),
        ], 'Unit', select=True, sort=False, required=True)

class InsurancePlan(ModelSQL, ModelView):
    'Insurance Plan'

    __name__ = 'gnuhealth.insurance.plan'
    _rec_name = 'company'

    name = fields.Many2One(
        'product.product', 'Plan', required=True,
        domain=[('is_insurance_plan', '=', True)],
        help='Insurance company plan')

    company = fields.Many2One(
        'party.party', 'Insurance Company', required=True,
        domain=[('is_insurance_company', '=', True)])

    is_default = fields.Boolean(
        'Default plan',
        help='Check if this is the default plan when assigning this insurance'
        ' company to a patient')

    notes = fields.Text('Extra info')

    def get_rec_name(self, name):
        return self.name.name


class Insurance(ModelSQL, ModelView):
    'Insurance'
    __name__ = 'gnuhealth.insurance'
    _rec_name = 'number'

    # Insurance associated to an individual

    name = fields.Many2One('party.party', 'Owner')
    number = fields.Char('Number', required=True)

    company = fields.Many2One(
        'party.party', 'Insurance Company',
        required=True, select=True,
        domain=[('is_insurance_company', '=', True)])

    member_since = fields.Date('Member since')
    member_exp = fields.Date('Expiration date')
    category = fields.Char(
        'Category', help='Insurance company category')

    insurance_type = fields.Selection([
        (None, ''),
        ('state', 'State'),
        ('labour_union', 'Labour Union / Syndical'),
        ('private', 'Private'),
        ], 'Insurance Type', select=True)
    plan_id = fields.Many2One(
        'gnuhealth.insurance.plan', 'Plan',
        help='Insurance company plan',
        domain=[('company', '=', Eval('company'))],
        depends=['company'])

    notes = fields.Text('Extra Info')

    def get_rec_name(self, name):
        return (self.company.name + ' : ' + self.number)

    @classmethod
    def __setup__(cls):
        super(Insurance, cls).__setup__()
        t = cls.__table__()
        cls._sql_constraints = [
            ('number_uniq', Unique(t,t.number,t.company),
                'The number must be unique per insurance company'),
        ]

class AlternativePersonID (ModelSQL, ModelView):
    'Alternative person ID'
    __name__ = 'gnuhealth.person_alternative_identification'

    name = fields.Many2One('party.party', 'Party', readonly=True)
    code = fields.Char('Code', required=True)
    alternative_id_type = fields.Selection(
        [
            (None, ''),
            ('country_id', 'Country of origin ID'),
            ('passport', 'Passport'),
            ('medical_record', 'Medical Record'),
            ('ghealth_federation', 'GNU Health Federation'),
            ('other', 'Other'),
        ], 'ID type', required=True, sort=False,)

    comments = fields.Char('Comments')


class BirthCertificate (ModelSQL, ModelView):
    'Birth Certificate'
    __name__ = 'gnuhealth.birth_certificate'

    STATES = {'readonly': Eval('state') == 'done'}

    name = fields.Many2One('party.party', 'Person', 
        required=True,
        domain=[('is_person', '=', True),],
        states = {'readonly': Eval('id', 0) > 0})

    mother = fields.Many2One('party.party', 'Mother', 
        domain=[('is_person', '=', True),],
        states = STATES )


    father = fields.Many2One('party.party', 'Father',
        domain=[('is_person', '=', True),],
        states = STATES )

    code = fields.Char('Code', required=True,
        states = STATES )

    dob = fields.Date('Date of Birth', required=True,
        states = STATES )

    observations = fields.Text('Observations',
        states = STATES )

    country = fields.Many2One('country.country','Country', required=True,
        states = STATES )

    country_subdivision = fields.Many2One(
        'country.subdivision', 'Subdivision',
        domain=[('country', '=', Eval('country'))],
        depends=['country'],
        states = STATES )

    state = fields.Selection([
        (None, ''),
        ('draft', 'Draft'),
        ('signed', 'Signed'),
        ('done', 'Done'),
        ], 'State', readonly=True, sort=False)


    @staticmethod
    def default_state():
        return 'draft'

    @fields.depends('name')
    def on_change_with_dob(self):
        if (self.name and self.name.dob):
            dob = self.name.dob
            return dob


    @classmethod
    def __setup__(cls):
        super(BirthCertificate, cls).__setup__()
        t = cls.__table__()
        cls._sql_constraints = [
            ('name_uniq', Unique(t,t.name), 'Certificate already exists !'),
            ('code_uniq', Unique(t,t.code), 'Certificate already exists !'),
        ]

        cls._buttons.update({
            'sign': {'invisible': Or(Equal(Eval('state'), 'signed'),
                Equal(Eval('state'), 'done'))}
        })


    @classmethod
    def validate(cls, certificates):
        super(BirthCertificate, cls).validate(certificates)
        for certificate in certificates:
            certificate.validate_dob()

    def validate_dob(self):
        if (self.name.dob != self.dob):
                        self.raise_user_error(
                "The date on the Party differs from the certificate !")

  
class DeathCertificate (ModelSQL, ModelView):
    'Death Certificate'
    __name__ = 'gnuhealth.death_certificate'

    STATES = {'readonly': Eval('state') == 'done'}

    name = fields.Many2One('party.party', 'Person', required=True,
        domain=[('is_person', '=', True),],
        states = STATES)

    code = fields.Char('Code', required=True,
        states = STATES)

    autopsy = fields.Boolean('Autopsy', help="Check this box "
        "if autopsy has been done",
        states = STATES)

    dod = fields.DateTime('Date', required=True,
        help="Date and time of Death",
        states = STATES)

    type_of_death = fields.Selection(
        [
            (None, ''),
            ('natural', 'Natural'),
            ('suicide', 'Suicide'),
            ('homicide', 'Homicide'),
            ('undetermined', 'Undetermined'),
            ('pending_investigation', 'Pending Investigation'),
        ], 'Type of death', required=True, sort=False,
        states = STATES)

    place_of_death = fields.Selection(
        [
            (None, ''),
            ('home', 'Home'),
            ('work', 'Work'),
            ('public_place', 'Public place'),
            ('health_center', 'Health Center'),
        ], 'Place', required=True, sort=False,
        states = STATES)

    operational_sector = fields.Many2One(
        'gnuhealth.operational_sector', 'Op. Sector',
        states = STATES)

    du = fields.Many2One(
        'gnuhealth.du', 'DU', help="Domiciliary Unit",
        states = STATES)

    place_details = fields.Char('Details',
        states = STATES)

    country = fields.Many2One('country.country','Country', required=True,
        states = STATES)

    country_subdivision = fields.Many2One(
        'country.subdivision', 'Subdivision',
        domain=[('country', '=', Eval('country'))],
        depends=['country'],
        states = STATES)

    age = fields.Function(fields.Char('Age'),'get_age_at_death')

    observations = fields.Text('Observations',
        states = STATES)

    state = fields.Selection([
        (None, ''),
        ('draft', 'Draft'),
        ('signed', 'Signed'),
        ('done', 'Done'),
        ], 'State', readonly=True, sort=False)

    @staticmethod
    def default_state():
        return 'draft'


    @classmethod
    def __setup__(cls):
        super(DeathCertificate, cls).__setup__()
        t = cls.__table__()
        cls._sql_constraints = [
            ('name_uniq', Unique(t,t.name), 'Certificate already exists !'),
            ('code_uniq', Unique(t,t.code), 'Certificate already exists !'),
        ]

        cls._buttons.update({
            'sign': {'invisible': Or(Equal(Eval('state'), 'signed'),
                Equal(Eval('state'), 'done'))}
            })


    def get_age_at_death(self,name):
        if (self.name.dob):
            delta = relativedelta(self.dod, self.name.dob)
            years_months_days = str(delta.years) + 'y ' \
                + str(delta.months) + 'm ' \
                + str(delta.days) + 'd'
        else:
            years_months_days = None
        return years_months_days


class Product(ModelSQL, ModelView):
    'Product'
    __name__ = 'product.product'

    is_medicament = fields.Boolean(
        'Medicament', help='Check if the product is a medicament')
    is_medical_supply = fields.Boolean(
        'Medical Supply', help='Check if the product is a medical supply')
    is_vaccine = fields.Boolean(
        'Vaccine', help='Check if the product is a vaccine')
    is_bed = fields.Boolean(
        'Bed', help='Check if the product is a bed on the gnuhealth.center')
    is_insurance_plan = fields.Boolean(
        'Insurance Plan', help='Check if the product is an insurance plan')

    @classmethod
    def check_xml_record(cls, records, values):
        return True


# GNU HEALTH SEQUENCES
class GnuHealthSequences(ModelSingleton, ModelSQL, ModelView):
    'Standard Sequences for GNU Health'
    __name__ = 'gnuhealth.sequences'

    patient_sequence = fields.Property(fields.Many2One(
        'ir.sequence', 'Patient Sequence', required=True,
        domain=[('code', '=', 'gnuhealth.patient')]))

    patient_evaluation_sequence = fields.Property(fields.Many2One(
        'ir.sequence', 'Patient Evaluation Sequence', required=True,
        domain=[('code', '=', 'gnuhealth.patient.evaluation')]))

    appointment_sequence = fields.Property(fields.Many2One(
        'ir.sequence', 'Appointment Sequence', required=True,
        domain=[('code', '=', 'gnuhealth.appointment')]))

    prescription_sequence = fields.Property(fields.Many2One(
        'ir.sequence', 'Prescription Sequence', required=True,
        domain=[('code', '=', 'gnuhealth.prescription.order')]))


# PATIENT GENERAL INFORMATION
class PatientData(ModelSQL, ModelView):
    'Patient related information'
    __name__ = 'gnuhealth.patient'

    def patient_critical_summary(self, name):
        # Patient Critical Information Summary
        # The information will be shown in the front page

        critical_info = ""
        allergies=""
        other_conditions=""
        conditions=[]
        for disease in self.diseases:
            for member in disease.pathology.groups:
                '''Retrieve patient allergies'''
                if (member.disease_group.name == "ALLERGIC"):
                    if disease.pathology.name not in conditions:
                        allergies=allergies + disease.pathology.rec_name + "\n"
                        conditions.append (disease.pathology.rec_name)

            '''Retrieve patient other relevant conditions '''
            '''Chronic and active'''        
            if (disease.status == "c" or disease.is_active):
                if disease.pathology.name not in conditions:
                            other_conditions=other_conditions + \
                             disease.pathology.rec_name + "\n"

        return allergies + other_conditions
        
    name = fields.Many2One(
        'party.party', 'Patient', required=True,
        domain=[
            ('is_patient', '=', True),
            ('is_person', '=', True),
            ],
        states = {'readonly': Eval('id', 0) > 0},
        help="Person associated to this patient")

    lastname = fields.Function(
        fields.Char('Lastname'), 'get_patient_lastname',
        searcher='search_patient_lastname')

    puid = fields.Function(
        fields.Char('PUID', help="Person Unique Identifier"),
        'get_patient_puid', searcher='search_patient_puid')

    # 2.6 Removed from the patient model and code moved to
    # the patient alternative id as "medical_record"
    # identification_code = fields.Char(
    #    'Code', readonly=True,
    #    help='Patient Identifier provided by the Health Center.Is not the'
    #    ' Social Security Number')

    family = fields.Many2One(
        'gnuhealth.family', 'Family', help='Family Code')

    current_insurance = fields.Many2One(
        'gnuhealth.insurance', 'Insurance',
        domain=[('name', '=', Eval('name'))],
        depends=['name'],
        help='Insurance information. You may choose from the different'
        ' insurances belonging to the patient')

    current_address = fields.Many2One(
        'party.address', 'Temp. Addr',
        domain=[('party', '=', Eval('name'))],
        depends=['name'],
        help="Use this address for temporary contact information. For example \
        if the patient is on vacation, you can put the hotel address. \
        In the case of a Domiciliary Unit, just link it to the name of the \
        contact in the address form.")
    primary_care_doctor = fields.Many2One(
        'gnuhealth.healthprofessional',
        'GP', help='Current General Practitioner / Family Doctor')

    # Removed in 2.0 . PHOTO It's now a functional field
    # Retrieves the information from the party.

    photo = fields.Function(fields.Binary('Picture'), 'get_patient_photo')

    # Removed in 2.0 . DOB It's now a functional field
    # Retrieves the information from the party.
    #    dob = fields.Date('DoB', help='Date of Birth')

    dob = fields.Function(fields.Date('DoB'), 'get_patient_dob')

    age = fields.Function(fields.Char('Age'), 'get_patient_age')

    gender = fields.Function(fields.Selection([
        (None, ''),
        ('m', 'Male'),
        ('f', 'Female'),
        ('f-m','Female -> Male'),
        ('m-f','Male -> Female'),
        ], 'Gender'), 'get_patient_gender')

    biological_sex = fields.Selection([
        (None, ''),
        ('m', 'Male'),
        ('f', 'Female'),
        ], 'Biological Sex', help="Biological sex. By defaults it takes the value" \
            " from the neonatal information")

    # Removed in 2.0 . MARITAL STATUS It's now a functional field
    # Retrieves the information from the party.

    marital_status = fields.Function(
        fields.Selection([
            (None, ''),
            ('s', 'Single'),
            ('m', 'Married'),
            ('c', 'Concubinage'),
            ('w', 'Widowed'),
            ('d', 'Divorced'),
            ('x', 'Separated'), 
            ], 'Marital Status', sort=False, help="Marital Status"),
            'get_patient_marital_status')

    blood_type = fields.Selection([
        (None, ''),
        ('A', 'A'),
        ('B', 'B'),
        ('AB', 'AB'),
        ('O', 'O'),
        ], 'Blood Type', sort=False)

    rh = fields.Selection([
        (None, ''),
        ('+', '+'),
        ('-', '-'),
        ], 'Rh')

    # Removed in 2.0 . ETHNIC GROUP is on the party model now

    # ethnic_group = fields.Many2One('gnuhealth.ethnicity', 'Ethnic group')
    vaccinations = fields.One2Many(
        'gnuhealth.vaccination', 'name', 'Vaccinations', readonly=True)
    medications = fields.One2Many(
        'gnuhealth.patient.medication', 'name', 'Medications')

# Removed in 1.6
#    prescriptions = fields.One2Many('gnuhealth.prescription.order', 'name',
#        'Prescriptions')

    diseases = fields.One2Many('gnuhealth.patient.disease', 'name',
     'Conditions', readonly=True)
     
    critical_summary = fields.Function(fields.Text(
        'Important health conditions related to this patient',
        help='Automated summary of patient important health conditions '
        'other critical information'),
        'patient_critical_summary')

    critical_info = fields.Text(
        'Free text information not included in the automatic summary',
        help='Write any important information on the patient\'s condition,'
        ' surgeries, allergies, ...')


# Removed it in 1.6
# Not used anymore . Now we relate with a shortcut. Clearer
#    evaluation_ids = fields.One2Many('gnuhealth.patient.evaluation',
#        'patient', 'Evaluation')
#    admissions_ids = fields.One2Many('gnuhealth.patient.admission', 'name',
#        'Admission / Discharge')

    general_info = fields.Text(
        'General Information',
        help='General information about the patient')

    deceased = fields.Function(fields.Boolean('Deceased'), 
        'check_is_alive')

    dod = fields.Function(fields.DateTime(
        'Date of Death',
        states={
            'invisible': Not(Bool(Eval('deceased'))),
            },
        depends=['deceased']),'get_dod')

    cod = fields.Function(fields.Many2One(
        'gnuhealth.pathology', 'Cause of Death',
        states={
            'invisible': Not(Bool(Eval('deceased'))),
            },
        depends=['deceased']),'get_cod')

    childbearing_age = fields.Function(
        fields.Boolean('Potential for Childbearing'), 'get_childbearing_age')

    appointments = fields.One2Many(
        'gnuhealth.appointment', 'patient', 'Appointments')

    active = fields.Boolean('Active', select=True)

    @staticmethod
    def default_active():
        return True

    @classmethod
    def __setup__(cls):
        super(PatientData, cls).__setup__()
        t = cls.__table__()
        cls._sql_constraints = [
            ('name_uniq', Unique(t,t.name), 'The Patient already exists !'),
        ]
        cls._order.insert(0, ('name', 'ASC'))



    def get_patient_dob(self, name):
        return self.name.dob

    def get_patient_gender(self, name):
        gender = self.name.gender
        sex = self.biological_sex
        if sex:
            if (gender != sex):
                res = sex + '-' + gender
            else:
                res = gender
        else:
            res = gender
        return res

    def get_patient_photo(self, name):
        return self.name.photo

    def get_patient_puid(self, name):
        return self.name.ref

    def get_patient_marital_status(self, name):
        return self.name.marital_status

    def check_is_alive(self, name):
        return self.name.deceased

    def get_patient_age(self, name):
        return self.name.age

    def get_childbearing_age(self, name):
        return compute_age_from_dates(self.dob, self.deceased,
                              self.dod, self.gender, name, None)

    def get_dod(self, name):
        if (self.deceased):
            return self.name.death_certificate.dod

    def get_cod(self, name):
        if (self.deceased):
            return self.name.death_certificate.cod.id


    # Show the gender upon entering the individual 
    @fields.depends('name')
    def on_change_name(self):
        gender=None
        age=None
        self.gender = self.name.gender
        self.age = self.name.age


    @classmethod
    def search_patient_puid(cls, name, clause):
        res = []
        value = clause[2]
        res.append(('name.ref', clause[1], value))
        return res

    def get_patient_lastname(self, name):
        return self.name.lastname

    @classmethod
    def search_patient_lastname(cls, name, clause):
        res = []
        value = clause[2]
        res.append(('name.lastname', clause[1], value))
        return res

    def get_rec_name(self, name):
        if self.name.lastname:
            return self.name.lastname + ', ' + self.name.name
        else:
            return self.name.name

    # Search by the patient name, lastname or PUID

    @classmethod
    def search_rec_name(cls, name, clause):
        if clause[1].startswith('!') or clause[1].startswith('not '):
            bool_op = 'AND'
        else:
            bool_op = 'OR'
        return [bool_op,
            ('puid',) + tuple(clause[1:]),
            ('name',) + tuple(clause[1:]),
            ('lastname',) + tuple(clause[1:]),
            ]


# PATIENT CONDITIONS INFORMATION
class PatientDiseaseInfo(ModelSQL, ModelView):
    'Patient Conditions History'
    __name__ = 'gnuhealth.patient.disease'

    name = fields.Many2One('gnuhealth.patient', 'Patient')

    pathology = fields.Many2One(
        'gnuhealth.pathology', 'Condition', required=True, help='Condition')

    disease_severity = fields.Selection([
        (None, ''),
        ('1_mi', 'Mild'),
        ('2_mo', 'Moderate'),
        ('3_sv', 'Severe'),
        ], 'Severity', select=True, sort=False)

    is_on_treatment = fields.Boolean('Currently on Treatment')
    is_infectious = fields.Boolean(
        'Infectious Disease',
        help='Check if the patient has an infectious / transmissible disease')

    short_comment = fields.Char(
        'Remarks',
        help='Brief, one-line remark of the disease. Longer description will'
        ' go on the Extra info field')

    healthprof = fields.Many2One(
        'gnuhealth.healthprofessional',
        'Health Prof', help='Health Professional who treated or diagnosed the patient')

    diagnosed_date = fields.Date('Date of Diagnosis')
    healed_date = fields.Date('Healed')
    is_active = fields.Boolean('Active disease')

    age = fields.Integer(
        'Age when diagnosed',
        help='Patient age at the moment of the diagnosis. Can be estimative')

    pregnancy_warning = fields.Boolean('Pregnancy warning')
    weeks_of_pregnancy = fields.Integer('Contracted in pregnancy week #')
    is_allergy = fields.Boolean('Allergic Disease')
    allergy_type = fields.Selection([
        (None, ''),
        ('da', 'Drug Allergy'),
        ('fa', 'Food Allergy'),
        ('ma', 'Misc Allergy'),
        ('mc', 'Misc Contraindication'),
        ], 'Allergy type', select=True, sort=False)
    pcs_code = fields.Many2One(
        'gnuhealth.procedure', 'Code',
        help='Procedure code, for example, ICD-10-PCS Code 7-character string')
    treatment_description = fields.Char('Treatment Description')
    date_start_treatment = fields.Date('Start', help='Start of treatment date')
    date_stop_treatment = fields.Date('End', help='End of treatment date')
    status = fields.Selection([
        (None, ''),
        ('a', 'acute'),
        ('c', 'chronic'),
        ('u', 'unchanged'),
        ('h', 'healed'),
        ('i', 'improving'),
        ('w', 'worsening'),
        ], 'Status', select=True, sort=False)
    extra_info = fields.Text('Extra Info')

    healthprof = fields.Many2One(
        'gnuhealth.healthprofessional', 'Health Prof', readonly=True,
        help='Health Professional')

    related_evaluations = fields.One2Many(
        'gnuhealth.patient.evaluation', 'related_condition',
        'Related Evaluations', readonly=True)


    @classmethod
    def __setup__(cls):
        super(PatientDiseaseInfo, cls).__setup__()
        cls._order.insert(0, ('is_active', 'DESC'))
        cls._order.insert(1, ('disease_severity', 'DESC'))
        cls._order.insert(2, ('is_infectious', 'DESC'))
        cls._order.insert(3, ('diagnosed_date', 'DESC'))
        cls._error_messages.update({
            'end_date_before_start': 'The HEALED date "%(healed_date)s" is'
            ' BEFORE DIAGNOSED DATE "%(diagnosed_date)s"!',
            'end_treatment_date_before_start': 'The Treatment END DATE'
            ' "%(date_stop_treatment)s" is BEFORE the start date'
            ' "%(date_start_treatment)s"!',
            })

    @staticmethod
    def default_is_active():
        return True

    @classmethod
    def validate(cls, diseases):
        super(PatientDiseaseInfo, cls).validate(diseases)
        for disease in diseases:
            disease.validate_disease_period()
            disease.validate_treatment_dates()

    def validate_disease_period(self):
        Lang = Pool().get('ir.lang')

        language, = Lang.search([
            ('code', '=', Transaction().language),
            ])
        if (self.healed_date and self.diagnosed_date):
            if (self.healed_date < self.diagnosed_date):
                self.raise_user_error('end_date_before_start', {
                        'healed_date': Lang.strftime(self.healed_date,
                            language.code, language.date),
                        'diagnosed_date': Lang.strftime(self.diagnosed_date,
                            language.code, language.date),
                        })

    def validate_treatment_dates(self):
        Lang = Pool().get('ir.lang')

        language, = Lang.search([
            ('code', '=', Transaction().language),
            ])
        if (self.date_stop_treatment and self.date_start_treatment):
            if (self.date_stop_treatment < self.date_start_treatment):
                self.raise_user_error('end_treatment_date_before_start', {
                        'date_stop_treatment': Lang.strftime(
                            self.date_stop_treatment,
                            language.code, language.date),
                        'date_start_treatment': Lang.strftime(
                            self.date_start_treatment,
                            language.code, language.date),
                        })


    # Show warning on infectious disease
    infectious_disease_icon = \
        fields.Function(fields.Char('Infect'), 'get_infect_disease_icon')
    
    def get_infect_disease_icon(self, name):
        if (self.is_infectious):
            return 'gnuhealth-warning'

    @staticmethod
    def default_healthprof():
        pool = Pool()
        HealthProfessional = pool.get('gnuhealth.healthprofessional')
        return HealthProfessional.get_health_professional()

    def get_rec_name(self, name):
        return self.pathology.rec_name

# PATIENT APPOINTMENT
class Appointment(ModelSQL, ModelView):
    'Patient Appointments'
    __name__ = 'gnuhealth.appointment'

    name = fields.Char('Appointment ID', readonly=True)

    healthprof = fields.Many2One(
        'gnuhealth.healthprofessional', 'Health Prof',
        select=True, help='Health Professional')

    patient = fields.Many2One(
        'gnuhealth.patient', 'Patient',
        select=True, help='Patient Name',
        states={'required': (Eval('state') != 'free')})

    appointment_date = fields.DateTime('Date and Time')

    checked_in_date = fields.DateTime('Checked-in Time')

    institution = fields.Many2One(
        'gnuhealth.institution', 'Institution',
        help='Health Care Institution')

    speciality = fields.Many2One(
        'gnuhealth.specialty', 'Specialty',
        help='Medical Specialty / Sector')

    state = fields.Selection([
        (None, ''),
        ('free', 'Free'),
        ('confirmed', 'Confirmed'),
        ('checked_in', 'Checked in'),
        ('done', 'Done'),
        ('user_cancelled', 'Cancelled by patient'),
        ('center_cancelled', 'Cancelled by Health Center'),
        ('no_show', 'No show')
        ], 'State', sort=False)

    urgency = fields.Selection([
        (None, ''),
        ('a', 'Normal'),
        ('b', 'Urgent'),
        ('c', 'Medical Emergency'),
        ], 'Urgency', sort=False)

    comments = fields.Text('Comments')

    appointment_type = fields.Selection([
        (None, ''),
        ('outpatient', 'Outpatient'),
        ('inpatient', 'Inpatient'),
        ], 'Type', sort=False)

    visit_type = fields.Selection([
        (None, ''),
        ('new', 'New health condition'),
        ('followup', 'Followup'),
        ('well_child', 'Well Child visit'),
        ('well_woman', 'Well Woman visit'),
        ('well_man', 'Well Man visit'),
        ], 'Visit', sort=False)

    consultations = fields.Many2One(
        'product.product', 'Consultation Services',
        domain=[('type', '=', 'service')],
        help='Consultation Services')

    @classmethod
    def __setup__(cls):
        super(Appointment, cls).__setup__()
        cls._order.insert(0, ('appointment_date', 'ASC'))

        cls._buttons.update({
            'checked_in': {'invisible': Not(Equal(Eval('state'), 'confirmed'))}
            })

        cls._buttons.update({
            'no_show': {'invisible': Not(Equal(Eval('state'), 'confirmed'))}
            })

    @classmethod
    @ModelView.button
    def checked_in(cls, appointments):
        cls.write(appointments, {
            'state': 'checked_in'})

    @classmethod
    @ModelView.button
    def no_show(cls, appointments):
        cls.write(appointments, {
            'state': 'no_show'})

    @classmethod
    def create(cls, vlist):
        Sequence = Pool().get('ir.sequence')
        Config = Pool().get('gnuhealth.sequences')

        vlist = [x.copy() for x in vlist]
        for values in vlist:
            if values['state'] == 'confirmed' and not values.get('name'):
                config = Config(1)
                values['name'] = Sequence.get_id(
                    config.appointment_sequence.id)

        return super(Appointment, cls).create(vlist)

    @classmethod
    def write(cls, appointments, values):
        Sequence = Pool().get('ir.sequence')
        Config = Pool().get('gnuhealth.sequences')

        for appointment in appointments:
            if values.get('state') == 'confirmed' and not values.get('name'):
                config = Config(1)
                values['name'] = Sequence.get_id(
                    config.appointment_sequence.id)

            #Update the checked-in time only if unset
            if values.get('state') == 'checked_in' \
                    and values.get('checked_in_date') is None:
                values['checked_in_date'] = datetime.now()

        return super(Appointment, cls).write(appointments, values)

    @classmethod
    def copy(cls, appointments, default=None):
        if default is None:
            default = {}
        default = default.copy()
        default['name'] = None
        default['appointment_date'] = cls.default_appointment_date()
        default['state'] = cls.default_state()
        return super(Appointment, cls).copy(appointments, default=default)

    @staticmethod
    def default_healthprof():
        pool = Pool()
        HealthProfessional = pool.get('gnuhealth.healthprofessional')
        return HealthProfessional.get_health_professional()

    @staticmethod
    def default_urgency():
        return 'a'

    @staticmethod
    def default_appointment_date():
        return datetime.now()

    @staticmethod
    def default_appointment_type():
        return 'outpatient'

    @staticmethod
    def default_state():
        return 'confirmed'

    @staticmethod
    def default_institution():
        return HealthInstitution().get_institution()

    @fields.depends('patient')
    def on_change_patient(self):
        res = {'state': 'free'}
        if self.patient:
            self.state = 'confirmed'

    @fields.depends('healthprof')
    def on_change_with_speciality(self):
        # Return the Current / Main speciality of the Health Professional
        # if this speciality has been specified in the HP record.
        if (self.healthprof and self.healthprof.main_specialty):
            specialty = self.healthprof.main_specialty.specialty.id
            return specialty

    @staticmethod
    def default_speciality():
        # This method will assign the Main specialty to the appointment
        # if there is a health professional associated to the login user
        # as a default value.
        # It will be overwritten if the health professional is modified in
        # this view, the on_change_with will take effect.

        pool = Pool()
        HealthProfessional = pool.get('gnuhealth.healthprofessional')

        # Get Party ID associated to the Health Professional
        hp_party_id = HealthProfessional.get_health_professional()

        if hp_party_id:
            # Retrieve the health professional Main specialty, if assigned

            health_professional_obj = Pool().get('gnuhealth.healthprofessional')
            health_professional = health_professional_obj.search(
                [('id', '=', hp_party_id)], limit=1)[0]
            hp_main_specialty = health_professional.main_specialty

            if hp_main_specialty:
                return hp_main_specialty.specialty.id

    def get_rec_name(self, name):
        return self.name


class AppointmentReport(ModelSQL, ModelView):
    'Appointment Report'
    __name__ = 'gnuhealth.appointment.report'

    # 2.6 Remove the legacy internal identification code for the institution
    # It's now as part of the party alternative ID (medical_record)
    # identification_code = fields.Char('Identification Code')
    ref = fields.Char('PUID')
    patient = fields.Many2One('gnuhealth.patient', 'Patient')
    healthprof = fields.Many2One('gnuhealth.healthprofessional', 'Health Prof')
    age = fields.Function(fields.Char('Age'), 'get_patient_age')
    gender = fields.Selection([
        (None, ''),
        ('m', 'Male'),
        ('f', 'Female')], 'Gender')
    address = fields.Function(fields.Char('Address'), 'get_address')
    insurance = fields.Function(fields.Char('Insurance'), 'get_insurance')
    appointment_date = fields.Date('Date')
    appointment_date_time = fields.DateTime('Date and Time')
    diagnosis = fields.Function(
        fields.Many2One(
            'gnuhealth.pathology',
            'Main Codition'), 'get_diagnosis')

    @classmethod
    def __setup__(cls):
        super(AppointmentReport, cls).__setup__()
        cls._order.insert(0, ('appointment_date_time', 'ASC'))

    @classmethod
    def table_query(cls):
        pool = Pool()
        appointment = pool.get('gnuhealth.appointment').__table__()
        party = pool.get('party.party').__table__()
        patient = pool.get('gnuhealth.patient').__table__()
        join1 = Join(appointment, patient)
        join1.condition = join1.right.id == appointment.patient
        join2 = Join(join1, party)
        join2.condition = join2.right.id == join1.right.name
        where = Literal(True)
        if Transaction().context.get('date_start'):
            where &= (appointment.appointment_date >=
                    Transaction().context['date_start'])
        if Transaction().context.get('date_end'):
            where &= (appointment.appointment_date <
                    Transaction().context['date_end'] + timedelta(days=1))
        if Transaction().context.get('healthprof'):
            where &= \
                appointment.healthprof == Transaction().context['healthprof']

        return join2.select(
            appointment.id,
            appointment.create_uid,
            appointment.create_date,
            appointment.write_uid,
            appointment.write_date,
            join2.right.ref,
            join1.right.id.as_('patient'),
            join2.right.gender,
            appointment.appointment_date,
            appointment.appointment_date.as_('appointment_date_time'),
            appointment.healthprof,
            where=where)

    def get_address(self, name):
        res = ''
        if self.patient.name.addresses:
            res = self.patient.name.addresses[0].full_address
        return res

    def get_insurance(self, name):
        res = ''
        if self.patient.current_insurance:
            res = self.patient.current_insurance.company.name
        return res

    def get_diagnosis(self, name):
        Evaluation = Pool().get('gnuhealth.patient.evaluation')

        res = None
        evaluations = Evaluation.search([
            ('appointment', '=', self.id)
        ])
        if evaluations:
            evaluation = evaluations[0]
            if evaluation.diagnosis:
                res = evaluation.diagnosis.id
        return res

    def get_patient_age(self, name):
        return self.patient.name.age


class OpenAppointmentReportStart(ModelView):
    'Open Appointment Report'
    __name__ = 'gnuhealth.appointment.report.open.start'
    date_start = fields.Date('Date Start', required=True)
    date_end = fields.Date('Date End', required=True)
    healthprof = fields.Many2One('gnuhealth.healthprofessional', 'Health Prof')

    @staticmethod
    def default_date_start():
        return datetime.now()

    @staticmethod
    def default_date_end():
        return datetime.now()

    @staticmethod
    def default_healthprof():
        pool = Pool()
        HealthProfessional = pool.get('gnuhealth.healthprofessional')
        return HealthProfessional.get_health_professional()


class OpenAppointmentReport(Wizard):
    'Open Appointment Report'
    __name__ = 'gnuhealth.appointment.report.open'

    start = StateView(
        'gnuhealth.appointment.report.open.start',
        'health.appointments_report_open_start_view_form', [
            Button('Cancel', 'end', 'tryton-cancel'),
            Button('Open', 'open_', 'tryton-ok', default=True),
            ])
    open_ = StateAction('health.act_appointments_report_view_tree')

    def do_open_(self, action):
        health_prof = ''
        if self.start.healthprof:
            health_prof = self.start.healthprof.id
            
        action['pyson_context'] = PYSONEncoder().encode({
            'date_start': self.start.date_start,
            'date_end': self.start.date_end,
            'healthprof': health_prof,
            })

        # Show action name depending on whether is an specific hp
        # or for all professionals
        
        if health_prof:
            action['name'] += ' - %s' % (self.start.healthprof.rec_name)
        else:
            action['name'] += ' - %s' % "All Health Professionals"
        
        return action, {}

    def transition_open_(self):
        return 'end'


# PATIENT MEDICATION TREATMENT
class PatientMedication(ModelSQL, ModelView):
    'Patient Medication'
    __name__ = 'gnuhealth.patient.medication'

    medicament = fields.Many2One(
        'gnuhealth.medicament', 'Medicament',
        required=True, help='Prescribed Medicament')

    indication = fields.Many2One(
        'gnuhealth.pathology', 'Indication',
        help='Choose a disease for this medicament from the disease list. It'
        ' can be an existing disease of the patient or a prophylactic.')

    name = fields.Many2One(
        'gnuhealth.patient', 'Patient', readonly=True)

    healthprof = fields.Many2One(
        'gnuhealth.healthprofessional', 'Health Prof', readonly=True,
        help='Health Professional who prescribed or reviewed the medicament')

    institution = fields.Many2One(
        'gnuhealth.institution', 'Institution')

    is_active = fields.Boolean(
        'Active',
        help='Check if the patient is currently taking the medication')

    discontinued = fields.Boolean(
        'Discontinued')

    course_completed = fields.Boolean(
        'Course Completed')

    discontinued_reason = fields.Char(
        'Reason for discontinuation',
        states={
            'invisible': Not(Bool(Eval('discontinued'))),
            'required': Bool(Eval('discontinued')),
            },
        depends=['discontinued'],
        help='Short description for discontinuing the treatment',)

    adverse_reaction = fields.Text(
        'Adverse Reactions',
        help='Side effects or adverse reactions that the patient experienced')

    notes = fields.Text('Extra Info')

    start_treatment = fields.DateTime(
        'Start',
        help='Date of start of Treatment')

    end_treatment = fields.DateTime(
        'End', help='Date of start of Treatment')

    dose = fields.Float(
        'Dose',
        help='Amount of medication (eg, 250 mg) per dose')

    dose_unit = fields.Many2One(
        'gnuhealth.dose.unit', 'dose unit',
        help='Unit of measure for the medication to be taken')

    route = fields.Many2One(
        'gnuhealth.drug.route', 'Administration Route',
        help='Drug administration route code.')
    form = fields.Many2One(
        'gnuhealth.drug.form', 'Form',
        help='Drug form, such as tablet or gel')

    qty = fields.Integer(
        'x',
        help='Quantity of units (eg, 2 capsules) of the medicament')

    duration = fields.Integer(
        'Treatment duration',
        help='Period that the patient must take the medication. in minutes,'
        ' hours, days, months, years or indefinately')

    duration_period = fields.Selection([
        (None, ''),
        ('minutes', 'minutes'),
        ('hours', 'hours'),
        ('days', 'days'),
        ('months', 'months'),
        ('years', 'years'),
        ('indefinite', 'indefinite'),
        ], 'Treatment period', sort=False,
        help='Period that the patient must take the medication in minutes,'
        ' hours, days, months, years or indefinately')

    common_dosage = fields.Many2One(
        'gnuhealth.medication.dosage', 'Frequency',
        help='Common / standard dosage frequency for this medicament')

    admin_times = fields.Char(
        'Admin hours',
        help='Suggested administration hours. For example, at 08:00, 13:00'
        ' and 18:00 can be encoded like 08 13 18')

    frequency = fields.Integer(
        'Frequency',
        help='Time in between doses the patient must wait (ie, for 1 pill'
        ' each 8 hours, put here 8 and select \"hours\" in the unit field')

    frequency_unit = fields.Selection([
        (None, ''),
        ('seconds', 'seconds'),
        ('minutes', 'minutes'),
        ('hours', 'hours'),
        ('days', 'days'),
        ('weeks', 'weeks'),
        ('wr', 'when required'),
        ], 'unit', select=True, sort=False)

    frequency_prn = fields.Boolean(
        'PRN', help='Use it as needed, pro re nata')

    infusion = fields.Boolean(
        'Infusion', 
        help='Mark if the medication is in the form of infusion' \
        ' Intravenous, Gastrostomy tube, nasogastric, etc...' )
    infusion_rate = fields.Float('Rate',
            states={'invisible': Not(Bool(Eval('infusion')))})

    infusion_rate_units = fields.Selection([
        (None, ''),
        ('mlhr', 'mL/hour'),
        ], 'Unit Rate',
        states={'invisible': Not(Bool(Eval('infusion')))},
        select=True, sort=False)

    prescription = fields.Many2One(
        'gnuhealth.prescription.order', 'Prescription', readonly=True,
        domain=[('patient', '=', Eval('name'))],
        depends=['name'],
        help='Related prescription')

    @classmethod
    def __setup__(cls):
        super(PatientMedication, cls).__setup__()
        cls._error_messages.update({
            'end_date_before_start': 'The Medication END DATE'
            ' "%(end_treatment)s" is BEFORE the start date'
            ' "%(start_treatment)s"!',
            })
        cls._order.insert(0, ('is_active', 'DESC'))
        cls._order.insert(1, ('start_treatment', 'DESC'))

    @fields.depends('discontinued', 'course_completed')
    def on_change_with_is_active(self):
        return not (self.discontinued or self.course_completed)

    @fields.depends('is_active', 'course_completed')
    def on_change_with_discontinued(self):
        return not (self.is_active or self.course_completed)

    @fields.depends('is_active', 'discontinued')
    def on_change_with_course_completed(self):
        return not (self.is_active or self.discontinued)

    @staticmethod
    def default_is_active():
        return True

    @staticmethod
    def default_frequency_unit():
        return 'hours'

    @staticmethod
    def default_duration_period():
        return 'days'

    @staticmethod
    def default_qty():
        return 1

    @staticmethod
    def default_institution():
        HealthInst = Pool().get('gnuhealth.institution')
        institution = HealthInst.get_institution()
        return institution

    @staticmethod
    def default_healthprof():
        pool = Pool()
        HealthProf= pool.get('gnuhealth.healthprofessional')
        return HealthProf.get_health_professional()

    @classmethod
    def validate(cls, medications):
        super(PatientMedication, cls).validate(medications)
        for medication in medications:
            medication.validate_medication_dates()

    def validate_medication_dates(self):
        Lang = Pool().get('ir.lang')

        language, = Lang.search([
            ('code', '=', Transaction().language),
            ])
        if self.end_treatment:
            if (self.end_treatment < self.start_treatment):
                self.raise_user_error('end_date_before_start', {
                    'start_treatment': Lang.strftime(self.start_treatment,
                        language.code, language.date),
                    'end_treatment': Lang.strftime(self.end_treatment,
                        language.code, language.date),
                    })



# PATIENT VACCINATION INFORMATION
class PatientVaccination(ModelSQL, ModelView):
    'Patient Vaccination information'
    __name__ = 'gnuhealth.vaccination'

    name = fields.Many2One('gnuhealth.patient', 'Patient', required=True)

    vaccine = fields.Many2One(
        'gnuhealth.medicament', 'Vaccine', required=True,
        domain=[('is_vaccine', '=', True)],
        help='Vaccine Name. Make sure that the vaccine has all the'
        ' proper information at product level. Information such as provider,'
        ' supplier code, tracking number, etc.. This  information must always'
        ' be present. If available, please copy / scan the vaccine leaflet'
        ' and attach it to this record')

    admin_route = fields.Selection([
        (None, ''),
        ('im', 'Intramuscular'),
        ('sc', 'Subcutaneous'),
        ('id', 'Intradermal'),
        ('nas', 'Intranasal'),
        ('po', 'Oral'),
        ], 'Route', sort=False)

    picture = fields.Binary('Label')

    # Deprecated
    # Since 2.8, we include the expiration date and lot number information
    # in the health_stock module
    vaccine_expiration_date = fields.Date('Expiration date')

    vaccine_lot = fields.Char(
        'Lot Number',
        help='Please check on the vaccine (product) production lot numberand'
        ' tracking number when available !')

    institution = fields.Many2One(
        'gnuhealth.institution', 'Institution',
        help='Medical Center where the patient is being or was vaccinated')

    date = fields.DateTime('Date')
    dose = fields.Integer('Dose #')
    next_dose_date = fields.DateTime('Next Dose')
    observations = fields.Text('Observations')

    institution = fields.Many2One('gnuhealth.institution', 'Institution')

    healthprof = fields.Many2One(
        'gnuhealth.healthprofessional', 'Health Prof', readonly=True,
        help="Health Professional who administered or reviewed the vaccine \
         information")

    signed_by = fields.Many2One(
        'gnuhealth.healthprofessional', 'Signed by', readonly=True,
        states={'invisible': Equal(Eval('state'), 'in_progress')},
        help="Health Professional that signed the vaccination document")

    amount = fields.Float(
        'Amount',
        help='Amount of vaccine administered, in mL . The dose per mL \
            (eg, mcg, EL.U ..) can be found at the related medicament')

    admin_site = fields.Selection([
        (None, ''),
        ('lvl', 'left vastus lateralis'),
        ('rvl', 'right vastus lateralis'),
        ('ld', 'left deltoid'),
        ('rd', 'right deltoid'),
        ('lalt', 'left anterolateral fat of thigh'),
        ('ralt', 'right anterolateral fat of thigh'),
        ('lpua', 'left posterolateral fat of upper arm'),
        ('rpua', 'right posterolateral fat of upper arm'),
        ('lfa', 'left fore arm'),
        ('rfa', 'right fore arm')],'Admin Site')
    

    state = fields.Selection([
        (None, ''),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ], 'State', readonly=True)

    @staticmethod
    def default_institution():
        HealthInst = Pool().get('gnuhealth.institution')
        institution = HealthInst.get_institution()
        return institution

    @staticmethod
    def default_healthprof():
        pool = Pool()
        HealthProf= pool.get('gnuhealth.healthprofessional')
        return HealthProf.get_health_professional()

    @staticmethod
    def default_state():
        return 'in_progress'

    @staticmethod
    def default_date():
        return datetime.now()

    @staticmethod
    def default_dose():
        return 1

    @classmethod
    def __setup__(cls):
        super(PatientVaccination, cls).__setup__()
        t = cls.__table__()
        cls._sql_constraints = [
            ('dose_uniq', Unique(t,t.name, t.vaccine, t.dose),
                'This vaccine dose has been given already to the patient'),
            ]
        cls._error_messages.update({
            'next_dose_before_first': 'The Vaccine next dose is BEFORE the '
                'first one !'
            })

        cls._buttons.update({
            'sign': {'invisible': Equal(Eval('state'), 'done')}
            })


    @classmethod
    @ModelView.button
    def sign(cls, vaccinations):
        # Change the state of the vaccination to "Done"
        # and write the name of the signing health professional
        pool = Pool()
        HealthProfessional = pool.get('gnuhealth.healthprofessional')

        signing_hp = HealthProfessional.get_health_professional()
        if not signing_hp:
            cls.raise_user_error(
                "No health professional associated to this user !")

        cls.write(vaccinations, {
            'state': 'done',
            'signed_by': signing_hp})

    @classmethod
    def write(cls, vaccinations, vals):
        # Don't allow to modify the record if the vaccination has been signed
        if vaccinations[0].state == 'done':
            cls.raise_user_error(
                "This vaccination is at state Done\n"
                "You can no longer modify it.")
        return super(PatientVaccination, cls).write(vaccinations, vals)

    @classmethod
    def validate(cls, vaccines):
        super(PatientVaccination, cls).validate(vaccines)
        for vaccine in vaccines:
            vaccine.validate_next_dose_date()

    def validate_next_dose_date(self):
        if (self.next_dose_date):
            if (self.next_dose_date < self.date):
                self.raise_user_error('next_dose_before_first')


class PatientPrescriptionOrder(ModelSQL, ModelView):
    'Prescription Order'
    __name__ = 'gnuhealth.prescription.order'
    _rec_name = 'prescription_id'

    STATES = {'readonly': Not(Eval('state') == 'draft')}

    patient = fields.Many2One(
        'gnuhealth.patient', 'Patient', required=True, states = STATES)

    prescription_id = fields.Char(
        'Prescription ID',
        readonly=True, help='Type in the ID of this prescription')

    prescription_date = fields.DateTime('Prescription Date', states = STATES)
# In 1.8 we associate the prescribing doctor to the physician name
# instead to the old user_id (res.user)
    user_id = fields.Many2One('res.user', 'Prescribing Doctor', readonly=True)

    pharmacy = fields.Many2One(
        'party.party', 'Pharmacy', domain=[('is_pharmacy', '=', True)],
        states={
            'readonly': (Eval('state') != 'draft') & Bool(Eval('pharmacy')),
            },
        depends=['state'])

    prescription_line = fields.One2Many(
        'gnuhealth.prescription.line', 'name', 'Prescription line',
            states = STATES)

    notes = fields.Text('Prescription Notes', states = STATES)
    pregnancy_warning = fields.Boolean('Pregnancy Warning', readonly=True)
    prescription_warning_ack = fields.Boolean('Prescription verified',
        states = STATES)

    healthprof = fields.Many2One(
        'gnuhealth.healthprofessional', 'Prescribed by', readonly=True)

    report_prescription_date = fields.Function(fields.Date(
        'Prescription Date'), 'get_report_prescription_date')
    report_prescription_time = fields.Function(fields.Time(
        'Prescription Time'), 'get_report_prescription_time')

    state = fields.Selection([
        ('draft', 'Draft'),
        ('done', 'Done'),        
        ('validated', 'Validated'),        
        ], 'State', readonly=True, sort=False, states = STATES)

    @classmethod
    def __setup__(cls):
        super(PatientPrescriptionOrder, cls).__setup__()
        cls._error_messages.update({
            'drug_pregnancy_warning':
            '== DRUG AND PREGNANCY VERIFICATION ==\n\n'
            '- IS THE PATIENT PREGNANT ? \n'
            '- IS PLANNING to BECOME PREGNANT ?\n'
            '- HOW MANY WEEKS OF PREGNANCY \n\n'
            '- IS THE PATIENT BREASTFEEDING \n\n'
            'Verify and check for safety the prescribed drugs\n',
            'health_professional_warning':
            'No health professional associated to this user',
        })

        cls._order.insert(0, ('prescription_date', 'DESC'))

        cls._buttons.update({
            'create_prescription': {'invisible': Equal(Eval('state'), 'done')}
            })

    @classmethod
    def validate(cls, prescriptions):
        super(PatientPrescriptionOrder, cls).validate(prescriptions)
        for prescription in prescriptions:
            prescription.check_health_professional()
            prescription.check_prescription_warning()

    def check_health_professional(self):
        if not self.healthprof:
            self.raise_user_error('health_professional_warning')

    def check_prescription_warning(self):
        if not self.prescription_warning_ack:
            self.raise_user_error('drug_pregnancy_warning')

    @staticmethod
    def default_healthprof():
        pool = Pool()
        HealthProfessional = pool.get('gnuhealth.healthprofessional')
        return HealthProfessional.get_health_professional()

    # Method that makes the doctor to acknowledge if there is any
    # warning in the prescription

    @fields.depends('patient')
    def on_change_patient(self):
        preg_warning = False
        presc_warning_ack = True
        if self.patient:
            # Trigger the warning if the patient is at a childbearing age
            if (self.patient.childbearing_age):
                preg_warning = True
                presc_warning_ack = False
        
        self.prescription_warning_ack = presc_warning_ack
        self.pregnancy_warning = preg_warning


    @staticmethod
    def default_prescription_date():
        return datetime.now()

    @staticmethod
    def default_user_id():
        User = Pool().get('res.user')
        user = User(Transaction().user)
        return int(user.id)

    @classmethod
    def default_state(cls):
        return 'draft'

    def get_report_prescription_date(self, name):
        Company = Pool().get('company.company')

        timezone = None
        company_id = Transaction().context.get('company')
        if company_id:
            company = Company(company_id)
            if company.timezone:
                timezone = pytz.timezone(company.timezone)

        dt = self.prescription_date
        return datetime.astimezone(dt.replace(tzinfo=pytz.utc), timezone).date()

    def get_report_prescription_time(self, name):
        Company = Pool().get('company.company')

        timezone = None
        company_id = Transaction().context.get('company')
        if company_id:
            company = Company(company_id)
            if company.timezone:
                timezone = pytz.timezone(company.timezone)

        dt = self.prescription_date
        return datetime.astimezone(dt.replace(tzinfo=pytz.utc), timezone).time()

    @classmethod
    def create(cls, vlist):
        Sequence = Pool().get('ir.sequence')
        Config = Pool().get('gnuhealth.sequences')

        vlist = [x.copy() for x in vlist]
        for values in vlist:
            if not values.get('prescription_id'):
                config = Config(1)
                values['prescription_id'] = Sequence.get_id(
                    config.prescription_sequence.id)

        return super(PatientPrescriptionOrder, cls).create(vlist)

    @classmethod
    def copy(cls, prescriptions, default=None):
        if default is None:
            default = {}
        default = default.copy()
        default['prescription_id'] = None
        default['prescription_date'] = cls.default_prescription_date()
        return super(PatientPrescriptionOrder, cls).copy(
            prescriptions, default=default)


    @classmethod
    @ModelView.button
    def create_prescription(cls, prescriptions):
        prescription = prescriptions[0]

        # Change the state of the prescription to "Done"        

        cls.write(prescriptions, {
            'state': 'done',})



# PRESCRIPTION LINE
class PrescriptionLine(ModelSQL, ModelView):
    'Prescription Line'
    __name__ = 'gnuhealth.prescription.line'

# Remove inherits to be compatible with Tryton 2.8
#    _inherits = {'gnuhealth.medication.template': 'template'}
#    template = fields.Many2One('gnuhealth.medication.template',
#        'Medication Template')

    name = fields.Many2One('gnuhealth.prescription.order', 'Prescription ID')
    review = fields.DateTime('Valid Until', help="Until this date, the patient \
        usually can ask for a refill / reorder of this medicament")

    quantity = fields.Integer(
        'Units',
        help="Number of units of the medicament."
        " Example : 30 capsules of amoxicillin")

    refills = fields.Integer('Refills #')
    allow_substitution = fields.Boolean('Allow substitution')

    short_comment = fields.Char(
        'Comment', help='Short comment on the specific drug')

    prnt = fields.Boolean(
        'Print',
        help='Check this box to print this line of the prescription.')

    add_to_history = fields.Boolean(
        'Hist',
        help='Include this medication in the patient medication history')

    medicament = fields.Many2One(
        'gnuhealth.medicament', 'Medicament',
        required=True, help='Prescribed Medicament')

    indication = fields.Many2One(
        'gnuhealth.pathology', 'Indication',
        help='Choose a disease for this medicament from the disease list. It'
        ' can be an existing disease of the patient or a prophylactic.')

    start_treatment = fields.DateTime(
        'Start',
        help='Date of start of Treatment')

    end_treatment = fields.DateTime(
        'End', help='Date of start of Treatment')

    dose = fields.Float(
        'Dose',
        help='Amount of medication (eg, 250 mg) per dose')

    dose_unit = fields.Many2One(
        'gnuhealth.dose.unit', 'dose unit',
        help='Unit of measure for the medication to be taken')

    route = fields.Many2One(
        'gnuhealth.drug.route', 'Administration Route',
        help='Drug administration route code.')

    form = fields.Many2One(
        'gnuhealth.drug.form', 'Form',
        help='Drug form, such as tablet or gel')

    qty = fields.Integer(
        'x',
        help='Quantity of units (eg, 2 capsules) of the medicament')

    common_dosage = fields.Many2One(
        'gnuhealth.medication.dosage', 'Frequency',
        help='Common / standard dosage frequency for this medicament')

    admin_times = fields.Char(
        'Admin hours',
        help='Suggested administration hours. For example, at 08:00, 13:00'
        ' and 18:00 can be encoded like 08 13 18')

    frequency = fields.Integer(
        'Frequency',
        help='Time in between doses the patient must wait (ie, for 1 pill'
        ' each 8 hours, put here 8 and select \"hours\" in the unit field')

    frequency_unit = fields.Selection([
        (None, ''),
        ('seconds', 'seconds'),
        ('minutes', 'minutes'),
        ('hours', 'hours'),
        ('days', 'days'),
        ('weeks', 'weeks'),
        ('wr', 'when required'),
        ], 'unit', select=True, sort=False)

    frequency_prn = fields.Boolean('PRN', help='Use it as needed, pro re nata')

    duration = fields.Integer(
        'Treatment duration',
        help='Period that the patient must take the medication. in minutes,'
        ' hours, days, months, years or indefinately')

    duration_period = fields.Selection([
        (None, ''),
        ('minutes', 'minutes'),
        ('hours', 'hours'),
        ('days', 'days'),
        ('months', 'months'),
        ('years', 'years'),
        ('indefinite', 'indefinite'),
        ], 'Treatment period', sort=False,
        help='Period that the patient must take the medication in minutes,'
        ' hours, days, months, years or indefinately')


    infusion = fields.Boolean(
        'Infusion', 
        help='Mark if the medication is in the form of infusion' \
        ' Intravenous, Gastrostomy tube, nasogastric, etc...' )
    infusion_rate = fields.Float('Rate',
            states={'invisible': Not(Bool(Eval('infusion')))})

    infusion_rate_units = fields.Selection([
        (None, ''),
        ('mlhr', 'mL/hour'),
        ], 'Unit Rate',
        states={'invisible': Not(Bool(Eval('infusion')))},
        select=True, sort=False)

    @staticmethod
    def default_qty():
        return 1

    @staticmethod
    def default_duration_period():
        return 'days'

    @staticmethod
    def default_frequency_unit():
        return 'hours'

    @staticmethod
    def default_quantity():
        return 1

    @staticmethod
    def default_prnt():
        return True

    @staticmethod
    def default_start_treatment():
        return datetime.now()

    @fields.depends('medicament')
    def on_change_medicament(self):
        if self.medicament:
            self.dose = self.medicament.strength
            self.dose_unit = self.medicament.unit
            self.form = self.medicament.form
            self.route = self.medicament.route
        
    @classmethod
    def create(cls, vlist):
        vlist = [x.copy() for x in vlist]

        for values in vlist:
            if values.get('add_to_history'):
                                               
                Medication = Pool().get('gnuhealth.patient.medication')
                med = []

                # Retrieve the patient ID from the prescription
                Prescs = Pool().get('gnuhealth.prescription.order')
                patient = Prescs.browse([values['name']])[0].patient.id

                medicament = values['medicament']
                indication = values['indication']
                start_treatment = values.get('start_treatment')
                prescription = values['name']
                
                values = {
                    'name': patient,
                    'medicament': medicament,
                    'indication': indication,
                    'start_treatment': start_treatment,
                    'prescription': prescription
                    }
                    
                # Add the medicament from the prescription
                med.append(values)
                Medication.create(med)
 
        return super(PrescriptionLine, cls).create(vlist)


class PatientEvaluation(ModelSQL, ModelView):
    'Patient Evaluation'
    __name__ = 'gnuhealth.patient.evaluation'

    STATES = {'readonly': Eval('state') == 'signed'}

    def patient_age_at_evaluation(self, name):
        if (self.patient.name.dob and self.evaluation_start):
            return compute_age_from_dates(self.patient.name.dob, None,
                        None, None, 'age', self.evaluation_start.date())


    def evaluation_duration(self, name):
        if (self.evaluation_endtime and self.evaluation_start):
            return self.evaluation_endtime - self.evaluation_start

    def get_wait_time(self, name):
        # Compute wait time between checked-in and start of evaluation
        if self.appointment:
            if self.appointment.checked_in_date:
                if self.appointment.checked_in_date < self.evaluation_start:
                    return self.evaluation_start-self.appointment.checked_in_date

    code = fields.Char('Code', help="Unique code that \
        identifies the evaluation")

    patient = fields.Many2One('gnuhealth.patient', 'Patient',
        states = STATES)

    appointment = fields.Many2One(
        'gnuhealth.appointment', 'Appointment',
        domain=[('patient', '=', Eval('patient'))], depends=['patient'],
        help='Enter or select the date / ID of the appointment related to'
        ' this evaluation',
        states = STATES)

    related_condition = fields.Many2One('gnuhealth.patient.disease', 'Related condition',
        domain=[('name', '=', Eval('patient'))], depends=['patient'],
        help="Related condition related to this follow-up evaluation",
        states = {'invisible': (Eval('visit_type') != 'followup')})

    evaluation_start = fields.DateTime('Start', required=True,
        states = STATES)
    evaluation_endtime = fields.DateTime('End', states = STATES)

    evaluation_length = fields.Function(
        fields.TimeDelta(
            'Evaluation length',
            help="Duration of the evaluation"),
        'evaluation_duration')

    wait_time = fields.Function(fields.TimeDelta('Patient wait time',
        help="How long the patient waited"),
        'get_wait_time')
    
    state = fields.Selection([
        (None, ''),
        ('in_progress', 'In progress'),
        ('done', 'Done'),
        ('signed', 'Signed'),
        ], 'State', readonly=True, sort=False)

    next_evaluation = fields.Many2One(
        'gnuhealth.appointment',
        'Next Appointment', domain=[('patient', '=', Eval('patient'))],
        depends=['patient'],
        states = STATES)

    user_id = fields.Many2One('res.user', 'Last Changed by', readonly=True)
    healthprof = fields.Many2One(
        'gnuhealth.healthprofessional', 'Health Prof',
        help="Health professional that initiates the evaluation."
        "This health professional might or might not be the same that"
        " signs and finishes the evaluation."
        "The evaluation remains in progress state until it is signed"
        ", when it becomes read-only", readonly=True)

    signed_by = fields.Many2One(
        'gnuhealth.healthprofessional', 'Health Prof', readonly=True,
        states={'invisible': Equal(Eval('state'), 'in_progress')},
        help="Health Professional that finnished the patient evaluation")

    specialty = fields.Many2One('gnuhealth.specialty', 'Specialty',
        states = STATES)

    visit_type = fields.Selection([
        (None, ''),
        ('new', 'New health condition'),
        ('followup', 'Followup'),
        ('well_child', 'Well Child visit'),
        ('well_woman', 'Well Woman visit'),
        ('well_man', 'Well Man visit'),
        ], 'Visit', sort=False,
        states = STATES)

    urgency = fields.Selection([
        (None, ''),
        ('a', 'Normal'),
        ('b', 'Urgent'),
        ('c', 'Medical Emergency'),
        ], 'Urgency', sort=False,
        states = STATES)

    computed_age = fields.Function(fields.Char(
            'Age',
            help="Computed patient age at the moment of the evaluation"),
            'patient_age_at_evaluation')
            

    gender = fields.Function(fields.Selection([
        (None, ''),
        ('m', 'Male'),
        ('f', 'Female'),
        ('f-m','Female -> Male'),
        ('m-f','Male -> Female'),
        ], 'Gender'), 'get_patient_gender', searcher='search_patient_gender')

    information_source = fields.Char(
        'Source', help="Source of"
        "Information, eg : Self, relative, friend ...",
        states = STATES)

    reliable_info = fields.Boolean(
        'Reliable', help="Uncheck this option"
        "if the information provided by the source seems not reliable",
        states = STATES)

    derived_from = fields.Many2One(
        'gnuhealth.healthprofessional', 'Derived from',
        help='Health Professional who derived the case',
        states = STATES)

    derived_to = fields.Many2One(
        'gnuhealth.healthprofessional', 'Derived to',
        help='Health Professional to derive the case',
        states = STATES)

    evaluation_type = fields.Selection([
        (None, ''),
        ('outpatient', 'Outpatient'),
        ('inpatient', 'Inpatient'),
        ], 'Type', sort=False,
        states = STATES)

    chief_complaint = fields.Char('Chief Complaint', help='Chief Complaint',
        states = STATES)
    notes_complaint = fields.Text('Complaint details',
        states = STATES)
    present_illness = fields.Text('Present Illness',
        states = STATES)
    evaluation_summary = fields.Text('Clinical and physical',
        states = STATES)

    glycemia = fields.Float(
        'Glycemia',
        help='Last blood glucose level. Can be approximative. Expressed in mg/dL or mmol/L.',
        states = STATES)

    hba1c = fields.Float(
        'Glycated Hemoglobin',
        help='Last Glycated Hb level. Can be approximative. Expressed in mmol/mol.',
        states = STATES)

    cholesterol_total = fields.Integer(
        'Last Cholesterol',
        help='Last cholesterol reading. Can be approximative. Expressed in mg/dL or mmol/L.',
        states = STATES)

    hdl = fields.Integer(
        'Last HDL',
        help='Last HDL Cholesterol reading. Can be approximative. Expressed in mg/dL or mmol/L.',
        states = STATES)

    ldl = fields.Integer(
        'Last LDL',
        help='Last LDL Cholesterol reading. Can be approximative. Expressed in mg/dL or mmol/L.',
        states = STATES)

    tag = fields.Integer(
        'Last TAGs',
        help='Triacylglycerol(triglicerides) level. Can be approximative. Expressed in mg/dL or mmol/L.',
        states = STATES)

    systolic = fields.Integer('Systolic Pressure',
        help='Systolic pressure expressed in mmHg',
        states = STATES)

    diastolic = fields.Integer('Diastolic Pressure',
        help='Diastolic pressure expressed in mmHg',
        states = STATES)

    bpm = fields.Integer(
        'Heart Rate',
        help='Heart rate expressed in beats per minute',
        states = STATES)

    respiratory_rate = fields.Integer(
        'Respiratory Rate',
        help='Respiratory rate expressed in breaths per minute',
        states = STATES)

    osat = fields.Integer(
        'Oxygen Saturation',
        help='Arterial oxygen saturation expressed as a percentage',
        states = STATES)

    malnutrition = fields.Boolean(
        'Malnutrition',
        help='Check this box if the patient show signs of malnutrition. If'
        ' associated  to a disease, please encode the correspondent disease'
        ' on the patient disease history. For example, Moderate'
        ' protein-energy malnutrition, E44.0 in ICD-10 encoding',
        states = STATES)

    dehydration = fields.Boolean(
        'Dehydration',
        help='Check this box if the patient show signs of dehydration. If'
        ' associated  to a disease, please encode the  correspondent disease'
        ' on the patient disease history. For example, Volume Depletion, E86'
        ' in ICD-10 encoding',
        states = STATES)

    temperature = fields.Float(
        'Temperature',
        help='Temperature in celcius',
        states = STATES)

    weight = fields.Float('Weight', digits=(3,2),help='Weight in kilos',
        states = STATES)

    height = fields.Float('Height', digits=(3,1), help='Height in centimeters',
        states = STATES)

    bmi = fields.Float(
        'BMI', digits=(2,2),
        help='Body mass index',
        states = STATES)

    head_circumference = fields.Float(
        'Head',
        help='Head circumference in centimeters',
        states = STATES)

    abdominal_circ = fields.Float('Waist', digits=(3,1),
        help='Waist circumference in centimeters',
        states = STATES)

    hip = fields.Float('Hip', digits=(3,1),
        help='Hip circumference in centimeters', 
        states = STATES)

    whr = fields.Float(
        'WHR', digits=(2,2),help='Waist to hip ratio . Reference values:\n'
        'Men : < 0.9 Normal // 0.9 - 0.99 Overweight // > 1 Obesity \n'
        'Women : < 0.8 Normal // 0.8 - 0.84 Overweight // > 0.85 Obesity',
        states = STATES)

    # DEPRECATION NOTE : SIGNS AND SYMPTOMS FIELDS TO BE REMOVED IN 1.6 .
    # NOW WE USE A O2M OBJECT TO MAKE IT MORE SCALABLE, CLEARER AND FUNCTIONAL
    # TO WORK WITH THE CLINICAL FINDINGS OF THE PATIENT
    loc = fields.Integer(
        'Glasgow',
        help='Level of Consciousness - on Glasgow Coma Scale :  < 9 severe -'
        ' 9-12 Moderate, > 13 minor',
        states = STATES)
    loc_eyes = fields.Selection([
        ('1', 'Does not Open Eyes'),
        ('2', 'Opens eyes in response to painful stimuli'),
        ('3', 'Opens eyes in response to voice'),
        ('4', 'Opens eyes spontaneously'),
        ], 'Glasgow - Eyes', sort=False,
        states = STATES)
    loc_verbal = fields.Selection([
        ('1', 'Makes no sounds'),
        ('2', 'Incomprehensible sounds'),
        ('3', 'Utters inappropriate words'),
        ('4', 'Confused, disoriented'),
        ('5', 'Oriented, converses normally'),
        ], 'Glasgow - Verbal', sort=False,
        states = STATES)
    loc_motor = fields.Selection([
        ('1', 'Makes no movement'),
        ('2', 'Extension to painful stimuli - decerebrate response -'),
        ('3', 'Abnormal flexion to painful stimuli (decorticate response)'),
        ('4', 'Flexion / Withdrawal to painful stimuli'),
        ('5', 'Localizes painful stimuli'),
        ('6', 'Obeys commands'),
        ], 'Glasgow - Motor', sort=False,
        states = STATES)

    tremor = fields.Boolean(
        'Tremor',
        help='If associated  to a disease, please encode it on the patient'
        ' disease history',
        states = STATES)

    violent = fields.Boolean(
        'Violent Behaviour',
        help='Check this box if the patient is aggressive or violent at the'
        ' moment',
        states = STATES)

    mood = fields.Selection([
        (None, ''),
        ('n', 'Normal'),
        ('s', 'Sad'),
        ('f', 'Fear'),
        ('r', 'Rage'),
        ('h', 'Happy'),
        ('d', 'Disgust'),
        ('e', 'Euphoria'),
        ('fl', 'Flat'),
        ], 'Mood', sort=False,
        states = STATES)

    orientation = fields.Boolean(
        'Orientation',
        help='Check this box if the patient is disoriented in time and/or'
        ' space',
        states = STATES)

    memory = fields.Boolean(
        'Memory',
        help='Check this box if the patient has problems in short or long'
        ' term memory',
        states = STATES)

    knowledge_current_events = fields.Boolean(
        'Knowledge of Current Events',
        help='Check this box if the patient can not respond to public'
        ' notorious events',
        states = STATES)

    judgment = fields.Boolean(
        'Judgment',
        help='Check this box if the patient can not interpret basic scenario'
        ' solutions',
        states = STATES)

    abstraction = fields.Boolean(
        'Abstraction',
        help='Check this box if the patient presents abnormalities in'
        ' abstract reasoning',
        states = STATES)

    vocabulary = fields.Boolean(
        'Vocabulary',
        help='Check this box if the patient lacks basic intelectual capacity,'
        ' when she/he can not describe elementary objects',
        states = STATES)

    calculation_ability = fields.Boolean(
        'Calculation Ability',
        help='Check this box if the patient can not do simple arithmetic'
        ' problems',
        states = STATES)

    object_recognition = fields.Boolean(
        'Object Recognition',
        help='Check this box if the patient suffers from any sort of gnosia'
        ' disorders, such as agnosia, prosopagnosia ...',
        states = STATES)

    praxis = fields.Boolean(
        'Praxis',
        help='Check this box if the patient is unable to make voluntary'
        'movements',
        states = STATES)

    diagnosis = fields.Many2One(
        'gnuhealth.pathology', 'Main Condition',
        help='Presumptive Diagnosis. If no diagnosis can be made'
        ', encode the main sign or symptom.',
        states = STATES)

    secondary_conditions = fields.One2Many(
        'gnuhealth.secondary_condition',
        'evaluation', 'Other Conditions', help='Other '
        ' conditions found on the patient',
        states = STATES)

    diagnostic_hypothesis = fields.One2Many(
        'gnuhealth.diagnostic_hypothesis',
        'evaluation', 'Hypotheses / DDx', help='Other Diagnostic Hypotheses /'
        ' Differential Diagnosis (DDx)',
        states = STATES)

    signs_and_symptoms = fields.One2Many(
        'gnuhealth.signs_and_symptoms',
        'evaluation', 'Signs and Symptoms', help='Enter the Signs and Symptoms'
        ' for the patient in this evaluation.',
        states = STATES)

    info_diagnosis = fields.Text('Presumptive Diagnosis: Extra Info',
        states = STATES)
    directions = fields.Text('Plan',
        states = STATES)

    actions = fields.One2Many(
        'gnuhealth.directions', 'name', 'Procedures',
        help='Procedures / Actions to take',
        states = STATES)

    notes = fields.Text('Notes',
        states = STATES)
    
    discharge_reason = fields.Selection([
        (None, ''),
        ('home','Home / Selfcare'),
        ('transfer','Transferred to another institution'),
        ('against_advice','Left against medical advice'),
        ('death','Death')],
        'Discharge Reason', required=True, sort=False,
        states={'invisible': Equal(Eval('state'), 'in_progress'),
            'readonly': Eval('state') == 'signed'},
        help="Reason for patient discharge")

    institution = fields.Many2One('gnuhealth.institution', 'Institution',
        states = STATES)

    report_evaluation_date = fields.Function(fields.Date(
        'Evaluation Date'), 'get_report_evaluation_date')
    report_evaluation_time = fields.Function(fields.Time(
        'Evaluation Time'), 'get_report_evaluation_time')

    @staticmethod
    def default_institution():
        return HealthInstitution().get_institution()

    @staticmethod
    def default_discharge_reason():
        return 'home'

    def get_patient_gender(self, name):
        return self.patient.gender

    @classmethod
    def search_patient_gender(cls, name, clause):
        res = []
        value = clause[2]
        res.append(('patient.name.gender', clause[1], value))
        return res

    @classmethod
    def validate(cls, evaluations):
        super(PatientEvaluation, cls).validate(evaluations)
        for evaluation in evaluations:
            evaluation.validate_evaluation_period()
            evaluation.check_health_professional()

    def validate_evaluation_period(self):
        Lang = Pool().get('ir.lang')

        language, = Lang.search([
            ('code', '=', Transaction().language),
            ])
        if (self.evaluation_endtime and self.evaluation_start):
            if (self.evaluation_endtime < self.evaluation_start):
                self.raise_user_error('end_date_before_start', {
                        'evaluation_start': Lang.strftime(
                            self.evaluation_start, language.code, language.date),
                        'evaluation_endtime': Lang.strftime(
                            self.evaluation_endtime, language.code, language.date),
                        })

    def check_health_professional(self):
        if not self.healthprof:
            self.raise_user_error('health_professional_warning')


    @staticmethod
    def default_healthprof():
        pool = Pool()
        HealthProfessional = pool.get('gnuhealth.healthprofessional')
        return HealthProfessional.get_health_professional()

    @staticmethod
    def default_loc_eyes():
        return '4'

    @staticmethod
    def default_loc_verbal():
        return '5'

    @staticmethod
    def default_loc_motor():
        return '6'

    @staticmethod
    def default_loc():
        return 15

    @staticmethod
    def default_evaluation_type():
        return 'outpatient'

    @staticmethod
    def default_state():
        return 'in_progress'

    @fields.depends('weight', 'height')
    def on_change_with_bmi(self):
        if self.height and self.weight:
            if (self.height > 0):
                return round(self.weight / ((self.height / 100) ** 2),2)
            return 0

    @fields.depends('weight', 'height', 'bmi')
    def on_change_bmi(self):
        if self.height and self.weight:
            if (self.height > 0):
                self.bmi = round(self.weight / ((self.height / 100) ** 2),2)
        elif (self.height and not self.weight):
            self.weight = round((((self.height / 100) ** 2) * self.bmi),2)
                
        elif (self.weight and not self.height):
            self.height = round(((self.weight / self.bmi)**(0.5)*100),2)

    @fields.depends('loc_verbal', 'loc_motor', 'loc_eyes')
    def on_change_with_loc(self):
        return int(self.loc_motor) + int(self.loc_eyes) + int(self.loc_verbal)


    # Show the gender and age upon entering the patient 
    # These two are function fields (don't exist at DB level)
    @fields.depends('patient')
    def on_change_patient(self):
        gender=None
        age=''
        self.gender = self.patient.gender
        self.computed_age = self.patient.age

    
    @staticmethod
    def default_information_source():
        return 'Self'

    @staticmethod
    def default_reliable_info():
        return True

    @staticmethod
    def default_evaluation_start():
        return datetime.now()

    # Calculate the WH ratio
    @fields.depends('abdominal_circ', 'hip', 'whr')
    def on_change_with_whr(self):
        waist = self.abdominal_circ
        hip = self.hip
        if (hip > 0):
            whr = round((waist / hip),2)
        else:
            whr = 0
        return whr

    def get_rec_name(self, name):
        return str(self.evaluation_start)

    def get_report_evaluation_date(self, name):
        Company = Pool().get('company.company')

        timezone = None
        company_id = Transaction().context.get('company')
        if company_id:
            company = Company(company_id)
            if company.timezone:
                timezone = pytz.timezone(company.timezone)

        dt = self.evaluation_start
        return datetime.astimezone(dt.replace(tzinfo=pytz.utc), timezone).date()

    def get_report_evaluation_time(self, name):
        Company = Pool().get('company.company')

        timezone = None
        company_id = Transaction().context.get('company')
        if company_id:
            company = Company(company_id)
            if company.timezone:
                timezone = pytz.timezone(company.timezone)

        dt = self.evaluation_start
        return datetime.astimezone(dt.replace(tzinfo=pytz.utc), timezone).time()

    @classmethod
    def __setup__(cls):
        super(PatientEvaluation, cls).__setup__()
        
        t = cls.__table__()
        cls._sql_constraints = [
            ('code_unique', Unique(t,t.code),
                'The evaluation code must be unique !'),
            ]


        cls._error_messages.update({
            'health_professional_warning':
                'No health professional associated to this user',
            'end_date_before_start': 'End time "%(evaluation_endtime)s" BEFORE'
                ' evaluation start "%(evaluation_start)s"'
        })

        cls._buttons.update({
            'end_evaluation': {'invisible': Or(Equal(Eval('state'), 'signed'),
                Equal(Eval('state'), 'done'))}
            })

    @classmethod
    def create(cls, vlist):
        Sequence = Pool().get('ir.sequence')
        Config = Pool().get('gnuhealth.sequences')

        vlist = [x.copy() for x in vlist]
        for values in vlist:
            if not values.get('code'):
                config = Config(1)
                values['code'] = Sequence.get_id(
                    config.patient_evaluation_sequence.id)

        return super(PatientEvaluation, cls).create(vlist)


    # End the evaluation and discharge the patient

    @classmethod
    @ModelView.button
    def end_evaluation(cls, evaluations):
        pool = Pool()
        HealthProfessional = pool.get('gnuhealth.healthprofessional')
        Appointment = pool.get('gnuhealth.appointment')
        
        evaluation_id = evaluations[0]

        patient_app=[]
        
        # Change the state of the evaluation to "Done"

        signing_hp = HealthProfessional.get_health_professional()
        
        cls.write(evaluations, {
            'state': 'done',
            'signed_by': signing_hp,
            'evaluation_endtime': datetime.now()
            })
        
        # If there is an appointment associated to this evaluation
        # set it to state "Done"
        
        if evaluations[0].appointment:
            patient_app.append(evaluations[0].appointment)
            Appointment.write(patient_app, {
                'state': 'done',
                })

# PATIENT EVALUATION DIRECTIONS
class Directions(ModelSQL, ModelView):
    'Patient Directions'
    __name__ = 'gnuhealth.directions'

    name = fields.Many2One(
        'gnuhealth.patient.evaluation', 'Evaluation', readonly=True)

    procedure = fields.Many2One(
        'gnuhealth.procedure', 'Procedure', required=True)

    comments = fields.Char('Comments')


# SECONDARY CONDITIONS ASSOCIATED TO THE PATIENT IN THE EVALUATION
class SecondaryCondition(ModelSQL, ModelView):
    'Secondary Conditions'
    __name__ = 'gnuhealth.secondary_condition'

    evaluation = fields.Many2One(
        'gnuhealth.patient.evaluation', 'Evaluation', readonly=True)

    pathology = fields.Many2One(
        'gnuhealth.pathology', 'Pathology', required=True)

    comments = fields.Char('Comments')


# PATIENT EVALUATION OTHER DIAGNOSTIC HYPOTHESES
class DiagnosticHypothesis(ModelSQL, ModelView):
    'Other Diagnostic Hypothesis'
    __name__ = 'gnuhealth.diagnostic_hypothesis'

    evaluation = fields.Many2One(
        'gnuhealth.patient.evaluation', 'Evaluation', readonly=True)

    pathology = fields.Many2One(
        'gnuhealth.pathology', 'Pathology', required=True)

    comments = fields.Char('Comments')


# PATIENT EVALUATION CLINICAL FINDINGS (SIGNS AND SYMPTOMS)
class SignsAndSymptoms(ModelSQL, ModelView):
    'Evaluation Signs and Symptoms'
    __name__ = 'gnuhealth.signs_and_symptoms'

    evaluation = fields.Many2One(
        'gnuhealth.patient.evaluation', 'Evaluation', readonly=True)

    sign_or_symptom = fields.Selection([
        (None, ''),
        ('sign', 'Sign'),
        ('symptom', 'Symptom')],
        'Subjective / Objective', required=True)

    clinical = fields.Many2One(
        'gnuhealth.pathology', 'Sign or Symptom',
        required=True)

    comments = fields.Char('Comments')

# ECG
class PatientECG(ModelSQL, ModelView):
    'Patient ECG'
    __name__ = 'gnuhealth.patient.ecg'

    name = fields.Many2One('gnuhealth.patient',
        'Patient', required=True)

    ecg_date = fields.DateTime('Date', required=True)
    lead = fields.Selection([
        (None, ''),
        ('i', 'I'),
        ('ii', 'II'),
        ('iii', 'III'),
        ('avf', 'aVF'),
        ('avr', 'aVR'),
        ('avl', 'aVL'),
        ('v1', 'V1'),
        ('v2', 'V2'),
        ('v3', 'V3'),
        ('v4', 'V4'),
        ('v5', 'V5'),
        ('v6', 'V6')],
        'Lead', sort=False)

    axis = fields.Selection([
        (None, ''),
        ('normal', 'Normal Axis'),
        ('left', 'Left deviation'),
        ('right', 'Right deviation'),
        ('extreme_right', 'Extreme right deviation')],
        'Axis', sort=False, required=True)

    rate = fields.Integer('Rate', required=True)

    rhythm = fields.Selection([
        (None, ''),
        ('regular', 'Regular'),
        ('irregular', 'Irregular')],
        'Rhythm', sort=False, required=True)

    pacemaker = fields.Selection([
        (None, ''),
        ('sa', 'Sinus Node'),
        ('av', 'Atrioventricular'),
        ('pk', 'Purkinje')
        ],
        'Pacemaker', sort=False, required=True)

    pr = fields.Integer('PR', help="Duration of PR interval in milliseconds")
    qrs = fields.Integer('QRS',
        help="Duration of QRS interval in milliseconds")
    qt = fields.Integer('QT', help="Duration of QT interval in milliseconds")
    st_segment = fields.Selection([
        (None, ''),
        ('normal', 'Normal'),
        ('depressed', 'Depressed'),
        ('elevated', 'Elevated')],
        'ST Segment', sort=False, required=True)

    twave_inversion = fields.Boolean('T wave inversion')

    interpretation = fields.Char('Interpretation', required=True)
    ecg_strip = fields.Binary('ECG Strip')

    healthprof = fields.Many2One(
        'gnuhealth.healthprofessional',
        'Health Prof', readonly=True,
        help='Health Professional who performed the ECG')

    institution = fields.Many2One('gnuhealth.institution', 'Institution')

    # Default ECG date
    @staticmethod
    def default_ecg_date():
        return datetime.now()
        
    @staticmethod
    def default_institution():
        return HealthInstitution().get_institution()

    @staticmethod
    def default_healthprof():
        pool = Pool()
        HealthProfessional = pool.get('gnuhealth.healthprofessional')
        return HealthProfessional.get_health_professional()

    @classmethod
    def validate(cls, ecgs):
        super(PatientECG, cls).validate(ecgs)
        for ecg in ecgs:
            ecg.check_health_professional()

    def check_health_professional(self):
        if not self.healthprof:
            self.raise_user_error('health_professional_warning')


    # Return the ECG Interpretation with main components
    def get_rec_name(self, name):
        if self.name:
            res = str(self.interpretation) + ' // Rate ' + str(self.rate)
        return res


    @classmethod
    def __setup__(cls):
        super(PatientECG, cls).__setup__()
        cls._error_messages.update({
            'health_professional_warning':
                'No health professional associated to this user',
        })

class ProductTemplate(ModelSQL, ModelView):
    __name__ = 'product.template'
    """
    Allow to change the values from the product templates 
    coming from XML files
    """
    @classmethod
    def check_xml_record(cls, records, values):
        return True
