from flask import Blueprint
from flask.ext.restful import Resource
from health_fhir import health_Conformance
from extensions import tryton, Api

# This sits on the root
base_endpoint = Blueprint('base_endpoint', __name__,
                                template_folder='templates')


# Initialize api restful
api = Api(base_endpoint)

# Don't require authentication
# on this resource
class Conformance(Resource):
    def get(self):
        """Conformance interaction"""
        c = health_Conformance()
        return c, 200

    def options(self):
        """Conformance interaction"""
        c = health_Conformance()
        return c, 200

api.add_resource(Conformance, '', 'metadata') #adds '/' on metadata route on register
