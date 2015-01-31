# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2008-2015 Luis Falcon <lfalcon@gnusolidario.org>
#    Copyright (C) 2011-2015 GNU Solidario <health@gnusolidario.org>
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
from trytond.model import ModelView, ModelSingleton, ModelSQL, fields
from trytond.transaction import Transaction
from trytond.pool import Pool
from trytond.pyson import Eval, Not, Bool, And, Equal


__all__ = ['InpatientSequences', 'DietTherapeutic', 'DietBelief',
    'InpatientRegistration', 'BedTransfer', 'Appointment', 'PatientData',
    'InpatientMedication', 'InpatientMedicationAdminTimes',
    'InpatientMedicationLog', 'InpatientDiet']


class InpatientSequences(ModelSingleton, ModelSQL, ModelView):
    "Inpatient Registration Sequences for GNU Health"
    __name__ = "gnuhealth.sequences"

    inpatient_registration_sequence = fields.Property(fields.Many2One(
        'ir.sequence', 'Inpatient Sequence', required=True,
        domain=[('code', '=', 'gnuhealth.inpatient.registration')]))


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

        cls._sql_constraints = [
            ('code_uniq', 'unique(code)',
             'The Diet code already exists')]


# Diet by belief / religion

class DietBelief (ModelSQL, ModelView):
    'Diet by Belief'
    __name__="gnuhealth.diet.belief"

    name = fields.Char('Belief', required=True, translate=True)
    code = fields.Char('Code', required=True)
    description = fields.Text('Description', required=True, translate=True)

    @classmethod
    def __setup__(cls):
        super(DietBelief, cls).__setup__()

        cls._sql_constraints = [
            ('code_uniq', 'unique(code)',
             'The Diet code already exists')]


