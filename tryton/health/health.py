# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2008-2013  Luis Falcon <falcon@gnu.org>
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
from datetime import datetime
from trytond.model import ModelView, ModelSingleton, ModelSQL, fields
from trytond.wizard import Wizard, StateAction, StateView, Button
from trytond.transaction import Transaction
from trytond.backend import TableHandler
from trytond.pyson import Eval, Not, Bool, PYSONEncoder, Equal
from trytond.pool import Pool


__all__ = [
    'DrugDoseUnits', 'MedicationFrequency', 'DrugForm', 'DrugRoute',
    'Occupation', 'Ethnicity', 'MedicalSpecialty', 'HealthProfessional',
    'HealthProfessionalSpecialties', 'PhysicianSP', 'OperationalArea',
    'OperationalSector', 'Family', 'FamilyMember', 'DomiciliaryUnit',
    'MedicamentCategory', 'Medicament', 'PathologyCategory',
    'PathologyGroup', 'Pathology', 'DiseaseMembers', 'ProcedureCode',
    'InsurancePlan', 'Insurance', 'AlternativePersonID',
    'PartyPatient', 'PartyAddress', 'ProductCategory',
    'ProductTemplate', 'Product', 'GnuHealthSequences', 'PatientData',
    'PatientDiseaseInfo', 'Appointment', 'AppointmentReport',
    'OpenAppointmentReportStart', 'OpenAppointmentReport',
    'PatientMedication', 'PatientVaccination',
    'PatientPrescriptionOrder', 'PrescriptionLine', 'PatientEvaluation',
    'Directions', 'SecondaryCondition', 'DiagnosticHypothesis',
    'SignsAndSymptoms', 'HospitalBuilding', 'HospitalUnit',
    'HospitalOR', 'HospitalWard', 'HospitalBed']


class DrugDoseUnits(ModelSQL, ModelView):
    'Drug Dose Unit'
    __name__ = 'gnuhealth.dose.unit'

    name = fields.Char('Unit', required=True, select=True, translate=True)
    desc = fields.Char('Description', translate=True)

    @classmethod
    def __setup__(cls):
        super(DrugDoseUnits, cls).__setup__()
        cls._sql_constraints = [
            ('name_uniq', 'UNIQUE(name)', 'The Unit must be unique !'),
        ]


class MedicationFrequency(ModelSQL, ModelView):
    'Medication Common Frequencies'
    __name__ = 'gnuhealth.medication.dosage'

    name = fields.Char(
        'Frequency', required=True, select=True, translate=True,
        help='Common frequency name')
    code = fields.Char(
        'Code',
        help='Dosage Code,for example: SNOMED 229798009 = 3 times per day')
    abbreviation = fields.Char(
        'Abbreviation',
        help='Dosage abbreviation, such as tid in the US or tds in the UK')

    @classmethod
    def __setup__(cls):
        super(MedicationFrequency, cls).__setup__()
        cls._sql_constraints = [
            ('name_uniq', 'UNIQUE(name)', 'The Unit must be unique !'),
        ]


class DrugForm(ModelSQL, ModelView):
    'Drug Form'
    __name__ = 'gnuhealth.drug.form'

    name = fields.Char('Form', required=True, select=True, translate=True)
    code = fields.Char('Code')

    @classmethod
    def __setup__(cls):
        super(DrugForm, cls).__setup__()
        cls._sql_constraints = [
            ('name_uniq', 'UNIQUE(name)', 'The Unit must be unique !'),
        ]


class DrugRoute(ModelSQL, ModelView):
    'Drug Administration Route'
    __name__ = 'gnuhealth.drug.route'

    name = fields.Char('Unit', required=True, select=True, translate=True)
    code = fields.Char('Code')

    @classmethod
    def __setup__(cls):
        super(DrugRoute, cls).__setup__()
        cls._sql_constraints = [
            ('name_uniq', 'UNIQUE(name)', 'The Name must be unique !'),
        ]


class Occupation(ModelSQL, ModelView):
    'Occupation'
    __name__ = 'gnuhealth.occupation'

    name = fields.Char('Name', required=True, translate=True)
    code = fields.Char('Code')

    @classmethod
    def __setup__(cls):
        super(Occupation, cls).__setup__()
        cls._sql_constraints = [
            ('name_uniq', 'UNIQUE(name)', 'The Name must be unique !'),
        ]


class Ethnicity(ModelSQL, ModelView):
    'Ethnicity'
    __name__ = 'gnuhealth.ethnicity'

    name = fields.Char('Name', required=True, translate=True)
    code = fields.Char('Code')
    notes = fields.Char('Notes')

    @classmethod
    def __setup__(cls):
        super(Ethnicity, cls).__setup__()
        cls._sql_constraints = [
            ('name_uniq', 'UNIQUE(name)', 'The Name must be unique !'),
        ]


class MedicalSpecialty(ModelSQL, ModelView):
    'Medical Specialty'
    __name__ = 'gnuhealth.specialty'

    name = fields.Char(
        'Specialty', required=True, translate=True,
        help='ie, Addiction Psychiatry')
    code = fields.Char('Code', help='ie, ADP')

    @classmethod
    def __setup__(cls):
        super(MedicalSpecialty, cls).__setup__()
        cls._sql_constraints = [
            ('name_uniq', 'UNIQUE(name)', 'The Specialty must be unique !'),
        ]


class HealthProfessional(ModelSQL, ModelView):
    'Health Professional'
    __name__ = 'gnuhealth.physician'

    @classmethod
    def get_health_professional(cls):
        # Get the professional associated to the internal user id
        # that logs into GNU Health
        cursor = Transaction().cursor
        User = Pool().get('res.user')
        user = User(Transaction().user)
        login_user_id = int(user.id)
        cursor.execute('SELECT id FROM party_party WHERE is_doctor=True AND \
            internal_user = %s LIMIT 1', (login_user_id,))
        partner_id = cursor.fetchone()
        if partner_id:
            cursor = Transaction().cursor
            cursor.execute('SELECT id FROM gnuhealth_physician WHERE \
                name = %s LIMIT 1', (partner_id[0],))
            doctor_id = cursor.fetchone()
            if (doctor_id):
                return int(doctor_id[0])

    name = fields.Many2One(
        'party.party', 'Health Professional', required=True,
        domain=[
            ('is_doctor', '=', True),
            ('is_person', '=', True),
            ],
        help='Health Professional\'s Name, from the partner list')

    institution = fields.Many2One(
        'party.party', 'Institution',
        domain=[('is_institution', '=', True)],
        help='Instituion where she/he works')

    code = fields.Char('ID', help='License ID')

    specialties = fields.One2Many(
        'gnuhealth.hp_specialty', 'name', 'Specialties')

    info = fields.Text('Extra info')

    def get_rec_name(self, name):
        if self.name:
            res = self.name.name
            if self.name.lastname:
                res = self.name.lastname + ', ' + self.name.name
        return res

    @classmethod
    def __setup__(cls):
        super(HealthProfessional, cls).__setup__()
        cls._sql_constraints = [
            ('hp_uniq', 'UNIQUE(name)',
                'The health professional must be unique'),
        ]

class HealthProfessionalSpecialties(ModelSQL, ModelView):
    'Health Professional Specialties'
    __name__ = 'gnuhealth.hp_specialty'

    name = fields.Many2One('gnuhealth.physician', 'Health Professional')

    specialty = fields.Many2One(
        'gnuhealth.specialty', 'Specialty', help='Specialty Code')

    def get_rec_name(self, name):
        return self.specialty.name


