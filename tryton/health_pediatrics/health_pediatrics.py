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
from trytond.model import ModelView, ModelSQL, fields
from trytond.transaction import Transaction
from trytond.pool import Pool


class Newborn(ModelSQL, ModelView):
    'Newborn Information'
    _name = 'gnuhealth.newborn'
    _description = __doc__
    
    name = fields.Char('Newborn ID')
    mother = fields.Many2One('gnuhealth.patient', 'Mother')
    newborn_name = fields.Char('Baby\'s name')
    birth_date = fields.DateTime('Date of Birth', required=True)
    photo = fields.Binary('Picture')
    sex = fields.Selection([
        ('m', 'Male'),
        ('f', 'Female'),
        ('a', 'Ambiguous genitalia'),
        ], 'Sex', sort=False, required=True)
    cephalic_perimeter = fields.Integer('Cephalic Perimeter',
        help="Perimeter in centimeters (cm)")
    length = fields.Integer('Length', help="Perimeter in centimeters (cm)")
    weight = fields.Integer('Weight', help="Weight in grams (g)")
    apgar1 = fields.Integer('APGAR 1st minute')
    apgar5 = fields.Integer('APGAR 5th minute')

    apgar_scores = fields.One2Many('gnuhealth.neonatal.apgar', 'name',
        'APGAR scores')
    meconium = fields.Boolean('Meconium')
    congenital_diseases = fields.One2Many('gnuhealth.patient.disease',
        'newborn_id', 'Congenital diseases')
    reanimation_stimulation = fields.Boolean('Stimulation')
    reanimation_aspiration = fields.Boolean('Aspiration')
    reanimation_intubation = fields.Boolean('Intubation')
    reanimation_mask = fields.Boolean('Mask')
    reanimation_oxygen = fields.Boolean('Oxygen')
    test_vdrl = fields.Boolean('VDRL')
    test_toxo = fields.Boolean('Toxoplasmosis')
    test_chagas = fields.Boolean('Chagas')
    test_billirubin = fields.Boolean('Billirubin')
    test_audition = fields.Boolean('Audition')
    test_metabolic = fields.Boolean('Metabolic ("heel stick screening")',
        help="Test for Fenilketonuria, Congenital Hypothyroidism, " \
        "Quistic Fibrosis, Galactosemia")
    neonatal_ortolani = fields.Boolean('Positive Ortolani')
    neonatal_barlow = fields.Boolean('Positive Barlow')
    neonatal_hernia = fields.Boolean('Hernia')
    neonatal_ambiguous_genitalia = fields.Boolean('Ambiguous Genitalia')
    neonatal_erbs_palsy = fields.Boolean('Erbs Palsy')
    neonatal_hematoma = fields.Boolean('Hematomas')
    neonatal_talipes_equinovarus = fields.Boolean('Talipes Equinovarus')
    neonatal_polydactyly = fields.Boolean('Polydactyly')
    neonatal_syndactyly = fields.Boolean('Syndactyly')
    neonatal_moro_reflex = fields.Boolean('Moro Reflex')
    neonatal_grasp_reflex = fields.Boolean('Grasp Reflex')
    neonatal_stepping_reflex = fields.Boolean('Stepping Reflex')
    neonatal_babinski_reflex = fields.Boolean('Babinski Reflex')
    neonatal_blink_reflex = fields.Boolean('Blink Reflex')
    neonatal_sucking_reflex = fields.Boolean('Sucking Reflex')
    neonatal_swimming_reflex = fields.Boolean('Swimming Reflex')
    neonatal_tonic_neck_reflex = fields.Boolean('Tonic Neck Reflex')
    neonatal_rooting_reflex = fields.Boolean('Rooting Reflex')
    neonatal_palmar_crease = fields.Boolean('Transversal Palmar Crease')
    medication = fields.One2Many('gnuhealth.patient.medication',
        'newborn_id', 'Medication')
    responsible = fields.Many2One('gnuhealth.physician', 'Doctor in charge',
        help="Signed by the health professional")
    dismissed = fields.DateTime('Discharged')
    bd = fields.Boolean('Stillbirth')
    died_at_delivery = fields.Boolean('Died at delivery room')
    died_at_the_hospital = fields.Boolean('Died at the hospital')
    died_being_transferred = fields.Boolean('Died being transferred',
        help="The baby died being transferred to another health institution")
    tod = fields.DateTime('Time of Death')
    cod = fields.Many2One('gnuhealth.pathology', 'Cause of death')
    notes = fields.Text('Notes')
    
    def __init__(self):
        super(Newborn, self).__init__()

        self._sql_constraints = [
            ('name_uniq', 'unique(name)', 'The Newborn ID must be unique !'),
        ]

