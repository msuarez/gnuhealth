from trytond.model import ModelView, ModelSQL, fields
from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta, date

__all__ = [
    'OphthalmologyLidFindingsList',
    'OphthalmologyNCSFindingsList',
    'OphthalmologyConjunctivaFindingsList',
    'OphthalmologyCorneaFindingsList',
    'OphthalmologyIrisFindingsList',
    'OphthalmologyAnteriorChamberFindingsList',
    'OphthalmologyPupilFindingsList',
    'OphthalmologyLensFindingsList',
    'OphthalmologyVitreousFindingsList',
    'OphthalmologyFundusDiscFindingsList',
    'OphthalmologyFundusMaculaFindingsList',
    'OphthalmologyFundusBackgroundFindingsList',
    'OphthalmologyFundusVesslesFindingsList',
    'OphthalmologyMiscFindingsList',
    
    'OphthalmologyFindings',
    
    'OphthalmologyLidFindings',
    'OphthalmologyNCSFindings',
    'OphthalmologyConjunctivaFindings',
    'OphthalmologyCorneaFindings',
    'OphthalmologyIrisFindings',
    'OphthalmologyAnteriorChamberFindings',
    'OphthalmologyPupilFindings',
    'OphthalmologyLensFindings',
    'OphthalmologyVitreousFindings',
    'OphthalmologyFundusDiscFindings',
    'OphthalmologyFundusMaculaFindings',
    'OphthalmologyFundusBackgroundFindings',
    'OphthalmologyFundusVesslesFindings',
    'OphthalmologyMiscFindings',
      
    'Ophthalmology',
    ]



