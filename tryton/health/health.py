# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
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
from dateutil.relativedelta import relativedelta
from datetime import datetime
from trytond.model import ModelView, ModelSingleton, ModelSQL, fields
from trytond.transaction import Transaction
from trytond.backend import TableHandler
from trytond.pyson import Eval, Not, Bool
from trytond.pool import Pool


class DrugDoseUnits(ModelSQL, ModelView):
    'Drug Dose Unit'
    _name = 'gnuhealth.dose.unit'
    _description = __doc__

    name = fields.Char('Unit', required=True, select=True, translate=True)
    desc = fields.Char('Description', translate=True)

    def __init__(self):
        super(DrugDoseUnits, self).__init__()
        self._sql_constraints = [
            ('name_uniq', 'UNIQUE(name)', 'The Unit must be unique !'),
        ]

DrugDoseUnits()


class MedicationFrequency(ModelSQL, ModelView):
    'Medication Common Frequencies'
    _name = 'gnuhealth.medication.dosage'
    _description = __doc__

    name = fields.Char('Frequency', required=True, select=True, translate=True,
        help='Common frequency name')
    code = fields.Char('Code',
        help='Dosage Code,for example: SNOMED 229798009 = 3 times per day')
    abbreviation = fields.Char('Abbreviation',
        help='Dosage abbreviation, such as tid in the US or tds in the UK')

    def __init__(self):
        super(MedicationFrequency, self).__init__()
        self._sql_constraints = [
            ('name_uniq', 'UNIQUE(name)', 'The Unit must be unique !'),
        ]

MedicationFrequency()


class DrugForm(ModelSQL, ModelView):
    'Drug Form'
    _name = 'gnuhealth.drug.form'
    _description = __doc__

    name = fields.Char('Form', required=True, select=True, translate=True)
    code = fields.Char('Code')

    def __init__(self):
        super(DrugForm, self).__init__()
        self._sql_constraints = [
            ('name_uniq', 'UNIQUE(name)', 'The Unit must be unique !'),
        ]

DrugForm()


class DrugRoute(ModelSQL, ModelView):
    'Drug Administration Route'
    _name = 'gnuhealth.drug.route'
    _description = __doc__

    name = fields.Char('Unit', required=True, select=True, translate=True)
    code = fields.Char('Code')

    def __init__(self):
        super(DrugRoute, self).__init__()
        self._sql_constraints = [
            ('name_uniq', 'UNIQUE(name)', 'The Name must be unique !'),
        ]

DrugRoute()


class Occupation(ModelSQL, ModelView):
    'Occupation'
    _name = 'gnuhealth.occupation'
    _description = __doc__

    name = fields.Char('Name', required=True, translate=True)
    code = fields.Char('Code')

    def __init__(self):
        super(Occupation, self).__init__()
        self._sql_constraints = [
            ('name_uniq', 'UNIQUE(name)', 'The Name must be unique !'),
        ]

Occupation()


class Ethnicity(ModelSQL, ModelView):
    'Ethnicity'
    _name = 'gnuhealth.ethnicity'
    _description = __doc__

    name = fields.Char('Name', required=True, translate=True)
    code = fields.Char('Code')
    notes = fields.Char('Notes')

    def __init__(self):
        super(Ethnicity, self).__init__()
        self._sql_constraints = [
            ('name_uniq', 'UNIQUE(name)', 'The Name must be unique !'),
        ]

Ethnicity()


class MedicalSpecialty(ModelSQL, ModelView):
    'Medical Specialty'
    _name = 'gnuhealth.specialty'
    _description = __doc__

    name = fields.Char('Specialty', required=True, translate=True,
        help='ie, Addiction Psychiatry')
    code = fields.Char('Code', help='ie, ADP')

    def __init__(self):
        super(MedicalSpecialty, self).__init__()
        self._sql_constraints = [
            ('name_uniq', 'UNIQUE(name)', 'The Specialty must be unique !'),
        ]

MedicalSpecialty()


class Physician(ModelSQL, ModelView):
    'Health Professional'
    _name = 'gnuhealth.physician'
    _description = __doc__

    name = fields.Many2One('party.party', 'Health Professional', required=True,
        domain=[
            ('is_doctor', '=', True),
            ('is_person', '=', True),
            ],
        help='Health Professional\'s Name, from the partner list')
    institution = fields.Many2One('party.party', 'Institution',
        domain=[('is_institution', '=', True)],
        help='Instituion where she/he works')
    code = fields.Char('ID', help='MD License ID')
    specialty = fields.Many2One('gnuhealth.specialty', 'Specialty',
        required=True, help='Specialty Code')
    info = fields.Text('Extra info')

    def get_rec_name(self, ids, name):
        if not ids:
            return {}
        res = {}
        for doctor in self.browse(ids):
            if doctor.name:
                name = doctor.name.name
                if doctor.name.lastname:
                    name = doctor.name.lastname + ', ' + name
            res[doctor.id] = name
        return res

Physician()


class OperationalArea(ModelSQL, ModelView):
    'Operational Area'
    _name = 'gnuhealth.operational_area'
    _description = __doc__

    name = fields.Char('Name', required=True,
        help='Operational Area of the city or region')
    operational_sector = fields.One2Many('gnuhealth.operational_sector',
        'operational_area', 'Operational Sector', readonly=True)
    info = fields.Text('Extra Information')

    def __init__(self):
        super(OperationalArea, self).__init__()
        self._sql_constraints += [
            ('name_uniq', 'UNIQUE(name)',
                    'The operational area must be unique !'),
        ]

OperationalArea()


class OperationalSector(ModelSQL, ModelView):
    'Operational Sector'
    _name = 'gnuhealth.operational_sector'
    _description = __doc__

    name = fields.Char('Op. Sector', required=True,
        help='Region included in an operational area')
    operational_area = fields.Many2One('gnuhealth.operational_area',
        'Operational Area')
    info = fields.Text('Extra Information')

    def __init__(self):
        super(OperationalSector, self).__init__()
        self._sql_constraints += [
            ('name_uniq', 'UNIQUE(name, operational_area)',
                    'The operational sector must be unique in each' \
                    ' operational area!'),
        ]

OperationalSector()


class Family(ModelSQL, ModelView):
    'Family'
    _name = 'gnuhealth.family'
    _description = __doc__

    name = fields.Char('Family', required=True,
        help='Family code within an operational sector')
    operational_sector = fields.Many2One('gnuhealth.operational_sector',
        'Operational Sector')
    members = fields.One2Many('gnuhealth.family_member', 'name',
        'Family Members')
    info = fields.Text('Extra Information')

    def __init__(self):
        super(Family, self).__init__()
        self._sql_constraints = [
            ('name_uniq', 'UNIQUE(name)', 'The Family Code must be unique !'),
        ]

Family()


class FamilyMember(ModelSQL, ModelView):
    'Family Member'
    _name = 'gnuhealth.family_member'
    _description = __doc__

    name = fields.Many2One('gnuhealth.family', 'Family', required=True,
        select=True, help='Family code')
    party = fields.Many2One('party.party', 'Party', required=True,
        domain=[('is_person', '=', True)],
        help='Family code')
    role = fields.Char('Role', help='Father, Mother, sibbling...')

FamilyMember()


# Use the template as in Product category.
class MedicamentCategory(ModelSQL, ModelView):
    'Medicament Category'
    _name = 'gnuhealth.medicament.category'
    _description = __doc__

    name = fields.Char('Name', required=True, translate=True)
    parent = fields.Many2One('gnuhealth.medicament.category', 'Parent',
        select=True)
    childs = fields.One2Many('gnuhealth.medicament.category', 'parent',
        string='Children')

    def __init__(self):
        super(MedicamentCategory, self).__init__()
        self._order.insert(0, ('name', 'ASC'))
        self._constraints += [
            ('check_recursion', 'recursive_categories'),
        ]
        self._error_messages.update({
            'recursive_categories': 'You can not create recursive categories!',
        })

    def get_rec_name(self, ids, name):
        if not ids:
            return {}
        res = {}

        def _name(category):
            if category.id in res:
                return res[category.id]
            elif category.parent:
                return _name(category.parent) + ' / ' + category.name
            else:
                return category.name
        for category in self.browse(ids):
            res[category.id] = _name(category)
        return res

