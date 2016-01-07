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
import subprocess
import os
from signal import SIGTERM

logger = logging.getLogger(__name__)

MLLP_SERVER_MODULE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "mllp_server.py")


class MLLPServerLauncher():
    def __init__(self, host, port, database_name, pid_dir, message_logger_enabled):
        self.host = host
        self.port = port
        self.database_name = database_name
        self.pid_dir = pid_dir
        self.MLLP_SERVER_PID_FILENAME = os.path.join(os.path.dirname(pid_dir), "mllp_server.pid")
        self.message_logger_enabled = str(message_logger_enabled)
        
    def start_mllp_server(self):
        if not os.path.isfile(self.MLLP_SERVER_PID_FILENAME):
            args = ["python", MLLP_SERVER_MODULE, "-H", self.host, "-p",
                    str(self.port), "-d", self.database_name]
            if self.message_logger_enabled:
                args.append("-l")

            pipe = subprocess.Popen(args)
            logger.info("Created MLLP server process")
            logger.info("Process PID: %s Database: %s message logger: %s" % (pipe.pid, self.database_name,
                                                                             str(self.message_logger_enabled)))
            
            # create pid file
            out_file = open(self.MLLP_SERVER_PID_FILENAME, "w")
            out_file.write("%s" % pipe.pid)
            out_file.flush()
            out_file.close()
            logger.info("PID file: %s " % self.MLLP_SERVER_PID_FILENAME)
        else:
            logger.warn("MLLP server not launched. is it already running?")
        
    def stop_mllp_server(self):
        if os.path.isfile(self.MLLP_SERVER_PID_FILENAME):
            try:
                # read the pid file
                in_file = open(self.MLLP_SERVER_PID_FILENAME, "r")
                pid = in_file.read()
                in_file.close()
                logger.info("Killing mllp process with pid: %s" % pid)
                os.kill(int(pid), SIGTERM)
                logger.debug("removing file:%s" % self.MLLP_SERVER_PID_FILENAME)
                os.remove(self.MLLP_SERVER_PID_FILENAME)
            except Exception, ex:
                logger.error("Cannot find the pid process!:%s" % str(ex))
                os.remove(self.MLLP_SERVER_PID_FILENAME)
        else:
            logger.warn("No %s file found. Is the server already stopped?" % self.MLLP_SERVER_PID_FILENAME)
