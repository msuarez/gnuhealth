# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2008-2017 Luis Falcon <lfalcon@gnusolidario.org>
#    Copyright (C) 2011-2017 GNU Solidario <health@gnusolidario.org>
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
from datetime import datetime
from trytond.model import ModelView, ModelSingleton, ModelSQL, fields, Unique
from trytond.transaction import Transaction
from trytond.tools import grouped_slice, reduce_ids
from sql import Literal, Table
from trytond.pool import Pool
from trytond.pyson import Eval, Not, Bool, And, Equal, Or
from trytond import backend
import pytz


__all__ = ['InpatientSequences', 'DietTherapeutic','InpatientRegistration', 
    'BedTransfer', 'Appointment', 'PatientEvaluation', 'PatientData',
    'InpatientMedication', 'InpatientMedicationAdminTimes',
    'InpatientMedicationLog', 'InpatientDiet', 'InpatientMeal',
    'InpatientMealOrder','InpatientMealOrderItem', 'ECG']


class InpatientSequences(ModelSingleton, ModelSQL, ModelView):
    "Inpatient Registration Sequences for GNU Health"
    __name__ = "gnuhealth.sequences"

    inpatient_registration_sequence = fields.Property(fields.Many2One(
        'ir.sequence', 'Inpatient Sequence', required=True,
        domain=[('code', '=', 'gnuhealth.inpatient.registration')]))

    inpatient_meal_order_sequence = fields.Property(fields.Many2One(
        'ir.sequence', 'Inpatient Meal Sequence', required=True,
        domain=[('code', '=', 'gnuhealth.inpatient.meal.order')]))


# Therapeutic Diet types

class DietTherapeutic (ModelSQL, ModelView):
    'Diet Therapy'
    __name__="gnuhealth.diet.therapeutic"

    name = fields.Char('Diet type', required=True, translate=True)
    code = fields.Char('Code', required=True)
    description = fields.Text('Indications', required=True, translate=True)

    @classmethod
    def __setup__(cls):
        super(DietTherapeutic, cls).__setup__()

        t = cls.__table__()
        cls._sql_constraints = [
            ('code_unique', Unique(t,t.code),
                'The Diet code already exists'),
            ]


