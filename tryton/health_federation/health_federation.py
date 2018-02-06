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
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import requests


__all__ = ['FederationNodeConfig','FederationQueue', 'FederationObject']

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


class FederationQueue(ModelSQL, ModelView):
    'Federation Queue'
    __name__ = 'gnuhealth.federation.queue'

    msgid = fields.Char('Message ID', required=True,
        help="Message UID")
    model = fields.Char('Model', help="Source Model")
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

class FederationObject(ModelSQL, ModelView):
    'Federation Object'
    __name__ = 'gnuhealth.federation.object'

    model = fields.Char('Model', help="Local Model")
    fields = fields.Text('Fields', help="Contains a list of "
        "the local model fields that participate on the federation.\n" \
        "Field, endpoint in Thalamus" \
        " and key in the federation, with the form field:endpoint:key")

    @classmethod
    def __setup__(cls):
        super(FederationObject, cls).__setup__()
        t = cls.__table__()
        cls._sql_constraints = [
            ('model_uniq', Unique(t, t.model),
             'The Model is already defined !')
        ]

