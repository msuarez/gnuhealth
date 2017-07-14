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
from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta, date
from trytond.model import ModelView, ModelSQL, fields
from trytond.pyson import Eval, Not, Bool, PYSONEncoder, Equal, And, Or, If
from trytond.pool import Pool

from trytond import backend

__all__ = ['Party','PatientSESAssessment','GnuHealthPatient']


class Party (ModelSQL, ModelView):
    __name__ = 'party.party'

    occupation = fields.Many2One('gnuhealth.occupation', 'Occupation')

    education = fields.Selection([
        (None, ''),
        ('0', 'None'),
        ('1', 'Incomplete Primary School'),
        ('2', 'Primary School'),
        ('3', 'Incomplete Secondary School'),
        ('4', 'Secondary School'),
        ('5', 'University'),
        ], 'Education', help="Education Level", sort=False)


class PatientSESAssessment(ModelSQL, ModelView):
    'Socioeconomics and Family Functionality Assessment'
    __name__ = 'gnuhealth.ses.assessment'

    STATES = {'readonly': Eval('state') == 'done'}

    patient = fields.Many2One('gnuhealth.patient', 'Patient',
        required=True, states = STATES)
    gender = fields.Function(fields.Selection([
        (None, ''),
        ('m', 'Male'),
        ('f', 'Female'),
        ], 'Gender'), 'get_patient_gender', searcher='search_patient_gender')


    assessment_date = fields.DateTime('Date', help="Assessment date",
        states = STATES)
        
    computed_age = fields.Function(fields.Char(
            'Age',
            help="Computed patient age at the moment of the evaluation"),
            'patient_age_at_assessment')
            
    health_professional = fields.Many2One(
        'gnuhealth.healthprofessional', 'Health Professional', readonly=True,
        help="Health professional"
        )

    du = fields.Many2One(
        'gnuhealth.du', 'DU', help="Domiciliary Unit",
        states = STATES)

    ses = fields.Selection([
        (None, ''),
        ('0', 'Lower'),
        ('1', 'Lower-middle'),
        ('2', 'Middle'),
        ('3', 'Middle-upper'),
        ('4', 'Higher'),
        ], 'Socioeconomics', help="SES - Socioeconomic Status", sort=False,
            states = STATES)

    housing = fields.Selection([
        (None, ''),
        ('0', 'Shanty, deficient sanitary conditions'),
        ('1', 'Small, crowded but with good sanitary conditions'),
        ('2', 'Comfortable and good sanitary conditions'),
        ('3', 'Roomy and excellent sanitary conditions'),
        ('4', 'Luxury and excellent sanitary conditions'),
        ], 'Housing conditions',
         help="Housing and sanitary living conditions", sort=False,
            states = STATES)

    occupation = fields.Many2One('gnuhealth.occupation','Occupation',
        states = STATES)

    income = fields.Selection([
        (None, ''),
        ('l', 'Low'),
        ('m', 'Medium'),
        ('h', 'High'),
        ], 'Income', sort=False, states = STATES)


    fam_apgar_help = fields.Selection([
        (None, ''),
        ('0', 'None'),
        ('1', 'Moderately'),
        ('2', 'Very much'),
        ], 'Help from family',
        help="Is the patient satisfied with the level of help coming from " \
        "the family when there is a problem ?", sort=False,
            states = STATES)

    fam_apgar_discussion = fields.Selection([
        (None, ''),
        ('0', 'None'),
        ('1', 'Moderately'),
        ('2', 'Very much'),
        ], 'Problems discussion',
        help="Is the patient satisfied with the level talking over the " \
        "problems as family ?", sort=False, states = STATES)

    fam_apgar_decisions = fields.Selection([
        (None, ''),
        ('0', 'None'),
        ('1', 'Moderately'),
        ('2', 'Very much'),
        ], 'Decision making',
        help="Is the patient satisfied with the level of making important " \
        "decisions as a group ?", sort=False, states = STATES)

    fam_apgar_timesharing = fields.Selection([
        (None, ''),
        ('0', 'None'),
        ('1', 'Moderately'),
        ('2', 'Very much'),
        ], 'Time sharing',
        help="Is the patient satisfied with the level of time that they " \
        "spend together ?", sort=False, states = STATES)

    fam_apgar_affection = fields.Selection([
        (None, ''),
        ('0', 'None'),
        ('1', 'Moderately'),
        ('2', 'Very much'),
        ], 'Family affection',
        help="Is the patient satisfied with the level of affection coming " \
        "from the family ?", sort=False, states = STATES)

    fam_apgar_score = fields.Integer('Score',
        help="Total Family APGAR \n" \
        "7 - 10 : Functional Family \n" \
        "4 - 6  : Some level of disfunction \n" \
        "0 - 3  : Severe disfunctional family \n", states = STATES)

    education = fields.Selection([
        (None, ''),
        ('0', 'None'),
        ('1', 'Incomplete Primary School'),
        ('2', 'Primary School'),
        ('3', 'Incomplete Secondary School'),
        ('4', 'Secondary School'),
        ('5', 'University'),
        ], 'Education Level', help="Education Level", sort=False,
            states = STATES)

    notes = fields.Text('Notes', states = STATES)

    state = fields.Selection([
        (None, ''),
        ('in_progress', 'In progress'),
        ('done', 'Done'),
        ], 'State', readonly=True, sort=False)

    signed_by = fields.Many2One(
        'gnuhealth.healthprofessional', 'Signed by', readonly=True,
        states={'invisible': Equal(Eval('state'), 'in_progress')},
        help="Health Professional that finished the patient evaluation")


    @fields.depends('fam_apgar_help', 'fam_apgar_timesharing',
        'fam_apgar_discussion', 'fam_apgar_decisions', 'fam_apgar_affection')
    def on_change_with_fam_apgar_score(self):
        fam_apgar_help = int(self.fam_apgar_help or '0')
        fam_apgar_timesharing = int(self.fam_apgar_timesharing or '0')
        fam_apgar_discussion = int(self.fam_apgar_discussion or '0')
        fam_apgar_decisions = int(self.fam_apgar_decisions or '0')
        fam_apgar_affection = int(self.fam_apgar_affection or '0')
        total = (fam_apgar_help + fam_apgar_timesharing +
            fam_apgar_discussion + fam_apgar_decisions +
            fam_apgar_affection)

        return total

    @staticmethod
    def default_assessment_date():
        return datetime.now()

    @staticmethod
    def default_state():
        return 'in_progress'

    @staticmethod
    def default_health_professional():
        pool = Pool()
        HealthProf= pool.get('gnuhealth.healthprofessional')
        health_professional = HealthProf.get_health_professional()
        return health_professional

    # Show the gender and age upon entering the patient 
    # These two are function fields (don't exist at DB level)
    @fields.depends('patient')
    def on_change_patient(self):
        gender=None
        age=''
        self.gender = self.patient.gender
        self.computed_age = self.patient.age

        occupation=education=du=housing=None
        if (self.patient and self.patient.name.occupation):
            occupation = self.patient.name.occupation
        
        if (self.patient and self.patient.name.education):
            education = self.patient.name.education

        if (self.patient and self.patient.name.du):
            du = self.patient.name.du

        if (self.patient and self.patient.name.du):
            housing = self.patient.name.du.housing

        self.occupation = occupation
        self.education = education
        self.du = du
        self.housing = housing



    def get_patient_gender(self, name):
        return self.patient.gender

    @classmethod
    def search_patient_gender(cls, name, clause):
        res = []
        value = clause[2]
        res.append(('patient.name.gender', clause[1], value))
        return res

    @classmethod
    @ModelView.button
    def end_assessment(cls, assessments):
        
        assessment_id = assessments[0]

        # Change the state of the assessment to "Done"
        HealthProf= Pool().get('gnuhealth.healthprofessional')

        signing_hp = HealthProf.get_health_professional()

        cls.write(assessments, {
            'state': 'done',
            'signed_by': signing_hp,
            })
        

    def patient_age_at_assessment(self, name):
        if (self.patient.name.dob and self.assessment_date):
            rdelta = relativedelta (self.assessment_date.date(),
                self.patient.name.dob)
            years_months_days = str(rdelta.years) + 'y ' \
                + str(rdelta.months) + 'm ' \
                + str(rdelta.days) + 'd'
            return years_months_days
        else:
            return None


    @classmethod
    def __setup__(cls):
        super(PatientSESAssessment, cls).__setup__()

        cls._buttons.update({
            'end_assessment': {'invisible': Equal(Eval('state'), 'done')}
            })



