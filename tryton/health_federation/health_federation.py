# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2008-2019 Luis Falcon <lfalcon@gnusolidario.org>
#    Copyright (C) 2011-2019 GNU Solidario <health@gnusolidario.org>
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

import ssl
from trytond.model import ModelView, ModelSQL, ModelSingleton, fields, Unique
from trytond.transaction import Transaction
from trytond.pool import Pool
from trytond.pyson import Eval, Not, Bool, PYSONEncoder, Equal, And, Or, If
import requests
import json
from uuid import uuid4
from trytond.rpc import RPC
from datetime import datetime, date

__all__ = ['FederationNodeConfig','FederationQueue', 'FederationObject',
    'PartyFed','PoLFed']


def set_fsync(model, records, flag):
    #Sets or disables the fsync flag that enables the record to be
    #enter in the Federation queue
    vals = {'fsync': flag}
    model.write(records, vals)

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

        if (not user or not password):
            cls.raise_user_error("Please setup the login credentials")

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
    node = fields.Char('Node', required=True,
        help="The originating node id")

    time_stamp = fields.Char('Timestamp', required=True,
        help="UTC timestamp at the moment of writing record on the node")

    federation_locator = fields.Char('Fed ID',
        help="Unique locator in Federation, "
        "such as person Federation account or Page of Life code")

    args = fields.Text('Arguments', required=True,
        help="Arguments")

    method = fields.Selection([
        (None, ''),
        ('POST', 'POST'),
        ('PATCH', 'PATCH'),
        ('DELETE', 'DELETE'),
        ('GET', 'GET'),
        ], 'Method', required=True,sort=False)

    state = fields.Selection([
        (None, ''),
        ('queued', 'Queued'),
        ('sent', 'Sent'),
        ('failed', 'Failed'),
        ], 'Status', sort=False)

    url_suffix = fields.Char('URL suffix',
        help="suffix to be passed to the URL")

    @staticmethod
    def default_node():
        # Get the Institution code as the originating node.
        HealthInst = Pool().get('gnuhealth.institution')
        institution = HealthInst.get_institution()

        if (institution):
            #Get the institution code associated to the ID
            institution_code = HealthInst(institution).code

        else:
            FederationQueue.raise_user_error(
                "You need to create a health Institution first")

        return institution_code

    @classmethod
    def send_record(cls,record):
        rc = False

        host, port, user, password, ssl_conn, verify_ssl, protocol = \
            FederationNodeConfig.get_conn_params()


        if (record.method == 'PATCH'):
            if (record.federation_locator):
                #Traverse each resource and its data fields.
                # arg : Dictionary for each of the data elements in the
                #       list of values
                # [{resource, fields[{name, value}]

                for arg in json.loads(record.args):
                    vals = {}
                    modification_info = {}

                    # Include the modification information
                    modification_info = {'user':user, \
                        'timestamp': record.time_stamp,
                        'node': record.node}

                    vals['modification_info'] = modification_info

                    url = protocol + host + ':' + str(port)

                    resource, fields = arg['resource'],\
                        arg['fields']

                    # Add resource and instance to URL
                    url = url + '/' + resource + '/' + record.url_suffix

                    for field in fields:
                        fname, fvalue = field['name'], field['value']
                        vals[fname]= fvalue

                    send_data = requests.request('PATCH',url,
                        data=json.dumps(vals), \
                        auth=(user, password), verify=verify_ssl)

                    if (send_data):
                        rc = True
            else:
                print ("No federation record locator found .. no update")

        # Create the record on the Federation
        if (record.method == 'POST'):
            if (record.federation_locator):
                #Traverse each resource and its data fields.
                # arg : Dictionary for each of the data elements in the
                #       list of values
                # [{resource, fields[{name, value}]

                for arg in json.loads(record.args):
                    vals = {}
                    creation_info = {}

                    # Include the creation information
                    creation_info = {'user':user, \
                        'timestamp': record.time_stamp,
                        'node': record.node}

                    vals['creation_info'] = creation_info

                    url = protocol + host + ':' + str(port)

                    resource, fields = arg['resource'],\
                        arg['fields']

                    # Add resource and instance to URL
                    url = url + '/' + resource + '/' + record.url_suffix

                    for field in fields:
                        fname, fvalue = field['name'], field['value']
                        vals[fname]= fvalue

                    send_data = requests.request('POST',url,
                        data=json.dumps(vals), \
                        auth=(user, password), verify=verify_ssl)

                    if (send_data):
                        rc = True
            else:
                print ("No federation record locator found .. no update")

        return rc

    @classmethod
    def parse_fields(cls,values,action,fields):
        ''' Returns, depending on the action, the fields that will be
            passed as arguments to Thalamus
        '''
        # Fedvals : Values to send to the federation, that contain the
        # resource, the field, and the value of such field.

        field_mapping = fields.split(',')
        resources = []
        fedvals = []

        fed_key = {}
        n=0
        for val in field_mapping:
            #Retrieve the field name, the federation resource name
            #and the associated federation resource field .
            #string of the form field:fed_resource:fed_field
            field, fed_resource, fed_field = val.split(':')
            if (field in values.keys()):
                #Check that the local field is on shared federation list
                #and retrieve the equivalent federation field name

                # Optimize the process, by not duplicating the resources
                # Each resource will appear just once, with the list of
                # its fields.
                # Create a new item in the resource list
                # to be returned, if this is not yet there.

                # Serialize the date, datetime objects to be JSON compat
                if isinstance(values[field], (datetime, date)):
                    values[field] = values[field].isoformat()

                if fed_resource not in resources:
                    fed_key = {
                        "resource": fed_resource,
                        "fields":[
                            {
                            "name": fed_field,
                            "value": values[field]
                            }]
                        }

                    resources.append(fed_resource)
                    fedvals.append(fed_key)

                else:
                    # Otherwise, if the resource exists on the list,
                    # we add the new field values to it.

                    n=0
                    for record in fedvals:
                        if fed_resource == record['resource']:
                            fedvals[n]['fields'].append({"name": fed_field, \
                                "value": values[field]})
                        n=n+1

        return fedvals

    @classmethod
    def enqueue(cls,model, federation_loc, time_stamp, node, values,
        action, url_suffix):

        fields = FederationObject.get_object_fields(model)
        # Federation locator : Unique ID of the resource
        # such as personal federation account or institution ID
        # it depends on the resource (people, PoL, institution, ... )

        #Remove spaces and newlines from fields
        fields = fields.replace(" ","").replace("\n","")

        if (fields):
            # retrieve the federation field names and values in a dict
            fields_to_enqueue = cls.parse_fields(values,action,fields)
            # Continue the enqueue process with the fields

            if fields_to_enqueue:
                rec = []
                vals = {}
                vals['msgid'] = str(uuid4())
                vals['model'] = model
                vals['time_stamp'] = str(time_stamp)
                vals['args'] = json.dumps(fields_to_enqueue)
                vals['method'] = action
                vals['state'] = 'queued'
                vals['federation_locator'] = federation_loc
                vals['url_suffix'] = url_suffix
                rec.append(vals)
                #Write the record to the enqueue list
                cls.create(rec)

    @classmethod
    def __setup__(cls):
        super(FederationQueue, cls).__setup__()
        t = cls.__table__()
        cls._sql_constraints = [
            ('msgid_uniq', Unique(t,t.msgid), \
                'The Message ID must be unique !'),]

        cls._buttons.update({
            'send': {'invisible': Equal(Eval('state'), 'sent')}
            })

    @classmethod
    @ModelView.button
    def send(cls, records):
        # Verify and send each record to Thalamus individually
        # It allows to get specific status on each operation
        # record: individual record on gnuhealth.federation.queue model
        for record in records:
            rec = []
            res = cls.send_record(record)
            if res:
                rec.append(record)
                cls.write(rec, {'state': 'sent'})
            else:
                cls.write(rec, {'state': 'failed'})


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
        cls.__rpc__.update({
                'get_object_fields': RPC(check_access=False),
                })

