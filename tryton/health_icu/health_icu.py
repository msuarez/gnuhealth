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
from trytond.model import ModelView, ModelSQL, fields
from datetime import datetime
from dateutil.relativedelta import relativedelta
from trytond.transaction import Transaction
from trytond.pyson import Eval, Not, Bool, Equal


__all__ = ['InpatientRegistration', 'InpatientIcu', 'Glasgow', 'ApacheII',
            'MechanicalVentilation', 'ChestDrainageAssessment',
            'PatientRounding']


class InpatientRegistration(ModelSQL, ModelView):
    'Patient admission History'
    __name__ = 'gnuhealth.inpatient.registration'
    icu = fields.Boolean('ICU', help='Shows if patient was admitted to'
        ' the Intensive Care Unit during the hospitalization period')
    icu_admissions = fields.One2Many('gnuhealth.inpatient.icu',
        'name', "ICU Admissions")


class InpatientIcu(ModelSQL, ModelView):
    'Patient ICU Information'
    __name__ = 'gnuhealth.inpatient.icu'

    def icu_duration(self, name):
        if self.discharged_from_icu:
            end = self.icu_discharge_date
        else:
            end = datetime.now()
        return end.date() - self.icu_admission_date.date()

    name = fields.Many2One('gnuhealth.inpatient.registration',
        'Registration Code', required=True)

    admitted = fields.Boolean('Admitted', help="Will be set when the patient \
        is currently admitted at ICU")

    icu_admission_date = fields.DateTime('ICU Admission',
        help="ICU Admission Date", required=True)
    discharged_from_icu = fields.Boolean('Discharged')
    icu_discharge_date = fields.DateTime('Discharge', states={
            'invisible': Not(Bool(Eval('discharged_from_icu'))),
            'required': Bool(Eval('discharged_from_icu')),
            },
        depends=['discharged_from_icu'])
    icu_stay = fields.Function(fields.TimeDelta('Duration'), 'icu_duration')

    mv_history = fields.One2Many('gnuhealth.icu.ventilation',
        'name', "Mechanical Ventilation History")

    @classmethod
    def __setup__(cls):
        super(InpatientIcu, cls).__setup__()
        cls._error_messages.update({
            'patient_already_at_icu': 'Our records indicate that the patient'
                ' is already admitted at ICU'})

    @classmethod
    def validate(cls, inpatients):
        super(InpatientIcu, cls).validate(inpatients)
        for inpatient in inpatients:
            inpatient.check_patient_admitted_at_icu()

    def check_patient_admitted_at_icu(self):
        # Verify that the patient is not at ICU already
        cursor = Transaction().connection.cursor()
        cursor.execute("SELECT count(name) "
            "FROM " + self._table + "  \
            WHERE (name = %s AND admitted)",
            (str(self.name.id),))
        if cursor.fetchone()[0] > 1:
            self.raise_user_error('patient_already_at_icu')

    @staticmethod
    def default_admitted():
        return True

    @fields.depends('discharged_from_icu')
    def on_change_with_admitted(self):
        # Reset the admission flag when the patient is discharged from ICU
        if self.discharged_from_icu:
            res = False
        else:
            res = True
        return res


