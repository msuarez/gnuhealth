from trytond.pool import Pool
from .health_ophthalmology import *

def register():
    Pool.register(
        OphthalmologyLidFindingsList,
        OphthalmologyNCSFindingsList,
        OphthalmologyConjunctivaFindingsList,
        OphthalmologyCorneaFindingsList,
        OphthalmologyIrisFindingsList,
        OphthalmologyAnteriorChamberFindingsList,
        OphthalmologyPupilFindingsList,
        OphthalmologyLensFindingsList,
        OphthalmologyVitreousFindingsList,
        OphthalmologyFundusDiscFindingsList,
        OphthalmologyFundusMaculaFindingsList,
        OphthalmologyFundusBackgroundFindingsList,
        OphthalmologyFundusVesslesFindingsList,
        OphthalmologyMiscFindingsList,
        
        OphthalmologyFindings,
    
        OphthalmologyLidFindings,
        OphthalmologyNCSFindings,
        OphthalmologyConjunctivaFindings,
        OphthalmologyCorneaFindings,
        OphthalmologyIrisFindings,
        OphthalmologyAnteriorChamberFindings,
        OphthalmologyPupilFindings,
        OphthalmologyLensFindings,
        OphthalmologyVitreousFindings,
        OphthalmologyFundusDiscFindings,
        OphthalmologyFundusMaculaFindings,
        OphthalmologyFundusBackgroundFindings,
        OphthalmologyFundusVesslesFindings,
        OphthalmologyMiscFindings,
    
        Ophthalmology,
        module='health_ophthalmology', type_='model')