class PartyFed(ModelSQL):
    """
    Demographics Model to participate on the Federation

    Methods : write (PATCH), create (POST)
    """

    __name__ = 'party.party'

    # Controls if the updated information will be sent to the Federation.
    #   True: Info will be sent to the federation queue
    #   False: The info is up-todate with the federation or is local
    fsync = fields.Boolean('Fsync',
        help="If active, this record information will" \
            " be sent to the Federation")

    @staticmethod
    def default_fsync():
        return True

    @classmethod
    def write(cls, parties, values):
        #First exec the Party class write method from health package
        super(PartyFed, cls).write(parties, values)

        for party in parties:
            action = "PATCH"
            # Retrieve federation account (for people only)
            fed_acct = party.federation_account
            fsync = party.fsync
            # Verify that the person has a Federation account.
            # and the fsync flag is set for the record
            if (fed_acct and values):
                if (fsync or 'fsync' not in values.keys()):
                    # Start Enqueue process
                    node=None
                    #Because du_address is a functional field
                    # does not exist at DB level, we always pass the
                    # latest / current value
                    values['du_address'] = party.du_address
                    time_stamp = party.write_date
                    url_suffix = fed_acct
                    FederationQueue.enqueue(cls.__name__,
                        fed_acct, time_stamp, node, values,action,
                        url_suffix)

                    #Unset the fsync flag locally once the info has been
                    #sent to the Federation queue
                    set_fsync(cls, parties, False)

    @classmethod
    def create(cls, vlist):
        vlist = [x.copy() for x in vlist]

        # Execute first the creation of party
        parties = super(PartyFed, cls).create(vlist)

        for values in vlist:
            fed_acct = parties[0].federation_account

            # Check if the record has just been imported of modified
            # from the federation. In that case, skip sending it
            # to the federation queue

            fsync = parties[0].fsync
            # If the user has a federation ID, then enqueue the
            # record to be sent and created in the Federation

            if fed_acct and fsync:
                action="POST"
                node=None

                #Because du_address is a functional field
                # does not exist at DB level, we always pass the
                # latest / current value
                values['du_address'] = parties[0].du_address

                url_suffix = fed_acct
                time_stamp = parties[0].create_date
                FederationQueue.enqueue(cls.__name__,
                    fed_acct, time_stamp, node, values,
                    action,url_suffix)

                #Unset the fsync flag locally once the info has been
                #sent to the Federation queue
                if (fsync):
                    set_fsync(cls, parties, False)

        return parties

