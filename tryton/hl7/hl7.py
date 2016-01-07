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
import datetime
import os

from trytond.model import ModelView, ModelSQL,  ModelSingleton, fields
from trytond.pool import Pool
from mllp_server_launcher import MLLPServerLauncher

logger = logging.getLogger(__name__)

__all__ = ['HL7Config', 'TransactionHandler', 'MessageLogger']


class HL7Config(ModelSingleton, ModelSQL, ModelView):
    """HL7 Module Configuration"""
    __name__ = "hl7.hl7"

    enabled = fields.Boolean(string="Enabled", select=False,
                             help="Start/Stop the MLLP Server")
    message_logger_enabled = fields.Boolean(string="Enabled", select=False,
                                            help="Activate/Deactivate the HL7 Message Logger")
    mllp_server_port = fields.Integer(string="Port", required=True, readonly=False,
                                      help="Listening port of the MLLP Server")
    application_code = fields.Char(string="Application Code", required=True, readonly=False,
                                   help="value used for sending application field (MSH_3)")

    @staticmethod
    def default_enabled(): 
        return True
    
    @staticmethod
    def default_message_logger_enabled(): 
        return True
    
    @staticmethod
    def default_mllp_server_port():
        # default port for MLLP/HL7 (2575)
        return 2575 
    
    @staticmethod
    def default_application_code():
        return "gnuhealth"
    
    @staticmethod
    def check_module_status():
        pool = Pool()

        hl7_conf = pool.get("hl7.hl7")
        new_conf = hl7_conf.search([])
        
        hl7_enabled = new_conf[0].enabled
        message_logger_enabled = new_conf[0].message_logger_enabled
        logger.debug("NEW PORT VALUE IS: %s" % new_conf[0].mllp_server_port)
        logger.debug("NEW SENDING APP VALUE IS: %s" % new_conf[0].application_code)
        logger.debug("NEW ENABLED VALUE IS: %s" % hl7_enabled)
        logger.debug("NEW MESSAGE LOGGER ENABLED VALUE IS: %s" % message_logger_enabled)
        
        pid_dir = os.getcwd()
        
        mllp_server_launcher = MLLPServerLauncher("*", new_conf[0].mllp_server_port,
                                                  pool.database_name, pid_dir, message_logger_enabled)
            
        if hl7_enabled:
            logger.debug("Trying to (re)-start the mllp server... PID_DIR: %s" % pid_dir)
            mllp_server_launcher.stop_mllp_server()
            mllp_server_launcher.start_mllp_server()
        else:
            logger.debug("Trying to stop the mllp server")
            mllp_server_launcher.stop_mllp_server()
            
    @classmethod
    def write(cls, parties, vals, *args):
        super(HL7Config, cls).write(parties, vals)
        logger.debug("Record updated")
        cls.check_module_status()
  
  
class MessageLogger(ModelSQL, ModelView):
    """HL7 Message Logger"""
    __name__ = "hl7.message_logger"    
    
    request = fields.Char(string="HL7 Request", required=True, readonly=True,
                          help="The HL7 incoming message")
    response = fields.Char(string="HL7 Response", required=True, readonly=True,
                           help="The HL7 response message")
    handler_module = fields.Char(string="HL7 Handler", required=True, readonly=True,
                                 help="The module that handled the request and built the response")
    creation_date = fields.DateTime(string="Creation Date", required=True, readonly=True,
                                    help="The date related to this HL7 transaction")
    
    @classmethod
    def default_creation_date(cls):
        return datetime.datetime.now()
       
    
class TransactionHandler(ModelSQL):
    """HL7 Transaction Handler"""
    __name__ = "hl7.transaction_handler"
    
    message_type = fields.Char(string="HL7 Message type", required=True, readonly=True,
                               help="Message type (MSH_9)")
    message_handler_module_name = fields.Char(string="Message Handler Module Name", required=True, readonly=True,
                                              help="The name of the module handling this type of HL7 message")
    message_handler_class_name = fields.Char(string="Message Handler Class Name", required=True, readonly=True,
                                             help="The name of the class handling this type of HL7 message")