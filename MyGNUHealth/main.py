#!/usr/bin/env python3
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
#    Copyright (C) 2008-2020 Luis Falcon <falcon@gnuhealth.org>
#    Copyright (C) 2011-2020 GNU Solidario <health@gnusolidario.org>
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
from PySide2.QtCore import QObject, QUrl, Signal, Slot
from PySide2.QtQml import QQmlApplicationEngine, qmlRegisterType
from fedlogin import FederationLogin

VERSION_MAJOR = 0
VERSION_MINOR = 1


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Register FedLogin to use it QML
    qmlRegisterType(FederationLogin, "FedLogin", VERSION_MAJOR, VERSION_MINOR,
                    "FedLogin")

    engine = QQmlApplicationEngine()

    url = QUrl("qml/main.qml")
    engine.load(url)

    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec_())
