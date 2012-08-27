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


from trytond.model import ModelView, ModelSingleton, ModelSQL, fields
from trytond.transaction import Transaction
from trytond.pool import Pool
from trytond.pyson import Eval, Not, Bool, And, Equal
from datetime import datetime


class InpatientSequences(ModelSingleton, ModelSQL, ModelView):
    "Inpatient Registration Sequences for GNU Health"

    _name = "gnuhealth.sequences"

    inpatient_registration_sequence = fields.Property(fields.Many2One('ir.sequence',
        'Inpatient Sequence', domain=[('code', '=', 'gnuhealth.inpatient.registration')],
        required=True))

InpatientSequences()


# Therapeutic Diet types

class DietTherapeutic (ModelSQL, ModelView):
    'Diet Therapy'
    _name="gnuhealth.diet.therapeutic"
    _description = __doc__
    
    name = fields.Char('Diet type', required=True, translate=True)
    code = fields.Char('Code', required=True)
    description = fields.Text ('Indications', required=True , translate=True )

    def __init__(self):
        super(DietTherapeutic, self).__init__()

        self._sql_constraints = [
            ('code_uniq', 'unique(code)',
             'The Diet code already exists')]
    
DietTherapeutic()


# Diet by belief / religion

class DietBelief (ModelSQL, ModelView):
    'Diet by Belief'
    _name="gnuhealth.diet.belief"
    _description = __doc__
    
    name = fields.Char('Belief', required=True, translate=True)
    code = fields.Char('Code', required=True)
    description = fields.Text ('Description', required=True , translate=True )

    def __init__(self):
        super(DietBelief, self).__init__()

        self._sql_constraints = [
            ('code_uniq', 'unique(code)',
             'The Diet code already exists')]
    
DietBelief()

class InpatientRegistration(ModelSQL, ModelView):
    'Patient admission History'
    _name = 'gnuhealth.inpatient.registration'
    _description = __doc__

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
    attending_physician = fields.Many2One('gnuhealth.physician',
        'Attending Physician',select=True)
    operating_physician = fields.Many2One('gnuhealth.physician',
        'Operating Physician')
    admission_reason = fields.Many2One('gnuhealth.pathology',
        'Reason for Admission', help="Reason for Admission", select=True)
    bed = fields.Many2One('gnuhealth.hospital.bed', 'Hospital Bed',
     required=True, select=True)
    nursing_plan = fields.Text('Nursing Plan')
    medications = fields.One2Many('gnuhealth.inpatient.medication', 'name',
        'Medications')
    therapeutic_diets = fields.One2Many('gnuhealth.inpatient.diet', 'name',
        'Therapeutic Diets')

    diet_belief = fields.Many2One('gnuhealth.diet.belief',
        'Belief', help="Enter the patient belief or religion to choose the proper diet")

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
        ), 'Status', select=True)