class InpatientRegistration(ModelSQL, ModelView):
    'Patient admission History'
    __name__ = 'gnuhealth.inpatient.registration'

    STATES = {'readonly': Or(Eval('state') == 'done',
        Eval('state') == 'finished')}
    
    name = fields.Char('Registration Code', readonly=True, select=True)
    patient = fields.Many2One('gnuhealth.patient', 'Patient',
     required=True, select=True, states = STATES)
    admission_type = fields.Selection([
        (None, ''),
        ('routine', 'Routine'),
        ('maternity', 'Maternity'),
        ('elective', 'Elective'),
        ('urgent', 'Urgent'),
        ('emergency', 'Emergency'),
        ], 'Admission type', required=True, select=True, states = STATES)
    hospitalization_date = fields.DateTime('Hospitalization date',
        required=True, select=True, states = STATES)
    discharge_date = fields.DateTime('Expected Discharge Date', required=True,
        states = STATES)
    attending_physician = fields.Many2One('gnuhealth.healthprofessional',
        'Attending Physician',  states = STATES)
    operating_physician = fields.Many2One('gnuhealth.healthprofessional',
        'Operating Physician',  states = STATES)
    admission_reason = fields.Many2One('gnuhealth.pathology',
        'Reason for Admission', help="Reason for Admission",  states = STATES,
        select=True)
    bed = fields.Many2One('gnuhealth.hospital.bed', 'Hospital Bed',
        states={
            'required': Not(Bool(Eval('name'))),
            'readonly': Or(Eval('state') == 'done',
                            Eval('state') == 'finished', 
                            Bool(Eval('name')),
                        )
            },
        depends=['name'])
    nursing_plan = fields.Text('Nursing Plan', states = STATES)
    medications = fields.One2Many('gnuhealth.inpatient.medication', 'name',
        'Medications', states = STATES)
    therapeutic_diets = fields.One2Many('gnuhealth.inpatient.diet', 'name',
        'Meals / Diet Program', states = STATES)
        
    nutrition_notes = fields.Text('Nutrition notes / directions', states = STATES)
    discharge_plan = fields.Text('Discharge Plan', states = STATES)
    info = fields.Text('Notes',states = STATES)
    state = fields.Selection((
        (None, ''),
        ('free', 'free'),
        ('cancelled', 'cancelled'),
        ('confirmed', 'confirmed'),
        ('hospitalized', 'hospitalized'),
        ('done','Discharged - needs cleaning'),
        ('finished','Finished'),
        ), 'Status', select=True, readonly=True)
        
    bed_transfers = fields.One2Many('gnuhealth.bed.transfer', 'name',
        'Transfer History', readonly=True)

    discharged_by = fields.Many2One(
        'gnuhealth.healthprofessional', 'Discharged by', readonly=True,
        help="Health Professional that discharged the patient")

    discharge_reason = fields.Selection([
        (None, ''),
        ('home','Home / Selfcare'),
        ('transfer','Transferred to another institution'),
        ('death','Death'),
        ('against_advice','Left against medical advice')],
        'Discharge Reason', 
        states={'readonly': Not(Equal(Eval('state'), 'hospitalized')),},
        help="Reason for patient discharge")

    discharge_dx = fields.Many2One('gnuhealth.pathology',
        'Discharge Dx', help="Code for Discharge Diagnosis",
        states={'readonly': Not(Equal(Eval('state'), 'hospitalized')),})
  
    institution = fields.Many2One('gnuhealth.institution', 'Institution',
        readonly=True)

    puid = fields.Function(
        fields.Char('PUID', help="Person Unique Identifier"),
        'get_patient_puid', searcher="search_patient_puid")



    @staticmethod
    def default_institution():
        HealthInst = Pool().get('gnuhealth.institution')
        institution = HealthInst.get_institution()
        return institution

    def get_patient_puid(self, name):
        return self.patient.name.ref

    @classmethod
    def search_patient_puid(cls, name, clause):
        res = []
        value = clause[2]
        res.append(('patient.name.ref', clause[1], value))
        return res

    @classmethod
    def __setup__(cls):
        super(InpatientRegistration, cls).__setup__()
        t = cls.__table__()
        cls._sql_constraints = [
            ('name_unique', Unique(t,t.name),
                'The Registration code already exists'),
            ]

        cls._error_messages.update({
                'bed_is_not_available': 'Bed is not available',
                'discharge_reason_needed': 'Admission and Discharge reasons \n'
                'as well as Discharge Dx are needed',
                'destination_bed_unavailable': 'Destination bed unavailable',
                'need_timezone':'You need to set up the company timezone'})
        cls._buttons.update({
                'confirmed': {
                    'invisible': And(Not(Equal(Eval('state'), 'free')),
                        Not(Equal(Eval('state'), 'cancelled'))),
                    },
                'cancel': {
                    'invisible': Not(Equal(Eval('state'), 'confirmed')),
                    },
                'admission': {
                    'invisible': Not(Equal(Eval('state'), 'confirmed')),
                    },
                'discharge': {
                    'invisible': Not(Equal(Eval('state'), 'hospitalized')),
                    },
                'bedclean': {
                    'invisible': Not(Equal(Eval('state'), 'done')),
                    },
                })

    ## Method to check for availability and make the hospital bed reservation
    # Checks that there are not overlapping dates and status of the bed / room
    # is not confirmed, hospitalized or done but requiring cleaning ('done')
    @classmethod
    @ModelView.button
    def confirmed(cls, registrations):
        registration_id = registrations[0]
        Bed = Pool().get('gnuhealth.hospital.bed')
        cursor = Transaction().connection.cursor()
        bed_id = registration_id.bed.id
        cursor.execute("SELECT COUNT(*) \
            FROM gnuhealth_inpatient_registration \
            WHERE (hospitalization_date::timestamp,discharge_date::timestamp) \
                OVERLAPS (timestamp %s, timestamp %s) \
              AND (state = %s or state = %s or state = %s) \
              AND bed = CAST(%s AS INTEGER) ",
            (registration_id.hospitalization_date,
            registration_id.discharge_date,
            'confirmed', 'hospitalized', 'done', str(bed_id)))
        res = cursor.fetchone()
        if (registration_id.discharge_date.date() <
            registration_id.hospitalization_date.date()):
            cls.raise_user_error("The Discharge date must later than the " \
                "Admission")
        if res[0] > 0:
            cls.raise_user_error('bed_is_not_available')
        else:
            cls.write(registrations, {'state': 'confirmed'})
            Bed.write([registration_id.bed], {'state': 'reserved'})

    @classmethod
    @ModelView.button
    def discharge(cls, registrations):
        registration_id = registrations[0]
        Bed = Pool().get('gnuhealth.hospital.bed')

        signing_hp = Pool().get('gnuhealth.healthprofessional').get_health_professional()
        if not signing_hp:
            cls.raise_user_error(
                "No health professional associated to this user !")

        cls.write(registrations, {'state': 'done',
            'discharged_by': signing_hp})

        Bed.write([registration_id.bed], {'state': 'to_clean'})

    @classmethod
    @ModelView.button
    def bedclean(cls, registrations):
        registration_id = registrations[0]
        Bed = Pool().get('gnuhealth.hospital.bed')

        cls.write(registrations, {'state': 'finished'})

        Bed.write([registration_id.bed], {'state': 'free'})

    @classmethod
    @ModelView.button
    def cancel(cls, registrations):
        registration_id = registrations[0]
        Bed = Pool().get('gnuhealth.hospital.bed')

        cls.write(registrations, {'state': 'cancelled'})
        Bed.write([registration_id.bed], {'state': 'free'})

    @classmethod
    @ModelView.button
    def admission(cls, registrations):
        registration_id = registrations[0]
        Bed = Pool().get('gnuhealth.hospital.bed')

        Company = Pool().get('company.company')

        timezone = None
        company_id = Transaction().context.get('company')
        if company_id:
            company = Company(company_id)
            if company.timezone:
                timezone = pytz.timezone(company.timezone)
                
                dt = datetime.today()
                dt_local = datetime.astimezone(dt.replace(tzinfo=pytz.utc),
                 timezone)        

                if (registration_id.hospitalization_date.date() !=
                    dt_local.date()):
                    cls.raise_user_error("The Admission date must be today")
                else:
                    cls.write(registrations, {'state': 'hospitalized'})
                    Bed.write([registration_id.bed], {'state': 'occupied'})

            else:
               cls.raise_user_error('need_timezone')

    @classmethod
    def create(cls, vlist):
        Sequence = Pool().get('ir.sequence')
        Config = Pool().get('gnuhealth.sequences')

        vlist = [x.copy() for x in vlist]
        for values in vlist:
            if not values.get('name'):
                config = Config(1)
                values['name'] = Sequence.get_id(
                    config.inpatient_registration_sequence.id)
        return super(InpatientRegistration, cls).create(vlist)

    @staticmethod
    def default_state():
        return 'free'

    @classmethod
    def validate(cls, registrations):
        super(InpatientRegistration, cls).validate(registrations)
        for registration in registrations:
            registration.check_discharge_context()


    def check_discharge_context(self):
        if ((not self.discharge_reason or not self.discharge_dx
            or not self.admission_reason)
            and self.state == 'done'):
                self.raise_user_error('discharge_reason_needed')

    
    # Format Registration ID : Patient : Bed
    def get_rec_name(self, name):
        if self.patient:
            return self.name + ':' + self.bed.rec_name + ':' \
                + self.patient.rec_name 
                
        else:
            return self.name

    # Allow searching by the hospitalization code, patient name
    # or bed number 

    @classmethod
    def search_rec_name(cls, name, clause):
        field = None
        # Search by Registration Code ID or Patient
        for field in ('name', 'patient', 'bed'):
            registrations = cls.search([(field,) + tuple(clause[1:])], limit=1)
            if registrations:
                break
        if registrations:
            return [(field,) + tuple(clause[1:])]
        return [(cls._rec_name,) + tuple(clause[1:])]



        
