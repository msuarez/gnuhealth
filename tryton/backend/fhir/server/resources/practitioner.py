from flask import Blueprint, request, url_for
from StringIO import StringIO
from lxml.etree import XMLSyntaxError
from server.health_fhir import (health_Practitioner, health_OperationOutcome,
                parse, parseEtree, Bundle, find_record, health_Search)
from server.common import tryton, Resource, search_error_string, get_userid
import lxml
import os.path
import sys

# Practitioner models
practitioner = tryton.pool.get('gnuhealth.healthprofessional')

class HP_Create(Resource):
    @tryton.transaction(user=get_userid)
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
            return 'Created', 201, {'Location': url_for('hp_record', log_id=p.id)}

class HP_Search(Resource):
    @tryton.transaction(user=get_userid)
    def get(self):
        '''Search interaction'''
        try:
            s = health_Search(endpoint='practitioner')
            query=s.get_query(request.args)
            total_recs = practitioner.search_count(query)
            per_page = int(request.args.get('_count', 10))
            page = int(request.args.get('page', 1))
            bd=Bundle(request=request, total=total_recs)
            offset = (page-1) * per_page
            for rec in practitioner.search(query,
                                    offset=offset,
                                    limit=per_page,
                                    order=[('id', 'DESC')]):
                try:
                    p = health_Practitioner(gnu_record=rec)
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

class HP_Validate(Resource):
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

class HP_Record(Resource):
    @tryton.transaction(user=get_userid)
    def get(self, log_id):
        '''Read interaction'''
        record = find_record(practitioner, [('id', '=', log_id)])
        if record:
            try:
                d=health_Practitioner(gnu_record=record)
                return d, 200
            except:
                oo=health_OperationOutcome()
                oo.add_issue(details=sys.exc_info()[1], severity='error')
                return oo, 404
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

class HP_Version(Resource):
    @tryton.transaction(user=get_userid)
    def get(self, log_id, v_id=None):
        '''Vread interaction'''
        return 'Not supported', 405

__all__=['HP_Create', 'HP_Search', 'HP_Version', 'HP_Validate', 'HP_Record']
