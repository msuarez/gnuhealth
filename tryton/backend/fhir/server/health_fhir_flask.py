import fhir_xml
from flask import Flask
from flask.ext.tryton import Tryton
from flask.ext.restful import Api
from functools import partial
from defusedxml.lxml import parse, fromstring

#### Set safe xml parsing functions (TODO: set these in the xml code, too)
safe_parse = partial(parse, forbid_dtd=True,
                                forbid_entities=True)
safe_fromstring = partial(fromstring, forbid_dtd=True,
                                forbid_entities=True)
#### /XML

#### Extensions
tryton = Tryton()
api = Api()
#### /Extensions

def create_app(config=None):
    app = Flask(__name__)

    #Set db name --- CHANGE!
    app.config['TRYTON_DATABASE']='test'
    with app.app_context():

        # Initialize tryton
        tryton.init_app(app)

        # The patient model
        patient = tryton.pool.get('gnuhealth.patient')

        # The party model
        party = tryton.pool.get('party.party')

        # The user model
        user = tryton.pool.get('res.user')

        # Setup tryton config
        @tryton.default_context
        def default_context():
            return user.get_preferences(context_only=True)

        #Register the patient blueprint (and others, in the future)
        from health_fhir_patient_flask import patient_endpoint
        app.register_blueprint(patient_endpoint)

    return app

if __name__=="__main__":
    create_app().run(DEBUG=True)
