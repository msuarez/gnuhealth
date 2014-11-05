from flask import Blueprint, request, current_app, make_response
from flask.ext.restful import Resource, abort, reqparse
from StringIO import StringIO
from lxml.etree import XMLSyntaxError
from health_fhir import health_Patient, health_Observation, Observation_Map, health_OperationOutcome, parse, parseEtree, Bundle, find_record, FieldError
from extensions import tryton
import lxml
import json
import os.path
import sys
from flask.ext.restful import Api
from utils import search_query_generate


# Lab result model (sp?)
lab = tryton.pool.get('gnuhealth.lab.test.critearea')

# Patient evals
eva = tryton.pool.get('gnuhealth.patient.evaluation')

# Nurse rounds
rounds = tryton.pool.get('gnuhealth.patient.rounding')

# Ambulatory care
amb = tryton.pool.get('gnuhealth.patient.ambulatory_care')

# ICU
icu = tryton.pool.get('gnuhealth.icu.apache2')

#URL mapping (UGLY!)
model_map={ 'lab': lab,
        'eval': eva,
        'rounds': rounds,
        'amb': amb,
        'icu': icu}

# 'Observation' blueprint on '/Observation'
observation_endpoint = Blueprint('observation_endpoint', __name__,
                                template_folder='templates',
                                url_prefix="/Observation")

# Initialize api restful
api = Api(observation_endpoint)

class Create(Resource):
    @tryton.transaction()
    def post(self):
        '''Create interaction'''
        return 'Not implemented', 405
        try:
            c=StringIO(request.data)
            res=parse(c, silence=True)
            c.close()
            res.set_models()
            p = res.create_observation()
        except:
            e=sys.exc_info()[1]
            oo=health_OperationOutcome()
            oo.add_issue(details=e, severity='fatal')
            return oo, 400
        else:
            return 'Created', 201, {'Location': ''.join(['/Observation/', str(p.id)])}

class Search(Resource):
    @tryton.transaction()
    def get(self):
        '''Search interaction'''
        try:
            bd=Bundle(request=request)
            m = Observation_Map()
            for k,v in m.search_mapping.items():
                query, fields=search_query_generate(v, request.args)
                if query is not None:
                    recs = model_map[k].search(query)
                    for rec in recs:
                        # If specific fields match
                        if fields:
                            for f in fields:
                                try:
                                    o = health_Observation(gnu_record=rec, field=f)
                                except:
                                    continue
                                else:
                                    bd.add_entry(o)
                        else:
                            # No fields match
                            try:
                                o = health_Observation(gnu_record=rec)
                            except:
                                continue
                            else:
                                bd.add_entry(o)
            if bd.entries:
                return bd, 200
            else:
                st =[]
                for k,v in request.args.items():
                    st.append(':'.join([k,v]))
                return 'No matching record(s) for {0}'.format(' '.join(st)), 403
        except:
            oo=health_OperationOutcome()
            oo.add_issue(details=sys.exc_info()[1], severity='fatal')
            return oo, 400

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
            e = sys.exc_info()[1]
            oo=health_OperationOutcome()
            oo.add_issue(details=e, severity='fatal')
            return oo, 400

        else:
            if os.path.isfile('schemas/observation.xsd'):
                # 2) Validate against XMLSchema
                with open('schemas/observation.xsd') as t:
                    sch=lxml.etree.parse(t)

                xmlschema=lxml.etree.XMLSchema(sch)
                if not xmlschema.validate(doc):
                    error = xmlschema.error_log.last_error
                    oo=health_OperationOutcome()
                    oo.add_issue(details=error.message, severity='error')
                    return oo, 400
            else:
                # 2) If no schema, check if it correctly parses to an Observation
                try:
                    pat=parseEtree(StringIO(doc))
                    if not isinstance(pat, health_Observation):
                        oo=health_OperationOutcome()
                        oo.add_issue(details='Not an observation resource', severity='error')
                        return oo, 400
                except:
                    e = sys.exc_info()[1]
                    oo=health_OperationOutcome()
                    oo.add_issue(details=e, severity='fatal')
                    return oo, 400

            if log_id:
                # 3) Check if observation exists
                #     Observation updating.... No allow
                return 'Not supported', 405
            else:
                # 3) Passed checks
                return 'Valid', 200

class Record(Resource):
    @tryton.transaction()
    def get(self, log_id):
        '''Read interaction'''
        model = model_map.get(log_id[0])
        if model is None:
            return 'No record', 404
        id = log_id[1]
        field = log_id[2]
        record = find_record(model, [('id', '=', id)])
        if record:
            d=health_Observation()
            try:
                d.set_gnu_observation(record, field=field)
            except:
                # Classed raised error
                return 'Record not found', 404
            else:
                return d, 200
        else:
            return 'Record not found', 404
            #if track deleted records
            #return 'Record deleted', 410

    @tryton.transaction()
    def put(self, log_id):
        '''Update interaction'''
        return 'Not supported', 405

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
                        '/_validate/<item:log_id>')
api.add_resource(Record, '/<item:log_id>')
api.add_resource(Version,
                        '/<item:log_id>/_history',
                        '/<item:log_id>/_history/<string:v_id>')

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
