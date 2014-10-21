from flask import current_app
from StringIO import StringIO
from datetime import datetime
from .datastore import find_record
import fhir as supermod
from utils import get_address
import sys

class health_Practitioner(supermod.Practitioner):
    pass
