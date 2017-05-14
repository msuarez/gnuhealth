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
import pytz
from dateutil.relativedelta import relativedelta
from trytond.model import ModelView, ModelSingleton, ModelSQL, fields
from datetime import datetime
from trytond.transaction import Transaction
from trytond import backend
from trytond.pool import Pool
from trytond.pyson import Eval, Not, Bool, PYSONEncoder, Equal, And, Or

__all__ = ['SurgerySequences', 'RCRI', 'Surgery', 'Operation',
    'SurgeryMainProcedure','SurgerySupply', 'PatientData', 'SurgeryTeam']



class SurgerySequences(ModelSingleton, ModelSQL, ModelView):
    "Inpatient Registration Sequences for GNU Health"
    __name__ = "gnuhealth.sequences"

    surgery_code_sequence = fields.Property(fields.Many2One(
        'ir.sequence', 'Surgery Sequence', required=True,
        domain=[('code', '=', 'gnuhealth.surgery')]))


class RCRI(ModelSQL, ModelView):
    'Revised Cardiac Risk Index'
    __name__ = 'gnuhealth.rcri'

    patient = fields.Many2One('gnuhealth.patient', 'Patient ID', required=True)
    rcri_date = fields.DateTime('Date', required=True)
    health_professional = fields.Many2One(
        'gnuhealth.healthprofessional', 'Health Professional',
        help="Health professional /"
        "Cardiologist who signed the assesment RCRI")

    rcri_high_risk_surgery = fields.Boolean(
        'High Risk surgery',
        help='Includes andy suprainguinal vascular, intraperitoneal,'
        ' or intrathoracic procedures')

    rcri_ischemic_history = fields.Boolean(
        'History of ischemic heart disease',
        help="history of MI or a positive exercise test, current \
        complaint of chest pain considered to be secondary to myocardial \
        ischemia, use of nitrate therapy, or ECG with pathological \
        Q waves; do not count prior coronary revascularization procedure \
        unless one of the other criteria for ischemic heart disease is \
        present")

    rcri_congestive_history = fields.Boolean(
        'History of congestive heart disease')

    rcri_diabetes_history = fields.Boolean(
        'Preoperative Diabetes',
        help="Diabetes Mellitus requiring treatment with Insulin")

    rcri_cerebrovascular_history = fields.Boolean(
        'History of Cerebrovascular disease')

    rcri_kidney_history = fields.Boolean(
        'Preoperative Kidney disease',
        help="Preoperative serum creatinine >2.0 mg/dL (177 mol/L)")

    rcri_total = fields.Integer(
        'Score',
        help='Points 0: Class I Very Low (0.4% complications)\n'
        'Points 1: Class II Low (0.9% complications)\n'
        'Points 2: Class III Moderate (6.6% complications)\n'
        'Points 3 or more : Class IV High (>11% complications)')

    rcri_class = fields.Selection([
        (None, ''),
        ('I', 'I'),
        ('II', 'II'),
        ('III', 'III'),
        ('IV', 'IV'),
        ], 'RCRI Class', sort=False)

    @fields.depends('rcri_high_risk_surgery', 'rcri_ischemic_history',
        'rcri_congestive_history', 'rcri_diabetes_history',
        'rcri_cerebrovascular_history', 'rcri_kidney_history')
    def on_change_with_rcri_total(self):

        total = 0
        if self.rcri_high_risk_surgery:
            total = total + 1
        if self.rcri_ischemic_history:
            total = total + 1
        if self.rcri_congestive_history:
            total = total + 1
        if self.rcri_diabetes_history:
            total = total + 1
        if self.rcri_kidney_history:
            total = total + 1
        if self.rcri_cerebrovascular_history:
            total = total + 1

        return total

    @fields.depends('rcri_high_risk_surgery', 'rcri_ischemic_history',
        'rcri_congestive_history', 'rcri_diabetes_history',
        'rcri_cerebrovascular_history', 'rcri_kidney_history')
    def on_change_with_rcri_class(self):
        rcri_class = ''

        total = 0
        if self.rcri_high_risk_surgery:
            total = total + 1
        if self.rcri_ischemic_history:
            total = total + 1
        if self.rcri_congestive_history:
            total = total + 1
        if self.rcri_diabetes_history:
            total = total + 1
        if self.rcri_kidney_history:
            total = total + 1
        if self.rcri_cerebrovascular_history:
            total = total + 1

        if total == 0:
            rcri_class = 'I'
        if total == 1:
            rcri_class = 'II'
        if total == 2:
            rcri_class = 'III'
        if (total > 2):
            rcri_class = 'IV'

        return rcri_class

    @staticmethod
    def default_rcri_date():
        return datetime.now()

    @staticmethod
    def default_rcri_total():
        return 0

    @staticmethod
    def default_rcri_class():
        return 'I'

    def get_rec_name(self, name):
        res = 'Points: ' + str(self.rcri_total) + ' (Class ' + \
            str(self.rcri_class) + ')'
        return res


