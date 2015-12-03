from trytond.pool import Pool
from .health_ophthalmology import *

def register():
    Pool.register(
        OphthalmologyEvaluation,
        OphthalmologyFindings,    
        module='health_ophthalmology', type_='model')
