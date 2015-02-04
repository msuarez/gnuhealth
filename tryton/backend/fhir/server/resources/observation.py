from flask import Blueprint, request, url_for
from StringIO import StringIO
from lxml.etree import XMLSyntaxError
from server.health_fhir import (health_Patient, health_Observation,
        Observation_Map, health_OperationOutcome, parse, parseEtree, Bundle,
        health_Search, find_record, FieldError)
from server.common import search_error_string, tryton, Resource, get_userid
import lxml
import os.path
import sys


# Observation models
lab = tryton.pool.get('gnuhealth.lab.test.critearea')
#eva = tryton.pool.get('gnuhealth.patient.evaluation')
#rounds = tryton.pool.get('gnuhealth.patient.rounding')
#amb = tryton.pool.get('gnuhealth.patient.ambulatory_care')
#icu = tryton.pool.get('gnuhealth.icu.apache2')

# Prefix mapping
model_map={ 'lab': lab}
        #'eval': eva,
        #'rounds': rounds,
        #'amb': amb,
        #'icu': icu}

class OBS_Create(Resource):
    @tryton.transaction(user=get_userid)
    def post(self):
        '''Create interaction'''
        return 'Not implemented', 405
        try:
            c=StringIO(request.data)
            res=parse(c, silence=True)
            c.close()
            res.set_models()
            p = res.create_observation()
        except:
            e=sys.exc_info()[1]
            oo=health_OperationOutcome()
            oo.add_issue(details=e, severity='fatal')
            return oo, 400
        else:
            return 'Created', 201, {'Location':  url_for('obs_record', log_id=())}

class OBS_Search(Resource):
    @tryton.transaction(user=get_userid)
    def get(self):
        '''Search interaction'''
        try:
            # TODO Pass the models to the class to cleanup this uglines
            bd = Bundle(request=request)
            s = health_Search(endpoint='observation')
            queries = s.get_queries(request.args)
            for query in queries:
                if query['query'] is not None:
                    recs = model_map[query['model']].search(query['query'])
                    for rec in recs:
                        # If specific fields match
                        if query['fields']:
                            for f in query['fields']:
                                try:
                                    o = health_Observation(gnu_record=rec, field=f)
                                except:
                                    continue
                                else:
                                    bd.add_entry(o)
                        else:
                            # Model does not need field
                            try:
                                o = health_Observation(gnu_record=rec)
                            except:
                                continue
                            else:
                                bd.add_entry(o)
            if bd.entries:
                return bd, 200
            else:
                return search_error_string(request.args), 403
        except:
            oo=health_OperationOutcome()
            oo.add_issue(details=sys.exc_info()[1], severity='fatal')
            return oo, 400

class OBS_Validate(Resource):
    @tryton.transaction(user=get_userid)
    def post(self, log_id=None):
        '''Validate interaction'''
        try:
            # 1) Must correctly parse as XML
            c=StringIO(request.data)
            doc=lxml.etree.parse(c)
            c.close()
        except XMLSyntaxError as e:
            oo=health_OperationOutcome()
            oo.add_issue(details=e, severity='fatal')
            return oo, 400

        except:
            e = sys.exc_info()[1]
            oo=health_OperationOutcome()
            oo.add_issue(details=e, severity='fatal')
            return oo, 400

        else:
            if os.path.isfile('schemas/observation.xsd'):
                # 2) Validate against XMLSchema
                with open('schemas/observation.xsd') as t:
                    sch=lxml.etree.parse(t)

                xmlschema=lxml.etree.XMLSchema(sch)
                if not xmlschema.validate(doc):
                    error = xmlschema.error_log.last_error
                    oo=health_OperationOutcome()
                    oo.add_issue(details=error.message, severity='error')
                    return oo, 400
            else:
                # 2) If no schema, check if it correctly parses to an Observation
                try:
                    pat=parseEtree(StringIO(doc))
                    if not isinstance(pat, health_Observation):
                        oo=health_OperationOutcome()
                        oo.add_issue(details='Not an observation resource', severity='error')
                        return oo, 400
                except:
                    e = sys.exc_info()[1]
                    oo=health_OperationOutcome()
                    oo.add_issue(details=e, severity='fatal')
                    return oo, 400

            if log_id:
                # 3) Check if observation exists
                #     Observation updating.... No allow
                return 'Not supported', 405
            else:
                # 3) Passed checks
                return 'Valid', 200

class OBS_Record(Resource):
    @tryton.transaction(user=get_userid)
    def get(self, log_id):
        '''Read interaction'''
        model = model_map.get(log_id[0])
        if model is None:
            return 'No record', 404
        id = log_id[1]
        field = log_id[2]
        record = find_record(model, [('id', '=', id)])
        if record:
            d=health_Observation()
            try:
                d.set_gnu_observation(record, field=field)
            except:
                return 'Record not found', 404
            else:
                return d, 200
        else:
            return 'Record not found', 404
            #if track deleted records
            #return 'Record deleted', 410

    @tryton.transaction(user=get_userid)
    def put(self, log_id):
        '''Update interaction'''
        return 'Not supported', 405

    @tryton.transaction(user=get_userid)
    def delete(self, log_id):
        '''Delete interaction'''

        #For now, don't allow (never allow?)
        return 'Not implemented', 405

class OBS_Version(Resource):
    @tryton.transaction(user=get_userid)
    def get(self, log_id, v_id=None):
        '''Vread interaction'''

        #No support for this in Health... yet?
        return 'Not supported', 405

__all__=['OBS_Version', 'OBS_Record', 'OBS_Validate',
            'OBS_Search', 'OBS_Create']