Newborn()


class NeonatalApgar(ModelSQL, ModelView):
    'Neonatal APGAR Score'
    _name = 'gnuhealth.neonatal.apgar'
    _description = __doc__

    name = fields.Many2One('gnuhealth.newborn', 'Newborn ID')

    apgar_minute = fields.Integer('Minute', required=True)

    apgar_appearance = fields.Selection([
        ('0', 'central cyanosis'),
        ('1', 'acrocyanosis'),
        ('2', 'no cyanosis'),
        ], 'Appearance', required=True)

    apgar_pulse = fields.Selection([
        ('0', 'Absent'),
        ('1', '< 100'),
        ('2', '> 100'),
        ], 'Pulse', required=True)

    apgar_grimace = fields.Selection([
        ('0', 'No response to stimulation'),
        ('1', 'grimace when stimulated'),
        ('2', 'cry or pull away when stimulated'),
        ], 'Grimace', required=True, sort=False)

    apgar_activity = fields.Selection([
        ('0', 'None'),
        ('1', 'Some flexion'),
        ('2', 'flexed arms and legs'),
        ], 'Activity', required=True, sort=False)

    apgar_respiration = fields.Selection([
        ('0', 'Absent'),
        ('1', 'Weak / Irregular'),
        ('2', 'strong'),
        ], 'Respiration', required=True, sort=False)

    apgar_score = fields.Integer('APGAR Score',
        on_change_with=['apgar_respiration', 'apgar_activity',
        'apgar_grimace', 'apgar_pulse', 'apgar_appearance'])

    def on_change_with_apgar_score(self, vals):
        apgar_appearance = vals.get('apgar_appearance') or '0'
        apgar_pulse = vals.get('apgar_pulse') or '0'
        apgar_grimace = vals.get('apgar_grimace') or '0'
        apgar_activity = vals.get('apgar_activity') or '0'
        apgar_respiration = vals.get('apgar_respiration') or '0'

        apgar_score = int(apgar_appearance) + int(apgar_pulse) + \
            int(apgar_grimace) + int(apgar_activity) + int(apgar_respiration)

        return apgar_score

NeonatalApgar()


class NeonatalMedication(ModelSQL, ModelView):
    'Neonatal Medication. Inherit and Add field to Medication model'
    _name = 'gnuhealth.patient.medication'
    _description = __doc__

    newborn_id = fields.Many2One('gnuhealth.newborn', 'Newborn ID')

NeonatalMedication()


class NeonatalCongenitalDiseases(ModelSQL, ModelView):
    'Congenital Diseases. Inherit Disease object for use in neonatology'
    _name = 'gnuhealth.patient.disease'
    _description = __doc__

    newborn_id = fields.Many2One('gnuhealth.newborn', 'Newborn ID')

NeonatalCongenitalDiseases()