class Glasgow(ModelSQL, ModelView):
    'Glasgow Coma Scale'
    __name__ = 'gnuhealth.icu.glasgow'

    name = fields.Many2One('gnuhealth.inpatient.registration',
        'Registration Code', required=True)

    evaluation_date = fields.DateTime('Date', help="Date / Time",
        required=True)

    glasgow = fields.Integer('Glasgow',
        help='Level of Consciousness - on Glasgow Coma Scale :  < 9 severe -'
        ' 9-12 Moderate, > 13 minor')
    glasgow_eyes = fields.Selection([
        ('1', '1 : Does not Open Eyes'),
        ('2', '2 : Opens eyes in response to painful stimuli'),
        ('3', '3 : Opens eyes in response to voice'),
        ('4', '4 : Opens eyes spontaneously'),
        ], 'Eyes', sort=False)
    glasgow_verbal = fields.Selection([
        ('1', '1 : Makes no sounds'),
        ('2', '2 : Incomprehensible sounds'),
        ('3', '3 : Utters inappropriate words'),
        ('4', '4 : Confused, disoriented'),
        ('5', '5 : Oriented, converses normally'),
        ], 'Verbal', sort=False)
    glasgow_motor = fields.Selection([
        ('1', '1 : Makes no movement'),
        ('2', '2 : Extension to painful stimuli - decerebrate response -'),
        ('3', '3 : Abnormal flexion to painful stimuli \
            (decorticate response)'),
        ('4', '4 : Flexion / Withdrawal to painful stimuli'),
        ('5', '5 : localizes painful stimuli'),
        ('6', '6 : Obeys commands'),
        ], 'Motor', sort=False)

    @staticmethod
    def default_glasgow_eyes():
        return '4'

    @staticmethod
    def default_glasgow_verbal():
        return '5'

    @staticmethod
    def default_glasgow_motor():
        return '6'

    @staticmethod
    def default_glasgow():
        return 15

    # Default evaluation date
    @staticmethod
    def default_evaluation_date():
        return datetime.now()

    @fields.depends('glasgow_verbal', 'glasgow_motor', 'glasgow_eyes')
    def on_change_with_glasgow(self):
        return int(self.glasgow_motor) + int(self.glasgow_eyes) + \
            int(self.glasgow_verbal)

    # Return the Glasgow Score with each component
    def get_rec_name(self, name):
        if self.name:
            res = str(self.glasgow) + ': ' + 'E' + self.glasgow_eyes + ' V' + \
                self.glasgow_verbal + ' M' + self.glasgow_motor
        return res


