from flask import request
from server.common import Resource
from server.resources import SearchRecords
from server.resources import ReadRecord
from server.resources import ValidateRecord
from server.resources import Routing

class FH_Create(Resource):
    def post(self):
        '''Create interaction'''
        return 'Not implemented', 405

class FH_Search(Resource):
    def get(self):
        '''Search interaction'''
        # NOTE We search from patient, not family_history
        action = SearchRecords(endpoint='family_history', request=request)
        return action.records

class FH_Validate(Resource):
    def post(self, log_id=None):
        '''Validate interaction'''
        action = ValidateRecord(endpoint='family_history', record=request.data)
        return action.valid

class FH_Record(Resource):
    def get(self, log_id):
        '''Read interaction'''
        # NOTE We search from patient, not family_history
        action = ReadRecord(endpoint='family_history', log_id=log_id)
        return action.record

    def put(self, log_id):
        '''Update interaction'''
        return 'Not supported', 405

    def delete(self, log_id):
        '''Delete interaction'''
        return 'Not implemented', 405

class FH_Version(Resource):
    def get(self, log_id, v_id=None):
        '''Vread interaction'''
        return 'Not supported', 405

routing = Routing('FamilyHistory')
routing['create'] = FH_Create
routing['search'] = FH_Search
routing['validate'] = FH_Validate
routing['record'] = FH_Record
routing['version'] = FH_Version

__all__=['routing']
