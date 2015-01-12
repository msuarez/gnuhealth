from flask import Blueprint, request, url_for
from StringIO import StringIO
from lxml.etree import XMLSyntaxError
from server.health_fhir import (health_Procedure, health_OperationOutcome, parse,
                            parseEtree, Bundle, find_record, health_Search)
from server.common import tryton, Resource, search_error_string, get_userid
import lxml
import os.path
import sys

# Procedure models
amb_procedure = tryton.pool.get('gnuhealth.ambulatory_care_procedure')
surg_procedure = tryton.pool.get('gnuhealth.operation')
rounds_procedure = tryton.pool.get('gnuhealth.rounding_procedure')

# REST prefixes (e.g., amb-3 is amb_procedure model, id  = 3)
#   Note: Must match the Procedure_Map
model_map = {
        'amb': amb_procedure,
        'surg': surg_procedure,
        'rounds': rounds_procedure}

class OP_Create(Resource):
    @tryton.transaction(user=get_userid)
    def post(self):
        '''Create interaction'''
        return 'not implemented', 405
        try:
            c=StringIO(request.data)
            res=parse(c, silence=True)
            c.close()
            res.set_models()
        except:
            e=sys.exc_info()[1]
            oo=health_OperationOutcome()
            oo.add_issue(details=e, severity='fatal')
            return oo, 400
        else:
            return 'Created', 201, {'Location': url_for('op_record', log_id=())}

class OP_Search(Resource):
    @tryton.transaction(user=get_userid)
    def get(self):
        '''Search interaction'''
        s = health_Search(endpoint='procedure')
        queries=s.get_queries(request.args)
        try:
            bd=Bundle(request=request)
            for query in queries:
                if query['query'] is not None:
                    recs = model_map[query['model']].search(query['query'])
                    if recs:
                        for rec in recs:
                            try:
                                p = health_Procedure(gnu_record=rec)
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

class OP_Validate(Resource):
    @tryton.transaction(user=get_userid)
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
            if os.path.isfile('schemas/procedure.xsd'):
                # 2) Validate against XMLSchema
                with open('schemas/procedure.xsd') as t:
                    sch=lxml.etree.parse(t)

                xmlschema=lxml.etree.XMLSchema(sch)
                if not xmlschema.validate(doc):
                    error = xmlschema.error_log.last_error
                    oo=health_OperationOutcome()
                    oo.add_issue(details=error.message, severity='error')
                    return oo, 400
            else:
                # 2) If no schema, check if it correctly parses to a Procedure
                try:
                    pat=parseEtree(StringIO(doc))
                    if not isinstance(pat, health_Procedure):
                        oo=health_OperationOutcome()
                        oo.add_issue(details='Not a procedure resource', severity='error')
                        return oo, 400
                except:
                    e = sys.exc_info()[1]
                    oo=health_OperationOutcome()
                    oo.add_issue(details=e, severity='fatal')
                    return oo, 400

            if log_id:
                # 3) Check if procedure exists
                record = find_record(model_map[log_id[0]], [('id', '=', log_id)])
                if not record:
                    oo=health_OperationOutcome()
                    oo.add_issue(details='No procedure', severity='error')
                    return oo, 422
                else:
                    #TODO: More checks
                    return 'Valid update', 200
            else:
                # 3) Passed checks
                return 'Valid', 200

class OP_Record(Resource):
    @tryton.transaction(user=get_userid)
    def get(self, log_id):
        '''Read interaction'''
        model = model_map[log_id[0]]
        record = find_record(model, [('id', '=', log_id[1])])
        if record:
            try:
                d=health_Procedure(gnu_record=record)
            except:
                return 'Record not found', 404
            else:
                return d, 200
        else:
            return 'Record not found', 404
            #if track deleted records
            #return 'Record deleted', 410

    @tryton.transaction(user=get_userid)
    def put(self, log_id):
        '''Update interaction'''
        return 'Not supported', 405

    @tryton.transaction(user=get_userid)
    def delete(self, log_id):
        '''Delete interaction'''

        #For now, don't allow (never allow?)
        return 'Not implemented', 405

class OP_Version(Resource):
    @tryton.transaction(user=get_userid)
    def get(self, log_id, v_id=None):
        '''Vread interaction'''

        #No support for this in Health... yet?
        return 'Not supported', 405

__all__=['OP_Create', 'OP_Search', 'OP_Validate', 'OP_Record', 'OP_Version']