class Ophthalmology(ModelSQL, ModelView):
    'Ophthalmology'
    __name__ = 'gnuhealth.ophthalmology'

    patient = fields.Many2One('gnuhealth.patient', 'Patient', required=True)
    # todo placeholder for age from gnu health
    patient_age = fields.Char('Age')
    visit_date = fields.DateTime('Date', help="Date of Consultation")

    # toto this should be the name of the person who is entering the data
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
            (None,""),
            ("False","False"),
            ("True","True"),
           
        ],'RSYR',help="Syringing Right",sort=False)

    lsyringing = fields.Selection([  
            (None,""),
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
    
    patient = fields.Many2One('gnuhealth.patient', 'Patient', required=True)
    # todo placeholder for age from gnu health
    patient_age = fields.Char('Age')
    visit_date = fields.DateTime('Date', help="Date of Consultation")

    # toto this should be the name of the person who is entering the data
    health_professional = fields.Many2One(
        'gnuhealth.healthprofessional', 'Health Professional',
        help="Health professional / Ophthalmologist / OptoMetrist"
        )
    
    lid_findings = fields.One2Many(
        'gnuhealth.ophthalmology.lid.findings','findings', 'Lid Findings',
        help="enter lid findings"
    )
    
    ncs_findings = fields.One2Many(
        'gnuhealth.ophthalmology.ncs.findings','findings', 'NCS Findings',
        help="enter Naso Lacrimal System findings"
    )
    
    conjunctiva_findings = fields.One2Many(
        'gnuhealth.ophthalmology.conjunctiva.findings','findings',
        'Conjunctiva Findings',
        help="enter conjunctiva findings"
    )
    
    cornea_findings = fields.One2Many(
        'gnuhealth.ophthalmology.cornea.findings','findings', 'Cornea Findings',
        help="enter cornea findings"
    )
    
    anteriorchamber_findings = fields.One2Many(
        'gnuhealth.ophthalmology.anteriorchamber.findings','findings',
        'AnteriorChamber Findings',
        help="enter anteriorchamber findings"
    )
    
    iris_findings = fields.One2Many(
        'gnuhealth.ophthalmology.iris.findings','findings', 'Iris Findings',
        help="enter iris findings"
    )
    
    pupil_findings = fields.One2Many(
        'gnuhealth.ophthalmology.pupil.findings','findings', 'Pupil Findings',
        help="enter pupil findings"
    )
    
    lens_findings = fields.One2Many(
        'gnuhealth.ophthalmology.lens.findings','findings', 'Lens Findings',
        help="enter lens findings"
    )
    
    vitreous_findings = fields.One2Many(
        'gnuhealth.ophthalmology.vitreous.findings','findings', 'Vitreous Findings',
        help="enter vitreous findings"
    )
    
    ###########################################################
    
    fundusdisc_findings = fields.One2Many(
        'gnuhealth.ophthalmology.fundusdisc.findings','findings',
        'FundusDisc Findings',
        help="enter fundusdisc findings"
    )
    
    fundusmacula_findings = fields.One2Many(
        'gnuhealth.ophthalmology.fundusmacula.findings','findings',
        'FundusMacula Findings',
        help="enter fundusmacula findings"
    )
    
    fundusbackground_findings = fields.One2Many(
        'gnuhealth.ophthalmology.fundusbackground.findings','findings',
        'FundusBackground Findings',
        help="enter fundusbackground findings"
    )
    
    fundusvessles_findings = fields.One2Many(
        'gnuhealth.ophthalmology.fundusvessles.findings','findings', 
        'fundusvessles Findings',
        help="enter fundusvessles findings"
    )
    
    misc_findings = fields.One2Many(
        'gnuhealth.ophthalmology.misc.findings','findings', 'Misc Findings',
        help="enter misc findings"
    )
    
    
    
    # Use the following as template and comment it after use
    #
    # procedures = fields.One2Many(
    #     'gnuhealth.operation', 'name', 'Procedures',
    #     help="List of the procedures in the surgery. Please enter the first "
    #     "one as the main procedure")
    # 

    
# end

# lids
class OphthalmologyLidFindings(ModelSQL,ModelView):
    'Ophthalmology Lid Findings'
    __name__ ='gnuhealth.ophthalmology.lid.findings'
    findings = fields.Many2One('gnuhealth.ophthalmology.findings','lid_findings')
    values = fields.Many2One( 'gnuhealth.ophthalmology.lid.findings.list',
        'Findings', required=True, select=True, help="Finding Lists for Lid")
    reye = fields.Boolean("Right Eye")
    leye = fields.Boolean("Left Eye")
    both_eye = fields.Boolean("Both Eyes")
    notes = fields.Char('Notes')
    
    #to do
    # add a function
    # to auto update l & r if b is true
    
    @fields.depends('both_eye')
    def on_change_with_reye(self):
        return self.both_eye
    
    @fields.depends('both_eye')
    def on_change_with_leye(self):
        return self.both_eye
    
    @fields.depends('reye','leye')
    def on_change_with_both_eye(self):
        return self.reye & self.leye
    
#end

class OphthalmologyLidFindingsList(ModelSQL,ModelView):
    'Ophthalmology Lid Findings List'
    __name__='gnuhealth.ophthalmology.lid.findings.list'
    
    name = fields.Char('Findings')
    description = fields.Char('Long Text')

    # Search by the Procedure code or the description
    @classmethod
    def search_rec_name(cls, name, clause):
        field = None
        for field in ('name', 'description'):
            findings = cls.search([(field,) + tuple(clause[1:])], limit=1)
            if findings:
                break
        if findings:
            return [(field,) + tuple(clause[1:])]
        return [(cls._rec_name,) + tuple(clause[1:])]

    # Include code + description in result
    def get_rec_name(self, name):
        return (self.name + ' : ' + self.description)

#end

# ncs
class OphthalmologyNCSFindings(ModelSQL,ModelView):
    'Ophthalmology NCS Findings'
    __name__ ='gnuhealth.ophthalmology.ncs.findings'
    findings = fields.Many2One('gnuhealth.ophthalmology.findings','ncs_findings')
    values = fields.Many2One( 'gnuhealth.ophthalmology.ncs.findings.list',
        'Findings', required=True, select=True, help="Finding Lists for NCS")
    reye = fields.Boolean("Right Eye")
    leye = fields.Boolean("Left Eye")
    both_eye = fields.Boolean("Both Eyes")
    notes = fields.Char('Notes')
    
    #to do
    # add a function
    # to auto update l & r if b is true
    
    @fields.depends('both_eye')
    def on_change_with_reye(self):
        return self.both_eye
    
    @fields.depends('both_eye')
    def on_change_with_leye(self):
        return self.both_eye
    
    @fields.depends('reye','leye')
    def on_change_with_both_eye(self):
        return self.reye & self.leye
    
#end

class OphthalmologyNCSFindingsList(ModelSQL,ModelView):
    'Ophthalmology NCS Findings List'
    __name__='gnuhealth.ophthalmology.ncs.findings.list'
    
    name = fields.Char('Findings')
    description = fields.Char('Long Text')

    # Search by the Procedure code or the description
    @classmethod
    def search_rec_name(cls, name, clause):
        field = None
        for field in ('name', 'description'):
            findings = cls.search([(field,) + tuple(clause[1:])], limit=1)
            if findings:
                break
        if findings:
            return [(field,) + tuple(clause[1:])]
        return [(cls._rec_name,) + tuple(clause[1:])]

    # Include code + description in result
    def get_rec_name(self, name):
        return (self.name + ' : ' + self.description)

#end

#Conjunctiva

class OphthalmologyConjunctivaFindings(ModelSQL,ModelView):
    'Ophthalmology Conjunctiva Findings'
    __name__ ='gnuhealth.ophthalmology.conjunctiva.findings'
    findings = fields.Many2One('gnuhealth.ophthalmology.findings',
        'conjunctiva_findings')
    values = fields.Many2One( 'gnuhealth.ophthalmology.conjunctiva.findings.list','Findings', 
        required=True, select=True, help="Finding Lists for Conjunctiva")
    reye = fields.Boolean("Right Eye")
    leye = fields.Boolean("Left Eye")
    both_eye = fields.Boolean("Both Eyes")
    notes = fields.Char('Notes')
    
    #to do
    # add a function
    # to auto update l & r if b is true
    
    @fields.depends('both_eye')
    def on_change_with_reye(self):
        return self.both_eye
    
    @fields.depends('both_eye')
    def on_change_with_leye(self):
        return self.both_eye
    
    @fields.depends('reye','leye')
    def on_change_with_both_eye(self):
        return self.reye & self.leye
    
#end


class OphthalmologyConjunctivaFindingsList(ModelSQL,ModelView):
    'Ophthalmology Conjunctiva Findings List'
    __name__='gnuhealth.ophthalmology.conjunctiva.findings.list'
    
    name = fields.Char('Findings')
    description = fields.Char('Long Text')

    # Search by the Procedure code or the description
    @classmethod
    def search_rec_name(cls, name, clause):
        field = None
        for field in ('name', 'description'):
            findings = cls.search([(field,) + tuple(clause[1:])], limit=1)
            if findings:
                break
        if findings:
            return [(field,) + tuple(clause[1:])]
        return [(cls._rec_name,) + tuple(clause[1:])]

    # Include code + description in result
    def get_rec_name(self, name):
        return (self.name + ' : ' + self.description)

#end

#Cornea

class OphthalmologyCorneaFindings(ModelSQL,ModelView):
    'Ophthalmology Cornea Findings'
    __name__ ='gnuhealth.ophthalmology.cornea.findings'
    findings = fields.Many2One('gnuhealth.ophthalmology.findings','cornea_findings')
    values = fields.Many2One( 'gnuhealth.ophthalmology.cornea.findings.list',
        'Findings', required=True, select=True, help="Finding Lists for Cornea")
    reye = fields.Boolean("Right Eye")
    leye = fields.Boolean("Left Eye")
    both_eye = fields.Boolean("Both Eyes")
    notes = fields.Char('Notes')
    
    #to do
    # add a function
    # to auto update l & r if b is true
    
    @fields.depends('both_eye')
    def on_change_with_reye(self):
        return self.both_eye
    
    @fields.depends('both_eye')
    def on_change_with_leye(self):
        return self.both_eye
    
    @fields.depends('reye','leye')
    def on_change_with_both_eye(self):
        return self.reye & self.leye
    
#end


class OphthalmologyCorneaFindingsList(ModelSQL,ModelView):
    'Ophthalmology Cornea Findings List'
    __name__='gnuhealth.ophthalmology.cornea.findings.list'
    
    name = fields.Char('Findings')
    description = fields.Char('Long Text')

    # Search by the Procedure code or the description
    @classmethod
    def search_rec_name(cls, name, clause):
        field = None
        for field in ('name', 'description'):
            findings = cls.search([(field,) + tuple(clause[1:])], limit=1)
            if findings:
                break
        if findings:
            return [(field,) + tuple(clause[1:])]
        return [(cls._rec_name,) + tuple(clause[1:])]

    # Include code + description in result
    def get_rec_name(self, name):
        return (self.name + ' : ' + self.description)

#end

#Iris

class OphthalmologyIrisFindings(ModelSQL,ModelView):
    'Ophthalmology Iris Findings'
    __name__ ='gnuhealth.ophthalmology.iris.findings'
    findings = fields.Many2One('gnuhealth.ophthalmology.findings','iris_findings')
    values = fields.Many2One( 'gnuhealth.ophthalmology.iris.findings.list',
        'Findings', required=True, select=True, help="Finding Lists for Iris")
    reye = fields.Boolean("Right Eye")
    leye = fields.Boolean("Left Eye")
    both_eye = fields.Boolean("Both Eyes")
    notes = fields.Char('Notes')
    
    #to do
    # add a function
    # to auto update l & r if b is true
    
    @fields.depends('both_eye')
    def on_change_with_reye(self):
        return self.both_eye
    
    @fields.depends('both_eye')
    def on_change_with_leye(self):
        return self.both_eye
    
    @fields.depends('reye','leye')
    def on_change_with_both_eye(self):
        return self.reye & self.leye
    
#end


class OphthalmologyIrisFindingsList(ModelSQL,ModelView):
    'Ophthalmology Iris Findings List'
    __name__='gnuhealth.ophthalmology.iris.findings.list'
    
    name = fields.Char('Findings')
    description = fields.Char('Long Text')

    # Search by the Procedure code or the description
    @classmethod
    def search_rec_name(cls, name, clause):
        field = None
        for field in ('name', 'description'):
            findings = cls.search([(field,) + tuple(clause[1:])], limit=1)
            if findings:
                break
        if findings:
            return [(field,) + tuple(clause[1:])]
        return [(cls._rec_name,) + tuple(clause[1:])]

    # Include code + description in result
    def get_rec_name(self, name):
        return (self.name + ' : ' + self.description)

#end

#Anterior Chamber

class OphthalmologyAnteriorChamberFindings(ModelSQL,ModelView):
    'Ophthalmology AnteriorChamber Findings'
    __name__ ='gnuhealth.ophthalmology.anteriorchamber.findings'
    findings = fields.Many2One('gnuhealth.ophthalmology.findings',
        'anteriorchamber_findings')
    values = fields.Many2One( 'gnuhealth.ophthalmology.anteriorchamber.findings.list',
        'Findings', required=True, select=True,
        help="Finding Lists for AnteriorChamber")
    reye = fields.Boolean("Right Eye")
    leye = fields.Boolean("Left Eye")
    both_eye = fields.Boolean("Both Eyes")
    notes = fields.Char('Notes')
    
    #to do
    # add a function
    # to auto update l & r if b is true and b if l & r 1 1 -> 1 1_> 1 1 
    
    @fields.depends('both_eye')
    def on_change_with_reye(self):
        return self.both_eye
    
    @fields.depends('both_eye')
    def on_change_with_leye(self):
        return self.both_eye
    
    @fields.depends('reye','leye')
    def on_change_with_both_eye(self):
        return self.reye & self.leye
    
#end


class OphthalmologyAnteriorChamberFindingsList(ModelSQL,ModelView):
    'Ophthalmology AnteriorChamber Findings List'
    __name__='gnuhealth.ophthalmology.anteriorchamber.findings.list'
    
    name = fields.Char('Findings')
    description = fields.Char('Long Text')

    # Search by the Procedure code or the description
    @classmethod
    def search_rec_name(cls, name, clause):
        field = None
        for field in ('name', 'description'):
            findings = cls.search([(field,) + tuple(clause[1:])], limit=1)
            if findings:
                break
        if findings:
            return [(field,) + tuple(clause[1:])]
        return [(cls._rec_name,) + tuple(clause[1:])]

    # Include code + description in result
    def get_rec_name(self, name):
        return (self.name + ' : ' + self.description)

#end

# Pupil

class OphthalmologyPupilFindings(ModelSQL,ModelView):
    'Ophthalmology Pupil Findings'
    __name__ ='gnuhealth.ophthalmology.pupil.findings'
    findings = fields.Many2One('gnuhealth.ophthalmology.findings','pupil_findings')
    values = fields.Many2One( 'gnuhealth.ophthalmology.pupil.findings.list',
        'Findings', required=True, select=True, help="Finding Lists for Pupil")
    reye = fields.Boolean("Right Eye")
    leye = fields.Boolean("Left Eye")
    both_eye = fields.Boolean("Both Eyes")
    notes = fields.Char('Notes')
    
    #to do
    # add a function
    # to auto update l & r if b is true and b if l & r 1 1 -> 1 1_> 1 1 
    
    @fields.depends('both_eye')
    def on_change_with_reye(self):
        return self.both_eye
    
    @fields.depends('both_eye')
    def on_change_with_leye(self):
        return self.both_eye
    
    @fields.depends('reye','leye')
    def on_change_with_both_eye(self):
        return self.reye & self.leye
    
#end


class OphthalmologyPupilFindingsList(ModelSQL,ModelView):
    'Ophthalmology Pupil Findings List'
    __name__='gnuhealth.ophthalmology.pupil.findings.list'
    
    name = fields.Char('Findings')
    description = fields.Char('Long Text')

    # Search by the Procedure code or the description
    @classmethod
    def search_rec_name(cls, name, clause):
        field = None
        for field in ('name', 'description'):
            findings = cls.search([(field,) + tuple(clause[1:])], limit=1)
            if findings:
                break
        if findings:
            return [(field,) + tuple(clause[1:])]
        return [(cls._rec_name,) + tuple(clause[1:])]

    # Include code + description in result
    def get_rec_name(self, name):
        return (self.name + ' : ' + self.description)

#end

###########################################################

# Lens

class OphthalmologyLensFindings(ModelSQL,ModelView):
    'Ophthalmology Lens Findings'
    __name__ ='gnuhealth.ophthalmology.lens.findings'
    findings = fields.Many2One('gnuhealth.ophthalmology.findings','lens_findings')
    values = fields.Many2One( 'gnuhealth.ophthalmology.lens.findings.list',
        'Findings', required=True, select=True, help="Finding Lists for Lens")
    reye = fields.Boolean("Right Eye")
    leye = fields.Boolean("Left Eye")
    both_eye = fields.Boolean("Both Eyes")
    notes = fields.Char('Notes')
    
    #to do
    # add a function
    # to auto update l & r if b is true and b if l & r 1 1 -> 1 1_> 1 1 
    
    @fields.depends('both_eye')
    def on_change_with_reye(self):
        return self.both_eye
    
    @fields.depends('both_eye')
    def on_change_with_leye(self):
        return self.both_eye
    
    @fields.depends('reye','leye')
    def on_change_with_both_eye(self):
        return self.reye & self.leye
    
#end


class OphthalmologyLensFindingsList(ModelSQL,ModelView):
    'Ophthalmology Lens Findings List'
    __name__='gnuhealth.ophthalmology.lens.findings.list'
    
    name = fields.Char('Findings')
    description = fields.Char('Long Text')

    # Search by the Procedure code or the description
    @classmethod
    def search_rec_name(cls, name, clause):
        field = None
        for field in ('name', 'description'):
            findings = cls.search([(field,) + tuple(clause[1:])], limit=1)
            if findings:
                break
        if findings:
            return [(field,) + tuple(clause[1:])]
        return [(cls._rec_name,) + tuple(clause[1:])]

    # Include code + description in result
    def get_rec_name(self, name):
        return (self.name + ' : ' + self.description)

#end

# Vitreous

class OphthalmologyVitreousFindings(ModelSQL,ModelView):
    'Ophthalmology Vitreous Findings'
    __name__ ='gnuhealth.ophthalmology.vitreous.findings'
    findings = fields.Many2One('gnuhealth.ophthalmology.findings','vitreous_findings')
    values = fields.Many2One( 'gnuhealth.ophthalmology.vitreous.findings.list',
        'Findings', required=True, select=True, help="Finding Lists for Vitreous")
    reye = fields.Boolean("Right Eye")
    leye = fields.Boolean("Left Eye")
    both_eye = fields.Boolean("Both Eyes")
    notes = fields.Char('Notes')
    
    #to do
    # add a function
    # to auto update l & r if b is true and b if l & r 1 1 -> 1 1_> 1 1 
    
    @fields.depends('both_eye')
    def on_change_with_reye(self):
        return self.both_eye
    
    @fields.depends('both_eye')
    def on_change_with_leye(self):
        return self.both_eye
    
    @fields.depends('reye','leye')
    def on_change_with_both_eye(self):
        return self.reye & self.leye
    
#end


class OphthalmologyVitreousFindingsList(ModelSQL,ModelView):
    'Ophthalmology Vitreous Findings List'
    __name__='gnuhealth.ophthalmology.vitreous.findings.list'
    
    name = fields.Char('Findings')
    description = fields.Char('Long Text')

    # Search by the Procedure code or the description
    @classmethod
    def search_rec_name(cls, name, clause):
        field = None
        for field in ('name', 'description'):
            findings = cls.search([(field,) + tuple(clause[1:])], limit=1)
            if findings:
                break
        if findings:
            return [(field,) + tuple(clause[1:])]
        return [(cls._rec_name,) + tuple(clause[1:])]

    # Include code + description in result
    def get_rec_name(self, name):
        return (self.name + ' : ' + self.description)

#end

# FundusDisc

class OphthalmologyFundusDiscFindings(ModelSQL,ModelView):
    'Ophthalmology FundusDisc Findings'
    __name__ ='gnuhealth.ophthalmology.fundusdisc.findings'
    findings = fields.Many2One('gnuhealth.ophthalmology.findings','fundusdisc_findings')
    values = fields.Many2One( 'gnuhealth.ophthalmology.fundusdisc.findings.list',
        'Findings', required=True, select=True, help="Finding Lists for FundusDisc")
    reye = fields.Boolean("Right Eye")
    leye = fields.Boolean("Left Eye")
    both_eye = fields.Boolean("Both Eyes")
    notes = fields.Char('Notes')
    
    #to do
    # add a function
    # to auto update l & r if b is true and b if l & r 1 1 -> 1 1_> 1 1 
    
    @fields.depends('both_eye')
    def on_change_with_reye(self):
        return self.both_eye
    
    @fields.depends('both_eye')
    def on_change_with_leye(self):
        return self.both_eye
    
    @fields.depends('reye','leye')
    def on_change_with_both_eye(self):
        return self.reye & self.leye
    
#end


class OphthalmologyFundusDiscFindingsList(ModelSQL,ModelView):
    'Ophthalmology FundusDisc Findings List'
    __name__='gnuhealth.ophthalmology.fundusdisc.findings.list'
    
    name = fields.Char('Findings')
    description = fields.Char('Long Text')

    # Search by the Procedure code or the description
    @classmethod
    def search_rec_name(cls, name, clause):
        field = None
        for field in ('name', 'description'):
            findings = cls.search([(field,) + tuple(clause[1:])], limit=1)
            if findings:
                break
        if findings:
            return [(field,) + tuple(clause[1:])]
        return [(cls._rec_name,) + tuple(clause[1:])]

    # Include code + description in result
    def get_rec_name(self, name):
        return (self.name + ' : ' + self.description)

#end



# Fundus Macula

class OphthalmologyFundusMaculaFindings(ModelSQL,ModelView):
    'Ophthalmology FundusMacula Findings'
    __name__ ='gnuhealth.ophthalmology.fundusmacula.findings'
    findings = fields.Many2One('gnuhealth.ophthalmology.findings','fundusmacula_findings')
    values = fields.Many2One( 'gnuhealth.ophthalmology.fundusmacula.findings.list',
        'Findings', required=True, select=True, help="Finding Lists for FundusMacula")
    reye = fields.Boolean("Right Eye")
    leye = fields.Boolean("Left Eye")
    both_eye = fields.Boolean("Both Eyes")
    notes = fields.Char('Notes')
    
    #to do
    # add a function
    # to auto update l & r if b is true and b if l & r 1 1 -> 1 1_> 1 1 
    
    @fields.depends('both_eye')
    def on_change_with_reye(self):
        return self.both_eye
    
    @fields.depends('both_eye')
    def on_change_with_leye(self):
        return self.both_eye
    
    @fields.depends('reye','leye')
    def on_change_with_both_eye(self):
        return self.reye & self.leye
    
#end


class OphthalmologyFundusMaculaFindingsList(ModelSQL,ModelView):
    'Ophthalmology FundusMacula Findings List'
    __name__='gnuhealth.ophthalmology.fundusmacula.findings.list'
    
    name = fields.Char('Findings')
    description = fields.Char('Long Text')

    # Search by the Procedure code or the description
    @classmethod
    def search_rec_name(cls, name, clause):
        field = None
        for field in ('name', 'description'):
            findings = cls.search([(field,) + tuple(clause[1:])], limit=1)
            if findings:
                break
        if findings:
            return [(field,) + tuple(clause[1:])]
        return [(cls._rec_name,) + tuple(clause[1:])]

    # Include code + description in result
    def get_rec_name(self, name):
        return (self.name + ' : ' + self.description)

#end



# FundusBackground
class OphthalmologyFundusBackgroundFindings(ModelSQL,ModelView):
    'Ophthalmology FundusBackground Findings'
    __name__ ='gnuhealth.ophthalmology.fundusbackground.findings'
    findings = fields.Many2One('gnuhealth.ophthalmology.findings','fundusbackground_findings')
    values = fields.Many2One( 'gnuhealth.ophthalmology.fundusbackground.findings.list',
        'Findings', required=True, select=True, help="Finding Lists for FundusBackground")
    reye = fields.Boolean("Right Eye")
    leye = fields.Boolean("Left Eye")
    both_eye = fields.Boolean("Both Eyes")
    notes = fields.Char('Notes')
    
    #to do
    # add a function
    # to auto update l & r if b is true and b if l & r 1 1 -> 1 1_> 1 1 
    
    @fields.depends('both_eye')
    def on_change_with_reye(self):
        return self.both_eye
    
    @fields.depends('both_eye')
    def on_change_with_leye(self):
        return self.both_eye
    
    @fields.depends('reye','leye')
    def on_change_with_both_eye(self):
        return self.reye & self.leye
    
#end


class OphthalmologyFundusBackgroundFindingsList(ModelSQL,ModelView):
    'Ophthalmology FundusBackground Findings List'
    __name__='gnuhealth.ophthalmology.fundusbackground.findings.list'
    
    name = fields.Char('Findings')
    description = fields.Char('Long Text')

    # Search by the Procedure code or the description
    @classmethod
    def search_rec_name(cls, name, clause):
        field = None
        for field in ('name', 'description'):
            findings = cls.search([(field,) + tuple(clause[1:])], limit=1)
            if findings:
                break
        if findings:
            return [(field,) + tuple(clause[1:])]
        return [(cls._rec_name,) + tuple(clause[1:])]

    # Include code + description in result
    def get_rec_name(self, name):
        return (self.name + ' : ' + self.description)

#end

# FundusVessles
class OphthalmologyFundusVesslesFindings(ModelSQL,ModelView):
    'Ophthalmology FundusVessles Findings'
    __name__ ='gnuhealth.ophthalmology.fundusvessles.findings'
    findings = fields.Many2One('gnuhealth.ophthalmology.findings','fundusvessles_findings')
    values = fields.Many2One( 'gnuhealth.ophthalmology.fundusvessles.findings.list',
    'Findings', required=True, select=True, help="Finding Lists for FundusVessles")
    reye = fields.Boolean("Right Eye")
    leye = fields.Boolean("Left Eye")
    both_eye = fields.Boolean("Both Eyes")
    notes = fields.Char('Notes')
    
    #to do
    # add a function
    # to auto update l & r if b is true and b if l & r 1 1 -> 1 1_> 1 1 
    
    @fields.depends('both_eye')
    def on_change_with_reye(self):
        return self.both_eye
    
    @fields.depends('both_eye')
    def on_change_with_leye(self):
        return self.both_eye
    
    @fields.depends('reye','leye')
    def on_change_with_both_eye(self):
        return self.reye & self.leye
    
#end


class OphthalmologyFundusVesslesFindingsList(ModelSQL,ModelView):
    'Ophthalmology FundusVessles Findings List'
    __name__='gnuhealth.ophthalmology.fundusvessles.findings.list'
    
    name = fields.Char('Findings')
    description = fields.Char('Long Text')

    # Search by the Procedure code or the description
    @classmethod
    def search_rec_name(cls, name, clause):
        field = None
        for field in ('name', 'description'):
            findings = cls.search([(field,) + tuple(clause[1:])], limit=1)
            if findings:
                break
        if findings:
            return [(field,) + tuple(clause[1:])]
        return [(cls._rec_name,) + tuple(clause[1:])]

    # Include code + description in result
    def get_rec_name(self, name):
        return (self.name + ' : ' + self.description)

#end

# Misc
class OphthalmologyMiscFindings(ModelSQL,ModelView):
    'Ophthalmology Misc Findings'
    __name__ ='gnuhealth.ophthalmology.misc.findings'
    findings = fields.Many2One('gnuhealth.ophthalmology.findings','misc_findings')
    values = fields.Many2One( 'gnuhealth.ophthalmology.misc.findings.list',
        'Findings', required=True, select=True, help="Finding Lists for Misc")
    reye = fields.Boolean("Right Eye")
    leye = fields.Boolean("Left Eye")
    both_eye = fields.Boolean("Both Eyes")
    notes = fields.Char('Notes')
    
    #to do
    # add a function
    # to auto update l & r if b is true and b if l & r 1 1 -> 1 1_> 1 1 
    
    @fields.depends('both_eye')
    def on_change_with_reye(self):
        return self.both_eye
    
    @fields.depends('both_eye')
    def on_change_with_leye(self):
        return self.both_eye
    
    @fields.depends('reye','leye')
    def on_change_with_both_eye(self):
        return self.reye & self.leye
    
#end


class OphthalmologyMiscFindingsList(ModelSQL,ModelView):
    'Ophthalmology Misc Findings List'
    __name__='gnuhealth.ophthalmology.misc.findings.list'
    
    name = fields.Char('Findings')
    description = fields.Char('Long Text')

    # Search by the Procedure code or the description
    @classmethod
    def search_rec_name(cls, name, clause):
        field = None
        for field in ('name', 'description'):
            findings = cls.search([(field,) + tuple(clause[1:])], limit=1)
            if findings:
                break
        if findings:
            return [(field,) + tuple(clause[1:])]
        return [(cls._rec_name,) + tuple(clause[1:])]

    # Include code + description in result
    def get_rec_name(self, name):
        return (self.name + ' : ' + self.description)

#end


# Use the following as template and comment it after use
# #
# class Operation(ModelSQL, ModelView):
#     'Operation - Surgical Procedures'
#     __name__ = 'gnuhealth.operation'
# 
#     name = fields.Many2One('gnuhealth.surgery', 'Surgery')
#     procedure = fields.Many2One(
#         'gnuhealth.procedure', 'Code', required=True, select=True,
#         help="Procedure Code, for example ICD-10-PCS or ICPM")
#     notes = fields.Text('Notes')
