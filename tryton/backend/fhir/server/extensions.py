from flask.ext.tryton import Tryton
from flask.ext.restful import Api as base_api
from flask.ext.restful import Resource as base_resource
from flask.ext.login import LoginManager, login_required
from utils import output_xml

#### Extensions
tryton = Tryton()
login_manager = LoginManager()

# Handle different outputs
class Api(base_api):
    def __init__(self, *args, **kwargs):
        super(Api, self).__init__(*args, **kwargs)
        self.representations = {
            'xml': output_xml,
            'text/xml': output_xml,
            'application/xml': output_xml,
            'application/xml+fhir': output_xml,
        }

# Authentication on every resource
class Resource(base_resource):
    method_decorators = [login_required]
#### /Extensions