class PhysicianSP(ModelSQL, ModelView):
    # Add Main Specialty field after from the Health Professional Speciality
    'Health Professional'
    __name__ = 'gnuhealth.physician'

    main_specialty = fields.Many2One(
        'gnuhealth.hp_specialty', 'Main Specialty',
        domain=[('name', '=', Eval('active_id'))], help='Specialty Code')

    @classmethod
    # Update to version 2.2
    def __register__(cls, module_name):
        super(PhysicianSP, cls).__register__(module_name)

        cursor = Transaction().cursor
        table = TableHandler(cursor, cls, module_name)
        # Insert the current "specialty" associated to the HP in the
        # table that keeps the specialties associated to different health
        # professionals, gnuhealth.hp_specialty

        if table.column_exist('specialty'):
            # Update the list of specialties of that health professional
            # with the current specialty
            cursor.execute(
                "INSERT INTO gnuhealth_hp_specialty (name, specialty) \
                SELECT id, specialty from gnuhealth_physician;")
            # Drop old specialty column, replaced by main_specialty
            table.drop_column('specialty')


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
        cls._sql_constraints += [
            ('name_uniq', 'UNIQUE(name)',
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
        cls._sql_constraints += [
            ('name_uniq', 'UNIQUE(name, operational_area)',
                'The operational sector must be unique in each'
                ' operational area!'),
        ]


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
        cls._sql_constraints = [
            ('name_uniq', 'UNIQUE(name)', 'The Family Code must be unique !'),
        ]

    @classmethod
    # Update to version 2.0
    def __register__(cls, module_name):
        super(Family, cls).__register__(module_name)

        cursor = Transaction().cursor
        table = TableHandler(cursor, cls, module_name)
        # Remove Operational Sector from the family model
        # The operational Sector is linked to the Domiciliary Unit
        # Since GHealth 2.0 , the family model will contain their
        # members and their role.

        if table.column_exist('operational_sector'):
            table.drop_column('operational_sector')


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


class DomiciliaryUnit(ModelSQL, ModelView):
    'Domiciliary Unit'
    __name__ = 'gnuhealth.du'

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
        'country.subdivision', 'Province',
        domain=[('country', '=', Eval('address_country'))],
        depends=['address_country'])

    operational_sector = fields.Many2One(
        'gnuhealth.operational_sector', 'Operational Sector')

    picture = fields.Binary('Picture')

    latitude = fields.Numeric('Latidude', digits=(3, 14))
    longitude = fields.Numeric('Longitude', digits=(4, 14))

    urladdr = fields.Char(
        'OSM Map', on_change_with=[
            'latitude', 'longitude', 'address_street', 'address_street_number',
            'address_district', 'address_municipality', 'address_city',
            'address_zip', 'address_subdivision', 'address_country'],
        help="Locates the DU on the Open Street Map by default")

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

    def on_change_with_urladdr(self):
        # Generates the URL to be used in OpenStreetMap
        # The address will be mapped to the URL in the following way
        # If the latitud and longitude of the DU are given, then those
        # parameters will be used.
        # Otherwise, it will try to find the address by the
        # Street, municipality, city, postalcode, state and country.

        if (self.latitude and self.longitude):
            ret_url = 'http://openstreetmap.org/?mlat=' + \
                str(self.latitude) + '&mlon=' + str(self.longitude)

        else:
            state = ''
            country = ''
            street_number = str(self.address_street_number).encode('utf-8') \
                or ''
            street = (self.address_street).encode('utf-8') or ''
            municipality = (self.address_municipality).encode('utf-8') or ''
            city = (self.address_city).encode('utf-8') or ''
            if (self.address_subdivision):
                state = (self.address_subdivision.name).encode('utf-8') or ''
            postalcode = (self.address_zip).encode('utf-8') or ''

            if (self.address_country):
                country = (self.address_country.code).encode('utf-8') or ''

            ret_url = 'http://nominatim.openstreetmap.org/search?' + \
                'street=' + street_number + ' ' + \
                street + '&county=' + municipality \
                + '&city=' + city + '&state=' + state \
                + '&postalcode=' + postalcode + '&country=' + country

        return ret_url

    @classmethod
    def __setup__(cls):
        super(DomiciliaryUnit, cls).__setup__()
        cls._sql_constraints = [
            ('name_uniq', 'UNIQUE(name)',
                'The Domiciliary Unit must be unique !'),
        ]


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
    def __register__(cls, module_name):
        cursor = Transaction().cursor
        super(MedicamentCategory, cls).__register__(module_name)

        # Upgrade from GNU Health 1.8.1: moved who essential medicines
        cursor.execute(
            "UPDATE ir_model_data "
            "SET module = REPLACE(module, %s, %s) "
            "WHERE (fs_id like 'em%%' OR fs_id = 'medicament') "
            "  AND module = %s",
            ('health', 'health_who_essential_medicines', module_name,))

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
    _rec_name = 'active_component'

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
        help='** FDA Pregancy Categories ***\n'
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
    notes = fields.Text('Extra Info')

    @classmethod
    def __register__(cls, module_name):
        cursor = Transaction().cursor
        super(Medicament, cls).__register__(module_name)

        # Upgrade from GNU Health 1.8.1: moved who essential medicines
        cursor.execute(
            "UPDATE ir_model_data "
            "SET module = REPLACE(module, %s, %s) "
            "WHERE fs_id like 'meds_em%%' AND module = %s",
            ('health', 'health_who_essential_medicines', module_name,))

    def get_rec_name(self, name):
        return self.name.name

    @classmethod
    def check_xml_record(cls, records, values):
        return True


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

    @classmethod
    def __register__(cls, module_name):
        # Upgrade from GNU Health 1.4.5
        super(PathologyGroup, cls).__register__(module_name)

        cursor = Transaction().cursor
        table = TableHandler(cursor, cls, module_name)

        # Drop old foreign key and change to char name
        table.drop_fk('name')

        table.alter_type('name', 'varchar')

        # Drop group column. No longer required
        table.drop_column('group')

        # Migration from 2.4: drop required on sequence
        table.not_null_action('sequence', action='remove')


class Pathology(ModelSQL, ModelView):
    'Diseases'
    __name__ = 'gnuhealth.pathology'

    name = fields.Char(
        'Name', required=True, translate=True, help='Disease name')
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

    @classmethod
    def __setup__(cls):
        super(Pathology, cls).__setup__()
        cls._sql_constraints += [
            ('code_uniq', 'UNIQUE(code)', 'The disease code must be unique'),
        ]


# DISEASE GROUP MEMBERS
class DiseaseMembers(ModelSQL, ModelView):
    'Disease group members'
    __name__ = 'gnuhealth.disease_group.members'

    name = fields.Many2One('gnuhealth.pathology', 'Disease', readonly=True)
    disease_group = fields.Many2One(
        'gnuhealth.pathology.group', 'Group', required=True)


class ProcedureCode(ModelSQL, ModelView):
    'Medical Procedures'
    __name__ = 'gnuhealth.procedure'

    name = fields.Char('Code', required=True)
    description = fields.Char('Long Text', translate=True)

    # Search by the Procedure code or the description
    @classmethod
    def search_rec_name(cls, name, clause):
        field = None
        for field in ('name', 'description'):
            procedures = cls.search([(field,) + clause[1:]], limit=1)
            if procedures:
                break
        if procedures:
            return [(field,) + clause[1:]]
        return [(cls._rec_name,) + clause[1:]]

    # Include code + description in result
    def get_rec_name(self, name):
        return (self.name + ' : ' + self.description)


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
        'Category', help='Insurance company plan / category')

    insurance_type = fields.Selection([
        (None, ''),
        ('state', 'State'),
        ('labour_union', 'Labour Union / Syndical'),
        ('private', 'Private'),
        ], 'Insurance Type', select=True)
    plan_id = fields.Many2One(
        'gnuhealth.insurance.plan', 'Plan',
        help='Insurance company plan',
        domain=[('company', '=', Eval('company'))])

    notes = fields.Text('Extra Info')

    def get_rec_name(self, name):
        return (self.company.name + ' : ' + self.number)


class AlternativePersonID (ModelSQL, ModelView):
    'Alternative person ID'
    __name__ = 'gnuhealth.person_alternative_identification'

    name = fields.Many2One('party.party', 'Party', readonly=True)
    code = fields.Char('Code', required=True)
    alternative_id_type = fields.Selection(
        [
            ('country_id', 'Country of origin SSN'),
            ('passport', 'Passport'),
            ('other', 'Other'),
        ], 'ID type', required=True, sort=False,)

    comments = fields.Char('Comments')


