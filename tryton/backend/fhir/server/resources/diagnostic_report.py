from flask import request
from server.common import Resource
from server.resources import SearchRecords
from server.resources import ReadRecord
from server.resources import ValidateRecord
from server.resources import Routing

class DR_Create(Resource):
    def post(self):
        '''Create interaction'''
        return 'not implemented', 405

class DR_Search(Resource):
    def get(self):
        '''Search interaction'''
        action = SearchRecords(endpoint='diagnostic_report', request=request)
        return action.records

class DR_Validate(Resource):
    def post(self, log_id=None):
        action = ValidateRecord(endpoint='diagnostic_report', record=request.data)
        return action.valid

class DR_Record(Resource):
    def get(self, log_id):
        action = ReadRecord(endpoint='diagnostic_report', log_id=log_id)
        return action.record

    def put(self, log_id):
        '''Update interaction'''
        return 'Not supported', 405

    def delete(self, log_id):
        '''Delete interaction'''
        return 'Not implemented', 405

class DR_Version(Resource):
    def get(self, log_id, v_id=None):
        '''Vread interaction'''
        return 'Not supported', 405

routing = Routing('DiagnosticReport')
routing['create'] = DR_Create
routing['search'] = DR_Search
routing['validate'] = DR_Validate
routing['record'] = DR_Record
routing['version'] = DR_Version

__all__=['routing']