# Method to check for availability and make the hospital bed reservation

    def button_registration_confirm(self, ids):
        registration_id = self.browse(ids)[0]
        bed_obj = Pool().get('gnuhealth.hospital.bed')
        cursor = Transaction().cursor
        bed_id = registration_id.bed.id
        cursor.execute("SELECT COUNT(*) \
            FROM gnuhealth_inpatient_registration \
            WHERE (hospitalization_date::timestamp,discharge_date::timestamp) \
                OVERLAPS (timestamp %s, timestamp %s) \
              AND (state = %s or state = %s) \
              AND bed = CAST(%s AS INTEGER) ",
            (registration_id.hospitalization_date, registration_id.discharge_date,
            'confirmed','hospitalized', str(bed_id)))

        res = cursor.fetchone()

        if (registration_id.discharge_date.date() < registration_id.hospitalization_date.date()):
            self.raise_user_error ("The Discharge date must later than the Admission")

        if res[0] > 0:
            self.raise_user_error('bed_is_not_available')
        else:
            self.write(ids, {'state': 'confirmed'})
            bed_obj.write(registration_id.bed.id, {'state': 'reserved'})

        return True

    def button_patient_discharge(self, ids):
        registration_id = self.browse(ids)[0]
        bed_obj = Pool().get('gnuhealth.hospital.bed')

        self.write(ids, {'state': 'free'})
        bed_obj.write(registration_id.bed.id, {'state': 'free'})
        return True

    def button_registration_cancel(self, ids):
        registration_id = self.browse(ids)[0]
        bed_obj = Pool().get('gnuhealth.hospital.bed')

        self.write(ids, {'state': 'cancelled'})
        bed_obj.write(registration_id.bed.id, {'state': 'free'})
        return True

    def button_registration_admission(self, ids):
        registration_id = self.browse(ids)[0]
        bed_obj = Pool().get('gnuhealth.hospital.bed')
        
        if ( registration_id.hospitalization_date.date() <> datetime.today().date()):
            self.raise_user_error ("The Admission date must be today")
        else:
            self.write(ids, {'state': 'hospitalized'})

            bed_obj.write(registration_id.bed.id, {'state': 'occupied'})
            
        return True

    def create(self, values):
        sequence_obj = Pool().get('ir.sequence')
        config_obj = Pool().get('gnuhealth.sequences')

        values = values.copy()
        if not values.get('name'):
            config = config_obj.browse(1)
            values['name'] = sequence_obj.get_id(
            config.inpatient_registration_sequence.id)

        return super(InpatientRegistration, self).create(values)

    def default_state(self):
        return 'free'


    def __init__(self):
        super(InpatientRegistration, self).__init__()

        self._rpc.update({
            'button_registration_confirm': True,
            'button_patient_discharge': True,
            'button_registration_cancel': True,
            'button_registration_admission': True,
        })

        self._sql_constraints = [
            ('name_uniq', 'unique(name)',
             'The Registration code already exists')
        ]

        self._error_messages.update({
                'bed_is_not_available': 'Bed is not available'})


        self._buttons.update({
                'button_registration_confirm': {
                    'invisible': And(Not(Equal(Eval('state'), 'free')), Not(Equal(Eval('state'), 'cancelled'))),
                    },
                'button_registration_cancel': {
                    'invisible': Not(Equal(Eval('state'), 'confirmed')),
                    },
                'button_patient_discharge': {
                    'invisible': Not(Equal(Eval('state'), 'hospitalized')),
                    },

                'button_registration_admission': {
                    'invisible': Not(Equal(Eval('state'), 'confirmed')),
                    },
                    
                })


InpatientRegistration()


class Appointment(ModelSQL, ModelView):
    'Add Inpatient Registration field to the Appointment model.'
    _name = 'gnuhealth.appointment'
    _description = __doc__

    inpatient_registration_code = fields.Many2One(
        'gnuhealth.inpatient.registration', 'Inpatient Registration',
        help="Enter the patient hospitalization code")

Appointment()


class PatientData(ModelSQL, ModelView):
    'Inherit patient model and add the patient status to the patient.'
    _name = 'gnuhealth.patient'
    _description = __doc__

    def get_patient_status(self, ids, name):
        cursor = Transaction().cursor

        def get_hospitalization_status(patient_dbid):
            cursor.execute('SELECT state ' \
                'FROM gnuhealth_inpatient_registration ' \
                'WHERE patient = %s ' \
                  'AND state = \'hospitalized\' ', (str(patient_dbid),))

            try:
                patient_status = str(cursor.fetchone()[0])
            except:
                patient_status = 'outpatient'

            return patient_status

        result = {}

# Get the patient (DB) id to be used in the search on the medical inpatient
# registration table lookup

        for patient_data in self.browse(ids):
            patient_dbid = patient_data.id

            if patient_dbid:
                result[patient_data.id] = \
                        get_hospitalization_status(patient_dbid)

        return result

    patient_status = fields.Function(fields.Char('Hospitalization Status'),
        'get_patient_status')

PatientData()

