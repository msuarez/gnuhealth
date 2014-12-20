from flask import Flask
from server.common import tryton, login_manager, api, recordConverter

def create_app(config=None):
    app = Flask(__name__)

    #Set db name --- CHANGE!
    app.config['TRYTON_DATABASE']='gnuhealth_demo'

    #Set secret --- CHANGE!
    app.config['SECRET_KEY'] = 'test'
    app.config['DEBUG'] = True
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

        # Add Model-ID-Field url converter
        app.url_map.converters['item']=recordConverter

        # Handle the authentication blueprint
        #   NOT PART OF THE FHIR STANDARD
        from server.resources.auth import auth_endpoint
        app.register_blueprint(auth_endpoint, url_prefix='/auth')

        #### ADD THE ROUTES ####
        from server.resources.system import Conformance
        api.add_resource(Conformance, '/', '/metadata')

        from server.resources.patient import (PAT_Create, PAT_Search,
                        PAT_Validate, PAT_Record, PAT_Version)
        api.add_resource(PAT_Create, '/Patient')
        api.add_resource(PAT_Search, '/Patient', '/Patient/_search')
        api.add_resource(PAT_Record, '/Patient/<int:log_id>')
        api.add_resource(PAT_Validate,
                        '/Patient/_validate',
                        '/Patient/_validate/<int:log_id>')
        api.add_resource(PAT_Version,
                        '/Patient/<int:log_id>/_history',
                        '/Patient/<int:log_id>/_history/<string:v_id>')

        from server.resources.diagnostic_report import (DR_Create, DR_Search,
                                        DR_Validate, DR_Record, DR_Version)
        api.add_resource(DR_Create, '/DiagnosticReport')
        api.add_resource(DR_Record, '/DiagnosticReport/<item:log_id>')
        api.add_resource(DR_Search,
                        '/DiagnosticReport',
                        '/DiagnosticReport/_search')
        api.add_resource(DR_Validate,
                        '/DiagnosticReport/_validate',
                        '/DiagnosticReport/_validate/<item:log_id>')
        api.add_resource(DR_Version,
                        '/DiagnosticReport/<item:log_id>/_history',
                        '/DiagnosticReport/<item:log_id>/_history/<string:v_id>')

        from server.resources.observation import (OBS_Create, OBS_Search,
                                        OBS_Validate, OBS_Record, OBS_Version)
        api.add_resource(OBS_Create, '/Observation')
        api.add_resource(OBS_Search, '/Observation', '/Observation/_search')
        api.add_resource(OBS_Record, '/Observation/<item:log_id>')
        api.add_resource(OBS_Validate,
                        '/Observation/_validate',
                        '/Observation/_validate/<item:log_id>')
        api.add_resource(OBS_Version,
                        '/Observation/<item:log_id>/_history',
                        '/Observation/<item:log_id>/_history/<string:v_id>')

        from .resources.practitioner import (HP_Create, HP_Search,
                                        HP_Validate, HP_Record, HP_Version)
        api.add_resource(HP_Create, '/Practitioner')
        api.add_resource(HP_Search, '/Practitioner', '/Practitioner/_search')
        api.add_resource(HP_Record, '/Practitioner/<int:log_id>')
        api.add_resource(HP_Validate,
                        '/Practitioner/_validate',
                        '/Practitioner/_validate/<int:log_id>')
        api.add_resource(HP_Version,
                        '/Practitioner/<int:log_id>/_history',
                        '/Practitioner/<int:log_id>/_history/<string:v_id>')


        from server.resources.procedure import (OP_Create, OP_Search,
                                        OP_Validate, OP_Record, OP_Version)
        api.add_resource(OP_Create, '/Procedure')
        api.add_resource(OP_Record, '/Procedure/<item:log_id>')
        api.add_resource(OP_Search, '/Procedure', '/Procedure/_search')
        api.add_resource(OP_Validate,
                        '/Procedure/_validate',
                        '/Procedure/_validate/<item:log_id>')
        api.add_resource(OP_Version,
                        '/Procedure/<item:log_id>/_history',
                        '/Procedure/<item:log_id>/_history/<string:v_id>')

        # Initiate the REST API
        api.init_app(app)

    return app
