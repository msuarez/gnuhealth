from flask import request, url_for, g
from StringIO import StringIO
from lxml.etree import XMLSyntaxError
from server.health_fhir import (health_DiagnosticReport,
                    health_OperationOutcome, parse, parseEtree, Bundle,
                    find_record, health_Search)
from server.common import search_error_string, tryton, Resource, get_userid
import lxml
import os.path
import sys

# DiagnosticReport models
diagnostic_report = tryton.pool.get('gnuhealth.lab')

class DR_Create(Resource):
    @tryton.transaction(user=get_userid)
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
                            url_for('dr_record',
                                    log_id=p.id)}

class DR_Search(Resource):
    @tryton.transaction(user=get_userid)
    def get(self):
        '''Search interaction'''
        try:
            s = health_Search(endpoint='diagnostic_report')
            query=s.get_query(request.args)
            total_recs = diagnostic_report.search_count(query)
            per_page = int(request.args.get('_count', 10))
            page = int(request.args.get('page', 1))
            bd=Bundle(request=request,
                            total=total_recs,
                            per_page = per_page,
                            page = page)
            offset = (page-1) * per_page
            for rec in diagnostic_report.search(query,
                                    offset=offset,
                                    limit=per_page,
                                    order=[('id', 'DESC')]):
                try:
                    p = health_DiagnosticReport(gnu_record=rec)
                except:
                    continue
                else:
                    bd.add_entry(p)

            if bd.entries:
                return bd, 200
            else:
                oo=health_OperationOutcome()
                oo.add_issue(details=search_error_string(request.args),
                        severity='warning')
                return oo, 403
        except:
            oo=health_OperationOutcome()
            oo.add_issue(details=sys.exc_info()[1], severity='fatal')
            return oo, 400

class DR_Validate(Resource):
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

class DR_Record(Resource):
    @tryton.transaction(user=get_userid)
    def get(self, log_id):
        '''Read interaction'''
        record = find_record(diagnostic_report, [('id', '=', log_id)])
        if record:
            try:
                d=health_DiagnosticReport(gnu_record=record)
                return d, 200
            except:
                oo=health_OperationOutcome()
                oo.add_issue(details='No record', severity='fatal')
                return oo, 404
        oo=health_OperationOutcome()
        oo.add_issue(details='No record', severity='fatal')
        return oo, 404

    @tryton.transaction(user=get_userid)
    def put(self, log_id):
        '''Update interaction'''
        return 'Not supported', 405

    @tryton.transaction(user=get_userid)
    def delete(self, log_id):
        '''Delete interaction'''
        return 'Not implemented', 405

class DR_Version(Resource):
    @tryton.transaction(user=get_userid)
    def get(self, log_id, v_id=None):
        '''Vread interaction'''
        return 'Not supported', 405

__all__=['DR_Version', 'DR_Record', 'DR_Validate', 'DR_Search', 'DR_Create']