class ApacheII(ModelSQL, ModelView):
    'Apache II scoring'
    __name__ = 'gnuhealth.icu.apache2'

    name = fields.Many2One('gnuhealth.inpatient.registration',
        'Registration Code', required=True)
    score_date = fields.DateTime('Date', help="Date of the score",
        required=True)

    age = fields.Integer('Age', help='Patient age in years')
    temperature = fields.Float('Temperature', help='Rectal temperature')
    mean_ap = fields.Integer('MAP', help='Mean Arterial Pressure')
    heart_rate = fields.Integer('Heart Rate')
    respiratory_rate = fields.Integer('Respiratory Rate')
    fio2 = fields.Float('FiO2')
    pao2 = fields.Integer('PaO2')
    paco2 = fields.Integer('PaCO2')
    aado2 = fields.Integer('A-a DO2')

    ph = fields.Float('pH')
    serum_sodium = fields.Integer('Sodium')
    serum_potassium = fields.Float('Potassium')
    serum_creatinine = fields.Float('Creatinine')
    arf = fields.Boolean('ARF', help='Acute Renal Failure')
    wbc = fields.Float('WBC', help="White blood cells x 1000 - if you"
        " want to input 4500 wbc / ml, type in 4.5")
    hematocrit = fields.Float('Hematocrit')
    gcs = fields.Integer('GSC', help='Last Glasgow Coma Scale'
        ' You can use the GSC calculator from the Patient Evaluation Form.')
    chronic_condition = fields.Boolean('Chronic condition',
        help='Organ Failure or immunocompromised patient')
    hospital_admission_type = fields.Selection([
        (None, ''),
        ('me', 'Medical or emergency postoperative'),
        ('el', 'elective postoperative')],
        'Hospital Admission Type', states={
            'invisible': Not(Bool(Eval('chronic_condition'))),
            'required': Bool(Eval('chronic_condition'))}, sort=False)

    apache_score = fields.Integer('Score')

    #Default FiO2 PaO2 and PaCO2 so we do the A-a gradient
    #calculation with non-null values

    @fields.depends('fio2', 'pao2', 'paco2')
    def on_change_with_aado2(self):
    # Calculates the Alveolar-arterial difference
    # based on FiO2, PaCO2 and PaO2 values
        if (self.fio2 and self.paco2 and self.pao2):
            return (713 * self.fio2) - (self.paco2 / 0.8) - self.pao2

    @fields.depends('age', 'temperature', 'mean_ap', 'heart_rate',
        'respiratory_rate', 'fio2', 'pao2', 'aado2', 'ph', 'serum_sodium',
        'serum_potassium', 'serum_creatinine', 'arf', 'wbc', 'hematocrit',
        'gcs', 'chronic_condition', 'hospital_admission_type')
    def on_change_with_apache_score(self):
    # Calculate the APACHE SCORE from the variables in the

        total = 0
        # Age
        if (self.age):
            if (self.age > 44 and self.age < 55):
                total = total + 2
            elif (self.age > 54 and self.age < 65):
                total = total + 3
            elif (self.age > 64 and self.age < 75):
                total = total + 5
            elif (self.age > 74):
                total = total + 6

        # Temperature
        if (self.temperature):
            if ((self.temperature >= 38.5 and self.temperature < 39) or
                (self.temperature >= 34 and self.temperature < 36)):
                    total = total + 1
            elif (self.temperature >= 32 and self.temperature < 34):
                total = total + 2
            elif ((self.temperature >= 30 and self.temperature < 32) or
                (self.temperature >= 39 and self.temperature < 41)):
                total = total + 3
            elif (self.temperature >= 41 or self.temperature < 30):
                total = total + 4

        # Mean Arterial Pressure (MAP)
        if (self.mean_ap):
            if ((self.mean_ap >= 110 and self.mean_ap < 130) or
                (self.mean_ap >= 50 and self.mean_ap < 70)):
                    total = total + 2
            elif (self.mean_ap >= 130 and self.mean_ap < 160):
                total = total + 3
            elif (self.mean_ap >= 160 or self.mean_ap < 50):
                total = total + 4

        # Heart Rate
        if (self.heart_rate):
            if ((self.heart_rate >= 55 and self.heart_rate < 70) or
                (self.heart_rate >= 110 and self.heart_rate < 140)):
                    total = total + 2
            elif ((self.heart_rate >= 40 and self.heart_rate < 55) or
                (self.heart_rate >= 140 and self.heart_rate < 180)):
                    total = total + 3
            elif (self.heart_rate >= 180 or self.heart_rate < 40):
                total = total + 4

        # Respiratory Rate
        if (self.respiratory_rate):
            if ((self.respiratory_rate >= 10 and self.respiratory_rate < 12) or
                (self.respiratory_rate >= 25 and self.respiratory_rate < 35)):
                    total = total + 1
            elif (self.respiratory_rate >= 6 and self.respiratory_rate < 10):
                    total = total + 2
            elif (self.respiratory_rate >= 35 and self.respiratory_rate < 50):
                    total = total + 3
            elif (self.respiratory_rate >= 50 or self.respiratory_rate < 6):
                total = total + 4

        # FIO2
        if (self.fio2):
            # If Fi02 is greater than 0.5, we measure the AaDO2 gradient
            # Otherwise, we take into account the Pa02 value

            if (self.fio2 >= 0.5):
                if (self.aado2 >= 200 and self.aado2 < 350):
                    total = total + 2

                elif (self.aado2 >= 350 and self.aado2 < 500):
                    total = total + 3

                elif (self.aado2 >= 500):
                    total = total + 4

            else:
                if (self.pao2 >= 61 and self.pao2 < 71):
                    total = total + 1

                elif (self.pao2 >= 55 and self.pao2 < 61):
                    total = total + 3

                elif (self.pao2 < 55):
                    total = total + 4

        # Arterial pH
        if (self.ph):
            if (self.ph >= 7.5 and self.ph < 7.6):
                    total = total + 1
            elif (self.ph >= 7.25 and self.ph < 7.33):
                    total = total + 2
            elif ((self.ph >= 7.15 and self.ph < 7.25) or
                (self.ph >= 7.6 and self.ph < 7.7)):
                    total = total + 3
            elif (self.ph >= 7.7 or self.ph < 7.15):
                total = total + 4

        # Serum Sodium
        if (self.serum_sodium):
            if (self.serum_sodium >= 150 and self.serum_sodium < 155):
                    total = total + 1
            elif ((self.serum_sodium >= 155 and self.serum_sodium < 160) or
                (self.serum_sodium >= 120 and self.serum_sodium < 130)):
                    total = total + 2
            elif ((self.serum_sodium >= 160 and self.serum_sodium < 180) or
                (self.serum_sodium >= 111 and self.serum_sodium < 120)):
                    total = total + 3
            elif (self.serum_sodium >= 180 or self.serum_sodium < 111):
                total = total + 4

        # Serum Potassium
        if (self.serum_potassium):
            if ((self.serum_potassium >= 3 and self.serum_potassium < 3.5) or
                (self.serum_potassium >= 5.5 and self.serum_potassium < 6)):
                    total = total + 1
            elif (self.serum_potassium >= 2.5 and self.serum_potassium < 3):
                total = total + 2
            elif (self.serum_potassium >= 6 and self.serum_potassium < 7):
                total = total + 3
            elif (self.serum_potassium >= 7 or self.serum_potassium < 2.5):
                total = total + 4

        # Serum Creatinine
        if (self.serum_creatinine):
            arf_factor = 1
            if (self.arf):
            # We multiply by 2 the score if there is concomitant ARF
                arf_factor = 2
            if ((self.serum_creatinine < 0.6) or
                (self.serum_creatinine >= 1.5 and self.serum_creatinine < 2)):
                    total = total + 2 * arf_factor
            elif (self.serum_creatinine >= 2 and self.serum_creatinine < 3.5):
                total = total + 3 * arf_factor
            elif (self.serum_creatinine >= 3.5):
                total = total + 4 * arf_factor

        # Hematocrit
        if (self.hematocrit):
            if (self.hematocrit >= 46 and self.hematocrit < 50):
                total = total + 1
            elif ((self.hematocrit >= 50 and self.hematocrit < 60) or
                (self.hematocrit >= 20 and self.hematocrit < 30)):
                    total = total + 2
            elif (self.hematocrit >= 60 or self.hematocrit < 20):
                total = total + 4

        # WBC ( x 1000 )
        if (self.wbc):
            if (self.wbc >= 15 and self.wbc < 20):
                total = total + 1
            elif ((self.wbc >= 20 and self.wbc < 40) or
                (self.wbc >= 1 and self.wbc < 3)):
                    total = total + 2
            elif (self.wbc >= 40 or self.wbc < 1):
                total = total + 4

        # Immnunocompromised or severe organ failure
        if (self.chronic_condition):
            if (self.hospital_admission_type == 'me'):
                total = total + 5
            else:
                total = total + 2

        return total


