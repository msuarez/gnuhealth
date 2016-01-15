from server.resources.mappings import mappings
from server.common import get_userid, tryton
from server.health_fhir.datastore import find_record
from server.health_fhir import health_OperationOutcome as error
import lxml
import sys

class SearchRecords:
    
    def __init__(self, endpoint, request):
        if endpoint not in mappings:
            raise ValueError('Incorrect endpoint')

        self.endpoint = mappings[endpoint]
        self.request = request
        self.per_page = int(self.request.args.get('_count', 10))
        self.current_page = int(self.request.args.get('page', 1))
        self.offset = (self.current_page-1) * self.per_page
        self.query = mappings['search'].adapter(endpoint=endpoint,
                                                request_args=request.args)\
                                                        .query

    def __repr__(self):
        print('Search %s(%s)' % (self.endpoint, self.query))

    @property
    #@tryton.transaction(user=get_userid)
    @tryton.transaction(user=get_userid, context={'_check_access': True})
    def records(self):
        try:
            # TODO Better handling total results
            total_recs = self.endpoint.model.search_count(self.query)
            bd = mappings['bundle'].adapter(request=self.request, total=total_recs)
            for rec in self.endpoint.model.search(self.query,
                                    offset=self.offset,
                                    limit=self.per_page,
                                    order=[('id', 'DESC')]):
                try:
                    p = self.endpoint.adapter(gnu_record=rec)
                except:
                    # TODO Log it
                    continue
                else:
                    bd.add_entry(p)
            return bd, 200
        except:
            oo=error()
            oo.add_issue(details=sys.exc_info()[1], severity='fatal')
            return oo, 400

class ReadRecord:

    def __init__(self, endpoint, log_id):
        if endpoint not in mappings:
            raise ValueError('Incorrect endpoint')
        self.endpoint = mappings[endpoint]
        self.id_ = log_id

    def __repr__(self):
        print('Read %s(%s)' % (self.endpoint, self.id_))

    @property
    @tryton.transaction(user=get_userid, context={'_check_access': True})
    def record(self):
        find_query = [('id', '=', self.id_)]
        if self.endpoint.adapter.root_search:
            find_query += self.endpoint.adapter.root_search[0]

        record = find_record(self.endpoint.model, find_query)
        if record:
            try:
                d=self.endpoint.adapter(gnu_record=record)
                return d, 200
            except:
                #TODO LOG IT
                oo=error()
                oo.add_issue(details='Invalid record', severity='error')
                return oo, 404
        else:
            #TODO LOG
            oo=error()
            oo.add_issue(details='No record', severity='error')
            return oo, 404

class ValidateRecord:
    
    def __init__(self, endpoint, record):
        if endpoint not in mappings:
            raise ValueError('Incorrect endpoint')
        self.endpoint = mappings[endpoint]
        self.record = record

    def __repr__(self):
        print('Validate %s' % (self.endpoint))

    @property
    @tryton.transaction(user=get_userid, context={'_check_access': True})
    def valid(self):

        try:
            # 1) Must correctly parse as XML
            c=StringIO(self.record)
            doc=lxml.etree.parse(c)
            c.close()
        except XMLSyntaxError as e:
            #TODO LOG
            oo=error()
            oo.add_issue(details='Not a valid XML structure', severity='fatal')
            return oo, 400

        except:
            #TODO LOG
            oo=error()
            oo.add_issue(details='Invalid document', severity='fatal')
            return oo, 400

        else:
            # 2) Check if it correctly parses to the class
            try:
                pat=parseEtree(StringIO(doc))
                if not isinstance(pat, self.endpoint.adapter):
                    oo=error()
                    oo.add_issue(details='Invalid resource type', severity='error')
                    return oo, 400
            except:
                # TODO LOG
                oo=error()
                oo.add_issue(details='Other error', severity='fatal')
                return oo, 400

            if log_id:
                # 3) Check if model id exists
                record = find_record(self.endpoint.model, [('id', '=', log_id)])
                if not record:
                    oo=error()
                    oo.add_issue(details='No medication with that id', severity='error')
                    return oo, 422
                else:
                    #TODO: More checks
                    return 'Valid update', 200
            else:
                # 3) Passed checks
                return 'Valid', 200
        

__all__ = ['SearchRecords', 'ReadRecord', 'ValidateRecord']
