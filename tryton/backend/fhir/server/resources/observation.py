from flask import request
from server.common import Resource
from server.resources import SearchRecords
from server.resources import ReadRecord
from server.resources import ValidateRecord
from server.resources import Routing


class OBS_Create(Resource):
    def post(self):
        '''Create interaction'''
        return 'Not implemented', 405

class OBS_Search(Resource):
    def get(self):
        '''Search interaction'''
        action = SearchRecords(endpoint='observation', request=request)
        return action.records

class OBS_Validate(Resource):
    def post(self, log_id=None):
        '''Validate interaction'''
        action = ValidateRecord(endpoint='observation', record=request.data)
        return action.valid

class OBS_Record(Resource):
    def get(self, log_id):
        '''Read interaction'''
        action = ReadRecord(endpoint='observation', log_id=log_id)
        return action.record

    def put(self, log_id):
        '''Update interaction'''
        return 'Not supported', 405

    def delete(self, log_id):
        '''Delete interaction'''
        return 'Not implemented', 405

class OBS_Version(Resource):
    def get(self, log_id, v_id=None):
        '''Vread interaction'''
        return 'Not supported', 405

routing = Routing('Observation')
routing['create'] = OBS_Create
routing['search'] = OBS_Search
routing['validate'] = OBS_Validate
routing['record'] = OBS_Record
routing['version'] = OBS_Version

__all__=['routing']