class PartyPatient (ModelSQL, ModelView):
    'Party'
    __name__ = 'party.party'

    activation_date = fields.Date(
        'Activation date', help='Date of activation of the party')

    alias = fields.Char('Alias', help='Common name that the Party is reffered')
    ref = fields.Char(
        'SSN',
        help='Patient Social Security Number or equivalent',
        states={'invisible': Not(Bool(Eval('is_person')))})

    unidentified = fields.Boolean(
        'Unidentified',
        help='Patient is currently unidentified',
        states={'invisible': Not(Bool(Eval('is_person')))})

    is_person = fields.Boolean(
        'Person',
        on_change_with=['is_person', 'is_patient', 'is_doctor'],
        help='Check if the party is a person.')

    is_patient = fields.Boolean(
        'Patient',
        states={'invisible': Not(Bool(Eval('is_person')))},
        help='Check if the party is a patient')

    is_doctor = fields.Boolean(
        'Health Prof',
        states={'invisible': Not(Bool(Eval('is_person')))},
        help='Check if the party is a health professional')

    is_institution = fields.Boolean(
        'Institution', help='Check if the party is a Medical Center')
    is_insurance_company = fields.Boolean(
        'Insurance Company', help='Check if the party is an Insurance Company')
    is_pharmacy = fields.Boolean(
        'Pharmacy', help='Check if the party is a Pharmacy')

    lastname = fields.Char('Last Name', help='Last Name')
    dob = fields.Date('DoB', help='Date of Birth')

    sex = fields.Selection([
        (None, ''),
        ('m', 'Male'),
        ('f', 'Female'),
        ], 'Sex', states={'required': Bool(Eval('is_person'))})

    photo = fields.Binary('Picture')
    ethnic_group = fields.Many2One('gnuhealth.ethnicity', 'Ethnic group')

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
        'country.country', 'Country of Residence', help='Country of Residence')
    alternative_identification = fields.Boolean(
        'Alternative ID', help='Other type of '
        'identification, not the official SSN from this country health'
        ' center. Examples : Passport, foreign ID,..')

    alternative_ids = fields.One2Many(
        'gnuhealth.person_alternative_identification',
        'name', 'Alternative IDs',
        states={'invisible': Not(Bool(Eval('alternative_identification')))})

    insurance = fields.One2Many('gnuhealth.insurance', 'name', 'Insurance')

    internal_user = fields.Many2One(
        'res.user', 'Internal User',
        help='In GNU Health is the user (doctor, nurse) that logins.When the'
        ' party is a doctor or a health professional, it will be the user'
        ' that maps the doctor\'s party name. It must be present.',
        states={
            'invisible': Not(Bool(Eval('is_doctor'))),
            'required': Bool(Eval('is_doctor')),
            })

    insurance_company_type = fields.Selection([
        (None, ''),
        ('state', 'State'),
        ('labour_union', 'Labour Union / Syndical'),
        ('private', 'Private'),
        ], 'Insurance Type', select=True)
    insurance_plan_ids = fields.One2Many(
        'gnuhealth.insurance.plan', 'company', 'Insurance Plans')

    du = fields.Many2One('gnuhealth.du', 'Domiciliary Unit')

    @classmethod
    def write(cls, parties, vals):
        # We use this method overwrite to make the fields that have a unique
        # constraint get the NULL value at PostgreSQL level, and not the value
        # '' coming from the client

        if vals.get('ref') == '':
            vals['ref'] = None
        return super(PartyPatient, cls).write(parties, vals)

    @classmethod
    def create(cls, vlist):
        # We use this method overwrite to make the fields that have a unique
        # constraint get the NULL value at PostgreSQL level, and not the value
        # '' coming from the client

        vlist = [x.copy() for x in vlist]
        for values in vlist:
            if 'ref' in values and not values['ref']:
                values['ref'] = None

        return super(PartyPatient, cls).create(vlist)

    @classmethod
    def __setup__(cls):
        super(PartyPatient, cls).__setup__()
        cls._sql_constraints += [
            ('ref_uniq', 'UNIQUE(ref)', 'The SSN must be unique'),
            ('internal_user_uniq', 'UNIQUE(internal_user)',
                'This health professional is already assigned to a party')]

    def get_rec_name(self, name):
        if self.lastname:
            return self.lastname + ', ' + self.name
        else:
            return self.name

    @classmethod
    def search_rec_name(cls, name, clause):
        field = None
        for field in ('name', 'lastname'):
            parties = cls.search([(field,) + clause[1:]], limit=1)
            if parties:
                break
        if parties:
            return [(field,) + clause[1:]]
        return [(cls._rec_name,) + clause[1:]]

    def on_change_with_is_person(self):
        # Set is_person if the party is a health professional or a patient
        if (self.is_doctor or self.is_patient or self.is_person):
            return True

    @classmethod
    def validate(cls, parties):
        super(PartyPatient, cls).validate(parties)
        for party in parties:
            party.check_person()

    def check_person(self):
    # Verify that health professional and patient
    # are unchecked when is_person is False

        if not self.is_person and (self.is_patient or self.is_doctor):
            self.raise_user_error(
                "The Person field must be set if the party is a health"
                " professional or a patient")


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


class ProductCategory(ModelSQL, ModelView):
    'Product Category'
    __name__ = 'product.category'

    @classmethod
    def __register__(cls, module_name):
        cursor = Transaction().cursor
        super(ProductCategory, cls).__register__(module_name)

        # Upgrade from GNU Health 1.8.1: moved who essential medicines
        cursor.execute(
            "UPDATE ir_model_data "
            "SET module = REPLACE(module, %s, %s) "
            "WHERE fs_id like 'prod_medicament%%' AND module = %s",
            ('health', 'health_who_essential_medicines', module_name,))


class ProductTemplate(ModelSQL, ModelView):
    'Product Template'
    __name__ = 'product.template'

    @classmethod
    def __register__(cls, module_name):
        cursor = Transaction().cursor
        super(ProductTemplate, cls).__register__(module_name)

        # Upgrade from GNU Health 1.8.1: moved who essential medicines
        cursor.execute(
            "UPDATE ir_model_data "
            "SET module = REPLACE(module, %s, %s), "
            "    fs_id = REPLACE(fs_id, 'prod_em', 'templ_em') "
            "WHERE fs_id like 'prod_em%%' AND module = %s "
            "  AND model = %s",
            ('health', 'health_who_essential_medicines', module_name,
                'product.template',))


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
    def __register__(cls, module_name):
        cursor = Transaction().cursor
        super(Product, cls).__register__(module_name)

        # Upgrade from GNU Health 1.8.1: moved who essential medicines
        cursor.execute(
            "UPDATE ir_model_data "
            "SET module = REPLACE(module, %s, %s) "
            "WHERE fs_id like 'prod_em%%' AND module = %s "
            "  AND model = %s",
            ('health', 'health_who_essential_medicines', module_name,
                'product.product',))

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

    # Get the patient age in the following format : 'YEARS MONTHS DAYS'
    # It will calculate the age of the patient while the patient is alive.
    # When the patient dies, it will show the age at time of death.

    def patient_age(self, name):

        def compute_age_from_dates(patient_dob, patient_deceased,
                                   patient_dod, patient_sex):

            now = datetime.now()

            if (patient_dob):
                dob = datetime.strptime(str(patient_dob), '%Y-%m-%d')

                if patient_deceased:
                    dod = datetime.strptime(
                        str(patient_dod), '%Y-%m-%d %H:%M:%S')
                    delta = relativedelta(dod, dob)
                    deceased = ' (deceased)'
                else:
                    delta = relativedelta(now, dob)
                    deceased = ''
                years_months_days = str(delta.years) + 'y ' \
                    + str(delta.months) + 'm ' \
                    + str(delta.days) + 'd' + deceased
            else:
                years_months_days = 'No DoB !'

            # Return the age in format y m d when the caller is the field name
            if name == 'age':
                return years_months_days

            # Return if the patient is in the period of childbearing age >10 is
            # the caller is childbearing_potential

            if (name == 'childbearing_age' and patient_dob):
                if (delta.years >= 11
                   and delta.years <= 55 and patient_sex == 'f'):
                    return True
                else:
                    return False

        return compute_age_from_dates(self.dob, self.deceased,
                                      self.dod, self.sex)

    name = fields.Many2One(
        'party.party', 'Patient', required=True,
        domain=[
            ('is_patient', '=', True),
            ('is_person', '=', True),
            ],
        states={'readonly': Bool(Eval('name'))},
        help="Person associated to this patient")

    lastname = fields.Function(
        fields.Char('Lastname'), 'get_patient_lastname',
        searcher='search_patient_lastname')

    ssn = fields.Function(
        fields.Char('SSN'),
        'get_patient_ssn', searcher='search_patient_ssn')

    identification_code = fields.Char(
        'ID', readonly=True,
        help='Patient Identifier provided by the Health Center.Is not the'
        ' Social Security Number')

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
        'gnuhealth.physician',
        'GP', help='Current General Practitioner / Family Doctor')

    # Removed in 2.0 . PHOTO It's now a functional field
    # Retrieves the information from the party.

    photo = fields.Function(fields.Binary('Picture'), 'get_patient_photo')

    # Removed in 2.0 . DOB It's now a functional field
    # Retrieves the information from the party.
    #    dob = fields.Date('DoB', help='Date of Birth')

    dob = fields.Function(fields.Date('DoB'), 'get_patient_dob')

    age = fields.Function(fields.Char('Age'), 'patient_age')

    # Removed in 2.0 . SEX It's now a functional field
    # Retrieves the information from the party.

    # sex = fields.Selection([
    #    ('m', 'Male'),
    #    ('f', 'Female'),
    #    ], 'Sex', required=True)

    sex = fields.Function(fields.Selection([
        ('m', 'Male'),
        ('f', 'Female'),
        ], 'Sex'), 'get_patient_sex')

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
            ], 'Marital Status', sort=False), 'get_patient_marital_status')

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
        'gnuhealth.vaccination', 'name', 'Vaccinations')
    medications = fields.One2Many(
        'gnuhealth.patient.medication', 'name', 'Medications')

