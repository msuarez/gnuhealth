from flask import Blueprint, request, current_app, make_response, url_for
from flask.ext.restful import Resource, abort, reqparse
from StringIO import StringIO
from lxml.etree import XMLSyntaxError
from health_fhir import health_DiagnosticReport, health_OperationOutcome, parse, parseEtree, Bundle, find_record, health_Search
from extensions import tryton
from flask.ext.restful import Api
from utils import search_error_string
import lxml
import json
import os.path
import sys

# DiagnosticReport model
diagnostic_report = tryton.pool.get('gnuhealth.lab')

# 'diagnostic_report' blueprint on '/DiagnosticReport'
diagnostic_report_endpoint = Blueprint('diagnostic_report_endpoint', __name__,
                                template_folder='templates',
                                url_prefix="/DiagnosticReport")
# Initialize api restful
api = Api(diagnostic_report_endpoint)

model_map={
        'labreport': diagnostic_report}

class Create(Resource):
    @tryton.transaction()
    def post(self):
        '''Create interaction'''
        return 'not implemented', 405
        try:
            c=StringIO(request.data)
            res=parse(c, silence=True)
            c.close()
        except:
            e=sys.exc_info()[1]
            oo=health_OperationOutcome()
            oo.add_issue(details=e, severity='fatal')
            return oo, 400
        else:
            return 'Created', 201, {'Location': 
                            url_for('diagnostic_report_endpoint.record',
                                    log_id=('labreport', p.id))}

class Search(Resource):
    @tryton.transaction()
    def get(self):
        '''Search interaction'''
        s = health_Search(endpoint='diagnostic_report')
        queries=s.get_queries(request.args)
        bd=Bundle(request=request)
        try:
            for query in queries:
                if query['query'] is not None:
                    recs = diagnostic_report.search(query['query'])
                    for rec in recs:
                        try:
                            p = health_DiagnosticReport(gnu_record=rec)
                        except:
                            continue
                        else:
                            bd.add_entry(p)

            if bd.entries:
                return bd, 200
            else:
                return search_error_string(request.args), 403
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
            if os.path.isfile('schemas/diagnostic_report.xsd'):
                # 2) Validate against XMLSchema
                with open('schemas/diagnostic_report.xsd') as t:
                    sch=lxml.etree.parse(t)

                xmlschema=lxml.etree.XMLSchema(sch)
                if not xmlschema.validate(doc):
                    error = xmlschema.error_log.last_error
                    oo=health_OperationOutcome()
                    oo.add_issue(details=error.message, severity='error')
                    return oo, 400
            else:
                # 2) If no schema, check if it correctly parses to a diagnostic_report
                try:
                    pat=parseEtree(StringIO(doc))
                    if not isinstance(pat, health_diagnostic_report):
                        oo=health_OperationOutcome()
                        oo.add_issue(details='Not a diagnostic_report resource', severity='error')
                        return oo, 400
                except:
                    e = sys.exc_info()[1]
                    oo=health_OperationOutcome()
                    oo.add_issue(details=e, severity='fatal')
                    return oo, 400

            if log_id:
                # 3) Check if diagnostic_report exists
                record = find_record(diagnostic_report, [('id', '=', log_id)])
                if not record:
                    oo=health_OperationOutcome()
                    oo.add_issue(details='No diagnostic_report', severity='error')
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
        model = model_map.get(log_id[0])
        if model is None:
            return 'No record', 404
        id = log_id[1]
        field = log_id[2]
        record = find_record(model, [('id', '=', id)])
        if record:
            try:
                d=health_DiagnosticReport(gnu_record=record, field=field)
                return d, 200
            except:
                pass
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
