# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2008-2016 Luis Falcon <lfalcon@gnusolidario.org>
#    Copyright (C) 2011-2016 GNU Solidario <health@gnusolidario.org>
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


__all__ = ['FederationNodeConfig']

class FederationNodeConfig(ModelSingleton, ModelSQL, ModelView):
    'Federation Node Configuration'
    __name__ = 'gnuhealth.federation.config'

    host = fields.Char('Host', required=True, help="Federation HIS server")
    port = fields.Integer('Port', required=True, help="MongoDB port")
    database = fields.Char('DB',required=True, help="database name")
    user = fields.Char('User',required=True, help="User")
    password = fields.Char('Password', required=True, help="Password")
    
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