# Removed in 1.6
#    prescriptions = fields.One2Many('gnuhealth.prescription.order', 'name',
#        'Prescriptions')

    diseases = fields.One2Many('gnuhealth.patient.disease', 'name', 'Diseases')
    critical_info = fields.Text(
        'Important disease, allergy or procedures'
        ' information',
        help='Write any important information on the patient\'s disease,'
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

    deceased = fields.Boolean('Deceased', help='Mark if the patient has died')

    dod = fields.DateTime(
        'Date of Death',
        states={
            'invisible': Not(Bool(Eval('deceased'))),
            'required': Bool(Eval('deceased')),
            },
        depends=['deceased'])

    cod = fields.Many2One(
        'gnuhealth.pathology', 'Cause of Death',
        states={
            'invisible': Not(Bool(Eval('deceased'))),
            'required': Bool(Eval('deceased')),
            },
        depends=['deceased'])

    childbearing_age = fields.Function(
        fields.Boolean('Potential for Childbearing'), 'patient_age')

    appointments = fields.One2Many(
        'gnuhealth.appointment', 'patient', 'Appointments')

    @classmethod
    def __setup__(cls):
        super(PatientData, cls).__setup__()
        cls._sql_constraints = [
            ('name_uniq', 'UNIQUE(name)', 'The Patient already exists !'),
        ]

    def get_patient_dob(self, name):
        return self.name.dob

    def get_patient_sex(self, name):
        return self.name.sex

    def get_patient_photo(self, name):
        return self.name.photo

    def get_patient_ssn(self, name):
        return self.name.ref

    def get_patient_marital_status(self, name):
        return self.name.marital_status

    @classmethod
    def search_patient_ssn(cls, name, clause):
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

    # Search by the patient name, lastname or SSN

    @classmethod
    def search_rec_name(cls, name, clause):
        field = None
        for field in ('name', 'lastname', 'ssn'):
            patients = cls.search([(field,) + clause[1:]], limit=1)
            if patients:
                break
        if patients:
            return [(field,) + clause[1:]]
        return [(cls._rec_name,) + clause[1:]]

    @classmethod
    def create(cls, vlist):
        Sequence = Pool().get('ir.sequence')
        Config = Pool().get('gnuhealth.sequences')

        vlist = [x.copy() for x in vlist]
        for values in vlist:
            if not values.get('identification_code'):
                config = Config(1)
                values['identification_code'] = Sequence.get_id(
                    config.patient_sequence.id)

        return super(PatientData, cls).create(vlist)

    def get_rec_name(self, name):
        if self.name.lastname:
            return self.name.lastname + ', ' + self.name.name
        else:
            return self.name.name

    @classmethod
    # Update to version 2.0
    def __register__(cls, module_name):
        super(PatientData, cls).__register__(module_name)

        cursor = Transaction().cursor
        table = TableHandler(cursor, cls, module_name)
        # Move Date of Birth from patient to party

        if table.column_exist('dob'):
            cursor.execute(
                'UPDATE PARTY_PARTY '
                'SET DOB = GNUHEALTH_PATIENT.DOB '
                'FROM GNUHEALTH_PATIENT '
                'WHERE GNUHEALTH_PATIENT.NAME = PARTY_PARTY.ID')

            table.drop_column('dob')

        # Move Patient Gender from patient to party

        if table.column_exist('sex'):
            cursor.execute(
                'UPDATE PARTY_PARTY '
                'SET SEX = GNUHEALTH_PATIENT.SEX '
                'FROM GNUHEALTH_PATIENT '
                'WHERE GNUHEALTH_PATIENT.NAME = PARTY_PARTY.ID')

            table.drop_column('sex')

        # Move Patient Photo from patient to party

        if table.column_exist('photo'):
            cursor.execute(
                'UPDATE PARTY_PARTY '
                'SET PHOTO = GNUHEALTH_PATIENT.PHOTO '
                'FROM GNUHEALTH_PATIENT '
                'WHERE GNUHEALTH_PATIENT.NAME = PARTY_PARTY.ID')

            table.drop_column('photo')

        # Move Patient Ethnic Group from patient to party

        if table.column_exist('ethnic_group'):
            cursor.execute(
                'UPDATE PARTY_PARTY '
                'SET ETHNIC_GROUP = GNUHEALTH_PATIENT.ETHNIC_GROUP '
                'FROM GNUHEALTH_PATIENT '
                'WHERE GNUHEALTH_PATIENT.NAME = PARTY_PARTY.ID')

            table.drop_column('ethnic_group')

        # Move Patient Marital Status from patient to party

        if table.column_exist('marital_status'):
            cursor.execute(
                'UPDATE PARTY_PARTY '
                'SET MARITAL_STATUS = GNUHEALTH_PATIENT.MARITAL_STATUS '
                'FROM GNUHEALTH_PATIENT '
                'WHERE GNUHEALTH_PATIENT.NAME = PARTY_PARTY.ID')

            table.drop_column('marital_status')


# PATIENT DISESASES INFORMATION
class PatientDiseaseInfo(ModelSQL, ModelView):
    'Patient Disease History'
    __name__ = 'gnuhealth.patient.disease'

    name = fields.Many2One('gnuhealth.patient', 'Patient')

    pathology = fields.Many2One(
        'gnuhealth.pathology', 'Disease', required=True, help='Disease')

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

    doctor = fields.Many2One(
        'gnuhealth.physician',
        'Physician', help='Physician who treated or diagnosed the patient')

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
        ], 'Status of the disease', select=True, sort=False)
    extra_info = fields.Text('Extra Info')

    @classmethod
    def __setup__(cls):
        super(PatientDiseaseInfo, cls).__setup__()
        cls._order.insert(0, ('is_active', 'DESC'))
        cls._order.insert(1, ('disease_severity', 'DESC'))
        cls._order.insert(2, ('is_infectious', 'DESC'))
        cls._order.insert(3, ('diagnosed_date', 'DESC'))
        cls._constraints += [
            ('validate_disease_period', 'end_date_before_start'),
            ('validate_treatment_dates', 'end_treatment_date_before_start')]

        cls._error_messages.update({
            'end_date_before_start': 'The HEALED date is BEFORE DIAGNOSED'
            ' DATE !',
            'end_treatment_date_before_start': 'The Treatment END DATE is'
            ' BEFORE the start date!',
            })

    @staticmethod
    def default_is_active():
        return True

    def validate_disease_period(self):
        res = True
        if (self.healed_date and self.diagnosed_date):
            if (self.healed_date < self.diagnosed_date):
                res = False
        return res

    def validate_treatment_dates(self):
        if (self.date_stop_treatment and self.date_start_treatment):
            if (self.date_stop_treatment < self.date_start_treatment):
                return False
            else:
                return True
        else:
            return True


