#!/bin/bash

# GNU Health installer

##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2008-2013  Luis Falcon <lfalcon@gnusolidario.org>
#                             Bruno M. Villasanti <bvillasanti@thymbra.com>
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

#
# Main functions/variables declaration
#

# Colors
NONE="$(tput sgr0)"
RED="$(tput setaf 1)"
GREEN="$(tput setaf 2)"
YELLOW="\n$(tput setaf 3)"
BLUE="\n$(tput setaf 4)"

message () {
    # $1 : Message
    # $2 : Color
    # return : Message colorized
    local NOW="[$(date +%H:%M:%S)]"

    echo -e "${2}${NOW}${1}${NONE}"
}

check_requirements()
{
	# WGET command
	message "[INFO] CHECKING REQUIREMENTS" ${BLUE}
	message "Looking for wget...." ${BLUE}

	if ! type wget 2>/dev/null ; then
		message "[ERROR] wget command not found. Please install it or check your PATH variable" ${RED}
		exit 1
	fi

    # PYTHON version [2.7.x < 3.x]

	message "Looking for the Python Interpreter command...." ${BLUE}
    
	if ! type python 2>/dev/null ; then
		message "[ERROR] Python interpreter not found. Please install it or check your PATH variable" ${RED}
		exit 1
	fi
    
    local PVERSION=`python -V 2>&1 | grep 2.[789].[0-9]`
    
    if test "${PVERSION}" ; then
        message "[INFO] Found ${PVERSION}" ${BLUE}
    else
        python -V
        message "[ERROR] Found an Incompatible Python version" ${RED}
        exit 1
    
    fi    
    
    # PIP COMMAND
	message "-> Looking for PIP command...." ${BLUE}

    if [ -e /etc/arch-release ]; then
        PIP_NAME="pip2"
    elif [ -e /etc/fedora-release ]; then
        PIP_NAME="pip-python"
    else
        PIP_NAME="pip"
    fi

	if ! type $PIP_NAME 2>/dev/null ; then
		message "[ERROR] PIP command not found. Please install it or check your PATH variable" ${RED}
		exit 1
	fi
    message "[INFO] OK." ${GREEN}

exit 2

}


install_python_dependencies() {
    local PIP_CMD=$(which $PIP_NAME)

    # TODO: Change for virtualenv support.
    local PIP_ARGS="install --user"

    # Python packages
    local PIP_LXML="lxml"
    local PIP_RELATORIO="relatorio"
    local PIP_DATEUTIL="python-dateutil"
    local PIP_PSYCOPG2="psycopg2"
    local PIP_PYTZ="pytz"
    local PIP_LDAP="python-ldap"
    local PIP_VOBJECT="vobject"
    local PIP_PYWEBDAV="pywebdav"
    local PIP_QRCODE="qrcode"
    local PIP_PIL="PIL"
    local PIP_CALDAV="caldav"
    local PIP_POLIB="polib"

    local PIP_PKGS="$PIP_LXML $PIP_RELATORIO $PIP_DATEUTIL $PIP_PSYCOPG2 $PIP_PYTZ $PIP_LDAP $PIP_VOBJECT $PIP_PYWEBDAV $PIP_QRCODE $PIP_PIL $PIP_CALDAV $PIP_POLIB"

    message "[INFO] Installing python dependencies with pip..." ${YELLOW}
    for PKG in ${PIP_PKGS}; do
        ${PIP_CMD} ${PIP_ARGS} ${PKG}
    done
}


install_directories() {
    #
    # Temporary/staging area.
    #
    message "[INFO] Creating temporary directory..." ${YELLOW}

    TMP_DIR="/tmp/gnuhealth_installer"

    if [ -e ${TMP_DIR} ] ; then
        message "[ERROR] Directory ${TMP_DIR} exists. You need to delete it." ${RED}
        exit 1
    else
        mkdir ${TMP_DIR}
    fi
    message "[INFO] OK." ${GREEN}

    #
    # Create the destination directories.
    #
    message "[INFO] Creating destination directories..." ${YELLOW}

    BASEDIR="$HOME/tryton"
    TRYTOND_DIR="${BASEDIR}/server"
    MODULES_DIR="${TRYTOND_DIR}/modules"

    if [ -e ${BASEDIR} ] ; then
        message "[ERROR] Directory ${BASEDIR} exists. You need to delete it." ${RED}
        exit 1
    else
        mkdir -p ${MODULES_DIR}
    fi
    message "[INFO] OK." ${GREEN}
}