MedicamentCategory()


class Medicament(ModelSQL, ModelView):
    'Medicament'
    _name = 'gnuhealth.medicament'
    _description = __doc__
    _rec_name = 'active_component'

    name = fields.Many2One('product.product', 'Product', required=True,
        domain=[('is_medicament', '=', True)],
        help='Product Name')
    active_component = fields.Char('Active component', translate=True,
        help='Active Component')
    category = fields.Many2One('gnuhealth.medicament.category', 'Category',
        select=True)
    therapeutic_action = fields.Char('Therapeutic effect',
        help='Therapeutic action')
    composition = fields.Text('Composition', help='Components')
    indications = fields.Text('Indication', help='Indications')
    dosage = fields.Text('Dosage Instructions', help='Dosage / Indications')
    overdosage = fields.Text('Overdosage', help='Overdosage')
    pregnancy_warning = fields.Boolean('Pregnancy Warning',
        help='The drug represents risk to pregnancy or lactancy')
    pregnancy = fields.Text('Pregnancy and Lactancy',
        help='Warnings for Pregnant Women')

    pregnancy_category = fields.Selection([
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('X', 'X'),
        ('N', 'N'),
        ], 'Pregnancy Category',
        help='** FDA Pregancy Categories ***\n'\
        'CATEGORY A :Adequate and well-controlled human studies have failed'\
        ' to demonstrate a risk to the fetus in the first trimester of'\
        ' pregnancy (and there is no evidence of risk in later'\
        ' trimesters).\n\n'\
        'CATEGORY B : Animal reproduction studies have failed todemonstrate a'\
        ' risk to the fetus and there are no adequate and well-controlled'\
        ' studies in pregnant women OR Animal studies have shown an adverse'\
        ' effect, but adequate and well-controlled studies in pregnant women'\
        ' have failed to demonstrate a risk to the fetus in any'\
        ' trimester.\n\n'
        'CATEGORY C : Animal reproduction studies have shown an adverse'\
        ' effect on the fetus and there are no adequate and well-controlled'\
        ' studies in humans, but potential benefits may warrant use of the'\
        ' drug in pregnant women despite potential risks. \n\n '\
        'CATEGORY D : There is positive evidence of human fetal  risk based'\
        ' on adverse reaction data from investigational or marketing'\
        ' experience or studies in humans, but potential benefits may warrant'\
        ' use of the drug in pregnant women despite potential risks.\n\n'\
        'CATEGORY X : Studies in animals or humans have demonstrated fetal'\
        ' abnormalities and/or there is positive evidence of human fetal risk'\
        ' based on adverse reaction data from investigational or marketing'\
        ' experience, and the risks involved in use of the drug in pregnant'\
        ' women clearly outweigh potential benefits.\n\n'\
        'CATEGORY N : Not yet classified')

    presentation = fields.Text('Presentation', help='Packaging')
    adverse_reaction = fields.Text('Adverse Reactions')
    storage = fields.Text('Storage Conditions')
    notes = fields.Text('Extra Info')

    def get_rec_name(self, ids, name):
        if not ids:
            return {}
        res = {}
        for medicament in self.browse(ids):
            name = medicament.name.name
            res[medicament.id] = name
        return res

    def check_xml_record(self, ids, values):
        return True

Medicament()


class PathologyCategory(ModelSQL, ModelView):
    'Disease Categories'
    _name = 'gnuhealth.pathology.category'
    _description = __doc__

    name = fields.Char('Category Name', required=True, translate=True)
    parent = fields.Many2One('gnuhealth.pathology.category', 'Parent Category',
        select=True)
    childs = fields.One2Many('gnuhealth.pathology.category', 'parent',
        'Children Category')

    def __init__(self):
        super(PathologyCategory, self).__init__()
        self._order.insert(0, ('name', 'ASC'))
        self._constraints += [
            ('check_recursion', 'recursive_categories'),
        ]
        self._error_messages.update({
            'recursive_categories': 'You can not create recursive categories!',
        })

    def get_rec_name(self, ids, name):
        if not ids:
            return {}
        res = {}

        def _name(category):
            if category.id in res:
                return res[category.id]
            elif category.parent:
                return _name(category.parent) + ' / ' + category.name
            else:
                return category.name
        for category in self.browse(ids):
            res[category.id] = _name(category)
        return res

PathologyCategory()


class PathologyGroup(ModelSQL, ModelView):
    'Pathology Groups'
    _name = 'gnuhealth.pathology.group'
    _description = __doc__

    name = fields.Char('Name', required=True, translate=True,
        help='Group name')
    code = fields.Char('Code', required=True,
        help='for example MDG6 code will contain the Millennium Development'\
        ' Goals # 6 diseases : Tuberculosis, Malaria and HIV/AIDS')
    desc = fields.Char('Short Description', required=True)
    info = fields.Text('Detailed information')

    # Upgrade from GNU Health 1.4.5
    def init(self, module_name):
        super(PathologyGroup, self).init(module_name)

        cursor = Transaction().cursor
        table = TableHandler(cursor, self, module_name)

        # Drop old foreign key and change to char name
        table.drop_fk('name')

        table.alter_type('name', 'varchar')

        # Drop group column. No longer required
        table.drop_column('group')

PathologyGroup()


class Pathology(ModelSQL, ModelView):
    'Diseases'
    _name = 'gnuhealth.pathology'
    _description = __doc__

    name = fields.Char('Name', required=True, translate=True,
        help='Disease name')
    code = fields.Char('Code', required=True,
        help='Specific Code for the Disease (eg, ICD-10)')
    category = fields.Many2One('gnuhealth.pathology.category', 'Main Category',
        help='Select the main category for this disease This is usually'\
        ' associated to the standard. For instance, the chapter on the ICD-10'\
        ' will be the main category for de disease')
    groups = fields.One2Many('gnuhealth.disease_group.members', 'name',
        'Groups', help='Specify the groups this pathology belongs. Some' \
        ' automated processes act upon the code of the group')
    chromosome = fields.Char('Affected Chromosome', help='chromosome number')
    protein = fields.Char('Protein involved',
        help='Name of the protein(s) affected')
    gene = fields.Char('Gene', help='Name of the gene(s) affected')
    info = fields.Text('Extra Info')

    def __init__(self):
        super(Pathology, self).__init__()
        self._sql_constraints += [
            ('code_uniq', 'UNIQUE(code)', 'The disease code must be unique'),
        ]

Pathology()


# DISEASE GROUP MEMBERS
class DiseaseMembers(ModelSQL, ModelView):
    'Disease group members'
    _name = 'gnuhealth.disease_group.members'
    _description = __doc__

    name = fields.Many2One('gnuhealth.pathology', 'Disease', readonly=True)
    disease_group = fields.Many2One('gnuhealth.pathology.group', 'Group',
        required=True)

DiseaseMembers()


class ProcedureCode(ModelSQL, ModelView):
    'Medical Procedures'
    _name = 'gnuhealth.procedure'
    _description = __doc__

    name = fields.Char('Code', required=True)
    description = fields.Char('Long Text', translate=True)

ProcedureCode()


class InsurancePlan(ModelSQL, ModelView):
    'Insurance Plan'
    _name = 'gnuhealth.insurance.plan'
    _description = __doc__
    _rec_name = 'company'

    name = fields.Many2One('product.product', 'Plan', required=True,
        domain=[('type', '=', 'service')],
        help='Insurance company plan')

    company = fields.Many2One('party.party', 'Insurance Company',
        required=True,
        domain=[('is_insurance_company', '=', True)])

    is_default = fields.Boolean('Default plan',
        help='Check if this is the default plan when assigning this insurance'\
        ' company to a patient')

    notes = fields.Text('Extra info')

    def get_rec_name(self, ids, name):
        if not ids:
            return {}
        res = {}
        for plan in self.browse(ids):
            if plan.name:
                name = plan.name.name
            res[plan.id] = name
        return res

InsurancePlan()