class InpatientRegistration(ModelSQL, ModelView):
    'Patient admission History'
    __name__ = 'gnuhealth.inpatient.registration'

    name = fields.Char('Registration Code', readonly=True, select=True)
    patient = fields.Many2One('gnuhealth.patient', 'Patient',
     required=True, select=True)
    admission_type = fields.Selection([
        ('routine', 'Routine'),
        ('maternity', 'Maternity'),
        ('elective', 'Elective'),
        ('urgent', 'Urgent'),
        ('emergency', 'Emergency'),
        ], 'Admission type', required=True, select=True)
    hospitalization_date = fields.DateTime('Hospitalization date',
        required=True, select=True)
    discharge_date = fields.DateTime('Expected Discharge Date', required=True,
        select=True)
    attending_physician = fields.Many2One('gnuhealth.healthprofessional',
        'Attending Physician', select=True)
    operating_physician = fields.Many2One('gnuhealth.healthprofessional',
        'Operating Physician')
    admission_reason = fields.Many2One('gnuhealth.pathology',
        'Reason for Admission', help="Reason for Admission", select=True)
    bed = fields.Many2One('gnuhealth.hospital.bed', 'Hospital Bed',
        states={
            'required': Not(Bool(Eval('name'))),
            'readonly': Bool(Eval('name')),
            },
        depends=['name'])
    nursing_plan = fields.Text('Nursing Plan')
    medications = fields.One2Many('gnuhealth.inpatient.medication', 'name',
        'Medications')
    therapeutic_diets = fields.One2Many('gnuhealth.inpatient.diet', 'name',
        'Meals / Diet Program')
    diet_belief = fields.Many2One('gnuhealth.diet.belief',
        'Belief', help="Enter the patient belief or religion to choose the \
            proper diet")
    diet_vegetarian = fields.Selection((
        ('none', 'None'),
        ('vegetarian', 'Vegetarian'),
        ('lacto', 'Lacto vegetarian'),
        ('lactoovo', 'Lacto-ovo vegetarian'),
        ('pescetarian', 'Pescetarian'),
        ('vegan', 'Vegan'),
        ), 'Vegetarian', sort=False, required=True)
    nutrition_notes = fields.Text('Nutrition notes / directions')
    discharge_plan = fields.Text('Discharge Plan')
    info = fields.Text('Extra Info')
    state = fields.Selection((
        ('free', 'free'),
        ('cancelled', 'cancelled'),
        ('confirmed', 'confirmed'),
        ('hospitalized', 'hospitalized'),
        ('done','Done'),
        ), 'Status', select=True)
        
    bed_transfers = fields.One2Many('gnuhealth.bed.transfer', 'name',
        'Transfer History', readonly=True)

    discharged_by = fields.Many2One(
        'gnuhealth.healthprofessional', 'Discharged by', readonly=True,
        states={'invisible': Not(Equal(Eval('state'), 'done'))},
        help="Health Professional that discharged the patient")

    institution = fields.Many2One('gnuhealth.institution', 'Institution')

    @staticmethod
    def default_institution():
        HealthInst = Pool().get('gnuhealth.institution')
        institution = HealthInst.get_institution()
        return institution

    @classmethod
    def __setup__(cls):
        super(InpatientRegistration, cls).__setup__()
        cls._sql_constraints = [
            ('name_uniq', 'unique(name)',
             'The Registration code already exists')
        ]
        cls._error_messages.update({
                'bed_is_not_available': 'Bed is not available',
                'destination_bed_unavailable': 'Destination bed unavailable'})
        cls._buttons.update({
                'confirmed': {
                    'invisible': And(Not(Equal(Eval('state'), 'free')),
                        Not(Equal(Eval('state'), 'cancelled'))),
                    },
                'cancel': {
                    'invisible': Not(Equal(Eval('state'), 'confirmed')),
                    },
                'discharge': {
                    'invisible': Not(Equal(Eval('state'), 'hospitalized')),
                    },
                'admission': {
                    'invisible': Not(Equal(Eval('state'), 'confirmed')),
                    },
                })

    ## Method to check for availability and make the hospital bed reservation

    @classmethod
    @ModelView.button
    def confirmed(cls, registrations):
        registration_id = registrations[0]
        Bed = Pool().get('gnuhealth.hospital.bed')
        cursor = Transaction().cursor
        bed_id = registration_id.bed.id
        cursor.execute("SELECT COUNT(*) \
            FROM gnuhealth_inpatient_registration \
            WHERE (hospitalization_date::timestamp,discharge_date::timestamp) \
                OVERLAPS (timestamp %s, timestamp %s) \
              AND (state = %s or state = %s) \
              AND bed = CAST(%s AS INTEGER) ",
            (registration_id.hospitalization_date,
            registration_id.discharge_date,
            'confirmed', 'hospitalized', str(bed_id)))
        res = cursor.fetchone()
        if (registration_id.discharge_date.date() <
            registration_id.hospitalization_date.date()):
            cls.raise_user_error("The Discharge date must later than the \
                Admission")
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

        if (registration_id.hospitalization_date.date() !=
            datetime.today().date()):
            cls.raise_user_error("The Admission date must be today")
        else:
            cls.write(registrations, {'state': 'hospitalized'})
            Bed.write([registration_id.bed], {'state': 'occupied'})

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

    @classmethod
    def write(cls, registrations, vals):
        # Don't allow to write the record if the evaluation has been done
        if registrations[0].state == 'done':
            cls.raise_user_error(
                "This hospitalization is at state Done\n"
                "You can no longer modify it.")
        return super(InpatientRegistration, cls).write(registrations, vals)

    @staticmethod
    def default_state():
        return 'free'

    # Allow searching by the hospitalization code or patient name

    def get_rec_name(self, name):
        if self.patient:
            return self.name + ': ' + self.patient.name.name + ' ' + \
             self.patient.name.lastname
        else:
            return self.name

    @classmethod
    def search_rec_name(cls, name, clause):
        field = None
        # Search by Registration Code ID or Patient
        for field in ('name', 'patient'):
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
    'Add Inpatient Registration field to the Appointment model.'
    __name__ = 'gnuhealth.appointment'

    inpatient_registration_code = fields.Many2One(
        'gnuhealth.inpatient.registration', 'Inpatient Registration',
        help="Enter the patient hospitalization code")


class PatientData(ModelSQL, ModelView):
    'Inherit patient model and add the patient status to the patient.'
    __name__ = 'gnuhealth.patient'

    patient_status = fields.Function(fields.Boolean('Hospitalized',
        help="Show the hospitalization status of the patient"),
        'get_patient_status')

    def get_patient_status(self, name):
        
        cursor = Transaction().cursor

        def get_hospitalization_status(patient_dbid):
            is_hospitalized = False

            cursor.execute('SELECT count(state) \
                FROM gnuhealth_inpatient_registration \
                WHERE patient = %s \
                AND state = \'hospitalized\' LIMIT 1' , (patient_dbid,))
            
            if cursor.fetchone()[0] > 0:
                is_hospitalized = True
            
            return is_hospitalized

        result = ''

        # Get the patient (DB) id to be used in the search on the medical
        # inpatient registration table lookup
        
        patient_dbid = self.id
        if patient_dbid:
            result = get_hospitalization_status(patient_dbid)
        return result


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
