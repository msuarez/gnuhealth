#### SOME HELPFUL FUNCTIONS ####
def dt_parser(string):
    '''Fall-back date type parser.
        ...very narrow and error-prone parser
    '''
    from time import strptime
    prefixes=('<=', '>=', '<', '>')
    prefix, tmp = pop_prefix(string, prefixes)
    split = split_string(tmp)
    date=[strptime(x, "%Y-%m-%dT%H:%M:%S") for x in split]
    return (prefix, date)

try:
    from dateutil.parser import parse
    def wrap_parse(string):
        '''Parser for date type.
            Return ValueError, not TypeError
        '''
        try:
            prefixes=('<=', '>=', '<', '>')
            prefix, tmp = pop_prefix(string, prefixes)
            split = split_string(tmp)
            date=[parse(x) for x in split]
            return (prefix, date)
        except:
            raise ValueError
    date_parser=wrap_parse
except:
    date_parser=dt_parser

def split_string(string):
    '''Split the string according to discrete
            search criteria... it gets complicated

    Still work-in-progress
    '''
    # FIX Handling \ is difficult:
    #    the string is already escaped against singleton \,
    #    but the standard is... uggh - do it simply now...
    #    don't allow escaped and non-escaped special characters
    #    in same search
    seps=(',', '$', '|')
    if ('\,' or '\$' or '\|') in string:
        unescaped = string.replace("\$", '$')
        unescaped = unescaped.replace("\,", ',')
        unescaped = unescaped.replace("\|", '|')
        return [unescaped]
    else:
        #Checked for allowed \, so if its singleton, must be invalid
        if (len(string) - len(string.replace('\\', ''))) % 2:
            raise ValueError
        else:
            return string.split(',')

def pop_prefix(string, prefixes):
    '''Pop the string prefix,
            returning prefix + base
    '''
    # FIX Unescaping equals... with good url handling
    #    becomes complicated since it will handle
    #    non-escaped equals fine
    for pre in prefixes:
        if string.startswith(pre):
            return (pre, string[len(pre):])
    return (None, string)

def pop_suffix(string):
    '''Pop the string suffix,
            returning base + suffix
    '''

    split=string.split(':')[:2]
    return [split[0], split[1] if 1 < len(split) else None]

def number_parser(string):
    '''Parser for number type'''
    prefixes=('<=', '>=', '<', '>')
    prefix, tmp = pop_prefix(string, prefixes)
    split = split_string(tmp)
    floats=[float(x) for x in split]
    return (prefix, floats)

def string_parser(string):
    '''Parser for string type'''
    tmp = split_string(string)
    return (None, tmp)

def search_query_generate(endpoint_info, args):
    '''Generates an usable search query
        for tryton from endpoint_info

        endpoint_info :::
            {<parameter>: ([<model.attribute>, ...], <type>),
            ...}
        args ::::
            request.args object
    '''
    #TODO Make cleaner structures
    #TODO Add prefix and modifier support

    #structure:
    #    {<type>: (<type_conv>, (<modifier>, ..))
    #    ...}
    search_prefixes=('<\=', '>\=', '<', '>')
    search_types={'number': (number_parser, ('missing')),
                'date': (date_parser, ('missing')),
                'string': (string_parser, ('exact', 'missing')),
                'token': (string_parser, ('text' 'missing')),
                'quantity': (string_parser, ('missing')), 
                'reference': (string_parser, ('missing')), #todo [type]
                'composite': (string_parser, None)}
    #FIX WOW UGLY!
    query=[]
    for key in args.iterkeys():
        print 'key:', key

        #Converted key to key and suffix
        new_key, suffix= pop_suffix(key)
        print 'new_key:', new_key, suffix

        info=endpoint_info.get(new_key)
        if info is None:
            continue

        db_type = info[1]
        db_key = info[0]

        #Converted argument values
        values=args.getlist(key, type=search_types[db_type][0])
        if values is None:
            continue
        print 'values:',values

        for pre,value in values:
            #Could be singleton or list of lists
            composite = False
            if len(value) != 1:
                composite = True

            print 'comp:', composite

            if len(db_key) > 1:
                a=['OR']
            else:
                a=[]
            for k in db_key:
                if db_type == 'string':
                    if composite:
                        a=['OR']
                        for x in value:
                            a.append((k, 'ilike', ''.join(('%',x,'%'))))
                    else:
                        if suffix == 'exact':
                            a.append((k, '=', value[0]))
                        else:
                            a.append((k, 'ilike', ''.join(('%',value[0],'%'))))
                else:
                    if composite:
                        a.append((k, 'in', value))
                    else:
                        if db_type == 'token' and suffix == 'text':
                            a.append((k, 'ilike', ''.join(('%',value[0],'%'))))
                        else:
                            a.append((k, pre or '=', value[0]))
            query.append(a)
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
