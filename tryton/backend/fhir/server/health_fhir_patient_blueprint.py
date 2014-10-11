from flask import Blueprint, request, current_app, make_response
from flask.ext.restful import Resource, abort, reqparse
from StringIO import StringIO
from lxml.etree import XMLSyntaxError
from health_fhir import health_Patient, health_OperationOutcome, parse, parseEtree, Bundle
from extensions import (tryton, api)
from utils import search_query_generate, get_address
import lxml
import json
import os.path
import sys

try:
    from geopy import OpenMapQuest as query_location
except:
    query_location=None

# Patient model
patient = tryton.pool.get('gnuhealth.patient')

# Party model
party = tryton.pool.get('party.party')

# DU model
du = tryton.pool.get('gnuhealth.du')

# Contacts model
contact = tryton.pool.get('party.contact_mechanism')

# Language model
lang = tryton.pool.get('ir.lang')

# Country model
country = tryton.pool.get('country.country')

# Subdivision model
subdivision = tryton.pool.get('country.subdivision')

# 'Patient' blueprint on '/Patient'
patient_endpoint = Blueprint('patient_endpoint', __name__,
                                template_folder='templates',
                                url_prefix="/Patient")

# Initialize api restful
api.init_app(patient_endpoint)

class Create(Resource):
    @tryton.transaction()
    def post(self):
        '''Create interaction'''
        try:
            c=StringIO(request.data)
            res=parse(c, silence=True)
            c.close()
            ds = res.get_gnu_patient()

            #Find language (or not!)
            if ds.get('lang'):
                try:
                    comm = lang.search([['OR', [('code', 'like', '{0}%'.format(ds['lang'].get('code', None)))],
                                            [('name', 'ilike', '%{0}%'.format(ds['lang'].get('name', None)))]]],
                                    limit=1)[0]
                except:
                    comm = None
                finally:
                    ds['party']['lang']=comm


            #Find du (or not!)
            #TODO Shared addresses (apartments, etc.)
            if ds.get('du'):
                try:
                    d = du.search([('name', '=', ds['du'].get('name', None))], limit=1)[0]
                    ds['party']['du']=d.id
                except:

                    #This uses Nominatim to give complete address details
                    query = ', '.join([str(v) for k,v in ds['du'].items() if k in ['address_street_number','address_street','address_city']])
                    query = ', '.join([query, ds['subdivision'] or '', ds['country'] or ''])
                    details = get_address(query)
                    if details:
                        pass

                    # Find subdivision (or not!)
                    try:
                        if ds['subdivision']:
                            s = subdivision.search([['OR', [('code', 'ilike', '%{0}%'.format(ds['subdivision']))],
                                                    [('name', 'ilike', '%{0}%'.format(ds['subdivision']))]]],
                                                        limit=1)[0]
                            ds['du']['address_subdivision']=s.id
                            ds['du']['address_country']=s.country.id
                        else:
                            raise ValueError
                    except:
                        ds['du']['address_subdivision']= None

                    # Find country (or not!)
                    if not ds['du']['address_subdivision']:
                        try:
                            if ds['country']:
                                co = country.search([['OR', [('code', 'ilike', '%{0}%'.format(ds['country']))],
                                                    [('name', 'ilike', '%{0}%'.format(ds['country']))]]],
                                                            limit=1)[0]
                                ds['du']['address_country']=co.id
                            else:
                                raise ValueError
                        except:
                            ds['du']['address_country']=None

                    return ''
                    d = du.create([ds['du']])[0]
                    ds['party']['du']=d

            n = party.create([ds['party']])[0]

            if ds.get('contact_mechanism'):
                for cs in ds['contact_mechanism']:
                    if cs['value'] is not None:
                        cs['party']=n
                        contact.create([cs])

            ds['patient']['name']=n
            p=patient.create([ds['patient']])[0]
        except:
            print sys.exc_info()
            return 'Bad data', 400
        else:
            return 'Created', 201, {'Location': ''.join(['/Patient/', str(p.id)])}

class Search(Resource):
    @tryton.transaction()
    def get(self):
        '''Search interaction'''
        #TODO Search implementation is important, but
        #    also very robust, so keep it simple for now
        #    but need to write general search parser in 
        #    order that we can just plug in criteria for
        #    each resource

        allowed={'_id': ('id', 'token'), 
                '_language': None,
                'active': None,
                'address': None,
                'animal-breed': None,
                'animal-species': None,
                'birthdate': ('dob', 'date'),
                'family': ('name.lastname', 'string'),
                'gender': ('name.sex', 'token'),
                'given': ('name.name', 'string'),
                'identifier': ('puid', 'token'),
                'language': ('name.lang.code', 'token'),
                'link': None,
                'name': (['name.lastname', 'name.name'], 'string'),
                'phonetic': None,
                'provider': None,
                'telecom': None}
        query=search_query_generate(allowed, request.args)
        print query
        if query is not None:
            recs = patient.search(query)
            if recs:
                bd=Bundle(request=request)
                bd.add_entries(recs)
                return bd
        #TODO OperationOutcome; for now an error
        return 'No matching record(s)', 403

