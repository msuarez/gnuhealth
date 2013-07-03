#!/bin/bash

# GNU Health installer

##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2008-2013  Luis Falcon <lfalcon@gnusolidario.org>
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

# Main variables declaration

# PIP command 
# If the OS is Arch Linux, use pip2
# otherwise, use pip

if [ -e /etc/arch-release ]; then
    PIP_CMD="/usr/bin/pip2"
else
    PIP_CMD="/usr/bin/pip"
fi

# PIP arguments

PIP_ARGS="install --user"

# GNU Health / Tryton dependencies
PIP_LXML="lxml"
PIP_RELATORIO="relatorio"
PIP_DATEUTIL="python-dateutil"
PIP_PSYCOPG2="psycopg2"
PIP_PYTZ="polib"
PIP_LDAP="python-ldap"
PIP_VOBJECT="vobject"
PIP_PYWEBDAV="pywebdav"
PIP_QRCODE="qrcode"
PIP_PIL="PIL"

PIP_INSTALL="$PIP_LXML $PIP_RELATORIO $PIP_DATEUTIL $PIP_PYTZ $PIP_LDAP $PIP_VOBJECT $PIP_PYWEBDAV $PIP_QRCODE $PIP_PIL"

echo "Installing dependencies with PIP..."

for DEP_PIP_INSTALL in $PIP_INSTALL
    do
    $PIP_CMD $PIP_ARGS $DEP_PIP_INSTALL
    done