class Insurance(ModelSQL, ModelView):
    'Insurance'
    _name = 'gnuhealth.insurance'
    _description = __doc__
    _rec_name = 'number'

    name = fields.Many2One('party.party', 'Owner')
    number = fields.Char('Number', required=True)
    company = fields.Many2One('party.party', 'Insurance Company',
        required=True, select=True,
        domain=[('is_insurance_company', '=', True)])
    member_since = fields.Date('Member since')
    member_exp = fields.Date('Expiration date')
    category = fields.Char('Category',
        help='Insurance company plan / category')
    insurance_type = fields.Selection([
        ('state', 'State'),
        ('labour_union', 'Labour Union / Syndical'),
        ('private', 'Private'),
        ], 'Insurance Type', select=True)
    plan_id = fields.Many2One('gnuhealth.insurance.plan', 'Plan',
        help='Insurance company plan')
    notes = fields.Text('Extra Info')

    def get_rec_name(self, ids, name):
        if not ids:
            return {}
        res = {}
        for insurance in self.browse(ids):
            if insurance.company:
                name = insurance.company.name + ' : ' + insurance.number
            res[insurance.id] = name
        return res

Insurance()


class PartyPatient (ModelSQL, ModelView):
    'Party'
    _name = 'party.party'

    activation_date = fields.Date('Activation date',
        help='Date of activation of the party')
    alias = fields.Char('Alias', help='Common name that the Party is reffered')
    ref = fields.Char('SSN',
        help='Patient Social Security Number or equivalent')
    is_person = fields.Boolean('Person',
        help='Check if the party is a person.')
    is_patient = fields.Boolean('Patient',
        help='Check if the party is a patient')
    is_doctor = fields.Boolean('Health Prof', help='Check if the party is a health professional')
    is_institution = fields.Boolean('Institution',
        help='Check if the party is a Medical Center')
    is_insurance_company = fields.Boolean('Insurance Company',
        help='Check if the party is an Insurance Company')
    is_pharmacy = fields.Boolean('Pharmacy',
        help='Check if the party is a Pharmacy')

    lastname = fields.Char('Last Name', help='Last Name')
    insurance = fields.One2Many('gnuhealth.insurance', 'name', 'Insurance')
    internal_user = fields.Many2One('res.user', 'Internal User',
        help='In GNU Health is the user (doctor, nurse) that logins.When the'\
        ' party is a doctor or a health professional, it will be the user'\
        ' that maps the doctor\'s party name. It must be present.',
        states={
            'invisible': Not(Bool(Eval('is_doctor'))),
            'required': Bool(Eval('is_doctor')),
            }
        )
    insurance_company_type = fields.Selection([
        ('state', 'State'),
        ('labour_union', 'Labour Union / Syndical'),
        ('private', 'Private'),
        ], 'Insurance Type', select=True)
    insurance_plan_ids = fields.One2Many('gnuhealth.insurance.plan', 'company',
        'Insurance Plans')

    def __init__(self):
        super(PartyPatient, self).__init__()
        self._sql_constraints += [
            ('ref_uniq', 'UNIQUE(ref)', 'The Patient SSN must be unique'),
            ('internal_user_uniq', 'UNIQUE(internal_user)',
                'This health professional is already assigned to a party')
        ]

    def write(self, ids, values):
        # We use this method overwrite to make the fields that have a unique
        # constraint get the NULL value at PostgreSQL level, and not the value
        # '' coming from the client
        if 'ref' in values and not values['ref']:
            values = values.copy()
            values['ref'] = None
        return super(PartyPatient, self).write(ids, values)

    def create(self, values):
        # We use this method overwrite to make the fields that have a unique
        # constraint get the NULL value at PostgreSQL level, and not the value
        # '' coming from the client
        if 'ref' in values and not values['ref']:
            values = values.copy()
            values['ref'] = None
        return super(PartyPatient, self).create(values)

    def get_rec_name(self, ids, name):
        if not ids:
            return {}
        res = {}
        for patient in self.browse(ids):
            name = patient.name
            if patient.lastname:
                name = patient.lastname + ', ' + patient.name
            res[patient.id] = name
        return res

    def search_rec_name(self, name, clause):
        ids = []
        field = None
        for field in ('name', 'lastname'):
            ids = self.search([(field,) + clause[1:]], limit=1)
            if ids:
                break
        if ids:
            return [(field,) + clause[1:]]
        return [(self._rec_name,) + clause[1:]]

PartyPatient()


class PartyAddress(ModelSQL, ModelView):
    'Party Address'
    _name = 'party.address'

    relationship = fields.Char('Relationship',
        help='Include the relationship with the patient - friend, co-worker,'\
        ' brother,...')
    relative_id = fields.Many2One('party.party', 'Contact',
        domain=[('is_person', '=', True)],
        help='If the relative is also a patient, please include it here')

    is_school = fields.Boolean("School", help="Check this box to mark the \
        school address")
    is_work = fields.Boolean("Work", help="Check this box to mark the work \
        address")

PartyAddress()


class Product(ModelSQL, ModelView):
    'Product'
    _name = 'product.product'

    is_medicament = fields.Boolean('Medicament',
        help='Check if the product is a medicament')
    is_vaccine = fields.Boolean('Vaccine',
        help='Check if the product is a vaccine')
    is_bed = fields.Boolean('Bed',
        help='Check if the product is a bed on the gnuhealth.center')

    def check_xml_record(self, ids, values):
        return True

Product()


# GNU HEALTH SEQUENCES
class GnuHealthSequences(ModelSingleton, ModelSQL, ModelView):
    'Standard Sequences for GNU Health'
    _name = 'gnuhealth.sequences'
    _description = __doc__

    patient_sequence = fields.Property(fields.Many2One('ir.sequence',
        'Patient Sequence', required=True,
        domain=[('code', '=', 'gnuhealth.patient')]))

    appointment_sequence = fields.Property(fields.Many2One('ir.sequence',
        'Appointment Sequence', required=True,
        domain=[('code', '=', 'gnuhealth.appointment')]))

    prescription_sequence = fields.Property(fields.Many2One('ir.sequence',
        'Prescription Sequence', required=True,
        domain=[('code', '=', 'gnuhealth.prescription.order')]))

GnuHealthSequences()


# PATIENT GENERAL INFORMATION
class PatientData(ModelSQL, ModelView):
    'Patient related information'
    _name = 'gnuhealth.patient'
    _description = __doc__

# Get the patient age in the following format : 'YEARS MONTHS DAYS'
# It will calculate the age of the patient while the patient is alive.
# When the patient dies, it will show the age at time of death.

    def patient_age(self, ids, name):

        def compute_age_from_dates(patient_dob, patient_deceased,
            patient_dod, patient_sex):
            now = datetime.now()
            if (patient_dob):
                dob = datetime.strptime(str(patient_dob), '%Y-%m-%d')

                if patient_deceased:
                    dod = datetime.strptime(patient_dod, '%Y-%m-%d %H:%M:%S')
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

