from flask import request
from server.common import Resource
from server.resources import SearchRecords
from server.resources import ReadRecord
from server.resources import ValidateRecord
from server.resources import Routing

class MED_Create(Resource):
    def post(self):
        '''Create interaction'''
        return 'not implemented', 405

class MED_Search(Resource):
    def get(self):
        '''Search interaction'''
        action = SearchRecords(endpoint='medication', request=request)
        return action.records

class MED_Validate(Resource):
    def post(self, log_id=None):
        '''Validate interaction'''
        action = ValidateRecord(endpoint='medication', record=request.data)
        return action.valid

class MED_Record(Resource):
    def get(self, log_id):
        '''Read interaction'''
        action = ReadRecord(endpoint='medication', log_id=log_id)
        return action.record

    def put(self, log_id):
        '''Update interaction'''
        return 'Not supported', 405

    def delete(self, log_id):
        '''Delete interaction'''
        return 'Not implemented', 405

class MED_Version(Resource):
    def get(self, log_id, v_id=None):
        '''Vread interaction'''
        return 'Not supported', 405

routing = Routing('Medication')
routing['create'] = MED_Create
routing['search'] = MED_Search
routing['validate'] = MED_Validate
routing['record'] = MED_Record
routing['version'] = MED_Version

__all__=['routing']
