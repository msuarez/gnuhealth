#### SOME HELPFUL FUNCTIONS ####
def dt_parser(string):
    '''very narrow and error-prone parser'''
    from time import strptime
    date=strptime(string, "%Y-%m-%dT%H:%M:%S")
    return date

try:
    from dateutil.parser import parse
    def wrap_parse(string):
        '''Return ValueError, not TypeError'''
        try:
            return parse(string)
        except:
            raise ValueError
    date_parser=wrap_parse
except:
    date_parser=dt_parser


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
    search_prefixes=('<', '>', '<=', '>=')

    #structure:
    #    {<type>: (<type_conv>, (<modifier>, ..))
    #    ...}
    search_types={'number': (float, (':missing')),
                'date': (date_parser, (':missing')),
                'string': (str, (':exact', ':missing')),
                'token': (str, (':text' ':missing')),
                'quantity': (str, (':missing')), 
                'reference': (str, (':[type]', ':missing')), #todo [type]
                'composite': (str, None)}
    query=[]
    for key in args.iterkeys():
        print 'key:', key
        info=endpoint_info.get(key)
        if info is None:
            continue
        db_key = info[0]
        db_type = info[1]
        values=args.getlist(key, type=search_types[db_type][0])
        print 'values:',values
        if values is None:
            continue
        for value in values:
            #TODO Clean this up
            if isinstance(db_key, basestring):
                if db_type == 'string':
                    query.append((db_key, 'ilike', ''.join(('%',value,'%'))))
                else:
                    query.append((db_key, '=', value))
            else:
                a=['OR']
                for k in db_key:
                    if db_type == 'string':
                        a.append([(k, 'ilike', ''.join(('%',value,'%')))])
                    else:
                        a.append([(k, '=', value)])
                query.append(a)
                #if value.startswith(search_prefixes):
                    #a=None
                #else:
                    #t=value.split(',')
    return query
