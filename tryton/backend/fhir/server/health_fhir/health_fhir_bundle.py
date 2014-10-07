from werkzeug.contrib.atom import AtomFeed
from datetime import datetime
from .health_fhir_patient import health_Patient

class Bundle(AtomFeed):
    '''Bundle definition is Atom feed'''
    #TODO More requirements
    def __init__(self, *args, **kwargs):
        '''Add some default values
        '''
        self.request=kwargs.pop('request', None)
        if 'title' not in kwargs:
            kwargs['title']='Search results'
        if 'id' not in kwargs:
            kwargs['id']=getattr(self.request, 'url', None)
        if 'author' not in kwargs:
            kwargs['author']='GNU Health'
        if 'updated' not in kwargs:
            kwargs['updated']=datetime.utcnow()

        super(Bundle, self).__init__(*args, **kwargs)

    def add_entries(self, entries):
        '''Add entries to feed

        TODO: Generalize, not patient specific
        '''
        for entry in entries:
            d=health_Patient()
            d.set_gnu_patient(entry)
            d.import_from_gnu_patient()
            self.add(title=entry.rec_name,
                    id=entry.id,
                    published=entry.create_date,
                    updated=entry.write_date or entry.create_date,
                    content_type='text/xml',
                    content=d.export_to_xml_string())

    def export_to_xml_string(self):
        '''Wrapper for to_string()
        '''
        return self.to_string()