class MechanicalVentilation(ModelSQL, ModelView):
    'Mechanical Ventilation History'
    __name__ = 'gnuhealth.icu.ventilation'

    def mv_duration(self, name):
        start = end = datetime.now()

        if self.mv_start:
            start = self.mv_start

        if self.mv_end:
            end = self.mv_end

        return end.date() - start.date()

    name = fields.Many2One('gnuhealth.inpatient.icu', 'Patient ICU Admission',
        required=True)

    ventilation = fields.Selection([
        (None, ''),
        ('none', 'None - Maintains Own'),
        ('nppv', 'Non-Invasive Positive Pressure'),
        ('ett', 'ETT'),
        ('tracheostomy', 'Tracheostomy')],
        'Type', help="NPPV = Non-Invasive Positive "
            "Pressure Ventilation, BiPAP-CPAP \n"
            "ETT - Endotracheal Tube", sort=False)

    ett_size = fields.Integer('ETT Size', states={
            'invisible': Not(Equal(Eval('ventilation'), 'ett'))})

    tracheostomy_size = fields.Integer('Tracheostomy size', states={
            'invisible': Not(Equal(Eval('ventilation'), 'tracheostomy'))})

    mv_start = fields.DateTime('From', help="Start of Mechanical Ventilation",
        required=True)
    mv_end = fields.DateTime('To', help="End of Mechanical Ventilation",
        states={
            'invisible': Bool(Eval('current_mv')),
            'required': Not(Bool(Eval('current_mv'))),
            },
        depends=['current_mv'])
    mv_period = fields.Function(fields.TimeDelta('Duration'), 'mv_duration')
    current_mv = fields.Boolean('Current')
    remarks = fields.Char('Remarks')

    @classmethod
    def __setup__(cls):
        super(MechanicalVentilation, cls).__setup__()
        cls._error_messages.update({
            'patient_already_on_mv': 'Our records indicate that the patient'
                ' is already on Mechanical Ventilation !'})

    @classmethod
    def validate(cls, inpatients):
        super(MechanicalVentilation, cls).validate(inpatients)
        for inpatient in inpatients:
            inpatient.check_patient_current_mv()

    def check_patient_current_mv(self):
        # Check for only one current mechanical ventilation on patient
        cursor = Transaction().connection.cursor()
        cursor.execute("SELECT count(name) "
            "FROM " + self._table + "  \
            WHERE (name = %s AND current_mv)",
            (str(self.name.id),))
        if cursor.fetchone()[0] > 1:
            self.raise_user_error('patient_already_on_mv')

    @staticmethod
    def default_current_mv():
        return True


