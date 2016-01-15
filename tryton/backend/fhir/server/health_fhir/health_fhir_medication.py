from StringIO import StringIO
from operator import attrgetter
import server.fhir as supermod
from server.common import safe_attrgetter
from .health_mixin import ExportXMLMixin

try:
    from flask import url_for
    RUN_FLASK=True
except:
    from .datastore import dumb_url_generate
    RUN_FLASK=False


class Medication_Map:
    """Holds essential mappings and information for
        the Medication class
    """

    root_search=[]

    resource_search_params={
            '_id': 'token',
            'code': 'token',
            'form': None,
            'container': None,
            'content': None,
            'manufacturer': None,
            'ingredient': None,
            'name': None,
            '_language': None}

    chain_map={}
    search_mapping={
            '_id': ['id'],
            'code': ['name.code'],
            'code:text': ['name.name']
            }

    url_prefixes={}
    model_mapping={'gnuhealth.medicament':
                {
                    'display': 'active_component',
                    'code': 'name.code'
                }}

class health_Medication(supermod.Medication, Medication_Map, ExportXMLMixin):
    def __init__(self, *args, **kwargs):
        rec = kwargs.pop('gnu_record', None)
        super(health_Medication, self).__init__(*args, **kwargs)
        if rec:
            self.set_gnu_medication(rec)

    def set_gnu_medication(self, medication):
        """Set the GNU Health record
        ::::
            params:
                medication ===> Health model
            returns:
                instance

        """
        self.medication = medication
        self.model_type = self.medication.__name__

        # Only certain models
        if self.model_type not in self.model_mapping:
            raise ValueError('Not a valid model')

        self.map = self.model_mapping[self.model_type]

        self.__import_from_gnu_medication()
        self.__set_feed_info()

    def __import_from_gnu_medication(self):
        """Set the data from the model"""
        if self.medication:
            self.set_code(safe_attrgetter(self.medication, self.map['display']),
                            safe_attrgetter(self.medication, self.map['code']))
            self.set_kind('product')
            #self.set_package()
            #self.set_product()
            #self.set_manufacturer()
            #self.set_isBrand()
            #self.set_name()

    def __set_feed_info(self):
        """Set the feed-relevant data"""
        if self.medication:
            if RUN_FLASK:
                uri = url_for('med_record',
                            log_id=self.medication.id,
                            _external=True)
            else:
                uri = dumb_url_generate(['Medication', self.medication.id])
            self.feed={'id': uri,
                        'published': self.medication.create_date,
                        'updated': self.medication.write_date or self.medication.create_date,
                        'title': self.medication.name.name
                        }

    def set_name(self, name):
        """Set medication name"""

        #TODO Need common/commercial names
        if name:
            n = supermod.string(value=str(name))
            super(health_Medication, self).set_name(n)

    def set_code(self, name, code):
        """Extends superclass for convenience

        Keyword arguments:
        code -- code value
        name -- name of the medication
        """

        #TODO Better info, use recognized codes
        if name:
            c = supermod.Coding()
            c.display = supermod.string(value=str(name))
            if code:
                c.code = supermod.code(value=code)
            cc = supermod.CodeableConcept()
            cc.coding=[c]
            super(health_Medication, self).set_code(cc)

    def set_kind(self, kind='product'):
        """Extends superclass for convenience

        Keyword arguments:
        kind - basically, product or package
        """

        if kind in ['product', 'package']:
            c = supermod.code(value=kind)
            super(health_Medication, self).set_kind(c)

supermod.Medication.subclass=health_Medication
