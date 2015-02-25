from flask import Blueprint, request, url_for
from StringIO import StringIO
from lxml.etree import XMLSyntaxError
from server.health_fhir import (health_Patient, health_OperationOutcome, parse,
                        parseEtree, Bundle, find_record, health_Search)
from server.common import tryton, Resource, search_error_string, get_userid
import lxml
import os.path
import sys

# Patient models
patient = tryton.pool.get('gnuhealth.patient')
party = tryton.pool.get('party.party')
du = tryton.pool.get('gnuhealth.du')
contact = tryton.pool.get('party.contact_mechanism')
lang = tryton.pool.get('ir.lang')
country = tryton.pool.get('country.country')
subdivision = tryton.pool.get('country.subdivision')

class PAT_Create(Resource):
    @tryton.transaction(user=get_userid)
    def post(self):
        '''Create interaction'''
        return 'Not supported', 405
        try:
            c=StringIO(request.data)
            res=parse(c, silence=True)
            c.close()
            res.set_models()
            p = res.create_patient(subdivision=subdivision,
                                party=party,
                                country=country,
                                contact=contact,
                                lang=lang,
                                du=du,
                                patient=patient)
        except:
            e=sys.exc_info()[1]
            oo=health_OperationOutcome()
            oo.add_issue(details=e, severity='fatal')
            return oo, 400
        else:
            return 'Created', 201, {'Location': url_for('pat_record', log_id=p.id)}

class PAT_Search(Resource):
    @tryton.transaction(user=get_userid)
    def get(self):
        '''Search interaction'''
        try:
            s = health_Search(endpoint='patient')
            query=s.get_query(request.args)
            total_recs = patient.search_count(query)
            per_page = int(request.args.get('_count', 10))
            page = int(request.args.get('page', 1))
            bd=Bundle(request=request, total=total_recs)
            offset = (page-1) * per_page
            for rec in patient.search(query,
                                    offset=offset,
                                    limit=per_page,
                                    order=[('id', 'DESC')]):
                try:
                    p = health_Patient(gnu_record=rec)
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

class PAT_Validate(Resource):
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
                record = find_record(patient, [('id', '=', log_id)])
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

class PAT_Record(Resource):
    @tryton.transaction(user=get_userid)
    def get(self, log_id):
        '''Read interaction'''
        record = find_record(patient, [('id', '=', log_id)])
        if record:
            d=health_Patient(gnu_record=record)
            return d, 200
        else:
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

class PAT_Version(Resource):
    @tryton.transaction(user=get_userid)
    def get(self, log_id, v_id=None):
        '''Vread interaction'''
        return 'Not supported', 405

__all__=['PAT_Version', 'PAT_Record', 'PAT_Validate',
            'PAT_Search', 'PAT_Create']
