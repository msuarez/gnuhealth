#### SOME HELPFUL FUNCTIONS ####
def dt_parser(string):
    '''very narrow and error-prone parser'''
    from time import strptime
    date=[strptime(x, "%Y-%m-%dT%H:%M:%S") for x in split_string(string)]
    return date

try:
    from dateutil.parser import parse
    def wrap_parse(string):
        '''Return ValueError, not TypeError'''
        try:
            date=[parse(x) for x in split_string(string)]
            return date
        except:
            raise ValueError
    date_parser=wrap_parse
except:
    date_parser=dt_parser

def split_string(string):
    return string.split(',')

def float_parser(string):
    floats=[float(x) for x in split_string(string)]
    return floats

def search_query_generate(endpoint_info, args):
    '''Generates an usable search query
        for tryton from endpoint_info

        endpoint_info :::
            {<parameter>: (<model.attribute>, <type>),
            ...}
        args ::::
            request.args object
    '''
    #TODO Make cleaner structures
    #TODO Add prefix and modifier support
    search_prefixes=('<', '>', '<=', '>=')

    #structure:
    #    {<type>: (<type_conv>, (<modifier>, ..))
    #    ...}
    search_types={'number': (float_parser, (':missing')),
                'date': (date_parser, (':missing')),
                'string': (split_string, (':exact', ':missing')),
                'token': (split_string, (':text' ':missing')),
                'quantity': (split_string, (':missing')), 
                'reference': (split_string, (':[type]', ':missing')), #todo [type]
                'composite': (split_string, None)}
    query=[]
    for key in args.iterkeys():
        print 'key:', key
        info=endpoint_info.get(key)
        if info is None:
            continue
        db_key = info[0]
        db_type = info[1]

        #Actual argument values
        values=args.getlist(key, type=search_types[db_type][0])
        print 'values:',values
        if values is None:
            continue

        for value in values:
            #Could be string or list of lists
            if isinstance(value, basestring):
                composite=False
            else:
                composite=True

            #TODO Clean this up, terrible structure
            if isinstance(db_key, basestring):
                if db_type == 'string':
                    if composite:
                        a=['OR']
                        for x in value:
                            a.append([(db_key, 'ilike', ''.join(('%',x,'%')))])
                        query.append(a)
                    else:
                        query.append((db_key, 'ilike', ''.join(('%',value,'%'))))
                else:
                    if composite:
                        query.append((db_key, 'in', value))
                    else:
                        query.append((db_key, '=', value))
            else:
                a=['OR']
                for k in db_key:
                    if db_type == 'string':
                        if composite:
                            for x in value:
                                a.append([(k, 'ilike', ''.join(('%',x,'%')))])
                        else:
                            a.append([(k, 'ilike', ''.join(('%',value,'%')))])
                    else:
                        if composite:
                            a.append([(k, 'in', value)])
                        else:
                            a.append([(k, '=', value)])
                query.append(a)
                #if value.startswith(search_prefixes):
                    #a=None
                #else:
                    #t=value.split(',')
    return query

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
