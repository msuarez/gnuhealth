#!/usr/bin/env python
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
import logging.config
import importlib
import os
import argparse

from hl7apy.mllp import MLLPServer

from trytond.transaction import Transaction
from hl7_handlers import HL7ErrorHandler
from connection.pool_manager import PoolManager

logger = logging.getLogger('mllp_server')


def str_to_class(module_name, class_name):
    try:
        logger.debug("Try to import class %s from module %s" % (class_name, module_name))
        module_ = importlib.import_module("trytond.modules.%s" % module_name)
        try:
            return getattr(module_, class_name)
        except AttributeError:
            logger.error('Class does not exist')
    except ImportError:
        logger.error('Module does not exist')
    return None


def discover_handlers(database_name, logger_enabled):
    pool_manager = PoolManager(database_name)
    transaction = Transaction()
    logger.debug("Starting db transaction for domain:%s" % database_name)
    transaction.start(database_name, 0)
    logger.debug("Connecting to table")
    transaction_handler_table = pool_manager.get_table("hl7.transaction_handler")
    logger.debug("Preparing query for table -> %s" % transaction_handler_table)
    query = transaction_handler_table.select(*[transaction_handler_table.message_handler_module_name,
                                             transaction_handler_table.message_handler_class_name,
                                             transaction_handler_table.message_type])
    cursor = transaction.cursor
    logger.debug("Executing query:%s" % query)
    cursor.execute(*query)

    results = cursor.fetchall()  # return all results
    logger.debug("Query results: %s" % results)

    transaction.stop()

    handlers = {
        "ERR": (HL7ErrorHandler, pool_manager)
    }
    if results:
        for r in results:
            handler_module_name = r[0]
            handler_class_name = r[1]
            message_type = r[2]
            handlers[message_type] = (str_to_class(handler_module_name, handler_class_name), pool_manager,
                                      logger_enabled)

    logger.debug("handlers found: " + str(handlers))
    return handlers


class HealthMLLPServer(MLLPServer):
    
    def __init__(self, host, port, handlers):
        try:
            port = int(port)
            if host == '*':
                host = '0.0.0.0'
        except:
            raise Exception('Wrong port value: %s' % port)

        logger.info("TCP Socket Server binding on %s: %s" % (host, port))
        MLLPServer.__init__(self, host, port, handlers)
        
    def start(self):
        self.serve_forever()
        logger.info("MLLP server started")
        
    def stop(self):
        self.shutdown()
        logger.info("MLLP server stopped")


def parse_commandline():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config", dest="configfile", metavar='FILE',
                        default=os.environ.get('TRYTOND_CONFIG'), help="specify the tryton config file")
    parser.add_argument("-H", "--host", dest="hostname",
                        default='127.0.0.1', help="listening host")
    parser.add_argument("-p", "--port", dest="port", type=int,
                        default=2575, help="listening port")
    parser.add_argument("-d", "--database_name", dest="database_name",
                        help="the GNUHealth database name")
    parser.add_argument("--logconf", dest="logconf", metavar='FILE',
                        help="logging configuration file (ConfigParser format)")
    parser.add_argument("-l", "--enable_message_logger", dest="logger_enabled", action="store_true",
                        help="If present the HL7 transactions will be logged in the DB")

    return parser.parse_args()


if __name__ == '__main__':
    opts = parse_commandline()

    if opts.logconf:
        logging.config.fileConfig(opts.logconf)
        logging.getLogger('server').info('using %s as mllp logging configuration file', opts.logconf)
    else:
        logformat = '[%(asctime)s] %(levelname)s:%(name)s:%(message)s'
        datefmt = '%a %b %d %H:%M:%S %Y'
        logging.basicConfig(level=logging.INFO, format=logformat, datefmt=datefmt)

    try:
        from trytond.config import config
    except ImportError:
        pass
    else:
        config.update_etc(opts.configfile)  # we need to update the Pool configuration using the tryton config file

    hdlrs = discover_handlers(opts.database_name, opts.logger_enabled)

    server = HealthMLLPServer(opts.hostname, opts.port, hdlrs)
    logger.info("Starting MLLP Server")
    server.start()
