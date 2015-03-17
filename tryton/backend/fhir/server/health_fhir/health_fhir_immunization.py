from StringIO import StringIO
from operator import attrgetter
from .datastore import find_record
import server.fhir as supermod

class health_Immunization(supermod.Immunization):
    pass

supermod.Immunization.subclass=health_Immunization
