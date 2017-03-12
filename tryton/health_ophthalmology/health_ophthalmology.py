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
from trytond.pool import Pool
from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta, date
from trytond.pyson import Eval, Equal

__all__ = [    
    'OphthalmologyEvaluation',
    'OphthalmologyFindings',    
    ]



class OphthalmologyEvaluation(ModelSQL, ModelView):
    'Ophthalmology Evaluation'
    __name__ = 'gnuhealth.ophthalmology.evaluation'

    STATES = {'readonly': Eval('state') == 'done'}

    patient = fields.Many2One('gnuhealth.patient', 'Patient', required=True)
    visit_date = fields.DateTime('Date', help="Date of Consultation")
    computed_age = fields.Function(fields.Char(
            'Age',
            help="Computed patient age at the moment of the evaluation"),
            'patient_age_at_evaluation')

    gender = fields.Function(fields.Selection([
        (None, ''),
        ('m', 'Male'),
        ('f', 'Female'),
        ], 'Gender'), 'get_patient_gender', searcher='search_patient_gender')

    health_professional = fields.Many2One(
        'gnuhealth.healthprofessional', 'Health Professional', readonly=True,
        help="Health professional / Ophthalmologist / OptoMetrist"
        )

    # there are two types of charts, a meter chart.. 6/.. val
    # and ft chart.. 200/...
    snellen_chart = [
        (None, ''),
        ('6_6', '6/6'),
        ('6_9', '6/9'),
        ('6_12', '6/12'),
        ('6_18', '6/18'),
        ('6_24', '6/24'),
        ('6_36', '6/36'),
        ('6_60', '6/60'),
        ('5_60', '5/60'),
        ('4_60', '4/60'),
        ('3_60', '3/60'),
        ('2_60', '2/60'),
        ('1_60', '1/60'),
        ('1_meter_fc', '1 Meter FC'),
        ('1_2_meter_fc', '1/2 Meter FC'),
        ('hmfc', 'HMCF'),
        ('p_l', 'P/L'), 
        ]
    
    # Near vision chart
    near_vision_chart = [
        (None, ''),
        ('N6', 'N6'),
        ('N8', 'N8'),
        ('N12', 'N12'),
        ('N18', 'N18'),
        ('N24', 'N24'),
        ('N36', 'N36'),
        ('N60', 'N60'),
        ]
    # vision test using snellen chart
    rdva = fields.Selection(snellen_chart, 'RDVA',
                            help="Right Eye Vision of Patient without aid",
                            sort=False, states = STATES)
    ldva = fields.Selection(snellen_chart, 'LDVA',
                            help="Left Eye Vision of Patient without aid",
                            sort=False, states = STATES)
    # vision test using pinhole accurate manual testing
    rdva_pinhole = fields.Selection(snellen_chart, 'RDVA',
                                    help="Right Eye Vision Using Pin Hole",
                                    sort=False, states = STATES)
    ldva_pinhole = fields.Selection(snellen_chart, 'LDVA',
                                    help="Left Eye Vision Using Pin Hole",
                                    sort=False, states = STATES)
    # vison testing with glasses just to assess what the patient sees with
    # his existing aid # useful esp with vision syndromes that are not
    # happening because of the lens
    rdva_aid = fields.Selection(snellen_chart, 'RDVA AID',
                                help="Vision with glasses or contact lens",
                                sort=False, states = STATES)
    ldva_aid = fields.Selection(snellen_chart, 'LDVA AID',
                                help="Vision with glasses or contact lens",
                                sort=False, states = STATES)

    # spherical
    rspherical = fields.Float('SPH',help='Right Eye Spherical', states = STATES)
    lspherical = fields.Float('SPH',help='Left Eye Spherical', states = STATES)

    # cylinder
    rcylinder = fields.Float('CYL',help='Right Eye Cylinder', states = STATES)
    lcylinder = fields.Float('CYL',help='Left Eye Cylinder', states = STATES)
    
    #axis
    raxis = fields.Float('Axis',help='Right Eye Axis', states = STATES)
    laxis = fields.Float('Axis',help='Left Eye Axis', states = STATES)

    # near vision testing .... you will get it when u cross 40 :)
    # its also thinning of the lens.. the focus falls behind the retina
    # in case of distant vision the focus does not reach retina
    
    rnv_add = fields.Float('NV Add', help='Right Eye Best Corrected NV Add',
        states = STATES)
    lnv_add = fields.Float('NV Add', help='Left Eye Best Corrected NV Add'
        , states = STATES)
    
    rnv = fields.Selection(near_vision_chart, 'RNV',
                           help="Right Eye Near Vision", sort=False,
                            states = STATES)
    lnv = fields.Selection(near_vision_chart, 'LNV',
                           help="Left Eye Near Vision", sort=False,
                            states = STATES)

    # after the above tests the optometrist or doctor comes to a best conclusion
    # best corrected visual acuity
    # the above values are from autorefraction
    # the doctors decision is final
    # and there could be changes in values of cylinder, spherical and axis
    # these values will go into final prescription of glasses or contact lens
    # by default these values should be auto populated 
    # and should be modifiable by an ophthalmologist
    rbcva_spherical = fields.Float('SPH',
        help='Right Eye Best Corrected Spherical', states = STATES)
    lbcva_spherical = fields.Float('SPH',
        help='Left Eye Best Corrected Spherical', states = STATES)

    rbcva_cylinder = fields.Float('CYL',
        help='Right Eye Best Corrected Cylinder', states = STATES)
    lbcva_cylinder = fields.Float('CYL',
        help='Left Eye Best Corrected Cylinder', states = STATES)

    rbcva_axis = fields.Float('Axis', 
        help='Right Eye Best Corrected Axis', states = STATES)
    lbcva_axis = fields.Float('Axis',
        help='Left Eye Best Corrected Axis', states = STATES)

    rbcva = fields.Selection(snellen_chart, 'RBCVA', 
                help="Right Eye Best Corrected VA", sort=False, states = STATES)
    lbcva = fields.Selection(snellen_chart, 'LBCVA', 
                help="Left Eye Best Corrected VA", sort=False, states = STATES)
    
    rbcva_nv_add = fields.Float('BCVA - Add',
        help='Right Eye Best Corrected NV Add', states = STATES)
    lbcva_nv_add = fields.Float('BCVA - Add',
        help='Left Eye Best Corrected NV Add', states = STATES)

    rbcva_nv = fields.Selection(near_vision_chart, 'RBCVANV', 
                help="Right Eye Best Corrected Near Vision", 
                sort=False, states = STATES)
    lbcva_nv = fields.Selection(near_vision_chart, 'LBCVANV' , 
                help="Left Eye Best Corrected Near Vision",
                sort=False, states = STATES)        
        
    #some other tests of the eyes
    #useful for diagnosis of glaucoma a disease that builds up
    #pressure inside the eye and destroy the retina
    #its also called the silent vision stealer
    #intra ocular pressure
    #there are three ways to test iop
    #   SCHIOTZ
    #   NONCONTACT TONOMETRY
    #   GOLDMANN APPLANATION TONOMETRY

    #notes by the ophthalmologist or optometrist
    notes = fields.Text ('Notes', states = STATES)

    #Intraocular Pressure 
    iop_method = fields.Selection([
        (None,''),
        ('nct', 'Non-contact tonometry'),
        ('schiotz', 'Schiotz tonometry'),
        ('goldmann', 'Goldman tonometry'),
        ], 'Method', help='Tonometry / Intraocular pressure reading method',
        states = STATES)
    
    riop = fields.Float('RIOP',digits=(2,1),
        help="Right Intraocular Pressure in mmHg", states = STATES)

    liop = fields.Float('LIOP',digits=(2,1),
        help="Left Intraocular Pressure in mmHg", states = STATES)
        
    findings = fields.One2Many(
        'gnuhealth.ophthalmology.findings', 'name',
        'Findings',  states = STATES)

    state = fields.Selection([
        (None, ''),
        ('in_progress', 'In progress'),
        ('done', 'Done'),
        ], 'State', readonly=True, sort=False)

    signed_by = fields.Many2One(
        'gnuhealth.healthprofessional', 'Signed by', readonly=True,
        states={'invisible': Equal(Eval('state'), 'in_progress')},
        help="Health Professional that finished the patient evaluation")


    def patient_age_at_evaluation(self, name):
        if (self.patient.name.dob and self.visit_date):
            rdelta = relativedelta(self.visit_date.date(),
                self.patient.name.dob)
            years_months_days = str(rdelta.years) + 'y ' \
                + str(rdelta.months) + 'm ' \
                + str(rdelta.days) + 'd'
            return years_months_days
        else:
            return None

    def get_patient_gender(self, name):
        return self.patient.gender

    @classmethod
    def search_patient_gender(cls, name, clause):
        res = []
        value = clause[2]
        res.append(('patient.name.gender', clause[1], value))
        return res

    @fields.depends('rdva')
    def on_change_with_rbcva(self):
        return self.rdva

    @fields.depends('ldva')
    def on_change_with_lbcva(self):
        return self.ldva

    @fields.depends('rcylinder')
    def on_change_with_rbcva_cylinder(self):
        return self.rcylinder

    @fields.depends('lcylinder')
    def on_change_with_lbcva_cylinder(self):
        return self.lcylinder

    @fields.depends('raxis')
    def on_change_with_rbcva_axis(self):
        return self.raxis
        
    @fields.depends('laxis')
    def on_change_with_lbcva_axis(self):
        return self.laxis    
    
    @fields.depends('rspherical')
    def on_change_with_rbcva_spherical(self):
        return self.rspherical

    @fields.depends('lspherical')
    def on_change_with_lbcva_spherical(self):
        return self.lspherical
    
    @fields.depends('rnv_add')
    def on_change_with_rbcva_nv_add(self):
        return self.rnv_add
    
    @fields.depends('lnv_add')
    def on_change_with_lbcva_nv_add(self):
        return self.lnv_add

    @fields.depends('rnv')
    def on_change_with_rbcva_nv(self):
        return self.rnv

    @fields.depends('lnv')
    def on_change_with_lbcva_nv(self):
        return self.lnv

    @staticmethod
    def default_visit_date():
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


    @classmethod
    @ModelView.button
    def end_evaluation(cls, evaluations):
        
        evaluation_id = evaluations[0]

        # Change the state of the evaluation to "Done"
        HealthProf= Pool().get('gnuhealth.healthprofessional')

        signing_hp = HealthProf.get_health_professional()

        cls.write(evaluations, {
            'state': 'done',
            'signed_by': signing_hp,
            })
        

    @classmethod
    def __setup__(cls):
        super(OphthalmologyEvaluation, cls).__setup__()

        cls._buttons.update({
            'end_evaluation': {'invisible': Equal(Eval('state'), 'done')}
            })


