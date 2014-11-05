from werkzeug.contrib.atom import AtomFeed
from datetime import datetime
from .health_fhir_patient import health_Patient
from .health_fhir_observation import health_Observation

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

    def add_entry(self, entry):
        '''Add entry to feed
        '''
        feed_info = entry.feed
        self.add(title=feed_info['title'],
                id=feed_info['id'],
                published=feed_info['published'],
                updated=feed_info['updated'],
                content_type='text/xml',
                content=entry.export_to_xml_string())

    def export_to_xml_string(self):
        '''Wrapper for to_string()
        '''
        return self.to_string()
