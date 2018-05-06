# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2008-2018 Luis Falcon <lfalcon@gnusolidario.org>
#    Copyright (C) 2011-2018 GNU Solidario <health@gnusolidario.org>
#
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
import ssl
from trytond.model import ModelView, ModelSQL, ModelSingleton, fields, Unique
from trytond.transaction import Transaction
from trytond.pool import Pool
from trytond.pyson import Eval, Not, Bool, PYSONEncoder, Equal, And, Or, If
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import requests
import json
from ast import literal_eval
from uuid import uuid4


__all__ = ['FederationNodeConfig','FederationQueue', 'FederationObject',
    'Party']

   
class FederationNodeConfig(ModelSingleton, ModelSQL, ModelView):
    'Federation Node Configuration'
    __name__ = 'gnuhealth.federation.config'

    host = fields.Char('Thalamus server', required=True,
        help="GNU Health Thalamus server")
    port = fields.Integer('Port', required=True, help="Thalamus port")
    user = fields.Char('User',required=True,
        help="Admin associated to this institution")
    password = fields.Char('Password', required=True,
        help="Password of the institution admin user in the Federation")
    ssl = fields.Boolean('SSL',
        help="Use encrypted communication via SSL")
    verify_ssl = fields.Boolean('Verify SSL cert',
        help="Check this option if your certificate has been emitted" \
            " by a CA authority. If it is a self-signed certifiate" \
            " leave it unchecked")
    enabled = fields.Boolean('Enabled', help="Mark if the node is active" \
        " in the Federation")
    
    # TODO: Check the associated institution and use as
    # a default value its id
    
    @staticmethod
    def default_host():
        return 'localhost'

    @staticmethod
    def default_port():
        return 8443

    @staticmethod
    def default_ssl():
        return True

    @staticmethod
    def default_enabled():
        return True

    @staticmethod
    def default_verify_ssl():
        return False

    @staticmethod
    def default_database():
        return 'federation'

    @classmethod
    def __setup__(cls):
        super(FederationNodeConfig, cls).__setup__()

        cls._buttons.update({
                'test_connection': {}
                    }),
    
    @classmethod
    @ModelView.button
    def test_connection(cls, argvs):
        """ Make the connection test to Thalamus Server
            from the GNU Health HMIS using the institution 
            associated admin and the related credentials
        """

        host, port, user, password, ssl_conn, verify_ssl = \
            argvs[0].host, argvs[0].port,  \
            argvs[0].user, argvs[0].password, argvs[0].ssl, \
            argvs[0].verify_ssl

        if (ssl_conn):
            protocol = 'https://'
        else:
            protocol = 'http://'
            
        url = protocol + host + ':' + str(port) + '/people/' + user
       
        try:
            conn = requests.get(url,
                auth=(user, password), verify=verify_ssl)        
            
        except:
            cls.raise_user_error("ERROR authenticating to Server")
        
        if conn:
            cls.raise_user_error("Connection to Thalamus Server OK !")

        else:
            cls.raise_user_error("ERROR authenticating to Server")

    @classmethod
    def get_conn_params(cls):
        # Retrieve the connection information for Thalamus
        #Retrieve the information from the Singleton object

        TInfo = Pool().get(cls.__name__)(1)
        host = TInfo.host
        port = TInfo.port
        user = TInfo.user
        password = TInfo.password
        ssl_conn = TInfo.ssl
        verify_ssl = TInfo.verify_ssl

        if (ssl_conn):
            protocol = 'https://'
        else:
            protocol = 'http://'

        return host, port, user, password, ssl_conn, verify_ssl, protocol

