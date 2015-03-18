from StringIO import StringIO
from operator import attrgetter
from .datastore import find_record
import server.fhir as supermod

# URL values
try:
    from flask import url_for
    RUN_FLASK=True
except:
    from .datastore import dumb_url_generate
    RUN_FLASK=False

class Immunization_Map:
    """Holds essential mappings and information for
        the Immunization class
    """

    root_search=[]

    resource_search_params={
            '_id': 'token',
            '_language': None,
            'date': None,
            'dose-sequence': None,
            'identifier': None,
            'location': None,
            'lot-number': None,
            'manufacturer': None,
            'performer': None,
            'reaction': None,
            'reaction-date': None,
            'reason': None,
            'refusal-reason': None,
            'refused': None,
            'requester': None,
            'subject': None,
            'vaccine-type': None}

    chain_map={ 'subject': 'Patient',
            'performer': 'Practitioner',
            'requester': 'Practitioner',
            'reaction': 'Observation', #TODO AdverseReaction
            'location': 'Location', #TODO
            'manufacturer': 'Organization'} #TODO
    search_mapping={
            '_id': ['id']
                }

    url_prefixes={}
    model_mapping={'gnuhealth.vaccination':
            {
            }}


class health_Immunization(supermod.Immunization, Immunization_Map):
    pass

supermod.Immunization.subclass=health_Immunization
