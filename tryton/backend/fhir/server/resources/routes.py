from collections import namedtuple

class Routing:
    """Simple adapter for mapping the resource route
    to the request handler""" 

    def __init__(self, endpoint):
        self.routes = {}
        self.routes['create'] = {'handler': None, 'uri': ['/{}'.format(endpoint)]}
        self.routes['search'] = {'handler': None, 'uri': ['/{}'.format(endpoint),
                                            '/{}/_search'.format(endpoint)]}
        self.routes['record'] = {'handler': None, 'uri': ['/{}/<int:log_id>'.format(endpoint)]}
        self.routes['validate'] = {'handler': None, 'uri':
                                ['/{}/_validate'.format(endpoint),
                                '/{}/_validate/<int:log_id>'.format(endpoint)]}
        self.routes['version'] = {'handler': None, 'uri':
                                    ['/{}/<int:log_id>/_history'.format(endpoint),
                                    '/{}/<int:log_id>/_history/<string:v_id>'.format(endpoint)]}
        self.endpoint = endpoint

    def __len__(self):
        return len(self.routes)

    def __getitem__(self, type_):
        return self.routes[type_]

    def __setitem__(self, type_, handler):
        if type_ not in self.routes:
            raise KeyError('Invalid key')
        self.routes[type_]['handler'] = handler

    def __repr__(self):
        return 'Route %s' % self.endpoint

    @property
    def routing_table(self):
        return self.routes

__all__ = ['Routing']