# Return if the patient is in the period of childbearing age (10 is the caller
# is childbearing_potential

            if (name == 'childbearing_age' and patient_dob):
                if (delta.years >= 11 \
                and delta.years <= 55 \
                and patient_sex == 'f'):
                    return True
                else:
                    return False

        result = {}

        for patient_data in self.browse(ids):
            result[patient_data.id] = compute_age_from_dates(patient_data.dob,
            patient_data.deceased, patient_data.dod, patient_data.sex)
        return result

    name = fields.Many2One('party.party', 'Patient', required=True,
        domain=[
            ('is_patient', '=', True),
            ('is_person', '=', True),
            ],
        help='Patient Name')
    lastname = fields.Function(fields.Char('Lastname'),
        'get_patient_lastname', searcher='search_patient_lastname')

    ssn = fields.Function(fields.Char('SSN'),
        'get_patient_ssn', searcher='search_patient_ssn')

    identification_code = fields.Char('ID', readonly=True,
        help='Patient Identifier provided by the Health Center.Is not the'\
        ' Social Security Number')

    family = fields.Many2One('gnuhealth.family', 'Family',
        help='Family Code')
    current_insurance = fields.Many2One('gnuhealth.insurance', 'Insurance',
        domain=[('name', '=', Eval('name'))],
        depends=['name'],
        help='Insurance information. You may choose from the different'\
        ' insurances belonging to the patient')
    current_address = fields.Many2One('party.address', 'Address',
        domain=[('party', '=', Eval('name'))],
        depends=['name'],
        help='Contact information. You may choose from the different contacts'\
        ' and addresses this patient has.')
    primary_care_doctor = fields.Many2One('gnuhealth.physician',
        'Primary Care Doctor', help='Current primary care / family doctor')
    photo = fields.Binary('Picture')
    dob = fields.Date('DoB', help='Date of Birth')
    age = fields.Function(fields.Char('Age'), 'patient_age')
    sex = fields.Selection([
        ('m', 'Male'),
        ('f', 'Female'),
        ], 'Sex', required=True)
    marital_status = fields.Selection([
        ('s', 'Single'),
        ('m', 'Married'),
        ('w', 'Widowed'),
        ('d', 'Divorced'),
        ('x', 'Separated'),
        ], 'Marital Status', sort=False)
    blood_type = fields.Selection([
        ('A', 'A'),
        ('B', 'B'),
        ('AB', 'AB'),
        ('O', 'O'),
        ], 'Blood Type')
    rh = fields.Selection([
        ('+', '+'),
        ('-', '-'),
        ], 'Rh')

    ethnic_group = fields.Many2One('gnuhealth.ethnicity', 'Ethnic group')
    vaccinations = fields.One2Many('gnuhealth.vaccination', 'name',
        'Vaccinations')
    medications = fields.One2Many('gnuhealth.patient.medication', 'name',
        'Medications')

# Removed in 1.6
#    prescriptions = fields.One2Many('gnuhealth.prescription.order', 'name',
#        'Prescriptions')

    diseases = fields.One2Many('gnuhealth.patient.disease', 'name', 'Diseases')
    critical_info = fields.Text('Important disease, allergy or procedures'\
        ' information',
        help='Write any important information on the patient\'s disease,'\
        ' surgeries, allergies, ...')

# Removed it in 1.6
# Not used anymore . Now we relate with a shortcut. Clearer
#    evaluation_ids = fields.One2Many('gnuhealth.patient.evaluation', 'patient',
#        'Evaluation')
#    admissions_ids = fields.One2Many('gnuhealth.patient.admission', 'name',
#        'Admission / Discharge')

    general_info = fields.Text('General Information',
        help='General information about the patient')
    deceased = fields.Boolean('Deceased', help='Mark if the patient has died')
    dod = fields.DateTime('Date of Death',
        states={
            'invisible': Not(Bool(Eval('deceased'))),
            'required': Bool(Eval('deceased')),
            },
        depends=['deceased'])
    cod = fields.Many2One('gnuhealth.pathology', 'Cause of Death',
        states={
            'invisible': Not(Bool(Eval('deceased'))),
            'required': Bool(Eval('deceased')),
            },
        depends=['deceased'])

    childbearing_age = fields.Function(fields.Boolean(
            'Potential for Childbearing'), 'patient_age')

    def get_patient_ssn(self, ids, name):
        res = {}
        for patient in self.browse(ids):
            res[patient.id] = patient.name.ref
        return res

    def search_patient_ssn(self, name, clause):
        res = []
        value = clause[2]
        res.append(('name.ref', clause[1], value))
        return res

    def get_patient_lastname(self, ids, name):
        res = {}
        for patient in self.browse(ids):
            res[patient.id] = patient.name.lastname
        return res

    def search_patient_lastname(self, name, clause):
        res = []
        value = clause[2]
        res.append(('name.lastname', clause[1], value))
        return res

    # Search by the patient name, lastname or SSN

    def search_rec_name(self, name, clause):
        ids = []
        field = None
        for field in ('name', 'lastname', 'ssn'):
            ids = self.search([(field,) + clause[1:]], limit=1)
            if ids:
                break
        if ids:
            return [(field,) + clause[1:]]
        return [(self._rec_name,) + clause[1:]]

    def __init__(self):
        super(PatientData, self).__init__()
        self._sql_constraints = [
            ('name_uniq', 'UNIQUE(name)', 'The Patient already exists !'),
        ]

    def create(self, values):
        sequence_obj = Pool().get('ir.sequence')
        config_obj = Pool().get('gnuhealth.sequences')

        values = values.copy()
        if not values.get('identification_code'):
            config = config_obj.browse(1)
            values['identification_code'] = sequence_obj.get_id(
            config.patient_sequence.id)

        return super(PatientData, self).create(values)

    def get_rec_name(self, ids, name):
        if not ids:
            return {}
        res = {}
        for patient in self.browse(ids):
            if patient.name:
                name = patient.name.name
                if patient.name.lastname:
                    name = patient.name.lastname + ', ' + name
            res[patient.id] = name
        return res

PatientData()


# PATIENT DISESASES INFORMATION
class PatientDiseaseInfo(ModelSQL, ModelView):
    'Patient Disease History'
    _name = 'gnuhealth.patient.disease'
    _description = __doc__

    name = fields.Many2One('gnuhealth.patient', 'Patient')
    pathology = fields.Many2One('gnuhealth.pathology', 'Disease',
        required=True, help='Disease')
    disease_severity = fields.Selection([
        ('1_mi', 'Mild'),
        ('2_mo', 'Moderate'),
        ('3_sv', 'Severe'),
        ], 'Severity', select=True, sort=False)
    is_on_treatment = fields.Boolean('Currently on Treatment')
    is_infectious = fields.Boolean('Infectious Disease',
        help='Check if the patient has an infectious / transmissible disease')
    short_comment = fields.Char('Remarks',
        help='Brief, one-line remark of the disease. Longer description will'\
        ' go on the Extra info field')
    doctor = fields.Many2One('gnuhealth.physician', 'Physician',
        help='Physician who treated or diagnosed the patient')
    diagnosed_date = fields.Date('Date of Diagnosis')
    healed_date = fields.Date('Healed')
    is_active = fields.Boolean('Active disease')
    age = fields.Integer('Age when diagnosed',
        help='Patient age at the moment of the diagnosis. Can be estimative')
    pregnancy_warning = fields.Boolean('Pregnancy warning')
    weeks_of_pregnancy = fields.Integer('Contracted in pregnancy week #')
    is_allergy = fields.Boolean('Allergic Disease')
    allergy_type = fields.Selection([
        ('da', 'Drug Allergy'),
        ('fa', 'Food Allergy'),
        ('ma', 'Misc Allergy'),
        ('mc', 'Misc Contraindication'),
        ], 'Allergy type', select=True, sort=False)
    pcs_code = fields.Many2One('gnuhealth.procedure', 'Code',
        help='Procedure code, for example, ICD-10-PCS Code 7-character string')
    treatment_description = fields.Char('Treatment Description')
    date_start_treatment = fields.Date('Start', help='Start of treatment date')
    date_stop_treatment = fields.Date('End', help='End of treatment date')
    status = fields.Selection([
        ('a', 'acute'),
        ('c', 'chronic'),
        ('u', 'unchanged'),
        ('h', 'healed'),
        ('i', 'improving'),
        ('w', 'worsening'),
        ], 'Status of the disease', select=True, sort=False)
    extra_info = fields.Text('Extra Info')

    def default_is_active(self):
        return True

    def __init__(self):
        super(PatientDiseaseInfo, self).__init__()
        self._order.insert(0, ('is_active', 'DESC'))
        self._order.insert(1, ('disease_severity', 'DESC'))
        self._order.insert(2, ('is_infectious', 'DESC'))
        self._order.insert(3, ('diagnosed_date', 'DESC'))
        self._constraints += [
            ('validate_disease_period', 'end_date_before_start'),
            ('validate_treatment_dates', 'end_treatment_date_before_start'),
            ]
        self._error_messages.update({
            'end_date_before_start': 'The HEALED date is BEFORE DIAGNOSED DATE !',
            'end_treatment_date_before_start': 'The Treatment END DATE is BEFORE the start date!',
            })

    def validate_disease_period (self, ids):
        for disease_data in self.browse(ids):
            if (disease_data.healed_date < disease_data.diagnosed_date):
                return False
            else:
                return True

    def validate_treatment_dates (self, ids):
        for disease_data in self.browse(ids):
            if (disease_data.date_stop_treatment < disease_data.date_start_treatment):
                return False
            else:
                return True


