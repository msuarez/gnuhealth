from flask import request
from server.common import Resource
from server.resources import SearchRecords
from server.resources import ReadRecord
from server.resources import ValidateRecord
from server.resources import Routing

class IM_Create(Resource):
    def post(self):
        '''Create interaction'''
        return 'Not supported', 405

class IM_Search(Resource):
    def get(self):
        '''Read interaction'''
        action = SearchRecords(endpoint='immunization', request=request)
        return action.records


class IM_Validate(Resource):
    def post(self, log_id=None):
        '''Validate interaction'''
        action = ValidateRecord(endpoint='immunization', record=request.data)
        return action.valid

class IM_Record(Resource):
    def get(self, log_id):
        action = ReadRecord(endpoint='immunization', log_id=log_id)
        return action.record

    def put(self, log_id):
        '''Update interaction'''
        return 'Not supported', 405

    def delete(self, log_id):
        '''Delete interaction'''
        return 'Not implemented', 405

class IM_Version(Resource):
    def get(self, log_id, v_id=None):
        '''Vread interaction'''
        return 'Not supported', 405

routing = Routing('Immunization')
routing['create'] = IM_Create
routing['search'] = IM_Search
routing['validate'] = IM_Validate
routing['record'] = IM_Record
routing['version'] = IM_Version

__all__=['routing']
