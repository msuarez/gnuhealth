from .health_fhir_patient import Patient_Map
from .health_fhir_observation import Observation_Map
from .health_fhir_practitioner import Practitioner_Map
from .health_fhir_procedure import Procedure_Map
from .health_fhir_condition import Condition_Map 
from .health_fhir_diagnostic_report import DiagnosticReport_Map
from .health_fhir_family_history import FamilyHistory_Map
from .health_fhir_medication import Medication_Map
from .health_fhir_medication_statement import MedicationStatement_Map 
from .health_fhir_immunization import Immunization_Map 
from .health_fhir_organization import Organization_Map 
from server.common import safe_attrgetter
import re

# TODO: Add support for :missing modifier

class health_Search:
    """This class computes search queries to be used
    by Tryton models. In the future, hopefully add support
    for more complicated raw SQL queries.
    """

    def __init__(self, endpoint=None, request_args=None):
        """Create class

        Keyword arguments:
        endpoint -- name of endpoint (required!)
        """
        if endpoint is None:
            raise ValueError('Need endpoint value')
        if endpoint not in ('patient',
                            'observation',
                            'practitioner',
                            'procedure',
                            'diagnostic_report',
                            'condition',
                            'family_history',
                            'medication',
                            'medication_statement',
                            'immunization',
                            'organization'):
            raise ValueError('Not a valid endpoint')
        if request_args is None:
            raise ValueError('Need the request arguments!')

        self.request_args = request_args
        self.observation=Observation_Map()
        self.practitioner=Practitioner_Map()
        self.procedure=Procedure_Map()
        self.diagnostic_report=DiagnosticReport_Map()
        self.patient=Patient_Map()
        self.condition=Condition_Map()
        self.family_history=FamilyHistory_Map()
        self.medication=Medication_Map()
        self.medication_statement=MedicationStatement_Map()
        self.immunization=Immunization_Map()
        self.organization=Organization_Map()
        self.endpoint = getattr(self, endpoint)

        self.__get_dt_parser()
        self.valid_modifiers = { 'string': ['missing', 'exact'],
                                'token': ['missing', 'text'],
                                'number': ['missing'],
                                'date': ['missing'],
                                'reference': ['missing'], #:[type] from resources
                                'quantity': ['missing'] }

        self.valid_resources = [ 'Alert', 'AllergyIntolerance', 'CarePlan',
                'Composition', 'Condition', 'Conformance', 'Device',
                'DeviceObservationReport', 'DiagnosticOrder',
                'DiagnosticReport', 'DocumentReference', 'DocumentManifest',
                'Encounter', 'FamilyHistory', 'Group', 'ImagingStudy',
                'Immunization', 'ImmunizationRecommendation', 'List',
                'Location', 'Media', 'Medication', 'MedicationAdministration',
                'MedicationDispense', 'MedicationPrescription',
                'MedicationStatement', 'MessageHeader', 'Observation',
                'OperationOutcome', 'Order', 'OrderResponse', 'Organization',
                'Other', 'Patient', 'Practitioner', 'Procedure', 'Profile',
                'Provenance', 'Query', 'Questionnaire', 'RelatedPerson',
                'SecurityEvent', 'Specimen', 'Substance', 'Supply', 'ValueSet']

        self.type_parsers={'number': self.number_parser,
                    'date': self.date_parser,
                    'string': self.string_parser, 
                    'token': self.string_parser,
                    'quantity': self.quantity_parser,
                    'reference': self.string_parser}
                    #'user-defined': self.string_parser,
                    #'composite': self.string_parser}

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

    def __is_valid_modifier(self, type_, modifier):
        if modifier is not None:
            modifiers = self.valid_modifiers.get(type_, None)
            if modifiers is not None:
                if type_ == 'resource':
                    modifiers.extend(self.valid_resources)
                if modifier in modifiers:
                    return True
            return False
        else:
            return True

    def split_string(self, string):
        """Split the string according to discrete
        search criteria (complicated!)

        Still work-in-progress!

        Keyword arguments:
        string -- the string to split
        """
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
        """Pop the string prefix,
        returning (prefix, base)

        Keyword arguments:
        string -- string to parse
        prefixes -- prefixes to check
        """
        # FIX Unescaping equals... with good url handling
        #    becomes complicated since it will handle
        #    non-escaped equals fine
        for pre in prefixes:
            if string.startswith(pre):
                return (pre, string[len(pre):])
        return (None, string)

    def number_parser(self, string):
        """Parser for number type,
        returning (prefix, floats)

        Keyword arguments:
        string -- string to parse
        """
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
        """Parser for string type

        Keyword arguments:
        string -- the string to parse
        """
        tmp = self.split_string(string)
        return (None, tmp)

    def __key_parameter_parser(self, string):
        """Parse key, including chains 
        (e.g., name:text, subject.name, subject:Patient.name)

        return: {'key': <name>,
                'modifier': <modifier>,
                'chains': [ <param>, ... ]}
        """

        m = string.split(':')
        if len(m) > 2:
            # Too many modifiers
            return None

        elif len(m) == 2:
            # There is a modifier, and possible chains
            tmp = m[1].split('.')
            d = { 'key': m[0],
                    'modifier': tmp[0],
                    'chains': tmp[1:] or None}

        else:
            # No modifier, possible chains
            chains = self.__pop_chain(m[0])
            d = { 'key': chains[0],
                    'modifier': None,
                    'chains': chains[1:] or None}
        return d

    def __pop_chain(self, string):
        """Naively pop chained arguments"""

        return string.split('.')

    def __parse_url_parameter(self, parameter):
        """Return parameter info"""
        key_info = self.__key_parameter_parser(parameter)
        # Is key in search_params?
        if key_info['key'] in self.endpoint.resource_search_params:
            #Great, now, is it supported and valid modifier?
            type_ = self.endpoint.resource_search_params[key_info['key']]
            if type_ is not None:
                if self.__is_valid_modifier(type_, key_info['modifier']):
                    # For resource types, semantic checking
                    #   later, but allow for now
                    if key_info['chains'] and type_ != 'reference':
                        # No chains with non-reference types
                        return None
                    key_info['type']=type_
                    return key_info
        # Bad modifier OR Non-supported OR bad parameter
        #   whatever, return None
        return None

    def chain_parameter_parser(self, info):
        """Take chain info, and return correct attr(s),
        returning (new_model_attrs, new_search_target_type)

        Keyword arguments:
        info -- search argument info
        """

        assert info['type'] == 'reference'
        attrs = []
        t=self.endpoint.search_mapping[info['key']]
        # Fix for searching from different start from expected model
        #  (e.g., FamilyHistory --> patient.search()
        if t:
            attrs.extend(t)
        target_resource = info['modifier'] or self.endpoint.chain_map[info['key']]
        while True:
            if not info['chains']:
                # Default to _id
                #TODO: In future, need to change for multi-model
                return (self.__make_attrs(attrs+['id']), 'token')
            if target_resource == 'Patient':
                current_map=self.patient
            elif target_resource == 'DiagnosticReport':
                current_map=self.diagnostic_report
            elif target_resource == 'Observation':
                current_map=self.observation
            elif target_resource == 'Practitioner':
                current_map=self.practitioner
            elif target_resource == 'Procedure':
                current_map=self.procedure
            elif target_resource == 'Condition':
                current_map=self.condition
            elif target_resource == 'FamilyHistory':
                current_map=self.family_history
            elif target_resource == 'Medication':
                current_map=self.medication
            elif target_resource == 'MedicationStatement':
                current_map=self.medication_statement
            elif target_resource == 'Immunization':
                current_map=self.immunization
            elif target_resource == 'Organization':
                current_map=self.organization
            else:
                raise ValueError('Unknown chain target')
            try:
                chain=info['chains'].pop(0)
                attrs.append(current_map.search_mapping[chain])
                target_resource=current_map.chain_map[chain]
            except KeyError:
                raise ValueError('Invalid parameter: non-reference chain or unsupported')
            except:
                break
        return (self.__make_attrs(attrs), current_map.resource_search_params[chain])

    def __make_attrs(self, l, current_attrs=[]):
        """Create attributes from chain lists"""
        if len(l) == 0: return current_attrs
        at = l.pop(0)
        if isinstance(at, basestring):
            return self.__make_attrs(l, ['.'.join((s,at)) for s in current_attrs] or [at])
        else:
            return self.__make_attrs(l, ['.'.join((l,a)) for l in current_attrs for a in at] or [a for a in at])

    def parse_url_string(self, request_args):
        """Parse url string

        Keyword arguments:
        request_args -- url arguments
        """

        full_search_info=[]
        for key, values in request_args.iterlists():
            if key in ['_count', 'page']: continue
            search_info = self.__parse_url_parameter(key)
            if search_info is not None:
                parser = self.type_parsers[search_info['type']]
                search_info['args']=[]
                for argument in values:
                    try:
                        arg_info = parser(argument)
                        search_info['args'].append({'prefix': arg_info[0],
                                                'value': arg_info[1]})
                    except:
                        raise ValueError('Bad argument: {}'.format(argument))
            else:
                raise ValueError('Bad parameter: {}'.format(key))
            full_search_info.append(search_info)

        return self.__validate_search_info(full_search_info)

    def __validate_search_info(self, search_info):
        """Validate the naive search parser against misleading constructions

        TODO: Check if there are the same keys, with different modifiers
           that are exclusionary
              e.g., [{ 'key': 'name', 'modifier': 'exact', ...},
         - Do not allow multiple AND values with exact modifier
         - Do not allow prefixes with multiple OR values
         - Do not allow parameter without argument

         Keyword arguments:
         search_info -- parsed search arguments
        """

        for d in search_info:
            for arg in d['args']:
                if arg['prefix'] and len(arg['value']) > 1:
                    raise ValueError('Do not allow prefixes with multiple OR values')
                for a in arg['value']:
                    if not a:
                        raise ValueError('Do not allow parameters without values')
            if d['modifier'] == 'exact':
                if len(d['args']) > 1:
                    raise ValueError('Do not allow :exact with multiple AND values')
        return search_info

    def single_model_query_generate(self, full_search_info):
        """For single model searches (no weird outer joins, etc.)

        This function is bloated

        Keywoard arguments:
        full_search_info -- fully parsed search argumnts

        Returns:
        search domain -- (e.g., [('name', 'ilike', '%e%')])
        """

        full_query=[]
        #Look for key or key+modifier in the search_mapping
        for query in full_search_info:
            #Look for key+modifier first
            try:
                keymod = ':'.join([query['key'], query['modifier']])
            except:
                keymod = None

            if keymod and keymod in self.endpoint.search_mapping:

                model_attr=self.endpoint.search_mapping[keymod]

                #Only text modifiers on a different model attr
                #  get here (e.g., <token>:text)
                operator = 'ilike'

            else:
                if query['type'] == 'reference':
                    # Override query information with new info
                    model_attr, query['type']=self.chain_parameter_parser(query)
                    query['chains']=None
                else:
                    model_attr=self.endpoint.search_mapping[query['key']]
                if query['type'] == 'string':
                    if query['modifier'] == 'exact':
                        operator = '='
                    else:
                        operator = 'ilike'
                elif query['type'] == 'token':
                    if query['modifier'] == 'text':
                        operator = 'ilike'
                    else:
                        operator = '='
                else:
                    # Figure out later (could be 'in')
                    operator = '='

            #Now, handle multiple model_attrs and multiple values
            # These are AND
            and_queries=[]
            for arg in query['args']:
                or_queries=[]
                MULTIPLE=False
                if len(model_attr) > 1:
                    MULTIPLE=True
                #These are OR
                for attr in model_attr:
                    if len(arg['value']) > 1:
                        if operator == '=':
                            q = [(attr, 'in' ,arg['value'])]
                        else:
                            #ilike needs to do regex thing
                            if arg['prefix']:
                                q=[[(attr, arg['prefix'], a)] for a in arg['value']]
                            else:
                                if operator == 'ilike':
                                    q=[[(attr, operator, '{0}{1}{2}'.format('%',str(a),'%'))] for a in arg['value']]
                                else:
                                    q=[[(attr, operator, a)] for a in arg['value']]
                    else:
                        #ilike needs to do regex thing
                        if arg['prefix']:
                            q = [(attr, arg['prefix'],arg['value'][0])]
                        else:
                            if operator == 'ilike':
                                q = [(attr, operator ,'{0}{1}{2}'.format('%',str(arg['value'][0]),'%'))]
                            else:
                                q = [(attr, operator,arg['value'][0])]

                    # If there are multiple model attributes
                    #    AND only one statemement, then it
                    #    will be OR'd later...
                    if MULTIPLE == True and len(q) == 1:
                        or_queries.append(q)
                    else:
                        or_queries.extend(q)

                #If only one or_query, then cleanup
                #  Not absolutely necessary, but cleaner query
                if len(or_queries) == 1:
                    and_queries.extend(or_queries)
                else:
                    t=['OR']
                    t.extend(or_queries)
                    and_queries.append(t)
            full_query.extend(and_queries)

        # Extend with root search
        full_query.extend(getattr(self.endpoint, 'root_search', []))

        return full_query

    @property
    def query(self):
        """Get the search query

        For now, only single model support
        """

        full_search_info=self.parse_url_string(self.request_args)
        return self.single_model_query_generate(full_search_info)