PatientDiseaseInfo()


# PATIENT APPOINTMENT
class Appointment(ModelSQL, ModelView):
    'Patient Appointments'
    _name = 'gnuhealth.appointment'
    _description = __doc__

    name = fields.Char('Appointment ID', readonly=True)
    doctor = fields.Many2One('gnuhealth.physician', 'Physician',
        select=True, help='Physician\'s Name')
    patient = fields.Many2One('gnuhealth.patient', 'Patient', required=True,
        select=True, help='Patient Name')
    appointment_date = fields.DateTime('Date and Time')
    institution = fields.Many2One('party.party', 'Health Center',
        domain=[('is_institution', '=', True)],
        help='Medical Center')
    speciality = fields.Many2One('gnuhealth.specialty', 'Specialty',
        help='Medical Specialty / Sector')
    urgency = fields.Selection([
        ('a', 'Normal'),
        ('b', 'Urgent'),
        ('c', 'Medical Emergency'),
        ], 'Urgency Level', sort=False)

    comments = fields.Text('Comments')

    appointment_type = fields.Selection([
        ('ambulatory', 'Ambulatory'),
        ('outpatient', 'Outpatient'),
        ('inpatient', 'Inpatient'),
        ], 'Type', sort=False)
    consultations = fields.Many2One('product.product', 'Consultation Services',
        domain=[('type', '=', 'service')],
        help='Consultation Services')

    def __init__(self):
        super(Appointment, self).__init__()
        self._order.insert(0, ('name', 'DESC'))

    def create(self, values):
        sequence_obj = Pool().get('ir.sequence')
        config_obj = Pool().get('gnuhealth.sequences')

        values = values.copy()
        if not values.get('name'):
            config = config_obj.browse(1)
            values['name'] = sequence_obj.get_id(
            config.appointment_sequence.id)

        return super(Appointment, self).create(values)

    def default_doctor(self):
        cursor = Transaction().cursor
        user_obj = Pool().get('res.user')
        user = user_obj.browse(Transaction().user)
        login_user_id = int(user.id)
        cursor.execute('SELECT id FROM party_party WHERE is_doctor=True AND \
            internal_user = %s LIMIT 1', (login_user_id,))
        partner_id = cursor.fetchone()
        if partner_id:
            cursor = Transaction().cursor
            cursor.execute('SELECT id FROM gnuhealth_physician WHERE \
                name = %s LIMIT 1', (partner_id[0],))
            doctor_id = cursor.fetchone()
            return int(doctor_id[0])

    def default_urgency(self):
        return 'a'

    def default_appointment_date(self):
        return datetime.now()

    def default_appointment_type(self):
        return 'ambulatory'

    def get_rec_name(self, ids, name):
        if not ids:
            return {}
        res = {}
        for appointment in self.browse(ids):
            if appointment.name:
                name = appointment.name
#                name = str(appointment['appointment_date'])
            res[appointment.id] = name
        return res

Appointment()


# MEDICATION TEMPLATE
# TEMPLATE USED IN MEDICATION AND PRESCRIPTION ORDERS
class MedicationTemplate(ModelSQL, ModelView):
    'Template for medication'
    _name = 'gnuhealth.medication.template'
    _description = __doc__

    medicament = fields.Many2One('gnuhealth.medicament', 'Medicament',
        required=True, help='Prescribed Medicament')
    indication = fields.Many2One('gnuhealth.pathology', 'Indication',
        help='Choose a disease for this medicament from the disease list. It'\
        ' can be an existing disease of the patient or a prophylactic.')
    dose = fields.Float('Dose',
        help='Amount of medication (eg, 250 mg) per dose')
    dose_unit = fields.Many2One('gnuhealth.dose.unit', 'dose unit',
        help='Unit of measure for the medication to be taken')
    route = fields.Many2One('gnuhealth.drug.route', 'Administration Route',
        help='Drug administration route code.')
    form = fields.Many2One('gnuhealth.drug.form', 'Form',
        help='Drug form, such as tablet or gel')
    qty = fields.Integer('x',
        help='Quantity of units (eg, 2 capsules) of the medicament')
    common_dosage = fields.Many2One('gnuhealth.medication.dosage', 'Frequency',
        help='Common / standard dosage frequency for this medicament')
    frequency = fields.Integer('Frequency',
        help='Time in between doses the patient must wait (ie, for 1 pill'\
        ' each 8 hours, put here 8 and select \"hours\" in the unit field')
    frequency_unit = fields.Selection([
        ('seconds', 'seconds'),
        ('minutes', 'minutes'),
        ('hours', 'hours'),
        ('days', 'days'),
        ('weeks', 'weeks'),
        ('wr', 'when required'),
        ], 'unit', select=True, sort=False)

    frequency_prn = fields.Boolean('PRN',
        help='Use it as needed, pro re nata')
    admin_times = fields.Char('Admin hours',
        help='Suggested administration hours. For example, at 08:00, 13:00'\
        ' and 18:00 can be encoded like 08 13 18')
    duration = fields.Integer('Treatment duration',
        help='Period that the patient must take the medication. in minutes,'\
        ' hours, days, months, years or indefinately')
    duration_period = fields.Selection([
        ('minutes', 'minutes'),
        ('hours', 'hours'),
        ('days', 'days'),
        ('months', 'months'),
        ('years', 'years'),
        ('indefinite', 'indefinite'),
        ], 'Treatment period', sort=False,
        help='Period that the patient must take the medication in minutes,'\
        ' hours, days, months, years or indefinately')
    start_treatment = fields.DateTime('Start',
        help='Date of start of Treatment')
    end_treatment = fields.DateTime('End', help='Date of start of Treatment')

MedicationTemplate()


# PATIENT MEDICATION TREATMENT
class PatientMedication(ModelSQL, ModelView):
    'Patient Medication'
    _name = 'gnuhealth.patient.medication'
    _inherits = {'gnuhealth.medication.template': 'template'}
    _description = __doc__

    template = fields.Many2One('gnuhealth.medication.template',
        'Medication Template')
    name = fields.Many2One('gnuhealth.patient', 'Patient', readonly=True)
    doctor = fields.Many2One('gnuhealth.physician', 'Physician',
        help='Physician who prescribed the medicament')
    is_active = fields.Boolean('Active',
        on_change_with=['discontinued', 'course_completed'],
        help='Check if the patient is currently taking the medication')
    discontinued = fields.Boolean('Discontinued',
        on_change_with=['is_active', 'course_completed'])
    course_completed = fields.Boolean('Course Completed',
        on_change_with=['is_active', 'discontinued'])
    discontinued_reason = fields.Char('Reason for discontinuation',
        states={
            'invisible': Not(Bool(Eval('discontinued'))),
            'required': Bool(Eval('discontinued')),
            },
        depends=['discontinued'],
        help='Short description for discontinuing the treatment',)
    adverse_reaction = fields.Text('Adverse Reactions',
        help='Side effects or adverse reactions that the patient experienced')
    notes = fields.Text('Extra Info')
    patient = fields.Many2One('gnuhealth.patient', 'Patient')

    def on_change_with_is_active(self, vals):
        discontinued = vals.get('discontinued')
        course_completed = vals.get('course_completed')
        is_active = True
        if (discontinued or course_completed):
            is_active = False
        return is_active

    def on_change_with_discontinued(self, vals):
        discontinued = vals.get('discontinued')
        is_active = vals.get('is_active')
        course_completed = vals.get('course_completed')
        if (is_active or course_completed):
            discontinued = False
        return (discontinued)

    def on_change_with_course_completed(self, vals):
        is_active = vals.get('is_active')
        course_completed = vals.get('discontinued')
        discontinued = vals.get('discontinued')
        if (is_active or discontinued):
            course_completed = False
        return (course_completed)

    def default_is_active(self):
        return True

