from flask import Blueprint, request, current_app, make_response
from flask.ext.restful import Resource, abort, reqparse
from health_fhir_patient_class import gnu_patient, parse
from extensions import (tryton, api)
import json
import fhir_xml as supermod

# Patient model
patient = tryton.pool.get('gnuhealth.patient')

# Party model
party = tryton.pool.get('party.party')

def etree_to_dict(tree):
    '''Converts an etree into a dictionary.'''
    #TODO Peculiarities of FHIR standard need to
    #    be addresssed
    children=tree.getchildren()
    if children:
        return {tree.tag: [etree_to_dict(c) for c in children]}
    else:
        return {tree.tag: dict(tree.attrib)}

# 'Patient' blueprint on '/Patient'
patient_endpoint = Blueprint('patient_endpoint', __name__,
                                template_folder='templates',
                                url_prefix="/Patient")

# Initialize api restful
api.init_app(patient_endpoint)

class Create(Resource):
    @tryton.transaction()
    def post(self):
        try:
            # Doesn't work yet
            c=StringIO(request.data)
            res=parse(c)
            c.close()
            ds = res.get_gnu_patient()
            n = party.create([ds['party']])[0]
            ds['patient']['name']=n
            p=patient.create([ds['patient']])
        except:
            abort(400, message="Bad data")

class Search(Resource):
    @tryton.transaction()
    def get(self):
        #Search interaction
        #TODO Search implementation is important, but
        #    also very robust, so keep it simple for now
        #    but need to write general search parser in 
        #    order that we can just plug in criteria for
        #    each resource

        allowed={'_id': 'id', 'active': None, 'address': None,
                'animal-breed': None, 'animal-species': None,
                'birthdate': 'dob', 'family': None,
                'gender': 'sex', 'given': None,
                'identifier': 'puid', '_language': None,
                'language': None, 'link': None, 'name': None,
                'phonetic': None, 'provider': None, 'telecom': None}
        def crit():
            _id = request.args.get('_id')
            if _id:
                return (allowed['_id'], _id)
            identifier = request.args.get('identifier')
            if identifier:
                return (allowed['identifier'], identifier)
            return None
        m=crit()
        if m:
            rec = patient.search([m[0], '=', m[1]], limit=1)
            if rec:
                d=gnu_patient()
                d.set_gnu_patient(rec[0])
                d.import_from_gnu_patient()
                return d
        #TODO OperationOutcome; for now an error
        abort(403, message="No matching record(s)")

class Validate(Resource):
    @tryton.transaction()
    def post(self, log_id):
        #Validate interaction
        abort(405, message='Not implemented.')

class Record(Resource):
    @tryton.transaction()
    def get(self, log_id):
        #Read interaction
        record = patient.search(['id', '=', log_id], limit=1)
        if record:
            d=gnu_patient()
            d.set_gnu_patient(record[0])
            d.import_from_gnu_patient()
            return d
        else:
            abort(404, message="Record not found")
            #if track deleted records
            #abort(410, message="Record deleted")

    @tryton.transaction()
    def put(self, log_id):
        #Update interaction
        abort(405, message='Not implemented.')

    @tryton.transaction()
    def delete(self, log_id):
        #Delete interaction
        abort(405, message='Not implemented.')

class Version(Resource):
    @tryton.transaction()
    def get(self, log_id, v_id):
        #Vread interaction
        abort(405, message='Not implemented.')

api.add_resource(Create, '/')
api.add_resource(Search,
                        '/',
                        '/_search')
api.add_resource(Validate,
                        '/_validate',
                        '/_validate/<int:log_id>',
                defaults={'log_id': None})
api.add_resource(Record, '/<int:log_id>')
api.add_resource(Version,
                        '/<int:log_id>/_history',
                        '/<int:log_id>/_history/<string:v_id>',
                defaults={'v_id': None})

@api.representation('xml')
@api.representation('text/xml')
@api.representation('application/xml')
@api.representation('application/xml+fhir')
def output_xml(data, code, headers=None):
    resp = make_response(data.export_to_xml_string(), code)
    resp.headers.extend(headers or {})
    resp.headers['Content-type']='application/xml+fhir' #Return proper type
    return resp

@api.representation('json')
@api.representation('application/json')
@api.representation('application/json+fhir')
def output_json(data, code, headers=None):
    #resp = make_response(json.dumps(data),code)
    #resp.headers.extend(headers or {})
    #resp.headers['Content-type']='application/json+fhir' #Return proper type
    #return resp
    pass


@api.representation('atom')
@api.representation('application/atom')
@api.representation('application/atom+fhir')
def output_atom(data, code, headers=None):
    #resp = make_response(data, code)
    #resp.headers.extend(headers or {})
    #resp.headers['Content-type']='application/atom+fhir' #Return proper type
    #return resp
    pass