class PoLFed(ModelSQL):
    """
    Page of Life Model to participate on the Federation

    Methods : write (PATCH), create (POST)
    """

    __name__ = 'gnuhealth.pol'

    # Controls if the updated information will be sent to the Federation.
    #   True: Info will be sent to the federation queue
    #   False: The info is up-todate with the federation or is local
    fsync = fields.Boolean('Fsync',
        help="If active, this record information will" \
            " be sent to the Federation")

    @staticmethod
    def default_fsync():
        return True

    @classmethod
    def write(cls, pols, values):
        super(PoLFed, cls).write(pols, values)

        for pol in pols:
            action = "PATCH"
            # Retrieve page of life unique ID into fed_identifier
            fed_identifier = pol.page
            federation_account = pol.federation_account

            fsync = pol.fsync
            # Verify that the page has the federation identifier.
            # and the fsync flag is set for the record
            if (fed_identifier and values):
                if (fsync or 'fsync' not in values.keys()):
                    # Start Enqueue process
                    node=None
                    time_stamp = pol.write_date
                    url_suffix = federation_account + '/' + fed_identifier
                    FederationQueue.enqueue(cls.__name__,
                        fed_identifier, time_stamp, node, values,
                        action, url_suffix)

                    #Unset the fsync flag locally once the info has been
                    #sent to the Federation queue
                    set_fsync(cls, pols, False)


    @classmethod
    def create(cls, vlist):
        vlist = [x.copy() for x in vlist]

        # Execute first the creation of PoL
        pols = super(PoLFed, cls).create(vlist)

        for values in vlist:
            fed_identifier = pols[0].page
            federation_account = pols[0].federation_account
            # Check if the record has just been imported of modified
            # from the federation. In that case, skip sending it
            # to the federation queue

            fsync = pols[0].fsync
            # If the page has a federation ID, then enqueue the
            # record to be sent and created in the Federation

            if fed_identifier and fsync:
                action="POST"
                node=None
                time_stamp = pols[0].create_date
                url_suffix = federation_account + '/' + fed_identifier
                FederationQueue.enqueue(cls.__name__,
                    fed_identifier, time_stamp, node, values,
                    action, url_suffix)

                #Unset the fsync flag locally once the info has been
                #sent to the Federation queue
                if (fsync):
                    set_fsync(cls, pols, False)

        return pols
