from flask import Flask, g
from flask.ext.login import current_user
from server.common import tryton, login_manager, Api, recordConverter

def before_request():
    """Allows access to user object
        for every request
    """
    g.user = current_user

def create_app(config=None):
    app = Flask(__name__)
    app.config.from_object('server.config.DebugConfig')
    if config is not None:
        app.config.from_object(config)
    app.config.from_envvar('FHIR_SERVER_CONFIG', silent=True)

    with app.app_context():
        import logging
        logging.basicConfig(filename='flask.log', level=logging.INFO,
                format='%(asctime)s:::%(levelname)s:::%(name)s: %(message)s')

        # Initialize tryton
        tryton.init_app(app)

        # Login
        login_manager.init_app(app)
        login_manager.login_view='auth_endpoint.login'
        login_manager.session_protection='strong'

        # Initiate the REST API
        api=Api(app)

        # The user model
        user = tryton.pool.get('res.user')

        # Setup tryton config
        @tryton.default_context
        def default_context():
            return user.get_preferences(context_only=True)

        # Add Model-ID-Field url converter
        app.url_map.converters['item']=recordConverter

        # Store current user in g.user
        app.before_request(before_request)


        #### ADD THE ROUTES ####
        from server.resources.system import Conformance
        api.add_resource(Conformance, '/', '/metadata')

        def add_fhir_routes(endpoint, classes):
            """Adds complex FHIR routes
            """
            # Create
            api.add_resource(classes['create'],
                            '/{}'.format(endpoint))
            # Search
            api.add_resource(classes['search'],
                            '/{}'.format(endpoint),
                            '/{}/_search'.format(endpoint))
            # Record
            api.add_resource(classes['record'],
                            '/{}/<int:log_id>'.format(endpoint))
            # Validate
            api.add_resource(classes['validate'],
                            '/{}/_validate'.format(endpoint),
                            '/{}/_validate/<int:log_id>'.format(endpoint))
            # Version
            api.add_resource(classes['version'],
                            '/{}/<int:log_id>/_history'.format(endpoint),
                            '/{}/<int:log_id>/_history/<string:v_id>'.format(endpoint))

        from server.resources.patient import (PAT_Create, PAT_Search,
                        PAT_Validate, PAT_Record, PAT_Version)
        add_fhir_routes('Patient', {'create': PAT_Create,
                                    'search': PAT_Search,
                                    'record': PAT_Record,
                                    'validate': PAT_Validate,
                                    'version': PAT_Version})

        from server.resources.diagnostic_report import (DR_Create, DR_Search,
                                        DR_Validate, DR_Record, DR_Version)
        add_fhir_routes('DiagnosticReport',
                                    {'create': DR_Create,
                                    'search': DR_Search,
                                    'record': DR_Record,
                                    'validate': DR_Validate,
                                    'version': DR_Version})

        from server.resources.observation import (OBS_Create, OBS_Search,
                                        OBS_Validate, OBS_Record, OBS_Version)
        add_fhir_routes('Observation',
                                    {'create': OBS_Create,
                                    'search': OBS_Search,
                                    'record': OBS_Record,
                                    'validate': OBS_Validate,
                                    'version': OBS_Version})

        from server.resources.practitioner import (HP_Create, HP_Search,
                                        HP_Validate, HP_Record, HP_Version)

        add_fhir_routes('Practitioner',
                                    {'create': HP_Create,
                                    'search': HP_Search,
                                    'record': HP_Record,
                                    'validate': HP_Validate,
                                    'version': HP_Version})

        from server.resources.procedure import (OP_Create, OP_Search,
                                        OP_Validate, OP_Record, OP_Version)
        add_fhir_routes('Procedure',
                                    {'create': OP_Create,
                                    'search': OP_Search,
                                    'record': OP_Record,
                                    'validate': OP_Validate,
                                    'version': OP_Version})

        from server.resources.condition import (CO_Create, CO_Search,
                                        CO_Validate, CO_Record, CO_Version)
        add_fhir_routes('Condition',
                                    {'create': CO_Create,
                                    'search': CO_Search,
                                    'record': CO_Record,
                                    'validate': CO_Validate,
                                    'version': CO_Version})

        from server.resources.family_history import (FH_Create, FH_Search,
                                        FH_Validate, FH_Record, FH_Version)
        add_fhir_routes('FamilyHistory',
                                    {'create': FH_Create,
                                    'search': FH_Search,
                                    'record': FH_Record,
                                    'validate': FH_Validate,
                                    'version': FH_Version})

        from server.resources.medication import (MED_Create, MED_Search,
                                        MED_Validate, MED_Record, MED_Version)
        add_fhir_routes('Medication',
                                    {'create': MED_Create,
                                    'search': MED_Search,
                                    'record': MED_Record,
                                    'validate': MED_Validate,
                                    'version': MED_Version})

        from server.resources.medication_statement import (MS_Create, MS_Search,
                                        MS_Validate, MS_Record, MS_Version)
        add_fhir_routes('MedicationStatement',
                                    {'create': MS_Create,
                                    'search': MS_Search,
                                    'record': MS_Record,
                                    'validate': MS_Validate,
                                    'version': MS_Version})

        from server.resources.immunization import (IM_Create, IM_Search,
                                        IM_Validate, IM_Record, IM_Version)
        add_fhir_routes('Immunization',
                                    {'create': IM_Create,
                                    'search': IM_Search,
                                    'record': IM_Record,
                                    'validate': IM_Validate,
                                    'version': IM_Version})

        # Handle the authentication blueprint
        #   NOT PART OF THE FHIR STANDARD
        from server.resources.auth import auth_endpoint
        app.register_blueprint(auth_endpoint, url_prefix='/auth')

    return app