# PATIENT APPOINTMENT
class Appointment(ModelSQL, ModelView):
    'Patient Appointments'
    __name__ = 'gnuhealth.appointment'

    name = fields.Char('Appointment ID', readonly=True)

    doctor = fields.Many2One(
        'gnuhealth.physician', 'Physician',
        select=True, help='Physician\'s Name')

    patient = fields.Many2One(
        'gnuhealth.patient', 'Patient', required=True,
        select=True, help='Patient Name')

    appointment_date = fields.DateTime('Date and Time')

    institution = fields.Many2One(
        'party.party', 'Health Center',
        domain=[('is_institution', '=', True)],
        help='Medical Center')

    speciality = fields.Many2One(
        'gnuhealth.specialty', 'Specialty',
        on_change_with=['doctor'], help='Medical Specialty / Sector')

    state = fields.Selection([
        (None, ''),
        ('confirmed', 'Confirmed'),
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
        ('ambulatory', 'Ambulatory'),
        ('outpatient', 'Outpatient'),
        ('inpatient', 'Inpatient'),
        ], 'Type', sort=False)

    visit_type = fields.Selection([
        (None, ''),
        ('new', 'New health condition'),
        ('followup', 'Followup'),
        ('chronic', 'Chronic condition checkup'),
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
        cls._order.insert(0, ('name', 'DESC'))

    @classmethod
    def create(cls, vlist):
        Sequence = Pool().get('ir.sequence')
        Config = Pool().get('gnuhealth.sequences')

        vlist = [x.copy() for x in vlist]
        for values in vlist:
            if not values.get('name'):
                config = Config(1)
                values['name'] = Sequence.get_id(
                    config.appointment_sequence.id)

        return super(Appointment, cls).create(vlist)

    @staticmethod
    def default_doctor():
        return HealthProfessional().get_health_professional()

    @staticmethod
    def default_urgency():
        return 'a'

    @staticmethod
    def default_appointment_date():
        return datetime.now()

    @staticmethod
    def default_appointment_type():
        return 'ambulatory'

    @staticmethod
    def default_state():
        return 'confirmed'

    @staticmethod
    def default_institution():
        return Transaction().context.get('company')

    def on_change_with_speciality(self):
        # Return the Current / Main speciality of the Health Professional
        # if this speciality has been specified in the HP record.
        if (self.doctor and self.doctor.main_specialty):
            specialty = self.doctor.main_specialty.specialty.id
            return specialty

    @staticmethod
    def default_speciality():
        # This method will assign the Main specialty to the appointment
        # if there is a health professional associated to the login user
        # as a default value.
        # It will be overwritten if the health professional is modified in
        # this view, the on_change_with will take effect.

        # Get Party ID associated to the Health Professional
        hp_party_id = HealthProfessional().get_health_professional()

        if hp_party_id:
            # Retrieve the health professional Main specialty, if assigned

            health_professional_obj = Pool().get('gnuhealth.physician')
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

    identification_code = fields.Char('Identification Code')
    ref = fields.Char('SSN')
    patient = fields.Many2One('gnuhealth.patient', 'Patient')
    doctor = fields.Many2One('gnuhealth.physician', 'Doctor')
    age = fields.Function(fields.Char('Age'), 'get_patient_age')
    sex = fields.Selection([('m', 'Male'), ('f', 'Female')], 'Sex')
    address = fields.Function(fields.Char('Address'), 'get_address')
    insurance = fields.Function(fields.Char('Insurance'), 'get_insurance')
    appointment_date = fields.Date('Date')
    appointment_date_time = fields.DateTime('Date and Time')
    diagnosis = fields.Function(
        fields.Many2One(
            'gnuhealth.pathology',
            'Presumptive Diagnosis'), 'get_diagnosis')

    @classmethod
    def __setup__(cls):
        super(AppointmentReport, cls).__setup__()
        cls._order.insert(0, ('appointment_date_time', 'ASC'))

    @classmethod
    def table_query(cls):
        where_clause = ' '
        args = []
        if Transaction().context.get('date'):
            where_clause += "AND a.appointment_date >= %s AND " \
                "a.appointment_date < %s + integer '1' "
            args.append(Transaction().context['date'])
            args.append(Transaction().context['date'])
        if Transaction().context.get('doctor'):
            where_clause += 'AND a.doctor = %s '
            args.append(Transaction().context['doctor'])
        return ('SELECT id, create_uid, create_date, write_uid, write_date, '
                'identification_code, ref, patient, sex, '
                'appointment_date, appointment_date_time, doctor '
                'FROM ('
                'SELECT a.id, a.create_uid, a.create_date, '
                'a.write_uid, a.write_date, p.identification_code, '
                'r.ref, p.id as patient, r.sex, a.appointment_date, '
                'a.appointment_date as appointment_date_time, '
                'a.doctor '
                'FROM gnuhealth_appointment a, '
                'gnuhealth_patient p, party_party r '
                'WHERE a.patient = p.id '
                + where_clause +
                'AND p.name = r.id) AS ' + cls._table, args)

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
            ('evaluation_date', '=', self.id)
        ])
        if evaluations:
            evaluation = evaluations[0]
            if evaluation.diagnosis:
                res = evaluation.diagnosis.id
        return res

    def get_patient_age(self, name):
        return self.patient.age


class OpenAppointmentReportStart(ModelView):
    'Open Appointment Report'
    __name__ = 'gnuhealth.appointment.report.open.start'
    date = fields.Date('Date', required=True)
    doctor = fields.Many2One('gnuhealth.physician', 'Doctor', required=True)

    @staticmethod
    def default_date():
        return datetime.now()

    @staticmethod
    def default_doctor():
        return HealthProfessional().get_health_professional()


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
        action['pyson_context'] = PYSONEncoder().encode({
            'date': self.start.date,
            'doctor': self.start.doctor.id,
            })
        action['name'] += ' - %s, %s' % (self.start.doctor.name.lastname,
                                         self.start.doctor.name.name)
        return action, {}

    def transition_open_(self):
        return 'end'


# PATIENT MEDICATION TREATMENT
class PatientMedication(ModelSQL, ModelView):
    'Patient Medication'
    __name__ = 'gnuhealth.patient.medication'