class ChestDrainageAssessment(ModelSQL, ModelView):
    'Chest Drainage Asessment'
    __name__ = 'gnuhealth.icu.chest_drainage'

    name = fields.Many2One('gnuhealth.patient.rounding', 'Rounding',
        required=True)
    location = fields.Selection([
        (None, ''),
        ('rl', 'Right Pleura'),
        ('ll', 'Left Pleura'),
        ('mediastinum', 'Mediastinum')],
        'Location', sort=False)
    fluid_aspect = fields.Selection([
        (None, ''),
        ('serous', 'Serous'),
        ('bloody', 'Bloody'),
        ('chylous', 'Chylous'),
        ('purulent', 'Purulent')],
        'Aspect', sort=False)
    suction = fields.Boolean('Suction')
    suction_pressure = fields.Integer('cm H2O', states={
            'invisible': Not(Bool(Eval('suction'))),
            'required': Bool(Eval('suction')),
            },
        depends=['suction'])
    oscillation = fields.Boolean('Oscillation')
    air_leak = fields.Boolean('Air Leak')
    fluid_volume = fields.Integer('Volume')
    remarks = fields.Char('Remarks')


class PatientRounding(ModelSQL, ModelView):
    # Nursing Rounding for ICU
    # Inherit and append to the existing model the new functionality for ICU

    __name__ = 'gnuhealth.patient.rounding'

    STATES = {'readonly': Eval('state') == 'done'}

    icu_patient = fields.Boolean('ICU', help='Check this box if this is'
    'an Intensive Care Unit rounding.', states=STATES)
    # Neurological assesment
    gcs = fields.Many2One('gnuhealth.icu.glasgow', 'GCS',
        domain=[('name', '=', Eval('name'))], depends=['name'],states=STATES)

    pupil_dilation = fields.Selection([
        ('normal', 'Normal'),
        ('miosis', 'Miosis'),
        ('mydriasis', 'Mydriasis')],
        'Pupil Dilation', sort=False, states=STATES)

    left_pupil = fields.Integer('L', help="size in mm of left pupil",
        states=STATES)
    right_pupil = fields.Integer('R', help="size in mm of right pupil",
        states=STATES)

    anisocoria = fields.Boolean('Anisocoria', states=STATES)

    pupillary_reactivity = fields.Selection([
        (None, ''),
        ('brisk', 'Brisk'),
        ('sluggish', 'Sluggish'),
        ('nonreactive', 'Nonreactive')],
        'Pupillary Reactivity', sort=False, states=STATES)

    pupil_consensual_resp = fields.Boolean('Consensual Response',
        help="Pupillary Consensual Response", states=STATES)

    # Respiratory assesment
    # Mechanical ventilation information is on the patient ICU general info

    respiration_type = fields.Selection([
        (None, ''),
        ('regular', 'Regular'),
        ('deep', 'Deep'),
        ('shallow', 'Shallow'),
        ('labored', 'Labored'),
        ('intercostal', 'Intercostal')],
        'Respiration', sort=False, states=STATES)

    oxygen_mask = fields.Boolean('Oxygen Mask', states=STATES)
    fio2 = fields.Integer('FiO2', states=STATES)

    peep = fields.Boolean('PEEP', states=STATES)

    peep_pressure = fields.Integer('cm H2O', help="Pressure", states={
            'invisible': Not(Bool(Eval('peep'))),
            'required': Bool(Eval('peep')),
            'readonly': Eval('state') == 'done',
            },
        depends=['peep'])

    sce = fields.Boolean('SCE', help="Subcutaneous Emphysema",states=STATES)
    lips_lesion = fields.Boolean('Lips lesion',states=STATES)
    oral_mucosa_lesion = fields.Boolean('Oral mucosa lesion', states=STATES)

    # Chest expansion characteristics
    chest_expansion = fields.Selection([
        (None, ''),
        ('symmetric', 'Symmetrical'),
        ('asymmetric', 'Asymmetrical')],
        'Expansion', sort=False, states=STATES)
    paradoxical_expansion = fields.Boolean('Paradoxical',
        help="Paradoxical Chest Expansion", states=STATES)
    tracheal_tug = fields.Boolean('Tracheal Tug', states=STATES)

    # Trachea position
    trachea_alignment = fields.Selection([
        (None, ''),
        ('midline', 'Midline'),
        ('right', 'Deviated right'),
        ('left', 'Deviated left')],
        'Tracheal alignment', sort=False, states=STATES)

    # Chest Drainages
    chest_drainages = fields.One2Many('gnuhealth.icu.chest_drainage',
        'name', "Drainages", states=STATES)

    # Chest X-Ray
    xray = fields.Binary('Xray', states=STATES)

    # Cardiovascular assessment

    ecg = fields.Many2One('gnuhealth.patient.ecg', 'Inpatient ECG',
        domain=[('inpatient_registration_code', '=', Eval('name'))],
        depends=['name'],states=STATES)

    venous_access = fields.Selection([
        (None, ''),
        ('none', 'None'),
        ('central', 'Central catheter'),
        ('peripheral', 'Peripheral')],
        'Venous Access', sort=False, states=STATES)

    swan_ganz = fields.Boolean('Swan Ganz',
        help="Pulmonary Artery Catheterization - PAC -", states=STATES)

    arterial_access = fields.Boolean('Arterial Access', states=STATES)

    dialysis = fields.Boolean('Dialysis', states=STATES)

    edema = fields.Selection([
        (None, ''),
        ('none', 'None'),
        ('peripheral', 'Peripheral'),
        ('anasarca', 'Anasarca')],
        'Edema', sort=False, states=STATES)

    # Blood & Skin
    bacteremia = fields.Boolean('Bacteremia', states=STATES)
    ssi = fields.Boolean('Surgery Site Infection', states=STATES)
    wound_dehiscence = fields.Boolean('Wound Dehiscence', states=STATES)
    cellulitis = fields.Boolean('Cellulitis', states=STATES)
    necrotizing_fasciitis = fields.Boolean('Necrotizing fasciitis',
        states=STATES)

    # Abdomen & Digestive

    vomiting = fields.Selection([
        (None, ''),
        ('none', 'None'),
        ('vomiting', 'Vomiting'),
        ('hematemesis', 'Hematemesis')],
        'Vomiting', sort=False, states=STATES)

    bowel_sounds = fields.Selection([
        (None, ''),
        ('normal', 'Normal'),
        ('increased', 'Increased'),
        ('decreased', 'Decreased'),
        ('absent', 'Absent')],
        'Bowel Sounds', sort=False, states=STATES)

    stools = fields.Selection([
        (None, ''),
        ('normal', 'Normal'),
        ('constipation', 'Constipation'),
        ('diarrhea', 'Diarrhea'),
        ('melena', 'Melena')],
        'Stools', sort=False, states=STATES)

    peritonitis = fields.Boolean('Peritonitis signs', states=STATES)

    @fields.depends('left_pupil', 'right_pupil')
    def on_change_with_anisocoria(self):
        if (self.left_pupil == self.right_pupil):
            return False
        else:
            return True

    @staticmethod
    def default_pupil_dilation():
        return 'normal'
