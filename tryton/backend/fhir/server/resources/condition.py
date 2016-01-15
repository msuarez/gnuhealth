from flask import request
from server.common import get_userid, tryton
from server.common import Resource
from server.resources import SearchRecords
from server.resources import ReadRecord
from server.resources import ValidateRecord
from server.resources import Routing

class CO_Create(Resource):
    def post(self):
        '''Create interaction'''
        return 'not implemented', 405

class CO_Search(Resource):
    def get(self):
        action = SearchRecords(endpoint='condition', request=request)
        return action.records

class CO_Validate(Resource):
    def post(self, log_id=None):
        action = ValidateRecord(endpoint='condition', record=request.data)
        return action.valid

class CO_Record(Resource):
    def get(self, log_id):
        action = ReadRecord(endpoint='condition', log_id=log_id)
        return action.record

    def put(self, log_id):
        '''Update interaction'''
        return 'Not supported', 405

    def delete(self, log_id):
        '''Delete interaction'''
        return 'Not implemented', 405

class CO_Version(Resource):
    def get(self, log_id, v_id=None):
        '''Vread interaction'''
        return 'Not supported', 405


routing = Routing('Condition')
routing['create'] = CO_Create
routing['search'] = CO_Search
routing['validate'] = CO_Validate
routing['record'] = CO_Record
routing['version'] = CO_Version

__all__=['routing']