class BedTransfer(ModelSQL, ModelView):
    'Bed transfers'
    __name__ = 'gnuhealth.bed.transfer'

    name = fields.Many2One('gnuhealth.inpatient.registration',
        'Registration Code')
    transfer_date = fields.DateTime('Date')
    bed_from = fields.Many2One('gnuhealth.hospital.bed', 'From',
        )
    bed_to = fields.Many2One('gnuhealth.hospital.bed', 'To',
        )
    reason = fields.Char('Reason')


class Appointment(ModelSQL, ModelView):
    __name__ = 'gnuhealth.appointment'

    inpatient_registration_code = fields.Many2One(
        'gnuhealth.inpatient.registration', 'Inpatient Registration',
        help="Enter the patient hospitalization code")

class PatientEvaluation(ModelSQL, ModelView):
    __name__ = 'gnuhealth.patient.evaluation'

    inpatient_registration_code = fields.Many2One(
        'gnuhealth.inpatient.registration', 'IPC',
        help="Enter the patient hospitalization code")

class ECG(ModelSQL, ModelView):
    __name__ = 'gnuhealth.patient.ecg'

    inpatient_registration_code = fields.Many2One(
        'gnuhealth.inpatient.registration', 'Inpatient Registration',
        help="Enter the patient hospitalization code")


