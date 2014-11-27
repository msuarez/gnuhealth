from flask import Blueprint, request, current_app, make_response, url_for
from flask.ext.restful import Resource, abort, reqparse
from StringIO import StringIO
from lxml.etree import XMLSyntaxError
from health_fhir import health_Conformance
from extensions import tryton
from flask.ext.restful import Api
import lxml
import json
import os.path
import sys

# This sits on the root
base_endpoint = Blueprint('base_endpoint', __name__,
                                template_folder='templates')


# Initialize api restful
api = Api(base_endpoint)

class Conformance(Resource):
    def get(self):
        """Conformance interaction"""
        c = health_Conformance()
        return c, 200

    def options(self):
        """Conformance interaction"""
        c = health_Conformance()
        return c, 200

api.add_resource(Conformance,
                        '',
                        '/metadata')

@api.representation('xml')
@api.representation('text/xml')
@api.representation('application/xml')
@api.representation('application/xml+fhir')
def output_xml(data, code, headers=None):
    if hasattr(data, 'export_to_xml_string'):
        resp = make_response(data.export_to_xml_string(), code)
    elif hasattr(data, 'export'):
        output=StringIO()
        data.export(outfile=output, namespacedef_='xmlns="http://hl7.org/fhir"', pretty_print=False, level=4)
        content = output.getvalue()
        output.close()
        resp = make_response(content, code)
    else:
        try:
            resp = make_response(data['message'], code)
        except:
            resp = make_response(data, code)
    resp.headers.extend(headers or {})
    resp.headers['Content-type']='application/xml+fhir' #Return proper type
    return resp
