from flask import Blueprint, request, url_for
from StringIO import StringIO
from lxml.etree import XMLSyntaxError
from health_fhir import (health_Practitioner, health_OperationOutcome,
                parse, parseEtree, Bundle, find_record, health_Search)
from extensions import tryton, Api, Resource
import lxml
import os.path
import sys

# Practitioner model
practitioner = tryton.pool.get('gnuhealth.healthprofessional')

# 'Practitioner' blueprint on '/Practitioner'
practitioner_endpoint = Blueprint('practitioner_endpoint', __name__,
                                template_folder='templates',
                                url_prefix="/Practitioner")
# Initialize api restful
api = Api(practitioner_endpoint)

class Create(Resource):
    @tryton.transaction()
    def post(self):
        '''Create interaction'''
        return 'not implemented', 405
        try:
            c=StringIO(request.data)
            res=parse(c, silence=True)
            c.close()
            res.set_models()
            p=res.create_practitioner()
        except:
            e=sys.exc_info()[1]
            oo=health_OperationOutcome()
            oo.add_issue(details=e, severity='fatal')
            return oo, 400
        else:
            return 'Created', 201, {'Location': url_for('practitioner_endpoint.record', log_id=p.id)}

class Search(Resource):
    @tryton.transaction()
    def get(self):
        '''Search interaction'''
        s = health_Search(endpoint='practitioner')
        queries=s.get_queries(request.args)
        bd=Bundle(request=request)
        try:
            for query in queries:
                if query['query'] is not None:
                    recs = practitioner.search(query['query'])
                    if recs:
                        for rec in recs:
                            try:
                                p = health_Practitioner(gnu_record=rec)
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
            if os.path.isfile('schemas/practitioner.xsd'):
                # 2) Validate against XMLSchema
                with open('schemas/practitioner.xsd') as t:
                    sch=lxml.etree.parse(t)

                xmlschema=lxml.etree.XMLSchema(sch)
                if not xmlschema.validate(doc):
                    error = xmlschema.error_log.last_error
                    oo=health_OperationOutcome()
                    oo.add_issue(details=error.message, severity='error')
                    return oo, 400
            else:
                # 2) If no schema, check if it correctly parses to a Practitioner
                try:
                    pat=parseEtree(StringIO(doc))
                    if not isinstance(pat, health_Practitioner):
                        oo=health_OperationOutcome()
                        oo.add_issue(details='Not a practitioner resource', severity='error')
                        return oo, 400
                except:
                    e = sys.exc_info()[1]
                    oo=health_OperationOutcome()
                    oo.add_issue(details=e, severity='fatal')
                    return oo, 400

            if log_id:
                # 3) Check if practitioner exists
                record = find_record(practitioner, [('id', '=', log_id)])
                if not record:
                    oo=health_OperationOutcome()
                    oo.add_issue(details='No practitioner', severity='error')
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
        record = find_record(practitioner, [('id', '=', log_id)])
        if record:
            d=health_Practitioner(gnu_record=record)
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
                        '/_validate/<int:log_id>')
api.add_resource(Record, '/<int:log_id>')
api.add_resource(Version,
                        '/<int:log_id>/_history',
                        '/<int:log_id>/_history/<string:v_id>')
