# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2008-2016 Luis Falcon <lfalcon@gnusolidario.org>
#    Copyright (C) 2011-2016 GNU Solidario <health@gnusolidario.org>
#    Copyright (C) 2015 CRS4
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

import logging

from trytond.model import ModelView, ModelSQL,  ModelSingleton, fields
from trytond.pool import Pool
from trytond.modules.hl7.hl7_handlers import GenericTransactionHandler, log_hl7_transaction
from supplier import GnuHealthPDQSupplier

logger = logging.getLogger(__name__)

__all__ = ['PDQConfig', 'AllowedApplications']


class PDQTransactionHandler(GenericTransactionHandler):
     
    def __init__(self, incoming_message, pool_manager, logger_enabled):
        super(PDQTransactionHandler, self).__init__(incoming_message, pool_manager, logger_enabled)
        self.pdq_supplier = GnuHealthPDQSupplier(self.pool_manager, self.incoming_message)

    def is_enabled(self):
        return self.pdq_supplier.is_pdq_module_enabled()

    @log_hl7_transaction
    def reply(self):
        try:
            response = self.pdq_supplier.create_pdq_response()
            return response
        except Exception, e:
            logger.error("PDQ dispatcher error: %s" % e)
            return self.pdq_supplier.build_error_response("PDQ handler found, but an error occurred during processing")


class AllowedApplications(ModelSQL, ModelView):
    """PDQ Allowed Applications"""
    __name__ = "pdq.allowed_applications"
    
    allowed_application = fields.Char(string="Application Name",
                                      help="The list of sending applications accepted by the PDQ module")
    # allowed_app_cmd = fields.Many2One("pdq.pdq", "allowed app", select=True, required=True)
    
    
class PDQConfig(ModelSingleton, ModelSQL, ModelView):
    """PDQ Module Configuration"""
    __name__ = "pdq.pdq"

    enabled = fields.Boolean(string="Enabled", select=False, help="Enable/Disable the PDQ Handler")
    filter_by_allowed_app = fields.Boolean(string="AllowedAppsFilter", select=True,
                                           help="Enable/Disable Allowed Applications Filter for incoming messages")
    facility_name = fields.Char(string="Facility Name", required=True, readonly=False,
                                help="The MSH 4 field value used for PDQ responses")
    encoding_char = fields.Selection(string="Encoding", selection=[("utf-8", "utf-8"), ("ascii", "ascii")],
                                     help="The encoding used for PDQ messages")
    country = fields.Selection('get_countries', 'Countries', help="The MSH 17 field value used for PDQ responses")
    language = fields.Selection('get_languages', 'Languages', help="The MSH 19 field value used for PDQ responses")

    @classmethod
    def get_countries(cls):
        # You can access the pool here.
        country = Pool().get('country.country')
        countries = country.search([])
        ret = []
        for c in countries:
                ret.append((c.code, c.name))
        return ret
    
    @classmethod
    def get_languages(cls):
        # You can access the pool here.
        language = Pool().get('country.country')
        languages = language.search([])
        ret = []
        for l in languages:
                ret.append((l.code, "%s (%s)" % (l.code, l.name)))
        return ret
   
    @classmethod
    def register_transaction_handler(cls):
        message_module_name = "pdq.pdq"
        message_class_name = PDQTransactionHandler.__name__
        transaction_handler = Pool().get('hl7.transaction_handler')
        logger.debug("PDQ Transaction Handler:%s" % str(transaction_handler))
        transactions = transaction_handler.search([('message_handler_class_name', '=', message_class_name)])
        
        if not transactions:
            transaction_handler.create([{"message_type": "QBP^Q22^QBP_Q21",
                                         "message_handler_module_name": message_module_name,
                                         "message_handler_class_name": message_class_name}])
            transaction_handler.create([{"message_type": "QBP^ZV1^QBP_Q21",
                                         "message_handler_module_name": message_module_name,
                                         "message_handler_class_name": message_class_name}])

    @classmethod
    def __setup__(cls):
        super(PDQConfig, cls).__setup__()
        cls.register_transaction_handler()
    
    @staticmethod
    def default_enabled(): 
        return True
  
    @staticmethod
    def check_module_status():
        pool = Pool()
        pdq_conf = pool.get("pdq.pdq")
        new_conf = pdq_conf.search([])
        
        pdq_enabled = new_conf[0].enabled
        logger.debug("NEW PDQ ENABLED VALUE IS: %s" % pdq_enabled)
     
    @classmethod
    def write(cls, pdq_conf_fields, vals, *args):
        
        super(PDQConfig, cls).write(pdq_conf_fields, vals)
        logger.debug("Record updated")
        cls.check_module_status()