class PatientData(ModelSQL, ModelView):
    'Inherit patient model and add the patient status to the patient.'
    __name__ = 'gnuhealth.patient'

    patient_status = fields.Function(fields.Boolean('Hospitalized',
        help="Show the hospitalization status of the patient"),
        getter='get_patient_status', searcher='search_patient_status')

    @classmethod
    def get_patient_status(cls, patients, name):
        cursor = Transaction().connection.cursor()
        pool = Pool()
        Registration = pool.get('gnuhealth.inpatient.registration')
        registration = Registration.__table__()

        # Will store statuses {patient: True/False, ...}
        ids = list(map(int, patients))
        result = dict.fromkeys(ids, False)

        for sub_ids in grouped_slice(ids):
            # SQL expression for relevant patient ids
            clause_ids = reduce_ids(registration.id, sub_ids)

            # Hospitalized patient ids
            query = registration.select(registration.patient, Literal(True),
                where=(registration.state == 'hospitalized') & clause_ids,
                group_by=registration.patient)

            # Update dictionary of patient ids with True statuses
            cursor.execute(*query)
            result.update(cursor.fetchall())

        return result

    @classmethod
    def search_patient_status(cls, name, clause):
        p = Pool().get('gnuhealth.inpatient.registration')
        table = p.__table__()
        pat = cls.__table__()
        _, operator, value = clause

        # Validate operator and value
        if operator not in ['=', '!=']:
            raise ValueError('Wrong operator: %s' % operator)
        if value is not True and value is not False:
            raise ValueError('Wrong value: %s' % value)

        # Find hospitalized patient ids
        j = pat.join(table, condition = pat.id == table.patient)
        s = j.select(pat.id, where = table.state == 'hospitalized')

        # Choose domain operator
        if (operator == '=' and value) or (operator == '!=' and not value):
            d = 'in'
        else:
            d = 'not in'

        return [('id', d, s)]