class FederationQueue(ModelSQL, ModelView):
    'Federation Queue'
    __name__ = 'gnuhealth.federation.queue'

    msgid = fields.Char('Message ID', required=True,
        help="Message UID")
    model = fields.Char('Model', required=True, help="Source Model")
    origin = fields.Char('Origin', required=True,
        help="The originating node id")

    time_stamp = fields.Char('Timestamp', required=True,
        help="UTC timestamp at the moment of writing record on the node")

    federation_locator = fields.Char('Fed ID',
        help="Unique locator in Federation, " 
        "such as person Federation account or institution Code")

    args = fields.Text('Arguments', required=True,
        help="Arguments")

    method = fields.Selection([
        (None, ''),
        ('POST', 'POST'),
        ('PATCH', 'PATCH'),
        ('DELETE', 'DELETE'),
        ('GET', 'GET'),
        ], 'Method', required=True,sort=False)

    status = fields.Selection([
        (None, ''),
        ('queued', 'Queued'),
        ('sent', 'Sent'),
        ('failed', 'Failed'),
        ], 'Status', sort=False)

    @staticmethod
    def default_origin():
        # Get the Institution code as the originating node.
        HealthInst = Pool().get('gnuhealth.institution')
        institution = HealthInst.get_institution()
        institution_code, = HealthInst.search_read([("name", "=", institution)],
            limit=1, fields_names=['code'])
        return institution_code['code']

    @classmethod
    def send_record(cls,record):
        # TODO: Send the record to Thalamus
        host, port, user, password, ssl_conn, verify_ssl, protocol = \
            FederationNodeConfig.get_conn_params()

        if (record.method == 'PATCH'):
            if (record.federation_locator):
                #Traverse each resource and its data fields.
                # arg : Dictionary for each of the data elements in the
                # list of values
                for arg in literal_eval(record.args):
                    url = protocol + host + ':' + str(port)
                    resource, field, value = arg['resource'],\
                        arg['field'], arg['value']
                    # Add resource and instance to URL
                    url = url + '/' + resource + '/' + record.federation_locator

                    vals = {}
                    vals[field]=value

                    send_data = requests.request('PATCH',url, data=json.dumps(vals), \
                        auth=(user, password), verify=verify_ssl)

            else:
                print ("No federation record locator found .. no update")

        return False

    @classmethod
    def parse_fields(cls,values,action,fields):
        ''' Returns depending on the action the fields that will be
            passed as arguments to Thalamus
        '''
        field_mapping = fields.split(',')
        # Fedvals : Values to send to the federation, that contain the
        # resource, the field, and the value of such field.
        fedvals = []
        for value in values:
            #Check that the local field is on shared federation list
            #and retrieve the equivalent federation field name
            for val in field_mapping:
                #Retrieve the field name, the federation resource name
                #and the associated federation resource field .
                #string of the form field:fed_resource:fed_field
                field, fed_resource, fed_field = val.split(':')
                if (field == value):
                    fed_key = {
                        "resource": fed_resource,
                        "field": fed_field,
                        "value": values[value]
                        }
                    fedvals.append(fed_key)
                    break
        return fedvals

    @classmethod
    def enqueue(cls,model, federation_loc, time_stamp, node, values, action):
        fields = FederationObject.get_object_fields(model)
        # Federation locator : Unique ID of the resource
        # such as personal federation account or institution ID
        # it depends on the resource (people, institution, ... )
        
        if (fields):
            # retrieve the federation field names and values in a dict
            fields_to_enqueue = cls.parse_fields(values,action,fields)
            # Continue the enqueue process with the fields
            rec = []
            vals = {}
            vals['msgid'] = str(uuid4())
            vals['model'] = model
            vals['time_stamp'] = str(time_stamp)
            vals['args'] = str(fields_to_enqueue)
            vals['method'] = action
            vals['status'] = 'queued'
            vals['federation_locator'] = federation_loc
            rec.append(vals)
            #Write the record to the enqueue list
            cls.create(rec)

    @classmethod
    def __setup__(cls):
        super(FederationQueue, cls).__setup__()

        cls._buttons.update({
            'send': {'invisible': Equal(Eval('status'), 'sent')}
            })

    @classmethod
    @ModelView.button
    def send(cls, records):
        # Verify and send each record to Thalamus individually
        # It allows to get specific status on each operation
        for record in records:
            rec = []
            res = cls.send_record(record)
            if res:
                rec.append(record)
                cls.write(rec, {'status': 'sent'})

class FederationObject(ModelSQL, ModelView):
    'Federation Object'
    __name__ = 'gnuhealth.federation.object'

    model = fields.Char('Model', help="Local Model")

    enabled = fields.Boolean('Enabled', help="Check if the model" \
        " is active to participate on the Federation")

    fields = fields.Text('Fields', help="Contains a list of "
        "the local model fields that participate on the federation.\n" \
        "Each line will have the format field:endpoint:key")

    @staticmethod
    def default_enabled():
        return True

    @classmethod
    def get_object_fields(cls, obj):
        model, = cls.search_read([("model", "=", obj)],
            limit=1, fields_names=['fields','enabled'])

        # If the model exist on the Federation Object, 
        # and is currently enabled, return the field names and their
        # equivalents on the Federation
        if (model and model['enabled']):
            return model['fields']
        
    @classmethod
    def __setup__(cls):
        super(FederationObject, cls).__setup__()
        t = cls.__table__()
        cls._sql_constraints = [
            ('model_uniq', Unique(t, t.model),
             'The Model is already defined !')
        ]


class Party(ModelSQL):
    __name__ = 'party.party'
    
    @classmethod
    def write(cls, parties, values):
        #First exec the Party class write method from health package
        super(Party, cls).write(parties, values)
        for party in parties:
            action = "PATCH"
            # Retrieve federation account (for people only)
            fed_acct = party.federation_account
            # Verify that the person has a Federation account.
            if (fed_acct):
                # Start Enqueue process
                node=None
                time_stamp = party.write_date
                FederationQueue.enqueue(cls.__name__, 
                    fed_acct, time_stamp, node, values,action)
