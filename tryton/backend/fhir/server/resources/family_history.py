from flask import Blueprint, request, url_for
from StringIO import StringIO
from lxml.etree import XMLSyntaxError
from server.health_fhir import (health_FamilyHistory, health_OperationOutcome,
                parse, parseEtree, Bundle, find_record, health_Search)
from trytond.transaction import Transaction
from server.common import tryton, Resource, search_error_string, get_userid
import lxml
import os.path
import sys

# FamilyHistory models
family_history = tryton.pool.get('gnuhealth.patient.family.diseases')
patient = tryton.pool.get('gnuhealth.patient')

class FH_Create(Resource):
    @tryton.transaction(user=get_userid)
    def post(self):
        '''Create interaction'''
        return 'Not implemented', 405

class FH_Search(Resource):
    @tryton.transaction(user=get_userid)
    def get(self):
        '''Search interaction'''
        # NOTE We search from patient, not family_history
        try:
            s = health_Search(endpoint='family_history')
            query=s.get_query(request.args)
            total_recs = patient.search_count(query)
            per_page = int(request.args.get('_count', 10))
            page = int(request.args.get('page', 1))
            bd=Bundle(request=request, total=total_recs)
            offset = (page-1) * per_page
            for pat in patient.search(query,
                                    offset=offset,
                                    limit=per_page,
                                    order=[('id', 'DESC')]):
                try:
                    p = health_FamilyHistory(gnu_records=pat.family_history)
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

class FH_Validate(Resource):
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
            if os.path.isfile('schemas/family_history.xsd'):
                # 2) Validate against XMLSchema
                with open('schemas/family_history.xsd') as t:
                    sch=lxml.etree.parse(t)

                xmlschema=lxml.etree.XMLSchema(sch)
                if not xmlschema.validate(doc):
                    error = xmlschema.error_log.last_error
                    oo=health_OperationOutcome()
                    oo.add_issue(details=error.message, severity='error')
                    return oo, 400
            else:
                # 2) If no schema, check if it correctly parses to a FamilyHistory
                try:
                    pat=parseEtree(StringIO(doc))
                    if not isinstance(pat, health_FamilyHistory):
                        oo=health_OperationOutcome()
                        oo.add_issue(details='Not a family_history resource', severity='error')
                        return oo, 400
                except:
                    e = sys.exc_info()[1]
                    oo=health_OperationOutcome()
                    oo.add_issue(details=e, severity='fatal')
                    return oo, 400

            if log_id:
                # 3) Check if family_history exists
                record = family_history.search([('patient.id', '=', log_id)])
                if not record:
                    oo=health_OperationOutcome()
                    oo.add_issue(details='No family_history', severity='error')
                    return oo, 422
                else:
                    #TODO: More checks
                    return 'Valid update', 200
            else:
                # 3) Passed checks
                return 'Valid', 200

class FH_Record(Resource):
    @tryton.transaction(user=get_userid)
    def get(self, log_id):
        '''Read interaction'''
        records = family_history.search([('patient.id', '=', log_id)])
        if records:
            d=health_FamilyHistory(gnu_records=records)
            return d, 200
        else:
            oo=health_OperationOutcome()
            oo.add_issue(details='No record', severity='error')
            return oo, 404

    @tryton.transaction(user=get_userid)
    def put(self, log_id):
        '''Update interaction'''
        return 'Not supported', 405

    @tryton.transaction(user=get_userid)
    def delete(self, log_id):
        '''Delete interaction'''
        return 'Not implemented', 405

class FH_Version(Resource):
    @tryton.transaction(user=get_userid)
    def get(self, log_id, v_id=None):
        '''Vread interaction'''
        return 'Not supported', 405

__all__=['FH_Create', 'FH_Search', 'FH_Version', 'FH_Validate', 'FH_Record']
