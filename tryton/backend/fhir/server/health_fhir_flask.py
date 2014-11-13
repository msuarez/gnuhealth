from flask import Flask
from extensions import tryton, login_manager

def create_app(config=None):
    app = Flask(__name__)

    #Set db name --- CHANGE!
    app.config['TRYTON_DATABASE']='gnuhealth_demo'

    #Set secret --- CHANGE!
    app.config['SECRET_KEY'] = 'test'
    with app.app_context():

        # Initialize tryton
        tryton.init_app(app)

        # Login
        login_manager.init_app(app)
        login_manager.login_view='auth_endpoint.login'
        login_manager.session_protection='strong'

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
        from health_fhir_auth_blueprint import auth_endpoint
        app.register_blueprint(patient_endpoint)
        app.register_blueprint(observation_endpoint)
        app.register_blueprint(practitioner_endpoint)
        app.register_blueprint(procedure_endpoint)
        app.register_blueprint(auth_endpoint)


    return app

if __name__=="__main__":
    create_app().run(debug=True)