class Surgery(ModelSQL, ModelView):
    'Surgery'
    __name__ = 'gnuhealth.surgery'


    def surgery_duration(self, name):

        if (self.surgery_end_date and self.surgery_date):
            return self.surgery_end_date - self.surgery_date
        else:
            return None

    def patient_age_at_surgery(self, name):
        if (self.patient.name.dob and self.surgery_date):
            rdelta = relativedelta (self.surgery_date.date(),
                self.patient.name.dob)
            years_months_days = str(rdelta.years) + 'y ' \
                + str(rdelta.months) + 'm ' \
                + str(rdelta.days) + 'd'
            return years_months_days
        else:
            return None

    patient = fields.Many2One('gnuhealth.patient', 'Patient', required=True)
    admission = fields.Many2One('gnuhealth.appointment', 'Admission')
    operating_room = fields.Many2One('gnuhealth.hospital.or', 'Operating Room')
    code = fields.Char('Code', readonly=True, help="Health Center code / sequence")

    procedures = fields.One2Many(
        'gnuhealth.operation', 'name', 'Procedures',
        help="List of the procedures in the surgery. Please enter the first "
        "one as the main procedure")

    supplies = fields.One2Many(
        'gnuhealth.surgery_supply', 'name', 'Supplies',
        help="List of the supplies required for the surgery")

    pathology = fields.Many2One(
        'gnuhealth.pathology', 'Condition',
        help="Base Condition / Reason")

    classification = fields.Selection([
        (None, ''),
        ('o', 'Optional'),
        ('r', 'Required'),
        ('u', 'Urgent'),
        ('e', 'Emergency'),
        ], 'Urgency', help="Urgency level for this surgery", sort=False)
    surgeon = fields.Many2One(
        'gnuhealth.healthprofessional', 'Surgeon',
        help="Surgeon who did the procedure")

    anesthetist = fields.Many2One(
        'gnuhealth.healthprofessional', 'Anesthetist',
        help="Anesthetist in charge")

    surgery_date = fields.DateTime(
        'Date', help="Start of the Surgery")

    surgery_end_date = fields.DateTime(
        'End',
        states={
            'required': Equal(Eval('state'), 'done'),
            },
        help="Automatically set when the surgery is done."
            "It is also the estimated end time when confirming the surgery.")

    surgery_length = fields.Function(
        fields.TimeDelta(
            'Duration',
            states={'invisible': And(Not(Equal(Eval('state'), 'done')),
                    Not(Equal(Eval('state'), 'signed')))},
            help="Length of the surgery"),
        'surgery_duration')

    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('signed', 'Signed'),
        ], 'State', readonly=True, sort=False)

    signed_by = fields.Many2One(
        'gnuhealth.healthprofessional', 'Signed by', readonly=True,
        states={
            'invisible': Not(Equal(Eval('state'), 'signed'))
            },

        help="Health Professional that signed this surgery document")

    # age is deprecated in GNU Health 2.0
    age = fields.Char(
        'Estimative Age',
        help="Use this field for historical purposes, \
        when no date of surgery is given")

    computed_age = fields.Function(
        fields.Char(
            'Age',
            help="Computed patient age at the moment of the surgery"),
        'patient_age_at_surgery')

    gender = fields.Function(fields.Selection([
        (None, ''),
        ('m', 'Male'),
        ('f', 'Female'),
        ('f-m','Female -> Male'),
        ('m-f','Male -> Female'),
        ], 'Gender'), 'get_patient_gender', searcher='search_patient_gender')


    description = fields.Char('Description')
    preop_mallampati = fields.Selection([
        (None, ''),
        ('Class 1', 'Class 1: Full visibility of tonsils, uvula and soft '
                    'palate'),
        ('Class 2', 'Class 2: Visibility of hard and soft palate, '
                    'upper portion of tonsils and uvula'),
        ('Class 3', 'Class 3: Soft and hard palate and base of the uvula are '
                    'visible'),
        ('Class 4', 'Class 4: Only Hard Palate visible'),
        ], 'Mallampati Score', sort=False)
    preop_bleeding_risk = fields.Boolean(
        'Risk of Massive bleeding',
        help="Patient has a risk of losing more than 500 "
        "ml in adults of over 7ml/kg in infants. If so, make sure that "
        "intravenous access and fluids are available")

    preop_oximeter = fields.Boolean(
        'Pulse Oximeter in place',
        help="Pulse oximeter is in place "
        "and functioning")

    preop_site_marking = fields.Boolean(
        'Surgical Site Marking',
        help="The surgeon has marked the surgical incision")

    preop_antibiotics = fields.Boolean(
        'Antibiotic Prophylaxis',
        help="Prophylactic antibiotic treatment within the last 60 minutes")

    preop_sterility = fields.Boolean(
        'Sterility confirmed',
        help="Nursing team has confirmed sterility of the devices and room")

    preop_asa = fields.Selection([
        (None, ''),
        ('ps1', 'PS 1 : Normal healthy patient'),
        ('ps2', 'PS 2 : Patients with mild systemic disease'),
        ('ps3', 'PS 3 : Patients with severe systemic disease'),
        ('ps4', 'PS 4 : Patients with severe systemic disease that is'
            ' a constant threat to life '),
        ('ps5', 'PS 5 : Moribund patients who are not expected to'
            ' survive without the operation'),
        ('ps6', 'PS 6 : A declared brain-dead patient who organs are'
            ' being removed for donor purposes'),
        ], 'ASA PS',
        help="ASA pre-operative Physical Status", sort=False)

    preop_rcri = fields.Many2One(
        'gnuhealth.rcri', 'RCRI',
        help='Patient Revised Cardiac Risk Index\n'
        'Points 0: Class I Very Low (0.4% complications)\n'
        'Points 1: Class II Low (0.9% complications)\n'
        'Points 2: Class III Moderate (6.6% complications)\n'
        'Points 3 or more : Class IV High (>11% complications)')

    surgical_wound = fields.Selection([
        (None, ''),
        ('I', 'Clean . Class I'),
        ('II', 'Clean-Contaminated . Class II'),
        ('III', 'Contaminated . Class III'),
        ('IV', 'Dirty-Infected . Class IV'),
        ], 'Surgical wound', sort=False)


    extra_info = fields.Text('Extra Info')

    anesthesia_report = fields.Text('Anesthesia Report')

    institution = fields.Many2One('gnuhealth.institution', 'Institution')

    report_surgery_date = fields.Function(fields.Date('Surgery Date'), 
        'get_report_surgery_date')
    report_surgery_time = fields.Function(fields.Time('Surgery Time'), 
        'get_report_surgery_time')

    surgery_team = fields.One2Many(
        'gnuhealth.surgery_team', 'name', 'Team Members',
        help="Professionals Involved in the surgery")

    postoperative_dx = fields.Many2One(
        'gnuhealth.pathology', 'Post-op dx',
        states={'invisible': And(Not(Equal(Eval('state'), 'done')),
                    Not(Equal(Eval('state'), 'signed')))},
        help="Post-operative diagnosis")

    @staticmethod
    def default_institution():
        HealthInst = Pool().get('gnuhealth.institution')
        institution = HealthInst.get_institution()
        return institution

    @staticmethod
    def default_surgery_date():
        return datetime.now()

    @staticmethod
    def default_surgeon():
        pool = Pool()
        HealthProf= pool.get('gnuhealth.healthprofessional')
        surgeon = HealthProf.get_health_professional()
        return surgeon

    @staticmethod
    def default_state():
        return 'draft'

    def get_patient_gender(self, name):
        return self.patient.gender

    @classmethod
    def search_patient_gender(cls, name, clause):
        res = []
        value = clause[2]
        res.append(('patient.name.gender', clause[1], value))
        return res


    # Show the gender and age upon entering the patient 
    # These two are function fields (don't exist at DB level)
    @fields.depends('patient')
    def on_change_patient(self):
        gender=None
        age=''
        self.gender = self.patient.gender
        self.computed_age = self.patient.age


    @classmethod
    def create(cls, vlist):
        Sequence = Pool().get('ir.sequence')
        Config = Pool().get('gnuhealth.sequences')

        vlist = [x.copy() for x in vlist]
        for values in vlist:
            if not values.get('code'):
                config = Config(1)
                values['code'] = Sequence.get_id(
                    config.surgery_code_sequence.id)
        return super(Surgery, cls).create(vlist)


    @classmethod
    def __setup__(cls):
        super(Surgery, cls).__setup__()
        cls._error_messages.update({
            'end_date_before_start': 'End time "%(end_date)s" BEFORE '
                'surgery date "%(surgery_date)s"',
            'or_is_not_available': 'Operating Room is not available'})

        cls._buttons.update({
            'confirmed': {
                'invisible': And(Not(Equal(Eval('state'), 'draft')),
                    Not(Equal(Eval('state'), 'cancelled'))),
                },
            'cancel': {
                'invisible': Not(Equal(Eval('state'), 'confirmed')),
                },
            'start': {
                'invisible': Not(Equal(Eval('state'), 'confirmed')),
                },
            'done': {
                'invisible': Not(Equal(Eval('state'), 'in_progress')),
                },
            'signsurgery': {
                'invisible': Not(Equal(Eval('state'), 'done')),
                },

            })
        
    @classmethod
    def validate(cls, surgeries):
        super(Surgery, cls).validate(surgeries)
        for surgery in surgeries:
            surgery.validate_surgery_period()

    def validate_surgery_period(self):
        Lang = Pool().get('ir.lang')

        language, = Lang.search([
            ('code', '=', Transaction().language),
            ])
        if (self.surgery_end_date and self.surgery_date):
            if (self.surgery_end_date < self.surgery_date):
                self.raise_user_error('end_date_before_start', {
                        'surgery_date': Lang.strftime(self.surgery_date,
                            language.code,
                            language.date),
                        'end_date': Lang.strftime(self.surgery_end_date,
                            language.code,
                            language.date),
                        })


    @classmethod
    def write(cls, surgeries, vals):
        # Don't allow to write the record if the surgery has been signed
        if surgeries[0].state == 'signed':
            cls.raise_user_error(
                "This surgery is at state Done and has been signed\n"
                "You can no longer modify it.")
        return super(Surgery, cls).write(surgeries, vals)

    ## Method to check for availability and make the Operating Room reservation
     # for the associated surgery
     
    @classmethod
    @ModelView.button
    def confirmed(cls, surgeries):
        surgery_id = surgeries[0]
        Operating_room = Pool().get('gnuhealth.hospital.or')
        cursor = Transaction().connection.cursor()

        # Operating Room and end surgery time check
        if (not surgery_id.operating_room or not surgery_id.surgery_end_date):
            cls.raise_user_error("Operating Room and estimated end time  "
            "are needed in order to confirm the surgery")

        or_id = surgery_id.operating_room.id
        cursor.execute("SELECT COUNT(*) \
            FROM gnuhealth_surgery \
            WHERE (surgery_date::timestamp,surgery_end_date::timestamp) \
                OVERLAPS (timestamp %s, timestamp %s) \
              AND (state = %s or state = %s) \
              AND operating_room = CAST(%s AS INTEGER) ",
            (surgery_id.surgery_date,
            surgery_id.surgery_end_date,
            'confirmed', 'in_progress', str(or_id)))
        res = cursor.fetchone()
        if (surgery_id.surgery_end_date <
            surgery_id.surgery_date):
            cls.raise_user_error("The Surgery end date must later than the \
                Start")
        if res[0] > 0:
            cls.raise_user_error('or_is_not_available')
        else:
            cls.write(surgeries, {'state': 'confirmed'})
 
    # Cancel the surgery and set it to draft state
    # Free the related Operating Room
    
    @classmethod
    @ModelView.button
    def cancel(cls, surgeries):
        surgery_id = surgeries[0]
        Operating_room = Pool().get('gnuhealth.hospital.or')
        
        cls.write(surgeries, {'state': 'cancelled'})

    # Start the surgery
    
    @classmethod
    @ModelView.button
    def start(cls, surgeries):
        surgery_id = surgeries[0]
        Operating_room = Pool().get('gnuhealth.hospital.or')

        cls.write(surgeries, 
            {'state': 'in_progress',
             'surgery_date': datetime.now(),
             'surgery_end_date': datetime.now()})
        Operating_room.write([surgery_id.operating_room], {'state': 'occupied'})


    # Finnish the surgery
    # Free the related Operating Room
    
    @classmethod
    @ModelView.button
    def done(cls, surgeries):
        surgery_id = surgeries[0]
        Operating_room = Pool().get('gnuhealth.hospital.or')
        
        cls.write(surgeries, {'state': 'done',
                              'surgery_end_date': datetime.now()})
                              
        Operating_room.write([surgery_id.operating_room], {'state': 'free'})


    # Sign the surgery document, and the surgical act.

    @classmethod
    @ModelView.button
    def signsurgery(cls, surgeries):
        surgery_id = surgeries[0]

        # Sign, change the state of the Surgery to "Signed"
        # and write the name of the signing health professional

        signing_hp = Pool().get('gnuhealth.healthprofessional').get_health_professional()
        if not signing_hp:
            cls.raise_user_error(
                "No health professional associated to this user !")

        cls.write(surgeries, {
            'state': 'signed',
            'signed_by': signing_hp})

    def get_report_surgery_date(self, name):
        Company = Pool().get('company.company')

        timezone = None
        company_id = Transaction().context.get('company')
        if company_id:
            company = Company(company_id)
            if company.timezone:
                timezone = pytz.timezone(company.timezone)

        dt = self.surgery_date
        return datetime.astimezone(dt.replace(tzinfo=pytz.utc), timezone).date()

    def get_report_surgery_time(self, name):
        Company = Pool().get('company.company')

        timezone = None
        company_id = Transaction().context.get('company')
        if company_id:
            company = Company(company_id)
            if company.timezone:
                timezone = pytz.timezone(company.timezone)

        dt = self.surgery_date
        return datetime.astimezone(dt.replace(tzinfo=pytz.utc), timezone).time()