#    def default_start_treatment(self):
#        return time.strftime('%Y-%m-%d %H:%M:%S')

    def default_frequency_unit(self):
        return 'hours'

    def default_duration_period(self):
        return 'days'

    def default_qty(self):
        return 1

    def __init__(self):
        super(PatientMedication, self).__init__()

        self._constraints += [
            ('validate_medication_dates', 'end_date_before_start'),

            ]

        self._error_messages.update({
            'end_date_before_start': 'The Medication END DATE is BEFORE the start date!',
            })

    def validate_medication_dates (self, ids):
        for medication_data in self.browse(ids):
            if (medication_data.end_treatment < medication_data.start_treatment):
                return False
            else:
                return True


PatientMedication()


# PATIENT VACCINATION INFORMATION
class PatientVaccination(ModelSQL, ModelView):
    'Patient Vaccination information'
    _name = 'gnuhealth.vaccination'
    _description = __doc__

    def check_vaccine_expiration_date(self, ids):
        vaccine = self.browse(ids[0])
        if vaccine.vaccine_expiration_date:
            if vaccine.vaccine_expiration_date < datetime.date(vaccine.date):
                return False
        return True

    name = fields.Many2One('gnuhealth.patient', 'Patient', readonly=True)
    vaccine = fields.Many2One('product.product', 'Name', required=True,
        domain=[('is_vaccine', '=', True)],
        help='Vaccine Name. Make sure that the vaccine (product) has all the'\
        ' proper information at product level. Information such as provider,'\
        ' supplier code, tracking number, etc.. This  information must always'\
        ' be present. If available, please copy / scan the vaccine leaflet'\
        ' and attach it to this record')
    vaccine_expiration_date = fields.Date('Expiration date')
    vaccine_lot = fields.Char('Lot Number',
        help='Please check on the vaccine (product) production lot numberand'\
        ' tracking number when available !')
    institution = fields.Many2One('party.party', 'Institution',
        domain=[('is_institution', '=', True)],
        help='Medical Center where the patient is being or was vaccinated')
    date = fields.DateTime('Date')
    dose = fields.Integer('Dose #')
    next_dose_date = fields.DateTime('Next Dose')
    observations = fields.Char('Observations')

    def __init__(self):
        super(PatientVaccination, self).__init__()
        self._sql_constraints = [
            ('dose_uniq', 'UNIQUE(name, vaccine, dose)',
                    'This vaccine dose has been given already to the patient'),
        ]
        self._constraints = [
            ('check_vaccine_expiration_date', 'expired_vaccine'),
            ('validate_next_dose_date', 'next_dose_before_first'),

        ]
        self._error_messages.update({
            'expired_vaccine': 'EXPIRED VACCINE. PLEASE INFORM  THE LOCAL '\
                    'HEALTH AUTHORITIES AND DO NOT USE IT !!!',
            'next_dose_before_first': 'The Vaccine next dose is BEFORE the first one !'

        })

    def default_date(self):
        return datetime.now()

    def default_dose(self):
        return 1

    def validate_next_dose_date (self, ids):
        for vaccine_data in self.browse(ids):
            if (vaccine_data.next_dose_date < vaccine_data.date):
                return False
            else:
                return True

PatientVaccination()


class PatientPrescriptionOrder(ModelSQL, ModelView):
    'Prescription Order'
    _name = 'gnuhealth.prescription.order'
    _rec_name = 'prescription_id'
    _description = __doc__

    def check_prescription_warning(self, ids):
        prescription = self.browse(ids[0])
        if prescription.prescription_warning_ack:
            return True
        return False

    patient = fields.Many2One('gnuhealth.patient', 'Patient', required=True,
        on_change=['patient'])

    prescription_id = fields.Char('Prescription ID',
        readonly=True, help='Type in the ID of this prescription')
    prescription_date = fields.DateTime('Prescription Date')
    user_id = fields.Many2One('res.user', 'Prescribing Doctor', readonly=True)
    pharmacy = fields.Many2One('party.party', 'Pharmacy',
        domain=[('is_pharmacy', '=', True)])
    prescription_line = fields.One2Many('gnuhealth.prescription.line', 'name',
        'Prescription line')
    notes = fields.Text('Prescription Notes')

    pregnancy_warning = fields.Boolean('Pregancy Warning', readonly=True)

    prescription_warning_ack = fields.Boolean('Prescription verified')

    def __init__(self):
        super(PatientPrescriptionOrder, self).__init__()
        self._constraints = [
            ('check_prescription_warning', 'drug_pregnancy_warning'),
        ]
        self._error_messages.update({
            'drug_pregnancy_warning': \
                    '== DRUG AND PREGNANCY VERIFICATION ==\n\n' \
                    '- IS THE PATIENT PREGNANT ? \n' \
                    '- IS PLANNING to BECOME PREGNANT ?\n' \
                    '- HOW MANY WEEKS OF PREGNANCY \n\n' \
                    '- IS THE PATIENT BREASTFEEDING \n\n' \
                    'Verify and check for safety the prescribed drugs\n',
        })

# Method that makes the doctor to acknowledge if there is any
# warning in the prescription

    def on_change_patient(self, vals):
        preg_warning = False
        presc_warning_ack = True

        patient_obj = Pool().get('gnuhealth.patient')

        if vals.get('patient'):
            patient = patient_obj.browse(vals['patient'])
            patient_childbearing_age = patient.childbearing_age

# Trigger the warning if the patient is at a childbearing age
        if (patient_childbearing_age):
            preg_warning = True
            presc_warning_ack = False

        return {
            'prescription_warning_ack': presc_warning_ack,
            'pregnancy_warning': preg_warning,
        }

    def default_prescription_date(self):
        return datetime.now()

    def default_user_id(self):
        user_obj = Pool().get('res.user')
        user = user_obj.browse(Transaction().user)
        return int(user.id)

    def create(self, values):
        sequence_obj = Pool().get('ir.sequence')
        config_obj = Pool().get('gnuhealth.sequences')

        values = values.copy()
        if not values.get('prescription_id'):
            config = config_obj.browse(1)
            values['prescription_id'] = sequence_obj.get_id(
            config.prescription_sequence.id)

        return super(PatientPrescriptionOrder, self).create(values)

PatientPrescriptionOrder()


# PRESCRIPTION LINE
class PrescriptionLine(ModelSQL, ModelView):
    'Prescription Line'
    _name = 'gnuhealth.prescription.line'
    _inherits = {'gnuhealth.medication.template': 'template'}
    _description = __doc__

    template = fields.Many2One('gnuhealth.medication.template',
        'Medication Template')
    name = fields.Many2One('gnuhealth.prescription.order', 'Prescription ID')
    review = fields.DateTime('Review')
    quantity = fields.Integer('Quantity')
    refills = fields.Integer('Refills #')
    allow_substitution = fields.Boolean('Allow substitution')
    short_comment = fields.Char('Comment',
        help='Short comment on the specific drug')
    prnt = fields.Boolean('Print',
        help='Check this box to print this line of the prescription.')

    def default_qty(self):
        return 1

    def default_duration_period(self):
        return 'days'

    def default_frequency_unit(self):
        return 'hours'

    def default_quantity(self):
        return 1

    def default_prnt(self):
        return True

PrescriptionLine()


