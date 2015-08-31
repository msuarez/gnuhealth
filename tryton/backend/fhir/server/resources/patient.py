from flask import request
from server.common import Resource
from server.resources import SearchRecords
from server.resources import ReadRecord
from server.resources import ValidateRecord
from server.resources import Routing
#from server.common import tryton

# Extra patient models
#party = tryton.pool.get('party.party')
#du = tryton.pool.get('gnuhealth.du')
#contact = tryton.pool.get('party.contact_mechanism')
#lang = tryton.pool.get('ir.lang')
#country = tryton.pool.get('country.country')
#subdivision = tryton.pool.get('country.subdivision')

class PAT_Create(Resource):
    def post(self):
        '''Create interaction'''
        return 'Not supported', 405
        #try:
            #c=StringIO(request.data)
            #res=parse(c, silence=True)
            #c.close()
            #res.set_models()
            #p = res.create_patient(subdivision=subdivision,
                                #party=party,
                                #country=country,
                                #contact=contact,
                                #lang=lang,
                                #du=du,
                                #patient=patient)
        #except:
            #e=sys.exc_info()[1]
            #oo=health_OperationOutcome()
            #oo.add_issue(details=e, severity='fatal')
            #return oo, 400
        #else:
            #return 'Created', 201, {'Location': url_for('pat_record', log_id=p.id)}

class PAT_Search(Resource):
    def get(self):
        '''Search interaction'''
        action = SearchRecords(endpoint='patient', request=request)
        return action.records

class PAT_Validate(Resource):
    def post(self, log_id=None):
        '''Validate interaction'''
        action = ValidateRecord(endpoint='patient', record=request.data)
        return action.valid

class PAT_Record(Resource):
    def get(self, log_id):
        '''Read interaction'''
        action = ReadRecord(endpoint='patient', log_id=log_id)
        return action.record

    def put(self, log_id):
        '''Update interaction'''
        return 'Not supported', 405

    def delete(self, log_id):
        '''Delete interaction'''
        return 'Not implemented', 405

class PAT_Version(Resource):
    def get(self, log_id, v_id=None):
        '''Vread interaction'''
        return 'Not supported', 405

routing = Routing('Patient')
routing['create'] = PAT_Create
routing['search'] = PAT_Search
routing['validate'] = PAT_Validate
routing['record'] = PAT_Record
routing['version'] = PAT_Version

__all__=['routing']