class Operation(ModelSQL, ModelView):
    'Operation - Surgical Procedures'
    __name__ = 'gnuhealth.operation'

    name = fields.Many2One('gnuhealth.surgery', 'Surgery')
    procedure = fields.Many2One(
        'gnuhealth.procedure', 'Code', required=True, select=True,
        help="Procedure Code, for example ICD-10-PCS or ICPM")
    notes = fields.Text('Notes')

    def get_rec_name(self, name):
        return self.procedure.rec_name


class SurgeryMainProcedure(ModelSQL, ModelView):
    __name__ = 'gnuhealth.surgery'

    main_procedure = fields.Many2One('gnuhealth.operation','Main Proc',
        domain=[('name', '=', Eval('active_id'))],
        states={'readonly': Or(~Eval('procedures'), Eval('id', 0) < 0)},
        depends=['procedures'])

class SurgerySupply(ModelSQL, ModelView):
    'Supplies related to the surgery'
    __name__ = 'gnuhealth.surgery_supply'

    name = fields.Many2One('gnuhealth.surgery', 'Surgery')
    qty = fields.Numeric('Qty',required=True,
        help="Initial required quantity")
    supply = fields.Many2One(
        'product.product', 'Supply', required=True,
        domain=[('is_medical_supply', '=', True)],
        help="Supply to be used in this surgery")
   
    notes = fields.Char('Notes')
    qty_used = fields.Numeric('Used', required=True,
        help="Actual amount used")
    
class SurgeryTeam(ModelSQL, ModelView):
    'Team Involved in the surgery'
    __name__ = 'gnuhealth.surgery_team'

    name = fields.Many2One('gnuhealth.surgery', 'Surgery')
    team_member = fields.Many2One(
        'gnuhealth.healthprofessional', 'Member', required=True, select=True,
        help="Health professional that participated on this surgery")

    role = fields.Many2One(
        'gnuhealth.hp_specialty', 'Role',
        domain=[('name', '=', Eval('team_member'))],
        depends=['team_member'])
    
    notes = fields.Char('Notes')

class PatientData(ModelSQL, ModelView):
    __name__ = 'gnuhealth.patient'

    surgery = fields.One2Many(
        'gnuhealth.surgery', 'patient', 'Surgeries', readonly=True)