class GnuHealthPatient(ModelSQL, ModelView):
    __name__ = 'gnuhealth.patient'


    occupation = fields.Function(fields.Many2One('gnuhealth.occupation','Occupation'), 'get_patient_occupation')

    education = fields.Function(fields.Selection([
        (None, ''),
        ('0', 'None'),
        ('1', 'Incomplete Primary School'),
        ('2', 'Primary School'),
        ('3', 'Incomplete Secondary School'),
        ('4', 'Secondary School'),
        ('5', 'University'),
        ], 'Education Level', help="Education Level", sort=False), 'get_patient_education')


    housing = fields.Function(fields.Selection([
        (None, ''),
        ('0', 'Shanty, deficient sanitary conditions'),
        ('1', 'Small, crowded but with good sanitary conditions'),
        ('2', 'Comfortable and good sanitary conditions'),
        ('3', 'Roomy and excellent sanitary conditions'),
        ('4', 'Luxury and excellent sanitary conditions'),
        ], 'Housing conditions', help="Housing and sanitary living conditions", sort=False), 'get_patient_housing')


    ses_assessments = fields.One2Many('gnuhealth.ses.assessment',
        'patient','Assessments',readonly=True,
        help="Socioeconomics and Family assessments history")


    hostile_area = fields.Boolean('Hostile Area',
        help="Check if patient lives in a zone of high hostility (eg, war)")

    single_parent = fields.Boolean('Single parent family')
    domestic_violence = fields.Boolean('Domestic violence')
    working_children = fields.Boolean('Working children')
    teenage_pregnancy = fields.Boolean('Teenage pregnancy')
    sexual_abuse = fields.Boolean('Sexual abuse')
    drug_addiction = fields.Boolean('Drug addiction')
    school_withdrawal = fields.Boolean('School withdrawal')
    prison_past = fields.Boolean('Has been in prison')
    prison_current = fields.Boolean('Currently in prison')
    relative_in_prison = fields.Boolean('Relative in prison',
        help="Check if someone from the nuclear family - parents / " \
        "sibblings  is or has been in prison")

    ses_notes = fields.Text('Extra info')


    # GnuHealth 2.0 . Occupation and Education are now functional fields.
    # Retrives the information from the party model.
    occupation = fields.Function(fields.Many2One('gnuhealth.occupation',
        'Occupation'), 'get_patient_occupation')


    works_at_home = fields.Boolean('Works at home',
        help="Check if the patient works at his / her house")
    hours_outside = fields.Integer('Hours outside home',
        help="Number of hours a day the patient spend outside the house")


    def get_patient_occupation(self, name):
        if (self.name.occupation):
            return self.name.occupation.id

    def get_patient_education(self, name):
        return self.name.education

    def get_patient_housing(self, name):
        if (self.name.du):
            return self.name.du.housing
