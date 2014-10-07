import fhir_xml
from flask import Flask
from extensions import (api, tryton)

def create_app(config=None):
    app = Flask(__name__)

    #Set db name --- CHANGE!
    app.config['TRYTON_DATABASE']='gnuhealth_demo'
    with app.app_context():

        # Initialize tryton
        tryton.init_app(app)

        # The user model
        user = tryton.pool.get('res.user')

        # Setup tryton config
        @tryton.default_context
        def default_context():
            return user.get_preferences(context_only=True)

        #Register the patient blueprint (and others, in the future)
        from health_fhir_patient_blueprint import patient_endpoint
        app.register_blueprint(patient_endpoint)

    return app

if __name__=="__main__":
    create_app().run(debug=True)