class InpatientMedication (ModelSQL, ModelView):
    'Inpatient Medication'
    _name = 'gnuhealth.inpatient.medication'
    _description = __doc__
    name = fields.Many2One('gnuhealth.inpatient.registration', 'Registration Code')

    medicament = fields.Many2One('gnuhealth.medicament', 'Medicament',
        required=True, help='Prescribed Medicament')
    indication = fields.Many2One('gnuhealth.pathology', 'Indication',
        help='Choose a disease for this medicament from the disease list. It'\
        ' can be an existing disease of the patient or a prophylactic.')

    start_treatment = fields.DateTime('Start',
        help='Date of start of Treatment', required=True)
    end_treatment = fields.DateTime('End', help='Date of start of Treatment')

    dose = fields.Float('Dose',
        help='Amount of medication (eg, 250 mg) per dose', required=True)
    dose_unit = fields.Many2One('gnuhealth.dose.unit', 'dose unit',required=True,
        help='Unit of measure for the medication to be taken')
    route = fields.Many2One('gnuhealth.drug.route', 'Administration Route',required=True,
        help='Drug administration route code.')
    form = fields.Many2One('gnuhealth.drug.form', 'Form',required=True,
        help='Drug form, such as tablet or gel')
    qty = fields.Integer('x',required=True,
        help='Quantity of units (eg, 2 capsules) of the medicament')
    common_dosage = fields.Many2One('gnuhealth.medication.dosage', 'Frequency',
        help='Common / standard dosage frequency for this medicament')

    admin_times = fields.One2Many ('gnuhealth.inpatient.medication.admin_time','name',"Admin times")
    log_history = fields.One2Many ('gnuhealth.inpatient.medication.log','name',"Log History")

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
        help='Short description for discontinuing the treatment')
    adverse_reaction = fields.Text('Adverse Reactions',
        help='Side effects or adverse reactions that the patient experienced')

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
        return discontinued

    def on_change_with_course_completed(self, vals):
        is_active = vals.get('is_active')
        course_completed = vals.get('discontinued')
        discontinued = vals.get('discontinued')
        if (is_active or discontinued):
            course_completed = False
        return course_completed

    def default_is_active(self):
        return True

InpatientMedication()

class InpatientMedicationAdminTimes (ModelSQL, ModelView):
    'Inpatient Medication Admin Times'
    _name="gnuhealth.inpatient.medication.admin_time"
    _description = __doc__

    
    name = fields.Many2One('gnuhealth.inpatient.medication', 'Medication')
    admin_time = fields.Time ("Time")
    dose = fields.Float('Dose',
        help='Amount of medication (eg, 250 mg) per dose')
    dose_unit = fields.Many2One('gnuhealth.dose.unit', 'dose unit',
        help='Unit of measure for the medication to be taken')

    remarks = fields.Text('Remarks',
        help='specific remarks for this dose')
    
InpatientMedicationAdminTimes()

class InpatientMedicationLog (ModelSQL, ModelView):
    'Inpatient Medication Log History'
    _name="gnuhealth.inpatient.medication.log"
    _description = __doc__

    
    name = fields.Many2One('gnuhealth.inpatient.medication', 'Medication')
    admin_time = fields.DateTime ("Date", readonly=True)
    health_professional = fields.Many2One('gnuhealth.physician', 'Health Professional', readonly=True)

    dose = fields.Float('Dose',
        help='Amount of medication (eg, 250 mg) per dose')
    dose_unit = fields.Many2One('gnuhealth.dose.unit', 'dose unit',
        help='Unit of measure for the medication to be taken')

    remarks = fields.Text('Remarks',
        help='specific remarks for this dose')

    def default_health_professional(self):
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

    def default_admin_time(self):
        return datetime.now()

InpatientMedicationLog()



class InpatientDiet (ModelSQL, ModelView):
    'Inpatient Diet'
    _name="gnuhealth.inpatient.diet"
    _description = __doc__


    name = fields.Many2One('gnuhealth.inpatient.registration', 'Registration Code')    
    diet = fields.Many2One('gnuhealth.diet.therapeutic', 'Diet', required=True)
    remarks = fields.Text('Remarks / Directions',
        help='specific remarks for this diet / patient')
    
InpatientDiet()

