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
        s = health_Search(endpoint='patient')
        queries=s.get_queries(request.args)
        bd=Bundle(request=request)
        try:
            for query in queries:
                if query['query'] is not None:
                    recs = patient.search(query['query'])
                    if recs:
                        for rec in recs:
                            try:
                                p = health_Patient(gnu_record=rec)
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
        #TODO Use converter?
        record = find_record(patient, [('id', '=', log_id)])
        if record:
            d=health_Patient(gnu_record=record)
            return d, 200
        else:
            return 'Record not found', 404
            #if track deleted records
            #return 'Record deleted', 410

    @tryton.transaction(user=get_userid)
    def put(self, log_id):
        '''Update interaction'''
        return 'Not supported', 405
        #record = patient.search([('id', '=', log_id)], limit=1)
        #if record:
            #try:
                #c=StringIO(request.data)
                #res=parse(c)
                #c.close()
                #pat=parseEtree(StringIO(res))
                #if not isinstance(pat, health_Patient):
                    #return 'Resource type not supported', 404
                #ds = res.get_gnu_patient()
                #d = du.create([ds['du']])[0]
                #ds['party']['du']=d
                #n = party.create([ds['party']])[0]
                #for cs in ds['contact_mechanism']:
                    #if cs['value'] is not None:
                        #cs['party']=n
                        #contact.create([cs])
                #ds['patient']['name']=n
                #p=patient.create([ds['patient']])[0]
            #except XMLSyntaxError:
                #return 'Bad data', 400
            #except:
                #pass

        #else:
            # Do not allow client-defined ids
            #return 'Record not found', 405

    @tryton.transaction(user=get_userid)
    def delete(self, log_id):
        '''Delete interaction'''

        #For now, don't allow (never allow?)
        return 'Not implemented', 405

class PAT_Version(Resource):
    @tryton.transaction(user=get_userid)
    def get(self, log_id, v_id=None):
        '''Vread interaction'''

        #No support for this in Health... yet?
        return 'Not supported', 405

__all__=['PAT_Version', 'PAT_Record', 'PAT_Validate',
            'PAT_Search', 'PAT_Create']