# Remove inherits to be compatible with Tryton 2.8
#    _inherits = {'gnuhealth.medication.template': 'template'}
#    template = fields.Many2One('gnuhealth.medication.template',
#        'Medication')

    medicament = fields.Many2One(
        'gnuhealth.medicament', 'Medicament',
        required=True, help='Prescribed Medicament')

    indication = fields.Many2One(
        'gnuhealth.pathology', 'Indication',
        help='Choose a disease for this medicament from the disease list. It'
        ' can be an existing disease of the patient or a prophylactic.')

    name = fields.Many2One(
        'gnuhealth.patient', 'Patient', readonly=True)

    doctor = fields.Many2One(
        'gnuhealth.physician', 'Physician',
        help='Physician who prescribed the medicament')

    is_active = fields.Boolean(
        'Active',
        on_change_with=['discontinued', 'course_completed'],
        help='Check if the patient is currently taking the medication')

    discontinued = fields.Boolean(
        'Discontinued',
        on_change_with=['is_active', 'course_completed'])

    course_completed = fields.Boolean(
        'Course Completed',
        on_change_with=['is_active', 'discontinued'])

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

    @classmethod
    def __setup__(cls):
        super(PatientMedication, cls).__setup__()
        cls._constraints += [
            ('validate_medication_dates', 'end_date_before_start'),
            ]
        cls._error_messages.update({
            'end_date_before_start': 'The Medication END DATE is BEFORE the'
            ' start date!',
            })

    @classmethod
    def __register__(cls, module_name):
        super(PatientMedication, cls).__register__(module_name)

        cursor = Transaction().cursor
        table = TableHandler(cursor, cls, module_name)

        # Update to version 2.0
        # Move data from template to patient medication
        if table.column_exist('template'):
            cursor.execute(
                'UPDATE gnuhealth_patient_medication '
                'SET medicament = gmt.medicament, '
                'indication = gmt.indication, '
                'dose = gmt.dose, '
                'dose_unit = gmt.dose_unit, '
                'route = gmt.route, '
                'form = gmt.form, '
                'qty = gmt.qty, '
                'common_dosage = gmt.common_dosage, '
                'frequency = gmt.frequency, '
                'frequency_unit = gmt.frequency_unit, '
                'frequency_prn = gmt.frequency_prn, '
                'admin_times = gmt.admin_times, '
                'duration = gmt.duration, '
                'duration_period = gmt.duration_period, '
                'start_treatment = gmt.start_treatment, '
                'end_treatment = gmt.end_treatment '
                'FROM gnuhealth_medication_template gmt '
                'WHERE gnuhealth_patient_medication.template = gmt.id')

            table.drop_column('template')

    def on_change_with_is_active(self):
        return not (self.discontinued or self.course_completed)

    def on_change_with_discontinued(self):
        return not (self.is_active or self.course_completed)

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

    def validate_medication_dates(self):
        res = True
        if self.end_treatment:
            if (self.end_treatment < self.start_treatment):
                res = False
        return res