class Validate(Resource):
    @tryton.transaction()
    def post(self, log_id=None):
        '''Validate interaction'''
        try:
            # 1) Must correctly parse as XML
            c=StringIO(request.data)
            doc=lxml.etree.parse(c)
            c.close()
        except XMLSyntaxError as e:
            oo=health_OperationOutcome()
            oo.add_issue(details=e, severity='fatal')
            return oo, 400

        except:
            e = sys.exc_info()[0]
            oo=health_OperationOutcome()
            oo.add_issue(details=e, severity='fatal')
            return oo, 400

        else:
            if os.path.isfile('schemas/patient.xsd'):
                # 2) Validate against XMLSchema
                with open('schemas/patient.xsd') as t:
                    sch=lxml.etree.parse(t)

                xmlschema=lxml.etree.XMLSchema(sch)
                if not xmlschema.validate(doc):
                    error = xmlschema.error_log.last_error
                    oo=health_OperationOutcome()
                    oo.add_issue(details=error.message, severity='error')
                    return oo, 400
            else:
                # 2) If no schema, check if it correctly parses to a Patient
                try:
                    pat=parseEtree(StringIO(doc))
                    if not isinstance(pat, health_Patient):
                        oo=health_OperationOutcome()
                        oo.add_issue(details='Not a patient resource', severity='error')
                        return oo, 400
                except:
                    e = sys.exc_info()[1]
                    oo=health_OperationOutcome()
                    oo.add_issue(details=e, severity='fatal')
                    return oo, 400

            if log_id:
                # 3) Check if patient exists
                record = patient.search(['id', '=', log_id], limit=1)
                if not record:
                    oo=health_OperationOutcome()
                    oo.add_issue(details='No patient', severity='error')
                    return oo, 422
                else:
                    #TODO: More checks
                    return 'Valid update', 200
            else:
                # 3) Passed checks
                return 'Valid', 200

class Record(Resource):
    @tryton.transaction()
    def get(self, log_id):
        '''Read interaction'''
        record = patient.search([('id', '=', log_id)], limit=1)
        if record:
            d=health_Patient()
            d.set_gnu_patient(record[0])
            d.import_from_gnu_patient()
            return d, 200
        else:
            return 'Record not found', 404
            #if track deleted records
            #return 'Record deleted', 410

    @tryton.transaction()
    def put(self, log_id):
        '''Update interaction'''
        return 'Not supported', 405
        #record = patient.search([('id', '=', log_id)], limit=1)
        #if record:
            #try:
                #c=StringIO(request.data)
                #res=parse(c)
                #c.close()
                #pat=parseEtree(StringIO(res))
                #if not isinstance(pat, health_Patient):
                    #return 'Resource type not supported', 404
                #ds = res.get_gnu_patient()
                #d = du.create([ds['du']])[0]
                #ds['party']['du']=d
                #n = party.create([ds['party']])[0]
                #for cs in ds['contact_mechanism']:
                    #if cs['value'] is not None:
                        #cs['party']=n
                        #contact.create([cs])
                #ds['patient']['name']=n
                #p=patient.create([ds['patient']])[0]
            #except XMLSyntaxError:
                #return 'Bad data', 400
            #except:
                #pass

        #else:
            # Do not allow client-defined ids
            #return 'Record not found', 405

    @tryton.transaction()
    def delete(self, log_id):
        '''Delete interaction'''

        #For now, don't allow (never allow?)
        return 'Not implemented', 405

class Version(Resource):
    @tryton.transaction()
    def get(self, log_id, v_id=None):
        '''Vread interaction'''

        #No support for this in Health... yet?
        return 'Not supported', 405

api.add_resource(Create,
                        '')
api.add_resource(Search,
                        '',
                        '/_search')
api.add_resource(Validate,
                        '/_validate',
                        '/_validate/<int:log_id>')
api.add_resource(Record, '/<int:log_id>')
api.add_resource(Version,
                        '/<int:log_id>/_history',
                        '/<int:log_id>/_history/<string:v_id>')

@api.representation('xml')
@api.representation('text/xml')
@api.representation('application/xml')
@api.representation('application/xml+fhir')
def output_xml(data, code, headers=None):
    if hasattr(data, 'export_to_xml_string'):
        resp = make_response(data.export_to_xml_string(), code)
    elif hasattr(data, 'export'):
        output=StringIO()
        data.export(outfile=output, namespacedef_='xmlns="http://hl7.org/fhir"', pretty_print=False, level=4)
        content = output.getvalue()
        output.close()
        resp = make_response(content, code)
    else:
        resp = make_response(data, code)
    resp.headers.extend(headers or {})
    resp.headers['Content-type']='application/xml+fhir' #Return proper type
    return resp

@api.representation('json')
@api.representation('application/json')
@api.representation('application/json+fhir')
def output_json(data, code, headers=None):
    resp = make_response(data,code)
    resp.headers.extend(headers or {})
    resp.headers['Content-type']='application/json+fhir' #Return proper type
    return resp


@api.representation('atom')
@api.representation('application/atom')
@api.representation('application/atom+fhir')
def output_atom(data, code, headers=None):
    resp = make_response(data, code)
    resp.headers.extend(headers or {})
    resp.headers['Content-type']='application/atom+fhir' #Return proper type
    return resp
