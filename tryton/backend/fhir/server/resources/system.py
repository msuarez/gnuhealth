from flask import Blueprint
from flask.ext.restful import Resource
from server.health_fhir import health_Conformance

# NOTE: Don't require authentication
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
