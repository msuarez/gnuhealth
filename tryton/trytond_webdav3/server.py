# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.
"""
%prog [options]
"""
import logging
import logging.config
import logging.handlers
import sys
import os
import signal
import time

from trytond.config import config, parse_listen
from trytond.pool import Pool


class TrytonWebdavServer(object):

    def __init__(self, options):

        config.update_etc(options.configfile)

        if options.logconf:
            logging.config.fileConfig(options.logconf)
            logging.getLogger('server').info('using %s as logging '
                'configuration file', options.logconf)
        else:
            logformat = ('%(process)s %(thread)s [%(asctime)s] '
                '%(levelname)s %(name)s %(message)s')
            if options.verbose:
                if options.dev:
                    level = logging.DEBUG
                else:
                    level = logging.INFO
            else:
                level = logging.ERROR
            logging.basicConfig(level=level, format=logformat)

        self.logger = logging.getLogger(__name__)

        if options.configfile:
            self.logger.info('using %s as configuration file',
                options.configfile)
        else:
            self.logger.info('using default configuration')
        self.logger.info('initialising distributed objects services')
        self.webdavd = []
        self.options = options

        if time.tzname[0] != 'UTC':
            self.logger.error('timezone is not set to UTC')

    def run(self):
        "Run the server and never return"
        signal.signal(signal.SIGINT, lambda *a: self.stop())
        signal.signal(signal.SIGTERM, lambda *a: self.stop())
        if hasattr(signal, 'SIGQUIT'):
            signal.signal(signal.SIGQUIT, lambda *a: self.stop())
        if hasattr(signal, 'SIGUSR1'):
            signal.signal(signal.SIGUSR1, lambda *a: self.restart())

        if self.options.pidfile:
            with open(self.options.pidfile, 'w') as fd_pid:
                fd_pid.write("%d" % (os.getpid()))

        for db_name in self.options.database_names:
            Pool(db_name).init()

        self.start_servers()

        while True:
            if self.options.dev:
                time.sleep(1)
            else:
                time.sleep(60)

    def start_servers(self):
        ssl = config.get('ssl', 'privatekey')

        if config.get('webdav', 'listen'):
            from .protocol import WebDAVServerThread
            for hostname, port in parse_listen(
                    config.get('webdav', 'listen')):
                self.webdavd.append(WebDAVServerThread(hostname, port, ssl))
                self.logger.info("starting WebDAV%s protocol on %s:%d",
                    ssl and ' SSL' or '', hostname or '*', port)

        for server in self.webdavd:
            server.start()

    def stop(self, exit=True):
        for server in self.webdavd:
            server.stop()
            server.join()
        if exit:
            if self.options.pidfile:
                os.unlink(self.options.pidfile)
            logging.getLogger('server').info('stopped')
            logging.shutdown()
            sys.exit(0)

    def restart(self):
        self.stop(False)
        args = ([sys.executable] + ['-W%s' % o for o in sys.warnoptions]
            + sys.argv)
        if sys.platform == "win32":
            args = ['"%s"' % arg for arg in args]
        os.execv(sys.executable, args)
