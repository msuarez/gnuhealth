from flask import Flask
from extensions import tryton

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

        from utils import recordConverter
        app.url_map.converters['item']=recordConverter

        #Register the patient, observation, etc. blueprints
        from health_fhir_patient_blueprint import patient_endpoint
        from health_fhir_observation_blueprint import observation_endpoint
        from health_fhir_practitioner_blueprint import practitioner_endpoint
        from health_fhir_procedure_blueprint import procedure_endpoint
        app.register_blueprint(patient_endpoint)
        app.register_blueprint(observation_endpoint)
        app.register_blueprint(practitioner_endpoint)
        app.register_blueprint(procedure_endpoint)

    return app

if __name__=="__main__":
    create_app().run(debug=True)
