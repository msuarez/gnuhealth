from StringIO import StringIO
from operator import attrgetter
import server.fhir as supermod

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

class health_Medication(supermod.Medication, Medication_Map):
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

    def __import_from_gnu_medication(self):
        if self.medication:
            #self.__set_gnu_package()
            #self.__set_gnu_product()
            self.__set_gnu_kind()
            #self.__set_gnu_manufacturer()
            #self.__set_gnu_isBrand()
            self.__set_gnu_code()
            #self.__set_gnu_name()

            self.__set_feed_info()

    def __set_feed_info(self):
        ''' Sets the feed-relevant info
        '''
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

    def __set_gnu_name(self):
        #TODO Need common/commercial names
        if self.medication:
            pass
            #self.set_name(self.medication.active_compenent)

    def set_name(self, name):
        """Set medication name"""
        if name:
            n = supermod.string(value=str(name))
            super(health_Medication, self).set_name(n)

    def __set_gnu_code(self):
        #TODO Better info, use recognized codes
        if self.medication:
            c = supermod.Coding()
            c.display = supermod.string(value=attrgetter(self.map['display'])(self.medication))

            t = attrgetter(self.map['code'])(self.medication)
            if t:
                c.code = supermod.code(value=t)

            cc = supermod.CodeableConcept()
            cc.coding=[c]
            self.set_code(cc)

    def set_code(self, code):
        """Set code value"""
        if getattr(code, 'coding'):
            super(health_Medication, self).set_code(code)

    def __set_gnu_kind(self):
        #TODO Be better about this
        if self.medication:
            self.set_kind('product')

    def set_kind(self, kind):
        """Set medication kind - basically, product or package"""
        if kind == 'product':
            c = supermod.code(value='product')
            super(health_Medication, self).set_kind(c)
        elif kind == 'package':
            c = supermod.code(value='package')
            super(health_Medication, self).set_kind(c)
        else:
            pass

    def export_to_xml_string(self):
        """Export"""
        output = StringIO()
        self.export(outfile=output, namespacedef_='xmlns="http://hl7.org/fhir"', pretty_print=False, level=4)
        content = output.getvalue()
        output.close()
        return content

supermod.Medication.subclass=health_Medication
