from flask.ext.tryton import Tryton
from flask.ext import restful
from flask.ext.login import LoginManager, login_required
from .utils import output_xml

#### Extensions
tryton = Tryton()
login_manager = LoginManager()

# Handle different outputs
class Api(restful.Api):
    def __init__(self, *args, **kwargs):
        # Set application/xml as default content-type
        media = kwargs.pop('default_mediatype', 'application/xml')
        super(Api, self).__init__(*args, default_mediatype=media, **kwargs)
        self.representations = {
            'text/xml': output_xml,
            'application/xml': output_xml,
            'application/xml+fhir': output_xml
        }

# Authentication on every resource
#   Import this for authenticated routes
class Resource(restful.Resource):
    method_decorators = [login_required]
#### /Extensions

__all__=['Resource', 'Api', 'tryton', 'login_manager']