class InpatientMedication (ModelSQL, ModelView):
    'Inpatient Medication'
    __name__ = 'gnuhealth.inpatient.medication'

    name = fields.Many2One('gnuhealth.inpatient.registration',
        'Registration Code')
    medicament = fields.Many2One('gnuhealth.medicament', 'Medicament',
        required=True, help='Prescribed Medicament')
    indication = fields.Many2One('gnuhealth.pathology', 'Indication',
        help='Choose a disease for this medicament from the disease list. It'
        ' can be an existing disease of the patient or a prophylactic.')
    start_treatment = fields.DateTime('Start',
        help='Date of start of Treatment', required=True)
    end_treatment = fields.DateTime('End', help='Date of start of Treatment')
    dose = fields.Float('Dose',
        help='Amount of medication (eg, 250 mg) per dose', required=True)
    dose_unit = fields.Many2One('gnuhealth.dose.unit', 'dose unit',
        required=True, help='Unit of measure for the medication to be taken')
    route = fields.Many2One('gnuhealth.drug.route', 'Administration Route',
        required=True, help='Drug administration route code.')
    form = fields.Many2One('gnuhealth.drug.form', 'Form', required=True,
        help='Drug form, such as tablet or gel')
    qty = fields.Integer('x', required=True,
        help='Quantity of units (eg, 2 capsules) of the medicament')
    common_dosage = fields.Many2One('gnuhealth.medication.dosage', 'Frequency',
        help='Common / standard dosage frequency for this medicament')
    admin_times = fields.One2Many('gnuhealth.inpatient.medication.admin_time',
        'name', "Admin times")
    log_history = fields.One2Many('gnuhealth.inpatient.medication.log', 'name',
        "Log History")
    frequency = fields.Integer('Frequency',
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
    frequency_prn = fields.Boolean('PRN',
        help='Use it as needed, pro re nata')
    is_active = fields.Boolean('Active',
        help='Check if the patient is currently taking the medication')
    discontinued = fields.Boolean('Discontinued')
    course_completed = fields.Boolean('Course Completed')
    discontinued_reason = fields.Char('Reason for discontinuation',
        states={
            'invisible': Not(Bool(Eval('discontinued'))),
            'required': Bool(Eval('discontinued')),
            },
        depends=['discontinued'],
        help='Short description for discontinuing the treatment')
    adverse_reaction = fields.Text('Adverse Reactions',
        help='Side effects or adverse reactions that the patient experienced')

    @fields.depends('discontinued', 'course_completed')
    def on_change_with_is_active(self):
        is_active = True
        if (self.discontinued or self.course_completed):
            is_active = False
        return is_active

    @fields.depends('is_active', 'course_completed')
    def on_change_with_discontinued(self):
        return not (self.is_active or self.course_completed)

    @fields.depends('is_active', 'discontinued')
    def on_change_with_course_completed(self):
        return not (self.is_active or self.discontinued)

    @staticmethod
    def default_is_active():
        return True


class InpatientMedicationAdminTimes (ModelSQL, ModelView):
    'Inpatient Medication Admin Times'
    __name__="gnuhealth.inpatient.medication.admin_time"

    name = fields.Many2One('gnuhealth.inpatient.medication', 'Medication')
    admin_time = fields.Time("Time")
    dose = fields.Float('Dose',
        help='Amount of medication (eg, 250 mg) per dose')
    dose_unit = fields.Many2One('gnuhealth.dose.unit', 'dose unit',
        help='Unit of measure for the medication to be taken')
    remarks = fields.Text('Remarks',
        help='specific remarks for this dose')


class InpatientMedicationLog (ModelSQL, ModelView):
    'Inpatient Medication Log History'
    __name__="gnuhealth.inpatient.medication.log"

    name = fields.Many2One('gnuhealth.inpatient.medication', 'Medication')
    admin_time = fields.DateTime("Date", readonly=True)
    health_professional = fields.Many2One('gnuhealth.healthprofessional',
        'Health Professional', readonly=True)
    dose = fields.Float('Dose',
        help='Amount of medication (eg, 250 mg) per dose')
    dose_unit = fields.Many2One('gnuhealth.dose.unit', 'dose unit',
        help='Unit of measure for the medication to be taken')
    remarks = fields.Text('Remarks',
        help='specific remarks for this dose')

    @classmethod
    def __setup__(cls):
        super(InpatientMedicationLog, cls).__setup__()
        cls._error_messages.update({
            'health_professional_warning':
                    'No health professional associated to this user',
        })

    @classmethod
    def validate(cls, records):
        super(InpatientMedicationLog, cls).validate(records)
        for record in records:
            record.check_health_professional()

    def check_health_professional(self):
        if not self.health_professional:
            self.raise_user_error('health_professional_warning')

    @staticmethod
    def default_health_professional():
        pool = Pool()
        return pool.get('gnuhealth.healthprofessional').get_health_professional()

    @staticmethod
    def default_admin_time():
        return datetime.now()


class InpatientDiet (ModelSQL, ModelView):
    'Inpatient Diet'
    __name__="gnuhealth.inpatient.diet"

    name = fields.Many2One('gnuhealth.inpatient.registration',
        'Registration Code')
    diet = fields.Many2One('gnuhealth.diet.therapeutic', 'Diet', required=True)
    remarks = fields.Text('Remarks / Directions',
        help='specific remarks for this diet / patient')

class InpatientMeal (ModelSQL, ModelView):
    'Inpatient Meal'
    __name__="gnuhealth.inpatient.meal"

    name = fields.Many2One(
        'product.product', 'Food', required=True,
        help='Food')

    diet_therapeutic = fields.Many2One('gnuhealth.diet.therapeutic',
        'Diet')

    diet_belief = fields.Many2One('gnuhealth.diet.belief',
        'Belief')

    diet_vegetarian = fields.Many2One('gnuhealth.vegetarian_types',
        'Vegetarian')

    institution = fields.Many2One('gnuhealth.institution', 'Institution')

    @staticmethod
    def default_institution():
        HealthInst = Pool().get('gnuhealth.institution')
        institution = HealthInst.get_institution()
        return institution

    def get_rec_name(self, name):
        if self.name:
            return self.name.name

class InpatientMealOrderItem (ModelSQL, ModelView):
    'Inpatient Meal Item'
    __name__="gnuhealth.inpatient.meal.order.item"

    name = fields.Many2One('gnuhealth.inpatient.meal.order',
        'Meal Order')

    meal = fields.Many2One('gnuhealth.inpatient.meal', 'Meal')

    remarks = fields.Char('Remarks')


class InpatientMealOrder (ModelSQL, ModelView):
    'Inpatient Meal Order'
    __name__="gnuhealth.inpatient.meal.order"

    name = fields.Many2One('gnuhealth.inpatient.registration',
        'Registration Code', domain=[('state', '=', 'hospitalized')],
        required=True)

    mealtime = fields.Selection((
        (None, ''),
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('snack', 'Snack'),
        ('special', 'Special order'),
        ), 'Meal time', required=True, sort=False)

    meal_item = fields.One2Many('gnuhealth.inpatient.meal.order.item', 'name',
        'Items')

    meal_order = fields.Char('Order', readonly=True)

    health_professional = fields.Many2One('gnuhealth.healthprofessional',
        'Health Professional')

    remarks = fields.Text('Remarks')

    meal_warning = fields.Boolean('Warning',
        help="The patient has special needs on meals")

    meal_warning_ack = fields.Boolean('Ack',
        help="Check if you have verified the warnings on the"
        " patient meal items")

    order_date = fields.DateTime('Date',
        help='Order date', required=True)

    state = fields.Selection((
        (None, ''),
        ('draft', 'Draft'),
        ('cancelled', 'Cancelled'),
        ('ordered', 'Ordered'),
        ('processing', 'Processing'),
        ('done','Done'),
        ), 'Status', readonly=True)

    @staticmethod
    def default_order_date():
        return datetime.now()

    @staticmethod
    def default_state():
        return 'draft'

    @staticmethod
    def default_health_professional():
        pool = Pool()
        return pool.get('gnuhealth.healthprofessional').get_health_professional()

    @classmethod
    def create(cls, vlist):
        Sequence = Pool().get('ir.sequence')
        Config = Pool().get('gnuhealth.sequences')

        vlist = [x.copy() for x in vlist]
        for values in vlist:
            if not values.get('meal_order'):
                config = Config(1)
                values['meal_order'] = Sequence.get_id(
                    config.inpatient_meal_order_sequence.id)
        return super(InpatientMealOrder, cls).create(vlist)

    @classmethod
    def validate(cls, meal_orders):
        super(InpatientMealOrder, cls).validate(meal_orders)
        for meal_order in meal_orders:
            meal_order.check_meal_order_warning()
            meal_order.check_health_professional()
            
    def check_meal_order_warning(self):
        if not self.meal_warning_ack and self.meal_warning:
            self.raise_user_error('meal_order_warning')

    def check_health_professional(self):
        if not self.health_professional:
            self.raise_user_error('health_professional_warning')


    @fields.depends('name')
    def on_change_name(self):
        if self.name:
            # Trigger the warning if the patient 
            # has special needs on meals (religion / philosophy )
            if (self.name.patient.vegetarian_type or 
                self.name.patient.diet_belief):
                self.meal_warning = True
                self.meal_warning_ack = False


    @classmethod
    def __setup__(cls):
        super(InpatientMealOrder, cls).__setup__()
        cls._buttons.update({
            'cancel': {'invisible': Not(Equal(Eval('state'), 'ordered'))}
            })

        cls._buttons.update({
            'generate': {'invisible': Or(Equal(Eval('state'), 'ordered'),
                    Equal(Eval('state'), 'done'))},
            })

        cls._buttons.update({
            'done': {'invisible': Not(Equal(Eval('state'), 'ordered'))}
            })

        cls._error_messages.update({
            'meal_order_warning':
            '===== MEAL WARNING ! =====\n\n\n'
            'This patient has special meal needs \n\n'
            'Check and acknowledge that\n'
            'the meal items in this order are correct \n\n',
            'health_professional_warning':
            'No health professional associated to this user',
            })

        t = cls.__table__()
        cls._sql_constraints = [
            ('meal_order_uniq', Unique(t,t.meal_order),
                'The Meal Order code already exists'),
            ]


    @classmethod
    @ModelView.button
    def generate(cls, mealorders):
        cls.write(mealorders, {
            'state': 'ordered'})

    @classmethod
    @ModelView.button
    def cancel(cls, mealorders):
        cls.write(mealorders, {
            'state': 'cancelled'})

    @classmethod
    @ModelView.button
    def done(cls, mealorders):
        cls.write(mealorders, {
            'state': 'done'})
