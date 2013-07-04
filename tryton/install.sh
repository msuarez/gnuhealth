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

# TEMPORARY - STAGING AREA
TMP_DIR="/tmp/gnuhealth_installer/"

GHEALTH_INST_DIR=$PWD

# THE GNUHEALTH VARIABLES
GNUHEALTH_BASEDIR="$HOME"
GNUHEALTH_VERSION=`cat version`

# THE TRYTON SERVER VARIABLES 
TRYTOND_BASEDIR="$HOME"
TRYTOND_MAJOR_NUMBER="2"
TRYTOND_MINOR_NUMBER="8"
TRYTOND_REVISION_NUMBER="1"

TRYTOND_VERSION="$TRYTOND_MAJOR_NUMBER.$TRYTOND_MINOR_NUMBER.$TRYTOND_REVISION_NUMBER"

# PIP arguments

PIP_ARGS="install --user"

# GNU Health / Tryton dependencies
PIP_LXML="lxml"
PIP_RELATORIO="relatorio"
PIP_DATEUTIL="python-dateutil"
PIP_PSYCOPG2="psycopg2"
PIP_PYTZ="pytz"
PIP_LDAP="python-ldap"
PIP_VOBJECT="vobject"
PIP_PYWEBDAV="pywebdav"
PIP_QRCODE="qrcode"
PIP_PIL="PIL"
PIP_CALDAV="caldav"

PIP_INSTALL="$PIP_LXML $PIP_RELATORIO $PIP_DATEUTIL $PIP_PSYCOPG2 $PIP_PYTZ $PIP_LDAP $PIP_VOBJECT $PIP_PYWEBDAV $PIP_QRCODE $PIP_PIL $PIP_CALDAV"

echo "Installing dependencies with PIP..."

for DEP_PIP_INSTALL in $PIP_INSTALL
    do
        $PIP_CMD $PIP_ARGS $DEP_PIP_INSTALL
    done



# GET THE REVISION NUMBER FOR EACH MODULE
ACCOUNT_REV="1"
ACCOUNT_INVOICE_REV="1"
ACCOUNT_PRODUCT_REV="0"
CALENDAR_REV="0"
COMPANY_REV="0"
COUNTRY_REV="0"
CURRENCY_REV="0"
PARTY_REV="0"
PRODUCT_REV="0"
STOCK_REV="1"
STOCK_LOT_REV="0"


TRYTON_BASE_URL="http://downloads.tryton.org/$TRYTOND_MAJOR_NUMBER.$TRYTOND_MINOR_NUMBER"

MOD_PREFIX="$TRYTON_BASE_URL/trytond_"

TRYTOND_FILE="trytond-$TRYTOND_VERSION.tar.gz"

# DOWNLOAD TRYTON MODULES NEEDED IN GNU HEALTH

ACCOUNT="${MOD_PREFIX}account-$TRYTOND_MAJOR_NUMBER.$TRYTOND_MINOR_NUMBER.$ACCOUNT_REV.tar.gz"
ACCOUNT_INVOICE="${MOD_PREFIX}account_invoice-$TRYTOND_MAJOR_NUMBER.$TRYTOND_MINOR_NUMBER.$ACCOUNT_INVOICE_REV.tar.gz"
ACCOUNT_PRODUCT="${MOD_PREFIX}account_product-$TRYTOND_MAJOR_NUMBER.$TRYTOND_MINOR_NUMBER.$ACCOUNT_PRODUCT_REV.tar.gz"
CALENDAR="${MOD_PREFIX}calendar-$TRYTOND_MAJOR_NUMBER.$TRYTOND_MINOR_NUMBER.$CALENDAR_REV.tar.gz"
COMPANY="${MOD_PREFIX}company-$TRYTOND_MAJOR_NUMBER.$TRYTOND_MINOR_NUMBER.$COMPANY_REV.tar.gz"
COUNTRY="${MOD_PREFIX}country-$TRYTOND_MAJOR_NUMBER.$TRYTOND_MINOR_NUMBER.$COUNTRY_REV.tar.gz"
CURRENCY="${MOD_PREFIX}currency-$TRYTOND_MAJOR_NUMBER.$TRYTOND_MINOR_NUMBER.$CURRENCY_REV.tar.gz"
PARTY="${MOD_PREFIX}party-$TRYTOND_MAJOR_NUMBER.$TRYTOND_MINOR_NUMBER.$PARTY_REV.tar.gz"
PRODUCT="${MOD_PREFIX}product-$TRYTOND_MAJOR_NUMBER.$TRYTOND_MINOR_NUMBER.$PRODUCT_REV.tar.gz"
STOCK="${MOD_PREFIX}stock-$TRYTOND_MAJOR_NUMBER.$TRYTOND_MINOR_NUMBER.$STOCK_REV.tar.gz"
STOCK_LOT="${MOD_PREFIX}stock_lot-$TRYTOND_MAJOR_NUMBER.$TRYTOND_MINOR_NUMBER.$STOCK_LOT_REV.tar.gz"

MODULES="$ACCOUNT $ACCOUNT_INVOICE $ACCOUNT_PRODUCT $CALENDAR $COMPANY $COUNTRY $CURRENCY $PARTY $PRODUCT $STOCK $STOCK_LOT"

# CREATE TEMPORARY DIR
echo "INFO : Creating temporary directory"
if [ -e $TMP_DIR ] ; then
    echo "ERROR : Directory $TMP_DIR exists. You need to delete it"
    exit 1
else
    mkdir $TMP_DIR
fi

# CHANGE TO TEMPORARY DIRECTORY
echo "INFO : Changing to temporary directory"
cd $TMP_DIR

# Download the Tryton Server

echo "INFO : Downloading the Tryton Server ..."

wget "$TRYTON_BASE_URL/$TRYTOND_FILE"

# DOWNLOAD THE TRYTON MODULES

echo "INFO : Downloading the Tryton Modules ..."

for TMODULE in $MODULES
    do
        wget $TMODULE
    done

# CREATE THE DESTINATION DIRECTORIES

TRYTOND_DIR="${HOME}/tryton/server"
MODULES_DIR="${TRYTOND_DIR}/modules"

mkdir -p "$MODULES_DIR"

# Uncompress the Tryton Server

echo "INFO: ** UNCOMPRESSING THE TRYTON SERVER **"
cd $TRYTOND_DIR
tar -xzf $TMP_DIR/$TRYTOND_FILE

echo "INFO: ** UNCOMPRESSING THE TRYTON MODULES **"

cd  $MODULES_DIR

# EXTRACT TRYTON MODULES NEEDED IN GNU HEALTH

echo "INFO: ** EXTRACT TRYTON MODULES NEEDED IN GNU HEALTH **"

cd $MODULES_DIR

for MODULE in `ls $TMP_DIR/trytond_*`
    do
        tar -xzf $MODULE
    done


echo "INFO : ** LINKING THE TRYTON MODULES **"
    
MODULES="account account_invoice account_product calendar company country currency party product stock stock_lot"

TRYTOND_MOD_DIR="${TRYTOND_DIR}/trytond-$TRYTOND_VERSION/trytond/modules"

cd $TRYTOND_MOD_DIR


for LNMOD in $MODULES
    do
        ln -si $MODULES_DIR/trytond_${LNMOD}-* $LNMOD
    done

echo "INFO : ** COPYING GNU HEALTH MODULES TO THE TRYTON MODULES DIRECTORY **"

cp -a ${GHEALTH_INST_DIR}/health* $MODULES_DIR

ln -si $MODULES_DIR/health* .

echo "DONE !"

