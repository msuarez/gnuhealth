from flask_restful import Resource
from server.health_fhir import health_Conformance
from server.common import tryton

institution = tryton.pool.get('party.party')

@tryton.transaction()
def find_institution():
    try:
        i = institution.search_read([('is_institution', '=', True)],
                                        limit=1,
                                        fields_names=['name'])[0]
    except:
        i = {'name': 'GNU Health'}
    return i.get('name', 'GNU Health')

# NOTE: Don't require authentication on this resource
class Conformance(Resource):
    def get(self):
        """Conformance interaction"""
        c = health_Conformance(publisher=find_institution())
        return c, 200

    def options(self):
        """Conformance interaction"""
        c = health_Conformance(publisher=find_institution())
        return c, 200

__all__=['Conformance']
