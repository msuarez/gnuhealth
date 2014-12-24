class ProductionConfig(object):
    """A basic production config
    """
    TRYTON_DATABASE='gnuhealth_demo' #Change
    SECRET_KEY = 'test'    #Change
    PREFERRED_URL_SCHEME='https'

    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_NAME = 'fhir'
    PERMANENT_SESSION_LIFETIME = 365*24*60*60 #seconds

    SERVER_NAME="fhir.example.com"     #Set this

class DebugConfig(object):
    """Testing settings"""
    TRYTON_DATABASE='gnuhealth_demo_test'
    DEBUG = True
    SECRET_KEY = 'test'
    WTF_CSRF_ENABLED=False