class PatientEvaluation(ModelSQL, ModelView):
    'Patient Evaluation'
    _name = 'gnuhealth.patient.evaluation'
    _description = __doc__

    patient = fields.Many2One('gnuhealth.patient', 'Patient')
    evaluation_date = fields.Many2One('gnuhealth.appointment', 'Appointment',
        domain=[('patient', '=', Eval('patient'))],
        help='Enter or select the date / ID of the appointment related to'\
        ' this evaluation')
    evaluation_start = fields.DateTime('Start', required=True)
    evaluation_endtime = fields.DateTime('End', required=True)
    next_evaluation = fields.Many2One('gnuhealth.appointment',
        'Next Appointment', domain=[('patient', '=', Eval('patient'))])
    user_id = fields.Many2One('res.user', 'Last Changed by', readonly=True)
    doctor = fields.Many2One('gnuhealth.physician', 'Doctor', readonly=True)
    specialty = fields.Many2One('gnuhealth.specialty', 'Specialty')
    information_source = fields.Char('Source', help="Source of" \
        "Information, eg : Self, relative, friend ...")
    reliable_info = fields.Boolean('Reliable', help="Uncheck this option" \
        "if the information provided by the source seems not reliable")
    derived_from = fields.Many2One('gnuhealth.physician',
        'Derived from',
        help='Physician who derived the case')
    derived_to = fields.Many2One('gnuhealth.physician', 'Derived to',
        help='Physician to whom escalate / derive the case')
    evaluation_type = fields.Selection([
        ('a', 'Ambulatory'),
        ('e', 'Emergency'),
        ('i', 'Inpatient'),
        ('pa', 'Pre-arranged appointment'),
        ('pc', 'Periodic control'),
        ('p', 'Phone call'),
        ('t', 'Telemedicine'),
        ], 'Type', sort=False)
    chief_complaint = fields.Char('Chief Complaint', help='Chief Complaint')
    notes_complaint = fields.Text('Complaint details')
    present_illness = fields.Text('Present Illness')
    evaluation_summary = fields.Text('Evaluation Summary')
    glycemia = fields.Float('Glycemia',
        help='Last blood glucose level. Can be approximative.')
    hba1c = fields.Float('Glycated Hemoglobin',
        help='Last Glycated Hb level. Can be approximative.')
    cholesterol_total = fields.Integer('Last Cholesterol',
        help='Last cholesterol reading. Can be approximative')
    hdl = fields.Integer('Last HDL',
        help='Last HDL Cholesterol reading. Can be approximative')
    ldl = fields.Integer('Last LDL',
        help='Last LDL Cholesterol reading. Can be approximative')
    tag = fields.Integer('Last TAGs',
        help='Triacylglycerol(triglicerides) level. Can be approximative')
    systolic = fields.Integer('Systolic Pressure')
    diastolic = fields.Integer('Diastolic Pressure')
    bpm = fields.Integer('Heart Rate',
        help='Heart rate expressed in beats per minute')
    respiratory_rate = fields.Integer('Respiratory Rate',
        help='Respiratory rate expressed in breaths per minute')
    osat = fields.Integer('Oxygen Saturation',
        help='Oxygen Saturation(arterial).')
    malnutrition = fields.Boolean('Malnutrition',
        help='Check this box if the patient show signs of malnutrition. If'\
        ' associated  to a disease, please encode the correspondent disease'\
        ' on the patient disease history. For example, Moderate'\
        ' protein-energy malnutrition, E44.0 in ICD-10 encoding')
    dehydration = fields.Boolean('Dehydration',
        help='Check this box if the patient show signs of dehydration. If'\
        ' associated  to a disease, please encode the  correspondent disease'\
        ' on the patient disease history. For example, Volume Depletion, E86'\
        ' in ICD-10 encoding')
    temperature = fields.Float('Temperature',
        help='Temperature in celcius')
    weight = fields.Float('Weight', help='Weight in Kilos')
    height = fields.Float('Height', help='Height in centimeters, eg 175')
    bmi = fields.Float('Body Mass Index',
        on_change_with=['weight', 'height', 'bmi'])
    head_circumference = fields.Float('Head Circumference',
        help='Head circumference')
    abdominal_circ = fields.Float('Waist')
    hip = fields.Float('Hip', help='Hip circumference in centimeters, eg 100')
    whr = fields.Float('WHR', help='Waist to hip ratio',
        on_change_with=['abdominal_circ', 'hip', 'whr'])

# DEPRECATION NOTE : SIGNS AND SYMPTOMS FIELDS TO BE REMOVED IN 1.6 .
# NOW WE USE A O2M OBJECT TO MAKE IT MORE SCALABLE, CLEARER AND FUNCTIONAL
# TO WORK WITH THE CLINICAL FINDINGS OF THE PATIENT
    loc = fields.Integer('Level of Consciousness',
        on_change_with=['loc_verbal', 'loc_motor', 'loc_eyes'],
        help='Level of Consciousness - on Glasgow Coma Scale :  1=coma -'\
        ' 15=normal')
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

    tremor = fields.Boolean('Tremor',
        help='If associated  to a disease, please encode it on the patient'\
        ' disease history')
    violent = fields.Boolean('Violent Behaviour',
        help='Check this box if the patient is agressive or violent at the'\
        ' moment')
    mood = fields.Selection([
        ('n', 'Normal'),
        ('s', 'Sad'),
        ('f', 'Fear'),
        ('r', 'Rage'),
        ('h', 'Happy'),
        ('d', 'Disgust'),
        ('e', 'Euphoria'),
        ('fl', 'Flat'),
        ], 'Mood', sort=False)

    orientation = fields.Boolean('Orientation',
        help='Check this box if the patient is disoriented in time and/or'\
        ' space')
    memory = fields.Boolean('Memory',
        help='Check this box if the patient has problems in short or long'\
        ' term memory')
    knowledge_current_events = fields.Boolean('Knowledge of Current Events',
        help='Check this box if the patient can not respond to public'\
        ' notorious events')
    judgment = fields.Boolean('Jugdment',
        help='Check this box if the patient can not interpret basic scenario'\
        ' solutions')
    abstraction = fields.Boolean('Abstraction',
        help='Check this box if the patient presents abnormalities in'\
        ' abstract reasoning')
    vocabulary = fields.Boolean('Vocabulary',
        help='Check this box if the patient lacks basic intelectual capacity,'\
        ' when she/he can not describe elementary objects')
    calculation_ability = fields.Boolean('Calculation Ability',
        help='Check this box if the patient can not do simple arithmetic'\
        ' problems')
    object_recognition = fields.Boolean('Object Recognition',
        help='Check this box if the patient suffers from any sort of gnosia'\
        ' disorders, such as agnosia, prosopagnosia ...')
    praxis = fields.Boolean('Praxis',
        help='Check this box if the patient is unable to make voluntary'\
        'movements')
    diagnosis = fields.Many2One('gnuhealth.pathology', 'Presumptive Diagnosis',
        help='Presumptive Diagnosis. If no diagnosis can be made'\
        ', encode the main sign or symptom.')
    secondary_conditions = fields.One2Many('gnuhealth.secondary_condition',
        'evaluation', 'Secondary Conditions', help="Other, Secondary \
            conditions found on the patient")

    diagnostic_hypothesis = fields.One2Many('gnuhealth.diagnostic_hypothesis',
        'evaluation', 'Hypotheses / DDx', help="Other Diagnostic Hypotheses / \
            Differential Diagnosis (DDx)")
    signs_and_symptoms = fields.One2Many('gnuhealth.signs_and_symptoms',
        'evaluation', 'Signs and Symptoms', help="Enter the Signs and Symptoms \
        for the patient in this evaluation.")
    info_diagnosis = fields.Text('Presumptive Diagnosis: Extra Info')
    directions = fields.Text('Plan')
    actions = fields.One2Many('gnuhealth.directions', 'name', 'Procedures',
        help='Procedures / Actions to take')

    notes = fields.Text('Notes')

    def default_doctor(self):
        cursor = Transaction().cursor
        user_obj = Pool().get('res.user')
        user = user_obj.browse(Transaction().user)
        login_user_id = int(user.id)
        cursor.execute('SELECT id FROM party_party WHERE is_doctor=True AND \
            internal_user = %s LIMIT 1', (login_user_id,))
        partner_id = cursor.fetchone()
        if not partner_id:
            self.raise_user_error('No health professional associated to this \
                user')
        else:
            cursor = Transaction().cursor
            cursor.execute('SELECT id FROM gnuhealth_physician WHERE \
                name = %s LIMIT 1', (partner_id[0],))
            doctor_id = cursor.fetchone()

            return int(doctor_id[0])

    def default_loc_eyes(self):
        return '4'

    def default_loc_verbal(self):
        return '5'

    def default_loc_motor(self):
        return '6'

    def default_loc(self):
        return 15

    def default_evaluation_type(self):
        return 'pa'

    def on_change_with_bmi(self, vals):
        height = vals.get('height')
        weight = vals.get('weight')
        if (height > 0):
            bmi = weight / ((height / 100) ** 2)
        else:
            bmi = 0
        return bmi

    def on_change_with_loc(self, vals):
        loc_motor = vals.get('loc_motor')
        loc_eyes = vals.get('loc_eyes')
        loc_verbal = vals.get('loc_verbal')
        loc = int(loc_motor) + int(loc_eyes) + int(loc_verbal)
        return loc

    def default_information_source(self):
        return 'Self'

    def default_reliable_info(self):
        return True

    def default_evaluation_start(self):
        return datetime.now()

