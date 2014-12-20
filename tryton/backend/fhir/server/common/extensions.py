from flask.ext.tryton import Tryton
from flask.ext.restful import Api as base_api
from flask.ext.restful import Resource as base_resource
from flask.ext.login import LoginManager, login_required
from .utils import output_xml

#### Extensions
tryton = Tryton()
login_manager = LoginManager()

# Handle different outputs
class Api(base_api):
    def __init__(self, *args, **kwargs):
        # Set xml as default (application/xml)
        media = kwargs.pop('default_mediatype', 'application/xml')
        super(Api, self).__init__(*args, default_mediatype=media, **kwargs)
        self.representations = {
            'xml': output_xml,
            'text/xml': output_xml,
            'application/xml': output_xml,
            'application/xml+fhir': output_xml,
        }
api = Api()

# Authentication on every resource
#   Import this for authenticated routes
class Resource(base_resource):
    method_decorators = [login_required]
#### /Extensions
