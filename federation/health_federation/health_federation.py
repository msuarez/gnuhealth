# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2008-2017 Luis Falcon <lfalcon@gnusolidario.org>
#    Copyright (C) 2011-2017 GNU Solidario <health@gnusolidario.org>
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


__all__ = ['FederationNodeConfig']

class FederationNodeConfig(ModelSingleton, ModelSQL, ModelView):
    'Federation Node Configuration'
    __name__ = 'gnuhealth.federation.config'

    host = fields.Char('Host', required=True,
        help="GNU Health Thalamus server")
    port = fields.Integer('Port', required=True, help="Thalamus port")
    user = fields.Char('user',required=True,
        help="Admin associated to this institution")
    password = fields.Char('Password', required=True,
        help="Password of the institution admin user in the Federation")
    ssl = fields.Boolean('SSL',
        help="Use encrypted communication via SSL")
    self_signed = fields.Boolean('Self-signed certificate',
        help="Check it if your SSL certificate have been self-signed")
    
    # TODO: Check the associated institution and use as
    # a default value its id
    
    @staticmethod
    def default_host():
        return 'localhost'

    @staticmethod
    def default_port():
        return 8443

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

        host, port, user, password, ssl_conn, self_signed = \
            argvs[0].host, argvs[0].port,  \
            argvs[0].user, argvs[0].password, argvs[0].ssl, \
            argvs[0].self_signed
        
        
        if (ssl_conn):
            protocol = 'https://'
        else:
            protocol = 'http://'
            
        url = protocol + host + ':' + port + '/institution' + institution

        try:
            conn = requests.get(url,
                auth=(user, password), verify=self_signed)        

        except:
            cls.raise_user_error("ERROR authenticating to Server")
        
        if auth:
            cls.raise_user_error("Connection OK")