#this class model contains the detailed assesment of patient by an
#ophthalmologist


class OphthalmologyFindings(ModelSQL, ModelView):    #model class
    'Ophthalmology Findings'
    __name__ = 'gnuhealth.ophthalmology.findings'    #model Name
    
    # Findings associated to a particular evaluation
    name = fields.Many2One('gnuhealth.ophthalmology.evaluation',
        'Evaluation', readonly=True)

    # Structure
    structure = [
        (None, ''),
        ('lid', 'Lid'),
        ('ncs', 'Naso-lacrimal system'),
        ('conjuctiva', 'Conjunctiva'),
        ('cornea', 'Cornea'),
        ('anterior_chamber', 'Anterior Chamber'),
        ('iris', 'Iris'),
        ('pupil', 'Pupil'),
        ('lens', 'Lens'),
        ('vitreous', 'Vitreous'),
        ('fundus_disc', 'Fundus Disc'),
        ('macula', 'Macula'),
        ('fundus_background', 'Fundus background'),
        ('fundus_vessels', 'Fundus vessels'),
        ('other', 'Other'),
        ]

    eye_structure = fields.Selection(structure,  
        'Structure',help="Affected eye structure",sort=False)

    affected_eye = fields.Selection([  
            (None,''),
            ("right","right"),
            ("left","left"),
            ("both","both"),
        ],'Eye',help="Affected eye",sort=False)

    finding = fields.Char('Finding')    
