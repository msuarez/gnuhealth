from werkzeug.routing import BaseConverter, ValidationError
from operator import attrgetter
from flask import make_response, g
from StringIO import StringIO

def get_address(string):
    '''Given string, retrieve full address, easily parsed'''
    import requests
    ENDPOINT_URL='https://open.mapquestapi.com/nominatim/v1/search'
    resp = requests.get(ENDPOINT_URL, params={'q':str(string),
                                            'format': 'json',
                                            'addressdetails': 1,
                                            'limit': 1})
    details = resp.json()
    if details:
        ad = details[0].get('address', {})
        try:
            ad['lat']=float(details[0].get('lat'))
        except:
            pass
        try:
            ad['lon']=float(details[0].get('lon'))
        except:
            pass
        try:
            ad['house_number']=int(ad['house_number'])
        except:
            pass

        return ad

class recordConverter(BaseConverter):
    '''Handle Model-ID-Field endpoint values'''
    def to_python(self, value):
        tmp = [None, None, None]
        for k,v in enumerate(value.split('-')):
            if k == 3: raise ValidationError()
            tmp[k]=v
        try:
            tmp[1]=int(tmp[1])
        except:
            raise ValidationError()
        return tmp

    def to_url(self, values):
        return '-'.join([str(value) for value in values if value is not None])

def search_error_string(args):
    """Returns string for no matches with given arguments
        (used by search interactions)

        params:
            args ===> request.args object
        returns:
            string
    """
    st =[]
    for k,v in args.items():
        st.append(': '.join([k,v]))
    return 'No matching record(s) for {0}'.format('\n'.join(st) or '/')

def output_xml(data, code, headers=None):
    """Output response to xml

    Data could be dict, fhir class, string, etc.
    Code is code status of response
    Headers is dict of headers
    """
    if hasattr(data, 'export_to_xml_string'):
        resp = make_response(data.export_to_xml_string(), code)
    elif hasattr(data, 'export'):
        output=StringIO()
        data.export(outfile=output, namespacedef_='xmlns="http://hl7.org/fhir"', pretty_print=False, level=4)
        content = output.getvalue()
        output.close()
        resp = make_response(content, code)
    else:
        if isinstance(data, dict):
            #TODO Fix this to use Flask-Restful error catching
            #Check for error from Flask-Restful
            msg = data.get('message', 'Unknown return')
        elif isinstance(data, basestring):
            msg = data
        else:
            msg = 'Unknown return'
        resp = make_response(msg, code)
    resp.headers.extend(headers or {})
    #resp.headers['Content-type']='application/xml+fhir'
    return resp

def get_userid():
    """Return g.user.id, or None"""
    try:
        return int(g.user.id)
    except:
        return None

#def safe_attrgetter(obj, *attrs, default=None): #py3 declaration
def safe_attrgetter(obj, *attrs, **kwargs):
    """The fail-safe version of attrgetter"""
    default = kwargs.get('default', None) #py2 compatibility
    v = []
    for attr in attrs:
        try:
           x=attrgetter(attr)(obj)
        except:
           x=default
        v.append(x)
    if len(v) == 1:
        return v[0]
    return v

__all__=['get_address', 'recordConverter', 'search_error_string',
                'output_xml', 'get_userid', 'safe_attrgetter']
