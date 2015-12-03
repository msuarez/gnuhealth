from trytond.model import ModelView, ModelSQL, fields
from trytond.pool import Pool
from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta, date

__all__ = [    
    'OphthalmologyEvaluation',
    'OphthalmologyFindings',    
    ]



class OphthalmologyEvaluation(ModelSQL, ModelView):
    'Ophthalmology Evaluation'
    __name__ = 'gnuhealth.ophthalmology.evaluation'

    patient = fields.Many2One('gnuhealth.patient', 'Patient', required=True)
    visit_date = fields.DateTime('Date', help="Date of Consultation")
    computed_age = fields.Function(fields.Char(
            'Age',
            help="Computed patient age at the moment of the evaluation"),
            'patient_age_at_evaluation')

    sex = fields.Function(fields.Selection([
        (None, ''),
        ('m', 'Male'),
        ('f', 'Female'),
        ], 'Sex'), 'get_patient_sex', searcher='search_patient_sex')

    health_professional = fields.Many2One(
        'gnuhealth.healthprofessional', 'Health Professional',
        help="Health professional / Ophthalmologist / OptoMetrist"
        )

    # there are two types of charts, a meter chart.. 6/.. val
    # and ft chart.. 200/...
    snells_chart = [
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
    # vision test using snells chart
    rdva = fields.Selection(snells_chart, 'RDVA',
                            help="Right Eye Vision of Patient without aid",
                            sort=False)
    ldva = fields.Selection(snells_chart, 'LDVA',
                            help="Left Eye Vision of Patient without aid",
                            sort=False)
    # vision test using pinhole accurate manual testing
    rdva_pinhole = fields.Selection(snells_chart, 'RDVA',
                                    help="Right Eye Vision Using Pin Hole",
                                    sort=False)
    ldva_pinhole = fields.Selection(snells_chart, 'LDVA',
                                    help="Left Eye Vision Using Pin Hole",
                                    sort=False)
    # vison testing with glasses just to assess what the patient sees with
    # his existing aid # useful esp with vision syndroms that are not
    # happening because of the lens
    rdva_aid = fields.Selection(snells_chart, 'RDVA AID',
                                help="Vision with glasses or contact lens",
                                sort=False)
    ldva_aid = fields.Selection(snells_chart, 'LDVA AID',
                                help="Vision with glasses or contact lens",
                                sort=False)

    # spherical
    rspherical = fields.Float('Right Eye Spherical')
    lspherical = fields.Float('Left Eye Spherical')

    # cylinder
    rcylinder = fields.Float('Right Eye Cylinder')
    lcylinder = fields.Float('Left Eye Cylinder')
    
    #axis
    raxis = fields.Float('Right Eye Axis')
    laxis = fields.Float('Left Eye Axis')

    # near vision testing ie. long sight.. you will get it when u cross 40
    # its also thinning of the lens.. the focus falls behind the retina
    # in case of distant vision the focus does not reach retina
    
    rnv_add = fields.Float('Right Eye Best Corrected NV Add')
    lnv_add = fields.Float('Left Eye Best Corrected NV Add')
    
    rnv = fields.Selection(near_vision_chart, 'RNV',
                           help="Right Eye Near Vision", sort=False)
    lnv = fields.Selection(near_vision_chart, 'LNV',
                           help="Left Eye Near Vision", sort=False)

    # after the above tests the optometrist or doctor comes to a best conclusion
    # best corrected visual acuity
    # the above values are from autorefraction
    # the doctors decision is final
    # and there could be changes in values of cylinder, spherical and axis
    # these values will go into final prescription of glasses or contact lens
    # by default these values should be auto populated 
    # and should be modifiable by an ophthalmologist
    rbcva_spherical = fields.Float('Right Eye Best Corrected Spherical')
    lbcva_spherical = fields.Float('Left Eye Best Corrected Spherical')

    rbcva_cylinder = fields.Float('Right Eye Best Corrected Cylinder')
    lbcva_cylinder = fields.Float('Left Eye Best Corrected Cylinder')

    rbcva_axis = fields.Float('Right Eye Best Corrected Axis')
    lbcva_axis = fields.Float('Left Eye Best Corrected Axis')

    rbcva = fields.Selection(snells_chart, 'RBCVA', 
                help="Right Eye Best Corrected VA", sort=False)
    lbcva = fields.Selection(snells_chart, 'LBCVA', 
                help="Left Eye Best Corrected VA", sort=False)
    
    rbcva_nv_add = fields.Float('Right Eye Best Corrected NV Add')
    lbcva_nv_add = fields.Float('Left Eye Best Corrected NV Add')

    rbcva_nv = fields.Selection(near_vision_chart, 'RBCVANV', 
                help="Right Eye Best Corrected Near Vision", sort=False)
    lbcva_nv = fields.Selection(near_vision_chart, 'LBCVANV' , 
                help="Left Eye Best Corrected Near Vision", sort=False)        
        
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
    optometry_notes = fields.Text ('Notes')
    
    #this test is done using a prism fixed on a slit lamp
    #the reading is obtained from the slitlamp knobs
    rschiotz_iop = fields.Float('IOP Right Schiotz ')
    lschiotz_iop = fields.Float('IOP Left Schiotz')
    
    #this is a digital testing, using a machine
    #as it suggest, it does not touch the lens
    #it uses stream of air to get the pressure of the eye
    rnct_iop = fields.Float('IOP Right NCT')
    lnct_iop = fields.Float('IOP Left NCT')
    
    #the traditional way of using the goldmann apparatus
    #it looks like a compass /divider in instrument box,
    rgoldmann_iop = fields.Float('IOP Right Goldmann')
    lgoldmann_iop = fields.Float('IOP Left Goldmann')
    
    
    rsyringing = fields.Selection([  
            (None,''),
            ("False","False"),
            ("True","True"),
        ],'RSYR',help="Syringing Right",sort=False)

    lsyringing = fields.Selection([  
            (None,''),
            ("False","False"),
            ("True","True"),
        ],'LSYR',help="Syringing Left",sort=False)
        
    #Squint
    rsquint = fields.Selection([  
            (None,""),
            ("False","False"),
            ("True","True"),
        ],'RSQUINT',help="Syringing Right",sort=False)

    lsquint = fields.Selection([  
            (None,""),
            ("False","False"),
            ("True","True"),
        ],'LSQUINT',help="Syringing Left",sort=False)
        
    
    findings = fields.One2Many(
        'gnuhealth.ophthalmology.findings', 'name',
        'Findings')


    def patient_age_at_evaluation(self, name):

        if (self.patient.name.dob):
            dob = datetime.strptime(str(self.patient.name.dob), '%Y-%m-%d')

            if (self.visit_date):
                evaluation_start = datetime.strptime(
                    str(self.visit_date), '%Y-%m-%d %H:%M:%S')
                delta = relativedelta(self.visit_date, dob)

                years_months_days = str(
                    delta.years) + 'y ' \
                    + str(delta.months) + 'm ' \
                    + str(delta.days) + 'd'
            else:
                years_months_days = 'No evaluation Date !'
        else:
            years_months_days = 'No DoB !'

        return years_months_days


    def get_patient_sex(self, name):
        return self.patient.sex

    @classmethod
    def search_patient_sex(cls, name, clause):
        res = []
        value = clause[2]
        res.append(('patient.name.sex', clause[1], value))
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
    def default_health_professional():
        pool = Pool()
        HealthProf= pool.get('gnuhealth.healthprofessional')
        health_professional = HealthProf.get_health_professional()
        return health_professional


    # Show the sex and age upon entering the patient 
    # These two are function fields (don't exist at DB level)
    @fields.depends('patient')
    def on_change_patient(self):
        sex=None
        age=''
        self.sex = self.patient.sex
        self.computed_age = self.patient.age

    @classmethod
    @ModelView.button
    def confirmed(cls):
        return
    
#end


# class OphthalmologyPatientData(ModelSQL, ModelView):
#     __name__ = 'gnuhealth.patient'
#     
#end



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