# PATIENT VACCINATION INFORMATION
class PatientVaccination(ModelSQL, ModelView):
    'Patient Vaccination information'
    __name__ = 'gnuhealth.vaccination'

    def check_vaccine_expiration_date(self):
        if self.vaccine_expiration_date:
            if self.vaccine_expiration_date < datetime.date(self.date):
                return False
        return True

    name = fields.Many2One('gnuhealth.patient', 'Patient', readonly=True)

    vaccine = fields.Many2One(
        'product.product', 'Name', required=True,
        domain=[('is_vaccine', '=', True)],
        help='Vaccine Name. Make sure that the vaccine (product) has all the'
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

    vaccine_expiration_date = fields.Date('Expiration date')

    vaccine_lot = fields.Char(
        'Lot Number',
        help='Please check on the vaccine (product) production lot numberand'
        ' tracking number when available !')

    institution = fields.Many2One(
        'party.party', 'Institution',
        domain=[('is_institution', '=', True)],
        help='Medical Center where the patient is being or was vaccinated')

    date = fields.DateTime('Date')
    dose = fields.Integer('Dose #')
    next_dose_date = fields.DateTime('Next Dose')
    observations = fields.Char('Observations')

    @classmethod
    def __setup__(cls):
        super(PatientVaccination, cls).__setup__()
        cls._sql_constraints = [
            ('dose_uniq', 'UNIQUE(name, vaccine, dose)',
                'This vaccine dose has been given already to the patient'),
        ]
        cls._constraints += [
            ('check_vaccine_expiration_date', 'expired_vaccine'),
            ('validate_next_dose_date', 'next_dose_before_first'),

        ]
        cls._error_messages.update({
            'expired_vaccine': 'EXPIRED VACCINE. PLEASE INFORM  THE LOCAL '
            'HEALTH AUTHORITIES AND DO NOT USE IT !!!',
            'next_dose_before_first': 'The Vaccine next dose is BEFORE the '
            'first one !'
        })

    @staticmethod
    def default_date():
        return datetime.now()

    @staticmethod
    def default_dose():
        return 1

    def validate_next_dose_date(self):
        if (self.next_dose_date):
            if (self.next_dose_date < self.date):
                return False
            else:
                return True
        # If the next dose is not available, then keep going.
        else:
            return True


class PatientPrescriptionOrder(ModelSQL, ModelView):
    'Prescription Order'
    __name__ = 'gnuhealth.prescription.order'
    _rec_name = 'prescription_id'

    patient = fields.Many2One(
        'gnuhealth.patient', 'Patient', required=True, on_change=['patient'])

    prescription_id = fields.Char(
        'Prescription ID',
        readonly=True, help='Type in the ID of this prescription')

    prescription_date = fields.DateTime('Prescription Date')
# In 1.8 we associate the prescribing doctor to the physician name
# instead to the old user_id (res.user)
    user_id = fields.Many2One('res.user', 'Prescribing Doctor', readonly=True)

    pharmacy = fields.Many2One(
        'party.party', 'Pharmacy', domain=[('is_pharmacy', '=', True)])

    prescription_line = fields.One2Many(
        'gnuhealth.prescription.line', 'name', 'Prescription line')

    notes = fields.Text('Prescription Notes')
    pregnancy_warning = fields.Boolean('Pregancy Warning', readonly=True)
    prescription_warning_ack = fields.Boolean('Prescription verified')

    doctor = fields.Many2One(
        'gnuhealth.physician', 'Prescribing Doctor', readonly=True)

    @classmethod
    def __setup__(cls):
        super(PatientPrescriptionOrder, cls).__setup__()
        cls._constraints += [
            ('check_prescription_warning', 'drug_pregnancy_warning'),
            ('check_health_professional', 'health_professional_warning'),
        ]
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

    def check_health_professional(self):
        return self.doctor

    @staticmethod
    def default_doctor():
        return HealthProfessional().get_health_professional()

    def check_prescription_warning(self):
        return self.prescription_warning_ack

    # Method that makes the doctor to acknowledge if there is any
    # warning in the prescription

    def on_change_patient(self):
        preg_warning = False
        presc_warning_ack = True
        if self.patient:
            # Trigger the warning if the patient is at a childbearing age
            if (self.patient.childbearing_age):
                preg_warning = True
                presc_warning_ack = False
        return {
            'prescription_warning_ack': presc_warning_ack,
            'pregnancy_warning': preg_warning,
        }

    @staticmethod
    def default_prescription_date():
        return datetime.now()

    @staticmethod
    def default_user_id():
        User = Pool().get('res.user')
        user = User(Transaction().user)
        return int(user.id)

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


# PRESCRIPTION LINE
class PrescriptionLine(ModelSQL, ModelView):
    'Prescription Line'
    __name__ = 'gnuhealth.prescription.line'

# Remove inherits to be compatible with Tryton 2.8
#    _inherits = {'gnuhealth.medication.template': 'template'}
#    template = fields.Many2One('gnuhealth.medication.template',
#        'Medication Template')

    name = fields.Many2One('gnuhealth.prescription.order', 'Prescription ID')
    review = fields.DateTime('Review')

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

    @classmethod
    def __register__(cls, module_name):
        super(PrescriptionLine, cls).__register__(module_name)

        cursor = Transaction().cursor
        table = TableHandler(cursor, cls, module_name)

        # Update to version 2.0
        # Move data from template to prescription line
        if table.column_exist('template'):
            cursor.execute(
                'UPDATE gnuhealth_prescription_line '
                'SET medicament = gmt.medicament, '
                'indication = gmt.indication, '
                'dose = gmt.dose, '
                'dose_unit = gmt.dose_unit, '
                'route = gmt.route, '
                'form = gmt.form, '
                'qty = gmt.qty, '
                'common_dosage = gmt.common_dosage, '
                'frequency = gmt.frequency, '
                'frequency_unit = gmt.frequency_unit, '
                'frequency_prn = gmt.frequency_prn, '
                'admin_times = gmt.admin_times, '
                'duration = gmt.duration, '
                'duration_period = gmt.duration_period, '
                'start_treatment = gmt.start_treatment, '
                'end_treatment = gmt.end_treatment '
                'FROM gnuhealth_medication_template gmt '
                'WHERE gnuhealth_prescription_line.template = gmt.id')

            table.drop_column('template')

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


class PatientEvaluation(ModelSQL, ModelView):
    'Patient Evaluation'
    __name__ = 'gnuhealth.patient.evaluation'

    def evaluation_duration(self, name):

        duration = ''
        if (self.evaluation_endtime and self.evaluation_start):
                delta = relativedelta(
                    self.evaluation_endtime, self.evaluation_start)

                duration = str(
                    delta.days*24 + delta.hours*60 + delta.minutes)

        return duration

    patient = fields.Many2One('gnuhealth.patient', 'Patient')

    evaluation_date = fields.Many2One(
        'gnuhealth.appointment', 'Appointment',
        domain=[('patient', '=', Eval('patient'))], depends=['patient'],
        help='Enter or select the date / ID of the appointment related to'
        ' this evaluation')

    evaluation_start = fields.DateTime('Start', required=True)
    evaluation_endtime = fields.DateTime('End', required=True)

    evaluation_length = fields.Function(
        fields.Char(
            'Length',
            help="Duration of the evaluation, in minutes"),
        'evaluation_duration')

    state = fields.Selection([
        ('in_progress', 'In progress'),
        ('done', 'Done'),
        ], 'State', readonly=True, sort=False)

    next_evaluation = fields.Many2One(
        'gnuhealth.appointment',
        'Next Appointment', domain=[('patient', '=', Eval('patient'))],
        depends=['patient'])

    user_id = fields.Many2One('res.user', 'Last Changed by', readonly=True)
    doctor = fields.Many2One(
        'gnuhealth.physician', 'Health Prof',
        help="Health professional that initiates the evaluation."
        "This health professional might or might not be the same that"
        " signs and finishes the evaluation."
        "The evaluation remains in progress state until it is signed"
        ", when it becomes read-only", readonly=True)

    signed_by = fields.Many2One(
        'gnuhealth.physician', 'Signed by', readonly=True,
        states={'invisible': Equal(Eval('state'), 'in_progress')},
        help="Health Professional that signed the patient evaluation document")

    specialty = fields.Many2One('gnuhealth.specialty', 'Specialty')

    visit_type = fields.Selection([
        (None, ''),
        ('new', 'New health condition'),
        ('followup', 'Followup'),
        ('chronic', 'Chronic condition checkup'),
        ('well_child', 'Well Child visit'),
        ('well_woman', 'Well Woman visit'),
        ('well_man', 'Well Man visit'),
        ], 'Visit', sort=False)

    urgency = fields.Selection([
        (None, ''),
        ('a', 'Normal'),
        ('b', 'Urgent'),
        ('c', 'Medical Emergency'),
        ], 'Urgency', sort=False)

    information_source = fields.Char(
        'Source', help="Source of"
        "Information, eg : Self, relative, friend ...")

    reliable_info = fields.Boolean(
        'Reliable', help="Uncheck this option"
        "if the information provided by the source seems not reliable")

    derived_from = fields.Many2One(
        'gnuhealth.physician', 'Derived from',
        help='Physician who derived the case')

    derived_to = fields.Many2One(
        'gnuhealth.physician', 'Derived to',
        help='Physician to whom escalate / derive the case')

    evaluation_type = fields.Selection([
        (None, ''),
        ('ambulatory', 'Ambulatory'),
        ('outpatient', 'Outpatient'),
        ('inpatient', 'Inpatient'),
        ], 'Type', sort=False)

    chief_complaint = fields.Char('Chief Complaint', help='Chief Complaint')
    notes_complaint = fields.Text('Complaint details')
    present_illness = fields.Text('Present Illness')
    evaluation_summary = fields.Text('Evaluation Summary')

    glycemia = fields.Float(
        'Glycemia',
        help='Last blood glucose level. Can be approximative.')

    hba1c = fields.Float(
        'Glycated Hemoglobin',
        help='Last Glycated Hb level. Can be approximative.')

    cholesterol_total = fields.Integer(
        'Last Cholesterol',
        help='Last cholesterol reading. Can be approximative')

    hdl = fields.Integer(
        'Last HDL',
        help='Last HDL Cholesterol reading. Can be approximative')

    ldl = fields.Integer(
        'Last LDL',
        help='Last LDL Cholesterol reading. Can be approximative')

    tag = fields.Integer(
        'Last TAGs',
        help='Triacylglycerol(triglicerides) level. Can be approximative')

    systolic = fields.Integer('Systolic Pressure')
    diastolic = fields.Integer('Diastolic Pressure')

    bpm = fields.Integer(
        'Heart Rate',
        help='Heart rate expressed in beats per minute')

    respiratory_rate = fields.Integer(
        'Respiratory Rate',
        help='Respiratory rate expressed in breaths per minute')

    osat = fields.Integer(
        'Oxygen Saturation',
        help='Oxygen Saturation(arterial).')

    malnutrition = fields.Boolean(
        'Malnutrition',
        help='Check this box if the patient show signs of malnutrition. If'
        ' associated  to a disease, please encode the correspondent disease'
        ' on the patient disease history. For example, Moderate'
        ' protein-energy malnutrition, E44.0 in ICD-10 encoding')

    dehydration = fields.Boolean(
        'Dehydration',
        help='Check this box if the patient show signs of dehydration. If'
        ' associated  to a disease, please encode the  correspondent disease'
        ' on the patient disease history. For example, Volume Depletion, E86'
        ' in ICD-10 encoding')

    temperature = fields.Float(
        'Temperature',
        help='Temperature in celcius')

    weight = fields.Float('Weight', help='Weight in Kilos')
    height = fields.Float('Height', help='Height in centimeters, eg 175')

    bmi = fields.Float(
        'Body Mass Index',
        on_change_with=['weight', 'height', 'bmi'])

    head_circumference = fields.Float(
        'Head Circumference',
        help='Head circumference')

    abdominal_circ = fields.Float('Waist')
    hip = fields.Float('Hip', help='Hip circumference in centimeters, eg 100')

    whr = fields.Float(
        'WHR', help='Waist to hip ratio',
        on_change_with=['abdominal_circ', 'hip', 'whr'])

    # DEPRECATION NOTE : SIGNS AND SYMPTOMS FIELDS TO BE REMOVED IN 1.6 .
    # NOW WE USE A O2M OBJECT TO MAKE IT MORE SCALABLE, CLEARER AND FUNCTIONAL
    # TO WORK WITH THE CLINICAL FINDINGS OF THE PATIENT
    loc = fields.Integer(
        'Glasgow',
        on_change_with=['loc_verbal', 'loc_motor', 'loc_eyes'],
        help='Level of Consciousness - on Glasgow Coma Scale :  < 9 severe -'
        ' 9-12 Moderate, > 13 minor')
    loc_eyes = fields.Selection([
        ('1', 'Does not Open Eyes'),
        ('2', 'Opens eyes in response to painful stimuli'),
        ('3', 'Opens eyes in response to voice'),
        ('4', 'Opens eyes spontaneously'),
        ], 'Glasgow - Eyes', sort=False)
    loc_verbal = fields.Selection([
        ('1', 'Makes no sounds'),
        ('2', 'Incomprehensible sounds'),
        ('3', 'Utters inappropriate words'),
        ('4', 'Confused, disoriented'),
        ('5', 'Oriented, converses normally'),
        ], 'Glasgow - Verbal', sort=False)
    loc_motor = fields.Selection([
        ('1', 'Makes no movement'),
        ('2', 'Extension to painful stimuli - decerebrate response -'),
        ('3', 'Abnormal flexion to painful stimuli (decorticate response)'),
        ('4', 'Flexion / Withdrawal to painful stimuli'),
        ('5', 'Localizes painful stimuli'),
        ('6', 'Obeys commands'),
        ], 'Glasgow - Motor', sort=False)

    tremor = fields.Boolean(
        'Tremor',
        help='If associated  to a disease, please encode it on the patient'
        ' disease history')

    violent = fields.Boolean(
        'Violent Behaviour',
        help='Check this box if the patient is agressive or violent at the'
        ' moment')

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
        ], 'Mood', sort=False)

    orientation = fields.Boolean(
        'Orientation',
        help='Check this box if the patient is disoriented in time and/or'
        ' space')

    memory = fields.Boolean(
        'Memory',
        help='Check this box if the patient has problems in short or long'
        ' term memory')

    knowledge_current_events = fields.Boolean(
        'Knowledge of Current Events',
        help='Check this box if the patient can not respond to public'
        ' notorious events')

    judgment = fields.Boolean(
        'Jugdment',
        help='Check this box if the patient can not interpret basic scenario'
        ' solutions')

    abstraction = fields.Boolean(
        'Abstraction',
        help='Check this box if the patient presents abnormalities in'
        ' abstract reasoning')

    vocabulary = fields.Boolean(
        'Vocabulary',
        help='Check this box if the patient lacks basic intelectual capacity,'
        ' when she/he can not describe elementary objects')

    calculation_ability = fields.Boolean(
        'Calculation Ability',
        help='Check this box if the patient can not do simple arithmetic'
        ' problems')

    object_recognition = fields.Boolean(
        'Object Recognition',
        help='Check this box if the patient suffers from any sort of gnosia'
        ' disorders, such as agnosia, prosopagnosia ...')

    praxis = fields.Boolean(
        'Praxis',
        help='Check this box if the patient is unable to make voluntary'
        'movements')

    diagnosis = fields.Many2One(
        'gnuhealth.pathology', 'Presumptive Diagnosis',
        help='Presumptive Diagnosis. If no diagnosis can be made'
        ', encode the main sign or symptom.')

    secondary_conditions = fields.One2Many(
        'gnuhealth.secondary_condition',
        'evaluation', 'Secondary Conditions', help='Other, Secondary'
        ' conditions found on the patient')

    diagnostic_hypothesis = fields.One2Many(
        'gnuhealth.diagnostic_hypothesis',
        'evaluation', 'Hypotheses / DDx', help='Other Diagnostic Hypotheses /'
        ' Differential Diagnosis (DDx)')

    signs_and_symptoms = fields.One2Many(
        'gnuhealth.signs_and_symptoms',
        'evaluation', 'Signs and Symptoms', help='Enter the Signs and Symptoms'
        ' for the patient in this evaluation.')

    info_diagnosis = fields.Text('Presumptive Diagnosis: Extra Info')
    directions = fields.Text('Plan')

    actions = fields.One2Many(
        'gnuhealth.directions', 'name', 'Procedures',
        help='Procedures / Actions to take')

    notes = fields.Text('Notes')

    @classmethod
    def __setup__(cls):
        super(PatientEvaluation, cls).__setup__()
        cls._constraints += [
            ('check_health_professional', 'health_professional_warning'),
            ('validate_evaluation_period', 'end_date_before_start'),
        ]

        cls._error_messages.update({
            'health_professional_warning':
            'No health professional associated to this user',
            'end_date_before_start': 'End time BEFORE evaluation start'
        })

        cls._buttons.update({
            'discharge': {
                'invisible': Equal(Eval('state'), 'done'),
            },
        })

    def validate_evaluation_period(self):
        res = True
        if (self.evaluation_endtime and self.evaluation_start):
            if (self.evaluation_endtime < self.evaluation_start):
                res = False
        return res

    @classmethod
    def write(cls, evaluations, vals):
        # Don't allow to write the record if the evaluation has been done
        if evaluations[0].state == 'done':
            cls.raise_user_error(
                "This evaluation is at state Done\n"
                "You can no longer modify it.")
        return super(PatientEvaluation, cls).write(evaluations, vals)

    # End the evaluation and discharge the patient

    @classmethod
    @ModelView.button
    def discharge(cls, evaluations):
        evaluation_id = evaluations[0]

        # Change the state of the evaluation to "Done"
        # and write the name of the signing doctor

        signing_hp = HealthProfessional().get_health_professional()
        if not signing_hp:
            cls.raise_user_error(
                "No health professional associated to this user !")

        cls.write(evaluations, {
            'state': 'done',
            'signed_by': signing_hp})

    def check_health_professional(self):
        return self.doctor

    @staticmethod
    def default_doctor():
        return HealthProfessional().get_health_professional()

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
        return 'ambulatory'

    @staticmethod
    def default_state():
        return 'in_progress'

    def on_change_with_bmi(self):
        if self.height and self.weight:
            if (self.height > 0):
                return self.weight / ((self.height / 100) ** 2)
            return 0

    def on_change_with_loc(self):
        return int(self.loc_motor) + int(self.loc_eyes) + int(self.loc_verbal)

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
    def on_change_with_whr(self):
        waist = self.abdominal_circ
        hip = self.hip
        if (hip > 0):
            whr = waist / hip
        else:
            whr = 0
        return whr

    def get_rec_name(self, name):
        return str(self.evaluation_start)


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
        domain=[('code', 'like', 'R%')], required=True)

    comments = fields.Char('Comments')