#
# (0) Start.
#
GNUHEALTH_INST_DIR=$PWD
GNUHEALTH_VERSION=`cat version`

message "[INFO] Starting GNU Health ${GNUHEALTH_VERSION} installation..." ${BLUE}

# 
check_requirements

#
# (1) Install directories.
#
install_directories


#
# (2) Download settings.
#
TRYTON_VERSION="2.8"
TRYTON_BASE_URL="http://downloads.tryton.org"

get_url() {
    # $1 : Module name
    # return : URL to download

    echo ${TRYTON_BASE_URL}/${TRYTON_VERSION}/$(wget --quiet -O- ${TRYTON_BASE_URL}/${TRYTON_VERSION} | egrep -o "${1}-${TRYTON_VERSION}.[0-9\.]+.tar.gz" | sort -V | tail -1)
}

#
# Get the lastest revision number for each Tryton module.
#
message "[INFO] Getting list of lastest Tryton packages..." ${YELLOW}

TRYTOND_URL=$(get_url trytond)
TRYTOND_FILE=$(basename ${TRYTOND_URL})

TRYTON_MODULES="account account_invoice account_product calendar company country currency party product stock stock_lot"

TRYTON_MODULES_FILE=""
TRYTON_MODULES_URL=""
for MODULE in ${TRYTON_MODULES}
do
    AUX=$(get_url trytond_${MODULE})
    TRYTON_MODULES_URL="${TRYTON_MODULES_URL} ${AUX}"
    TRYTON_MODULES_FILE="${TRYTON_MODULES_FILE} $(basename ${AUX})"
done

message "[INFO] OK." ${GREEN}


#
# (3) Install Python dependencies.
#
install_python_dependencies


#
# (4) Download Tryton packages.
#
message "[INFO] Changing to temporary directory." ${BLUE}
cd ${TMP_DIR}

message "[INFO] Downloading the Tryton server..." ${YELLOW}
wget ${TRYTOND_URL}
message "[INFO] OK." ${GREEN}

message "[INFO] Downloading Tryton modules..." ${YELLOW}
for URL in ${TRYTON_MODULES_URL}; do
    wget ${URL}
done
message "[INFO] OK." ${GREEN}


#
# (5) Uncompress the Tryton packages.
#
message "[INFO] Uncompressing the Tryton server..." ${YELLOW}
cd ${TRYTOND_DIR}
tar -xzf ${TMP_DIR}/${TRYTOND_FILE}
message "[INFO] OK." ${GREEN}

message "[INFO] Uncompressing the Tryton modules..." ${YELLOW}
cd ${MODULES_DIR}
for MODULE in `ls ${TMP_DIR}/trytond_*`; do
    tar -xzf ${MODULE}
done
message "[INFO] OK." ${GREEN}


#
# (6) Links to modules.
#
message "[INFO] Changing directory to <../trytond/modules>." ${BLUE}
TRYTOND_FOLDER=$(basename ${TRYTOND_FILE} .tar.gz)
cd "${TRYTOND_DIR}/${TRYTOND_FOLDER}/trytond/modules"

message "[INFO] Linking the Tryton modules..." ${YELLOW}
for LNMOD in ${TRYTON_MODULES}; do
    ln -si ${MODULES_DIR}/trytond_${LNMOD}-* ${LNMOD}
done
message "[INFO] OK." ${GREEN}

message "[INFO] Copying GNU Health modules to the Tryton modules directory..." ${YELLOW}
cp -a ${GNUHEALTH_INST_DIR}/health* ${MODULES_DIR}

ln -si ${MODULES_DIR}/health* .
message "[INFO] OK." ${GREEN}


#
# (7) Clean.
#
message "[INFO] Cleaning..." ${YELLOW}
rm -rf ${TMP_DIR}

message "[INFO] OK." ${GREEN}


message "[INFO] Installed successfully in ${BASEDIR}." ${BLUE}
