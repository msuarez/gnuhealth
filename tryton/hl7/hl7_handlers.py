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
from hl7apy.core import Message
from hl7apy.parser import parse_message
from hl7apy.mllp import AbstractHandler, UnsupportedMessageType, InvalidHL7Message

from sql.functions import Now

from trytond.transaction import Transaction

logger = logging.getLogger(__name__)


def log_hl7_transaction(met):
    def wrap(self, *args, **kwargs):
        message_res = met(self, *args, **kwargs)
        if self.logger_enabled:
            message_req = self.incoming_message

            logger.debug("Saving transition:\nIN: %s\nOUT: %s\nHandler: %s\n" % (message_req, message_res,
                                                                                 self.__class__.__name__))
            transaction = Transaction()
            logger.debug("Starting db transaction for domain:%s" % self.pool_manager.get_domain())
            transaction.start(self.pool_manager.get_domain(), 0)
            logger.debug("Connecting to table")
            hl7_message_logger = self.pool_manager.get_table("hl7.message_logger")
            logger.debug("Preparing query for table:::%s" % hl7_message_logger)

            cursor = transaction.cursor

            insert_columns = [hl7_message_logger.create_uid, hl7_message_logger.create_date,
                              hl7_message_logger.creation_date, hl7_message_logger.request,
                              hl7_message_logger.response, hl7_message_logger.handler_module]
            insert_values = [transaction.user, Now(), Now(), message_req,  message_res[1:-2],  self.__class__.__name__]

            cursor.execute(*hl7_message_logger.insert(insert_columns, [insert_values]))
            cursor.execute("commit")

            logger.debug("Query executed")
            transaction.stop()

        return message_res
    return wrap


class GenericTransactionHandler(AbstractHandler):
    def __init__(self, incoming_message, pool_manager, logger_enabled=True):
        super(GenericTransactionHandler, self).__init__(incoming_message)
        self.pool_manager = pool_manager
        self.logger_enabled = logger_enabled

    def is_enabled(self):
        """
        Get the current module status (Only an enabled module is able to handle incoming HL7 messages)
        """
        raise NotImplementedError("The method is_enabled() must be implemented in subclasses")

    def reply(self):
        raise NotImplementedError


class HL7ErrorHandler(GenericTransactionHandler):
    def __init__(self, exc, incoming_message, pool_manager, logger_enabled=True):
        logger.debug("Exception occurred: %s" % exc)
        super(HL7ErrorHandler, self).__init__(incoming_message, pool_manager, logger_enabled)
        self.exc = exc

    def is_enabled(self):
        return True

    def reply(self):
        if isinstance(self.exc, InvalidHL7Message):
            handler = InvalidMessageHandler(self.incoming_message, self.logger_enabled)
        elif isinstance(self.exc, UnsupportedMessageType):
            handler = UnsupportedMessageTypeHandler(self.incoming_message, self.logger_enabled)
        else:
            handler = GenericErrorHandler(self.incoming_message, self.logger_enabled)
        return handler.reply()


class GenericErrorHandler(object):
    def __init__(self, incoming_message, logger_enabled=True,
                 error_code=100, error_msg="Unknown error occurred"):
        self.incoming_message = incoming_message
        self.error_code = error_code
        self.error_msg = error_msg
        self.logger_enabled = logger_enabled

    def _build_default_response(self):
        inc_msg = parse_message(self.incoming_message)

        m = Message("ACK")
        m.MSH.MSH_9 = "ACK^ACK"
        m.MSA.MSA_1 = "AR"
        m.MSA.MSA_2 = inc_msg.MSH.MSH_10
        m.ERR.ERR_1 = "%s" % self.error_code
        m.ERR.ERR_2 = "%s" % self.error_msg

        return m.to_mllp()

    def is_enabled(self):
        return True

    def reply(self):
        return self._build_default_response()


class UnsupportedMessageTypeHandler(GenericErrorHandler):
    
    def __init__(self, incoming_message, logger_enabled=True):
        super(UnsupportedMessageTypeHandler, self).__init__(incoming_message, logger_enabled, 101,
                                                            "Unsupported message handler")


class InvalidMessageHandler(GenericErrorHandler):
    
    def __init__(self, incoming_message, logger_enabled=True):
        super(InvalidMessageHandler, self).__init__(incoming_message, logger_enabled, 102,
                                                    "Incoming message is not an HL7 valid message")

    def _build_default_response(self):
        m = Message("ACK")
        m.MSH.MSH_9 = "ACK^ACK"
        m.MSA.MSA_1 = "AR"
        m.MSA.MSA_2 = ""
        m.ERR.ERR_1 = "%s" % self.error_code
        m.ERR.ERR_2 = "%s" % self.error_msg

        return m.to_mllp()