# HEALTH CENTER / HOSPITAL INFRASTRUCTURE
class HospitalBuilding(ModelSQL, ModelView):
    'Hospital Building'
    __name__ = 'gnuhealth.hospital.building'

    name = fields.Char(
        'Name', required=True,
        help='Name of the building within the institution')

    institution = fields.Many2One(
        'party.party', 'Institution',
        domain=[('is_institution', '=', True)],
        help='Medical Center')

    code = fields.Char('Code')
    extra_info = fields.Text('Extra Info')


class HospitalUnit(ModelSQL, ModelView):
    'Hospital Unit'
    __name__ = 'gnuhealth.hospital.unit'

    name = fields.Char(
        'Name', required=True,
        help='Name of the unit, eg Neonatal, Intensive Care, ...')

    institution = fields.Many2One(
        'party.party', 'Institution',
        domain=[('is_institution', '=', True)],
        help='Medical Center')

    code = fields.Char('Code')
    extra_info = fields.Text('Extra Info')


class HospitalOR(ModelSQL, ModelView):
    'Operating Room'
    __name__ = 'gnuhealth.hospital.or'

    name = fields.Char(
        'Name', required=True, help='Name of the Operating Room')

    institution = fields.Many2One(
        'party.party', 'Institution',
        domain=[('is_institution', '=', True)],
        help='Medical Center')

    building = fields.Many2One(
        'gnuhealth.hospital.building', 'Building', select=True)

    unit = fields.Many2One('gnuhealth.hospital.unit', 'Unit')
    extra_info = fields.Text('Extra Info')

    @classmethod
    def __setup__(cls):
        super(HospitalOR, cls).__setup__()
        cls._sql_constraints = [
            ('name_uniq', 'UNIQUE(name, institution)',
                'The Operating Room code must be unique per Health'
                ' Center'),
        ]


class HospitalWard(ModelSQL, ModelView):
    'Hospital Ward'
    __name__ = 'gnuhealth.hospital.ward'

    name = fields.Char('Name', required=True, help='Ward / Room code')

    institution = fields.Many2One(
        'party.party', 'Institution',
        domain=[('is_institution', '=', True)],
        help='Medical Center')

    building = fields.Many2One('gnuhealth.hospital.building', 'Building')
    floor = fields.Integer('Floor Number')
    unit = fields.Many2One('gnuhealth.hospital.unit', 'Unit')

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


class HospitalBed(ModelSQL, ModelView):
    'Hospital Bed'
    __name__ = 'gnuhealth.hospital.bed'
    _rec_name = 'telephone_number'

    name = fields.Many2One(
        'product.product', 'Bed', required=True,
        domain=[('is_bed', '=', True)],
        help='Bed Number')

    ward = fields.Many2One(
        'gnuhealth.hospital.ward', 'Ward',
        help='Ward or room')

    bed_type = fields.Selection((
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
        ('free', 'Free'),
        ('reserved', 'Reserved'),
        ('occupied', 'Occupied'),
        ('na', 'Not available'),
        ), 'Status', readonly=True, sort=False)

    @staticmethod
    def default_bed_type():
        return 'gatch'

    @staticmethod
    def default_state():
        return 'free'

    def get_rec_name(self, name):
        if self.name:
            return self.name.name

    @classmethod
    def search_rec_name(cls, name, clause):
        return [('name',) + clause[1:]]