# Calculate the WH ratio
    def on_change_with_whr(self, vals):
        waist = vals.get('abdominal_circ')
        hip = vals.get('hip')
        if (hip > 0):
            whr = waist / hip
        else:
            whr = 0
        return whr

    def get_rec_name(self, ids, name):
        if not ids:
            return {}
        res = {}
        for evaluation in self.browse(ids):
            if evaluation.evaluation_start:
                name = str(evaluation.evaluation_start)
            res[evaluation.id] = name
        return res


PatientEvaluation()


# PATIENT EVALUATION DIRECTIONS
class Directions(ModelSQL, ModelView):
    'Patient Directions'
    _name = 'gnuhealth.directions'
    _description = __doc__

    name = fields.Many2One('gnuhealth.patient.evaluation', 'Evaluation',
        readonly=True)
    procedure = fields.Many2One('gnuhealth.procedure', 'Procedure',
            required=True)
    comments = fields.Char('Comments')

Directions()


# SECONDARY CONDITIONS ASSOCIATED TO THE PATIENT IN THE EVALUATION
class SecondaryCondition(ModelSQL, ModelView):
    'Secondary Conditions'
    _name = 'gnuhealth.secondary_condition'
    _description = __doc__

    evaluation = fields.Many2One('gnuhealth.patient.evaluation', 'Evaluation',
        readonly=True)
    pathology = fields.Many2One('gnuhealth.pathology', 'Pathology',
        required=True)
    comments = fields.Char('Comments')

SecondaryCondition()


# PATIENT EVALUATION OTHER DIAGNOSTIC HYPOTHESES
class DiagnosticHypothesis(ModelSQL, ModelView):
    'Other Diagnostic Hypothesis'
    _name = 'gnuhealth.diagnostic_hypothesis'
    _description = __doc__

    evaluation = fields.Many2One('gnuhealth.patient.evaluation', 'Evaluation',
        readonly=True)
    pathology = fields.Many2One('gnuhealth.pathology', 'Pathology',
        required=True)
    comments = fields.Char('Comments')

DiagnosticHypothesis()


# PATIENT EVALUATION CLINICAL FINDINGS (SIGNS AND SYMPTOMS)
class SignsAndSymptoms(ModelSQL, ModelView):
    'Evaluation Signs and Symptoms'
    _name = 'gnuhealth.signs_and_symptoms'
    _description = __doc__

    evaluation = fields.Many2One('gnuhealth.patient.evaluation', 'Evaluation',
        readonly=True)
    sign_or_symptom = fields.Selection([
        ('sign', 'Sign'),
        ('symptom', 'Symptom')],
        'Subjective / Objective', required=True)
    clinical = fields.Many2One('gnuhealth.pathology', 'Sign or Symptom',
        domain=[('code', 'like', 'R%')], required=True)
    comments = fields.Char('Comments')

SignsAndSymptoms()


# HEALTH CENTER / HOSPITAL INFRASTRUCTURE
class HospitalBuilding(ModelSQL, ModelView):
    'Hospital Building'
    _name = 'gnuhealth.hospital.building'
    _description = __doc__

    name = fields.Char('Name', required=True,
        help='Name of the building within the institution')
    institution = fields.Many2One('party.party', 'Institution',
        domain=[('is_institution', '=', True)],
        help='Medical Center')
    code = fields.Char('Code')
    extra_info = fields.Text('Extra Info')

HospitalBuilding()


class HospitalUnit(ModelSQL, ModelView):
    'Hospital Unit'
    _name = 'gnuhealth.hospital.unit'
    _description = __doc__

    name = fields.Char('Name', required=True,
        help='Name of the unit, eg Neonatal, Intensive Care, ...')
    institution = fields.Many2One('party.party', 'Institution',
        domain=[('is_institution', '=', True)],
        help='Medical Center')
    code = fields.Char('Code')
    extra_info = fields.Text('Extra Info')

HospitalUnit()


class HospitalOR(ModelSQL, ModelView):
    'Operating Room'
    _name = 'gnuhealth.hospital.or'
    _description = __doc__

    name = fields.Char('Name', required=True,
        help='Name of the Operating Room')
    institution = fields.Many2One('party.party', 'Institution',
        domain=[('is_institution', '=', True)],
        help='Medical Center')
    building = fields.Many2One('gnuhealth.hospital.building', 'Building',
        select=True)
    unit = fields.Many2One('gnuhealth.hospital.unit', 'Unit')
    extra_info = fields.Text('Extra Info')

    def __init__(self):
        super(HospitalOR, self).__init__()
        self._sql_constraints = [
            ('name_uniq', 'UNIQUE(name, institution)',
                    'The Operating Room code must be unique per Health' \
                    ' Center'),
        ]

HospitalOR()


class HospitalWard(ModelSQL, ModelView):
    'Hospital Ward'
    _name = 'gnuhealth.hospital.ward'
    _description = __doc__

    name = fields.Char('Name', required=True, help='Ward / Room code')
    institution = fields.Many2One('party.party', 'Institution',
        domain=[('is_institution', '=', True)],
        help='Medical Center')
    building = fields.Many2One('gnuhealth.hospital.building', 'Building')
    floor = fields.Integer('Floor Number')
    unit = fields.Many2One('gnuhealth.hospital.unit', 'Unit')
    private = fields.Boolean('Private',
        help='Check this option for private room')
    bio_hazard = fields.Boolean('Bio Hazard',
        help='Check this option if there is biological hazard')
    number_of_beds = fields.Integer('Number of beds',
        help='Number of patients per ward')
    telephone = fields.Boolean('Telephone access')
    ac = fields.Boolean('Air Conditioning')
    private_bathroom = fields.Boolean('Private Bathroom')
    guest_sofa = fields.Boolean('Guest sofa-bed')
    tv = fields.Boolean('Television')
    internet = fields.Boolean('Internet Access')
    refrigerator = fields.Boolean('Refrigetator')
    microwave = fields.Boolean('Microwave')
    gender = fields.Selection((
        ('men', 'Men Ward'),
        ('women', 'Women Ward'),
        ('unisex', 'Unisex'),
        ), 'Gender', required=True, sort=False)
    state = fields.Selection((
        ('beds_available', 'Beds available'),
        ('full', 'Full'),
        ('na', 'Not available'),
        ), 'Status', sort=False)
    extra_info = fields.Text('Extra Info')

    def default_gender(self):
        return 'unisex'

    def default_number_of_beds(self):
        return 1

HospitalWard()


class HospitalBed(ModelSQL, ModelView):
    'Hospital Bed'
    _name = 'gnuhealth.hospital.bed'
    _description = __doc__
    _rec_name = 'telephone_number'

    name = fields.Many2One('product.product', 'Bed', required=True,
        domain=[('is_bed', '=', True)],
        help='Bed Number')
    ward = fields.Many2One('gnuhealth.hospital.ward', 'Ward',
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
    telephone_number = fields.Char('Telephone Number',
        help='Telephone number / Extension')
    extra_info = fields.Text('Extra Info')
    state = fields.Selection((
        ('free', 'Free'),
        ('reserved', 'Reserved'),
        ('occupied', 'Occupied'),
        ('na', 'Not available'),
        ), 'Status', readonly=True, sort=False)

    def default_bed_type(self):
        return 'gatch'

    def default_state(self):
        return 'free'

    def get_rec_name(self, ids, name):
        if not ids:
            return {}
        res = {}
        for bed in self.browse(ids):
            if bed.name:
                name = bed.name.name
            res[bed.id] = name
        return res

    def search_rec_name(self, name, clause):
        return [('name',) + clause[1:]]

HospitalBed()
