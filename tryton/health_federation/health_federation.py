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
from trytond.model import ModelView, ModelSQL, ModelSingleton, fields
from trytond.transaction import Transaction
from trytond.pool import Pool
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure


__all__ = ['FederationNodeConfig']

class FederationNodeConfig(ModelSingleton, ModelSQL, ModelView):
    'Federation Node Configuration'
    __name__ = 'gnuhealth.federation.config'

    host = fields.Char('Host', required=True, help="Federation HIS server")
    port = fields.Integer('Port', required=True, help="MongoDB port")
    database = fields.Char('DB',required=True, help="database name")
    user = fields.Char('User',required=True, help="User")
    password = fields.Char('Password', required=True, help="Password")
    ssl = fields.Boolean('SSL', help="Use encrypted communication via SSL")
    
    @staticmethod
    def default_host():
        return 'localhost'

    @staticmethod
    def default_port():
        return 27017

    @staticmethod
    def default_database():
        return 'federation'

    @staticmethod
    def default_user():
        return 'gnuhealth'

    @classmethod
    def __setup__(cls):
        super(FederationNodeConfig, cls).__setup__()

        cls._buttons.update({
                'test_connection': {}
                    }),
    
    @classmethod
    @ModelView.button
    def test_connection(cls, argvs):
        
        host, port, database, user, password, ssl = \
            argvs[0].host, argvs[0].port, argvs[0].database, \
            argvs[0].user, argvs[0].password, argvs[0].ssl
        

        dbconn = MongoClient(host, port)
        db = dbconn[database]
        
        try:
            auth = db.authenticate(user, password)
  
        except:
            cls.raise_user_error("ERROR authenticating to Server")
        
        if auth:
            cls.raise_user_error("Connection OK")
