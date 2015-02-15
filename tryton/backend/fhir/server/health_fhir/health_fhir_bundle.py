from math import ceil
from werkzeug.contrib.atom import AtomFeed
from werkzeug.urls import Href
from datetime import datetime
from .health_fhir_patient import health_Patient
from .health_fhir_observation import health_Observation

#TODO More requirements
#TODO Paging
class Bundle(AtomFeed):
    '''Bundle definition is Atom feed'''
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
        if 'links' not in kwargs:
            self.total=kwargs.pop('total', None)
            self.per_page=kwargs.pop('per_page', 10) or 10
            self.page = kwargs.pop('page', 1) or 1
            if self.page and self.per_page and self.total:
                kwargs['links']=self.__generate_links()

        super(Bundle, self).__init__(*args, **kwargs)

    def __generate_links(self):
        links = []

        total_pages= int(ceil(float(self.total)/self.per_page))
        args = self.request.args.copy()
        href = Href(self.request.base_url)

        if total_pages > 1:

            # first link
            args['page'] = 1
            links.append({'href': href(args), 'rel': 'first'})

            # last link
            args['page'] = total_pages
            links.append({'href': href(args), 'rel': 'last'})

            if self.page > 2:

                # prev link
                args['page'] = self.page-1
                links.append({'href': href(args), 'rel': 'previous'})

                # next link
                if self.page < total_pages:
                    args['page'] = self.page + 1
                    links.append({'href': href(args), 'rel': 'next'})

        return links

    def add_entry(self, entry):
        '''Add entry to feed

        ::::
            params:
                entry ===> Resource class
                    *must have feed_info set*
            returns:
                side effects, return value irrelevant
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