class PediatricSymptomsChecklist(ModelSQL, ModelView):
    'Pediatric Symptoms Checklist'
    _name = 'gnuhealth.patient.psc'
    _description = __doc__
    
    
    patient = fields.Many2One('gnuhealth.patient', 'Patient', required=True)

    evaluation_date = fields.Many2One('gnuhealth.appointment', 'Appointment',
        help="Enter or select the date / ID of the appointment related to " \
        "this evaluation")

    evaluation_start = fields.DateTime('Date', required=True)

    user_id = fields.Many2One('res.user', 'Healh Professional', readonly=True)

    notes = fields.Text('Notes')

    psc_aches_pains = fields.Selection([
        ('0', 'Never'),
        ('1', 'Sometimes'),
        ('2', 'Often'),
        ], 'Complains of aches and pains', sort=False)

    psc_spend_time_alone = fields.Selection([
        ('0', 'Never'),
        ('1', 'Sometimes'),
        ('2', 'Often'),
        ], 'Spends more time alone', sort=False)

    psc_tires_easily = fields.Selection([
        ('0', 'Never'),
        ('1', 'Sometimes'),
        ('2', 'Often'),
        ], 'Tires easily, has little energy', sort=False)

    psc_fidgety = fields.Selection([
        ('0', 'Never'),
        ('1', 'Sometimes'),
        ('2', 'Often'),
        ], 'Fidgety, unable to sit still', sort=False)

    psc_trouble_with_teacher = fields.Selection([
        ('0', 'Never'),
        ('1', 'Sometimes'),
        ('2', 'Often'),
        ], 'Has trouble with teacher', sort=False)

    psc_less_interest_in_school = fields.Selection([
        ('0', 'Never'),
        ('1', 'Sometimes'),
        ('2', 'Often'),
        ], 'Less interested in school', sort=False)

    psc_acts_as_driven_by_motor = fields.Selection([
        ('0', 'Never'),
        ('1', 'Sometimes'),
        ('2', 'Often'),
        ], 'Acts as if driven by a motor', sort=False)

    psc_daydreams_too_much = fields.Selection([
        ('0', 'Never'),
        ('1', 'Sometimes'),
        ('2', 'Often'),
        ], 'Daydreams too much', sort=False)

    psc_distracted_easily = fields.Selection([
        ('0', 'Never'),
        ('1', 'Sometimes'),
        ('2', 'Often'),
        ], 'Distracted easily', sort=False)

    psc_afraid_of_new_situations = fields.Selection([
        ('0', 'Never'),
        ('1', 'Sometimes'),
        ('2', 'Often'),
        ], 'Is afraid of new situations', sort=False)

    psc_sad_unhappy = fields.Selection([
        ('0', 'Never'),
        ('1', 'Sometimes'),
        ('2', 'Often'),
        ], 'Feels sad, unhappy', sort=False)

    psc_irritable_angry = fields.Selection([
        ('0', 'Never'),
        ('1', 'Sometimes'),
        ('2', 'Often'),
        ], 'Is irritable, angry', sort=False)

    psc_feels_hopeless = fields.Selection([
        ('0', 'Never'),
        ('1', 'Sometimes'),
        ('2', 'Often'),
        ], 'Feels hopeless', sort=False)

    psc_trouble_concentrating = fields.Selection([
        ('0', 'Never'),
        ('1', 'Sometimes'),
        ('2', 'Often'),
        ], 'Has trouble concentrating', sort=False)

    psc_less_interested_in_friends = fields.Selection([
        ('0', 'Never'),
        ('1', 'Sometimes'),
        ('2', 'Often'),
        ], 'Less interested in friends', sort=False)

    psc_fights_with_others = fields.Selection([
        ('0', 'Never'),
        ('1', 'Sometimes'),
        ('2', 'Often'),
        ], 'Fights with other children', sort=False)

    psc_absent_from_school = fields.Selection([
        ('0', 'Never'),
        ('1', 'Sometimes'),
        ('2', 'Often'),
        ], 'Absent from school', sort=False)

    psc_school_grades_dropping = fields.Selection([
        ('0', 'Never'),
        ('1', 'Sometimes'),
        ('2', 'Often'),
        ], 'School grades dropping', sort=False)

    psc_down_on_self = fields.Selection([
        ('0', 'Never'),
        ('1', 'Sometimes'),
        ('2', 'Often'),
        ], 'Is down on him or herself', sort=False)

    psc_visit_doctor_finds_ok = fields.Selection([
        ('0', 'Never'),
        ('1', 'Sometimes'),
        ('2', 'Often'),
        ], 'Visits the doctor with doctor finding nothing wrong', sort=False)

    psc_trouble_sleeping = fields.Selection([
        ('0', 'Never'),
        ('1', 'Sometimes'),
        ('2', 'Often'),
        ], 'Has trouble sleeping', sort=False)

    psc_worries_a_lot = fields.Selection([
        ('0', 'Never'),
        ('1', 'Sometimes'),
        ('2', 'Often'),
        ], 'Worries a lot', sort=False)

    psc_wants_to_be_with_parents = fields.Selection([
        ('0', 'Never'),
        ('1', 'Sometimes'),
        ('2', 'Often'),
        ], 'Wants to be with you more than before', sort=False)

    psc_feels_is_bad_child = fields.Selection([
        ('0', 'Never'),
        ('1', 'Sometimes'),
        ('2', 'Often'),
        ], 'Feels he or she is bad', sort=False)

    psc_takes_unnecesary_risks = fields.Selection([
        ('0', 'Never'),
        ('1', 'Sometimes'),
        ('2', 'Often'),
        ], 'Takes unnecessary risks', sort=False)

    psc_gets_hurt_often = fields.Selection([
        ('0', 'Never'),
        ('1', 'Sometimes'),
        ('2', 'Often'),
        ], 'Gets hurt frequently', sort=False)

    psc_having_less_fun = fields.Selection([
        ('0', 'Never'),
        ('1', 'Sometimes'),
        ('2', 'Often'),
        ], 'Seems to be having less fun', sort=False)

    psc_act_as_younger = fields.Selection([
        ('0', 'Never'),
        ('1', 'Sometimes'),
        ('2', 'Often'),
        ], 'Acts younger than children his or her age', sort=False)

    psc_does_not_listen_to_rules = fields.Selection([
        ('0', 'Never'),
        ('1', 'Sometimes'),
        ('2', 'Often'),
        ], 'Does not listen to rules', sort=False)

    psc_does_not_show_feelings = fields.Selection([
        ('0', 'Never'),
        ('1', 'Sometimes'),
        ('2', 'Often'),
        ], 'Does not show feelings', sort=False)


    psc_does_not_get_people_feelings = fields.Selection([
        ('0', 'Never'),
        ('1', 'Sometimes'),
        ('2', 'Often'),
        ], 'Does not get people feelings', sort=False)

    psc_teases_others = fields.Selection([
        ('0', 'Never'),
        ('1', 'Sometimes'),
        ('2', 'Often'),
        ], 'Teases others', sort=False)

    psc_blames_others = fields.Selection([
        ('0', 'Never'),
        ('1', 'Sometimes'),
        ('2', 'Often'),
        ], 'Blames others for his or her troubles', sort=False)

    psc_takes_things_from_others = fields.Selection([
        ('0', 'Never'),
        ('1', 'Sometimes'),
        ('2', 'Often'),
        ], 'Takes things that do not belong to him or her', sort=False)

    psc_refuses_to_share = fields.Selection([
        ('0', 'Never'),
        ('1', 'Sometimes'),
        ('2', 'Often'),
        ], 'Refuses to share', sort=False)

    psc_total = fields.Integer('PSC Total',
        on_change_with=['psc_aches_pains', 'psc_spend_time_alone',
        'psc_tires_easily', 'psc_fidgety', 'psc_trouble_with_teacher',
        'psc_less_interest_in_school', 'psc_acts_as_driven_by_motor',
        'psc_daydreams_too_much', 'psc_distracted_easily',
        'psc_afraid_of_new_situations', 'psc_sad_unhappy',
        'psc_irritable_angry', 'psc_feels_hopeless',
        'psc_trouble_concentrating', 'psc_less_interested_in_friends',
        'psc_fights_with_others', 'psc_absent_from_school',
        'psc_school_grades_dropping', 'psc_down_on_self',
        'psc_visit_doctor_finds_ok', 'psc_trouble_sleeping',
        'psc_worries_a_lot', 'psc_wants_to_be_with_parents',
        'psc_feels_is_bad_child', 'psc_takes_unnecesary_risks',
        'psc_gets_hurt_often', 'psc_having_less_fun',
        'psc_act_as_younger', 'psc_does_not_listen_to_rules',
        'psc_does_not_show_feelings',
        'psc_does_not_get_people_feelings',
        'psc_teases_others', 'psc_takes_things_from_others',
        'psc_refuses_to_share'])

    def default_user_id(self):
        user_obj = Pool().get('res.user')
        user = user_obj.browse(Transaction().user)
        return int(user.id)

    def default_psc_total(self):
        return 0

    def on_change_with_psc_total(self, vals):

        psc_aches_pains = vals.get('psc_aches_pains') or '0'
        psc_spend_time_alone = vals.get('psc_spend_time_alone') or '0'
        psc_tires_easily = vals.get('psc_tires_easily') or '0'
        psc_fidgety = vals.get('psc_fidgety') or '0'
        psc_trouble_with_teacher = vals.get('psc_trouble_with_teacher') or '0'
        psc_less_interest_in_school = vals.get('psc_less_interest_in_school') or '0'
        psc_acts_as_driven_by_motor = vals.get('psc_acts_as_driven_by_motor') or '0'
        psc_daydreams_too_much = vals.get('psc_daydreams_too_much') or '0'
        psc_distracted_easily = vals.get('psc_distracted_easily') or '0'
        psc_afraid_of_new_situations = vals.get('psc_afraid_of_new_situations') or '0'
        psc_sad_unhappy = vals.get('psc_sad_unhappy') or '0'
        psc_irritable_angry = vals.get('psc_irritable_angry') or '0'
        psc_feels_hopeless = vals.get('psc_feels_hopeless') or '0'
        psc_trouble_concentrating = vals.get('psc_trouble_concentrating') or '0'
        psc_less_interested_in_friends = \
                vals.get('psc_less_interested_in_friends') or '0'
        psc_fights_with_others = vals.get('psc_fights_with_others') or '0'
        psc_absent_from_school = vals.get('psc_absent_from_school') or '0'
        psc_school_grades_dropping = vals.get('psc_school_grades_dropping') or '0'
        psc_down_on_self = vals.get('psc_down_on_self') or '0'
        psc_visit_doctor_finds_ok = vals.get('psc_visit_doctor_finds_ok') or '0'
        psc_trouble_sleeping = vals.get('psc_trouble_sleeping') or '0'
        psc_worries_a_lot = vals.get('psc_worries_a_lot') or '0'
        psc_wants_to_be_with_parents = vals.get('psc_wants_to_be_with_parents') or '0'
        psc_feels_is_bad_child = vals.get('psc_feels_is_bad_child') or '0'
        psc_takes_unnecesary_risks = vals.get('psc_takes_unnecesary_risks') or '0'
        psc_gets_hurt_often = vals.get('psc_gets_hurt_often') or '0'
        psc_having_less_fun = vals.get('psc_having_less_fun') or '0'
        psc_act_as_younger = vals.get('psc_act_as_younger') or '0'
        psc_does_not_listen_to_rules = vals.get('psc_does_not_listen_to_rules') or '0'
        psc_does_not_show_feelings = vals.get('psc_does_not_show_feelings') or '0'
        psc_does_not_get_people_feelings = \
                vals.get('psc_does_not_get_people_feelings') or '0'
        psc_teases_others = vals.get('psc_teases_others') or '0'
        psc_takes_things_from_others = vals.get('psc_takes_things_from_others') or '0'
        psc_refuses_to_share = vals.get('psc_refuses_to_share') or '0'


        psc_total = int(psc_aches_pains) + int(psc_spend_time_alone) + \
            int(psc_tires_easily) + int(psc_fidgety) + \
            int(psc_trouble_with_teacher) + \
            int(psc_less_interest_in_school) + \
            int(psc_acts_as_driven_by_motor) + \
            int(psc_daydreams_too_much) + int(psc_distracted_easily) + \
            int(psc_afraid_of_new_situations) + int(psc_sad_unhappy) + \
            int(psc_irritable_angry) + int(psc_feels_hopeless) + \
            int(psc_trouble_concentrating) + \
            int(psc_less_interested_in_friends) + \
            int(psc_fights_with_others) + int(psc_absent_from_school) + \
            int(psc_school_grades_dropping) + int(psc_down_on_self) + \
            int(psc_visit_doctor_finds_ok) + int(psc_trouble_sleeping) + \
            int(psc_worries_a_lot) + int(psc_wants_to_be_with_parents) + \
            int(psc_feels_is_bad_child) + int(psc_takes_unnecesary_risks) + \
            int(psc_gets_hurt_often) + int(psc_having_less_fun) + \
            int(psc_act_as_younger) + int(psc_does_not_listen_to_rules) + \
            int(psc_does_not_show_feelings) + \
            int(psc_does_not_get_people_feelings) + \
            int(psc_teases_others) + \
            int(psc_takes_things_from_others) + \
            int(psc_refuses_to_share)

        return psc_total

        
PediatricSymptomsChecklist()


# REMOVED IN 1.6
# WE USE A RELATE ACTION

'''
class PscEvaluation(ModelSQL, ModelView):
    'Pediatric Symptoms Checklist Evaluation'
    _name = 'gnuhealth.patient'
    _description = __doc__

    psc = fields.One2Many('gnuhealth.patient.psc', 'patient',
        'Pediatric Symptoms Checklist')

PscEvaluation()
'''
