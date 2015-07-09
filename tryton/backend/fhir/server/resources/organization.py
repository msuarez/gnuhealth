from flask import Blueprint, request, url_for
from StringIO import StringIO
from lxml.etree import XMLSyntaxError
from server.health_fhir import (health_Organization, health_OperationOutcome,
                parse, parseEtree, Bundle, find_record, health_Search)
from trytond.transaction import Transaction
from server.common import tryton, Resource, search_error_string, get_userid
import lxml
import os.path
import sys

# Organization model(s)
organization = tryton.pool.get('gnuhealth.institution')

class ORG_Create(Resource):
    @tryton.transaction(user=get_userid)
    def post(self):
        """Create interaction"""

        return 'Not implemented', 405

class ORG_Search(Resource):
    @tryton.transaction(user=get_userid)
    def get(self):
        """Search interaction"""

        try:
            s = health_Search(endpoint='organization')
            query=s.get_query(request.args)
            total_recs = organization.search_count(query)
            per_page = int(request.args.get('_count', 10))
            page = int(request.args.get('page', 1))
            bd=Bundle(request=request, total=total_recs)
            offset = (page-1) * per_page
            for org in organization.search(query,
                                    offset=offset,
                                    limit=per_page,
                                    order=[('id', 'DESC')]):
                try:
                    p = health_Organization(gnu_record=org)
                except:
                    continue
                else:
                    bd.add_entry(p)
            return bd, 200
        except:
            oo=health_OperationOutcome()
            oo.add_issue(details=sys.exc_info()[1], severity='fatal')
            return oo, 400

class ORG_Validate(Resource):
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
            if os.path.isfile('schemas/organization.xsd'):
                # 2) Validate against XMLSchema
                with open('schemas/organization.xsd') as t:
                    sch=lxml.etree.parse(t)

                xmlschema=lxml.etree.XMLSchema(sch)
                if not xmlschema.validate(doc):
                    error = xmlschema.error_log.last_error
                    oo=health_OperationOutcome()
                    oo.add_issue(details=error.message, severity='error')
                    return oo, 400
            else:
                # 2) If no schema, check if it correctly parses to a Organization
                try:
                    pat=parseEtree(StringIO(doc))
                    if not isinstance(pat, health_Organization):
                        oo=health_OperationOutcome()
                        oo.add_issue(details='Not a organization resource', severity='error')
                        return oo, 400
                except:
                    e = sys.exc_info()[1]
                    oo=health_OperationOutcome()
                    oo.add_issue(details=e, severity='fatal')
                    return oo, 400

            if log_id:
                # 3) Check if organization exists
                record = organization.search([('id', '=', log_id)])
                if not record:
                    oo=health_OperationOutcome()
                    oo.add_issue(details='No organization', severity='error')
                    return oo, 422
                else:
                    #TODO: More checks
                    return 'Valid update', 200
            else:
                # 3) Passed checks
                return 'Valid', 200

class ORG_Record(Resource):
    @tryton.transaction(user=get_userid)
    def get(self, log_id):
        '''Read interaction'''
        record = find_record(organization, [('id', '=', log_id)])
        if record:
            try:
                d=health_Organization(gnu_record=record)
                return d, 200
            except:
                oo=health_OperationOutcome()
                oo.add_issue(details=sys.exc_info()[1], severity='error')
                return oo, 404
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

class ORG_Version(Resource):
    @tryton.transaction(user=get_userid)
    def get(self, log_id, v_id=None):
        '''Vread interaction'''
        return 'Not supported', 405

__all__=['ORG_Create', 'ORG_Search', 'ORG_Version', 'ORG_Validate', 'ORG_Record']
