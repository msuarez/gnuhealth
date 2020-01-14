# -*- coding: utf-8 -*-
##############################################################################
#
#    MyGNUHealth : Mobile and Desktop PHR node for GNU Health
#
#           MyGNUHealth is part of the GNU Health project
#
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2008-2019 Luis Falcon <falcon@gnuhealth.org>
#    Copyright (C) 2011-2019 GNU Solidario <health@gnusolidario.org>
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

import sys
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import QObject, QUrl, Slot
from PySide2.QtQml import QQmlApplicationEngine

import requests

class FedLogin(QObject):
    @Slot(str, str)
    def login(self, acct, passwd):
        self.test_connection(acct, passwd)

    def test_connection(self,acct, passwd):
        """ Make the connection test to Thalamus Server
            from the GNU Health HMIS using the institution
            associated admin and the related credentials
        """
        conn = ''
        host, port, user, password, ssl_conn, verify_ssl = \
            'localhost', 8443,  \
            acct, passwd, True, \
            False

        if (ssl_conn):
            protocol = 'https://'
        else:
            protocol = 'http://'

        if (not user or not password):
            print("Please provide login credentials")


        url = protocol + host + ':' + str(port) + '/people/' + user

        try:
            conn = requests.get(url,
                auth=(user, password), verify=verify_ssl)

        except:
            print("ERROR authenticating to Server")

        if conn:
            print("***** Connection to Thalamus Server OK !******")

        else:
            print("##### Wrong credentials ####")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()

    fed_login = FedLogin()

    url = QUrl("main.qml")
    engine.load(url)

    #Expose fedLogin var to QML
    engine.rootContext().setContextProperty("fedLogin", fed_login)

    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec_())
