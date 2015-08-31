from flask import request
from server.common import Resource
from server.resources import SearchRecords
from server.resources import ReadRecord
from server.resources import ValidateRecord
from server.resources import Routing

class ORG_Create(Resource):
    def post(self):
        """Create interaction"""

        return 'Not implemented', 405

class ORG_Search(Resource):
    def get(self):
        """Search interaction"""
        action = SearchRecords(endpoint='organization', request=request)
        return action.records


class ORG_Validate(Resource):
    def post(self, log_id=None):
        '''Validate interaction'''
        action = ValidateRecord(endpoint='organization', record=request.data)
        return action.valid

class ORG_Record(Resource):
    def get(self, log_id):
        '''Read interaction'''
        action = ReadRecord(endpoint='organization', log_id=log_id)
        return action.record

    def put(self, log_id):
        '''Update interaction'''
        return 'Not supported', 405

    def delete(self, log_id):
        '''Delete interaction'''
        return 'Not implemented', 405

class ORG_Version(Resource):
    def get(self, log_id, v_id=None):
        '''Vread interaction'''
        return 'Not supported', 405


routing = Routing('Organization')
routing['create'] = ORG_Create
routing['search'] = ORG_Search
routing['validate'] = ORG_Validate
routing['record'] = ORG_Record
routing['version'] = ORG_Version

__all__=['routing']
