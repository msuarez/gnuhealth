from .health_fhir_patient import Patient_Map
from .health_fhir_observation import Observation_Map
from .health_fhir_practitioner import Practitioner_Map
from .health_fhir_procedure import Procedure_Map
from .health_fhir_diagnostic_report import DiagnosticReport_Map
import re

# TODO: Raise Error on bad arguments or parameters
# TODO: Reference/chained parameters
# TODO: token:text has different attribute searched frequently
# TODO: :missing

class health_Search:
    """This class computes search queries"""

    def __init__(self, endpoint=None):
        if endpoint is None:
            raise ValueError('Need endpoint value')
        if endpoint not in ('patient',
                            'observation',
                            'practitioner',
                            'procedure',
                            'diagnostic_report'):
            raise ValueError('Not a valid endpoint')
        self.endpoint=endpoint
        self.patient=Patient_Map()
        self.observation=Observation_Map()
        self.practitioner=Practitioner_Map()
        self.procedure=Procedure_Map()
        self.diagnostic_report=DiagnosticReport_Map()

        self.__get_dt_parser()

    def __get_dt_parser(self):
        try:
            from dateutil.parser import parse
            def wrap_parse(string):
                '''Parser for date type.
                    Return ValueError, not TypeError
                '''
                try:
                    prefixes=('<=', '>=', '<', '>')
                    prefix, tmp = self.pop_prefix(string, prefixes)
                    split = self.split_string(tmp)
                    date=[parse(x) for x in split]
                    return (prefix, date)
                except:
                    raise ValueError
            self.date_parser=wrap_parse
        except:
            def fall_back(string):
                from time import strptime
                prefixes=('<=', '>=', '<', '>')
                prefix, tmp = self.pop_prefix(string, prefixes)
                split = self.split_string(tmp)
                date=[strptime(x, "%Y-%m-%dT%H:%M:%S") for x in split]
                return (prefix, date)
            self.date_parser=fallback

    def split_string(self, string):
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

    def pop_prefix(self, string, prefixes):
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

    def pop_suffix(self, string):
        '''Pop the string suffix,
                returning base + suffix
        '''

        split=string.split(':')[:2]
        return [split[0], split[1] if 1 < len(split) else None]

    def number_parser(self, string):
        '''Parser for number type'''
        prefixes=('<=', '>=', '<', '>')
        prefix, tmp = self.pop_prefix(string, prefixes)
        split = self.split_string(tmp)
        floats=[float(x) for x in split]
        return (prefix, floats)

    def quantity_parser(self, string):
        '''Parser for quantity type
            TODO: Handle ~
            TODO: Handle units, etc.'''
        prefixes=('<=', '>=', '<', '>')
        prefix, tmp = self.pop_prefix(string, prefixes)
        split = self.split_string(tmp)
        floats=[float(x) for x in split]
        return (prefix, floats)

    def string_parser(self, string):
        '''Parser for string type'''
        tmp = self.split_string(string)
        return (None, tmp)

    def chained_parameter_parser(self, string):
        '''Parse reference parameter
            (e.g., subject.name, subject:Patient.name)

            return: {'type': <resource type>, 'parameters': [ <param>, ... ]}
        '''

        m = string.split(':')
        if len(m) > 1:
            # There is a type
            tmp = m[1].split('.')
            res = tmp[0]
            pars = [m[0]]
            pars.extend(tmp[1:])
            d = { 'type': res,
                    'parameters': pars}

        else:
            d = { 'type': None,
                    'parameters': string.split('.')}
        return d

    def get_queries(self, args):
        queries = []
        self.endpoint_info = getattr(self, self.endpoint)
        if not self.endpoint_info:
            raise ValueError('No endpoint info; should not happen... weird')
        for k,v in self.endpoint_info.search_mapping.items():
            try:
                fields = self.endpoint_info.model_mapping[k].get('fields', [])
            except:
                fields = []
            queries.append(self.__search_query_generate(v, args, self.endpoint_info.url_prefixes.get(k, None), fields))
        return queries

    def __search_query_generate(self, model_info, args, model, fields):
        '''Generates an usable search query
            for tryton from endpoint_info

            endpoint_info :::
                {<parameter>: ([<model.attribute>, ...], <type>),
                ...}
                    --- NOTE: Different for user-defined parameters
                    --- NOTE: Different for reference parameters
            args ::::
                request.args object
                info endpoint
                model string (only relevant for multi-model resources)
                fields all possible fields w/i model (only set for multi-resource model singletons)
            returns :::
                (query, fields, model)
        '''

        #TODO Make cleaner structures

        #structure:
        #    {<type>: (<type_conv>, (<modifier>, ..))
        #    ...}
        search_prefixes=('<\=', '>\=', '<', '>')
        search_types={'number': (self.number_parser, ('missing')),
                    'date': (self.date_parser, ('missing')),
                    'string': (self.string_parser, ('exact', 'missing')),
                    'user-defined': (self.string_parser, ('text', 'exact', 'missing')),
                    'token': (self.string_parser, ('missing', 'text')), #'token-text' on diff attribute handled as string
                    'quantity': (self.quantity_parser, ('missing')), 
                    'reference': (self.string_parser, ('missing')), #todo [type]
                    'composite': (self.string_parser, None)}
        #FIX WOW UGLY!
        query=[]
        field_names=fields
        for key in args.iterkeys():
            # FIX Hack for token:text on different attribute
            if key not in model_info: 
                #Converted key to key and suffix
                new_key, suffix= self.pop_suffix(key)
                info=model_info.get(new_key)
                if info is None:
                    continue
            else:
                new_key, suffix = key, None
                info = model_info[key]

            db_type = info[1]
            db_key = info[0]

            #Converted argument values
            values=args.getlist(key, type=search_types[db_type][0])
            if values is None:
                continue

            if db_type == 'user-defined':
                # TODO Fix this hack
                #   Handle user-defined values
                #   {<Value>: <field_name>)...}
                #   If value matches, add field name
                
                # Since we are building, not sieving, start from scratch
                field_names = []

                for pre,value in values:
                    for v in value:
                        if suffix == 'text':
                            st = ''.join(['.*', v, '.*'])
                            reg = re.compile(st, re.IGNORECASE)
                            for k,att in db_key.items():
                                m = reg.match(k)
                                if m:
                                    field_names.append(att)
                        else:
                            # Must match exactly
                            if v in db_key:
                                field_names.append(db_key[v])
                if field_names:
                    continue
                else:
                    # No matches on this key... therefore break
                    return {'query': None, 'model': model ,'fields': []}

            for pre,value in values:
                #Could be singleton or list of lists
                composite = False
                if len(value) != 1:
                    composite = True

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
        return {'query': query, 'fields': field_names, 'model': model}
