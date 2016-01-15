from flask import request
from server.common import Resource
from server.resources import SearchRecords
from server.resources import ReadRecord
from server.resources import ValidateRecord
from server.resources import Routing

class MS_Create(Resource):
    def post(self):
        '''Create interaction'''
        return 'not implemented', 405

class MS_Search(Resource):
    def get(self):
        '''Search interaction'''
        action = SearchRecords(endpoint='medication_statement', request=request)
        return action.records

class MS_Validate(Resource):
    def post(self, log_id=None):
        '''Validate interaction'''
        action = ValidateRecord(endpoint='medication_statement', record=request.data)
        return action.valid

class MS_Record(Resource):
    def get(self, log_id):
        '''Read interaction'''
        action = ReadRecord(endpoint='medication_statement', log_id=log_id)
        return action.record

    def put(self, log_id):
        '''Update interaction'''
        return 'Not supported', 405

    def delete(self, log_id):
        '''Delete interaction'''
        return 'Not implemented', 405

class MS_Version(Resource):
    def get(self, log_id, v_id=None):
        '''Vread interaction'''
        return 'Not supported', 405

routing = Routing('MedicationStatement')
routing['create'] = MS_Create
routing['search'] = MS_Search
routing['validate'] = MS_Validate
routing['record'] = MS_Record
routing['version'] = MS_Version

__all__=['routing']
