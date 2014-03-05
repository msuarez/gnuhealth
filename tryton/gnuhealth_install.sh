#!/bin/bash

# GNU Health installer
# Version for 2.4 series

##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2008-2014  Luis Falcon <falcon@gnu.org>
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

# Colors constants
NONE="$(tput sgr0)"
RED="$(tput setaf 1)"
GREEN="$(tput setaf 2)"
YELLOW="\n$(tput setaf 3)"
BLUE="\n$(tput setaf 4)"

INSTDIR="$PWD"

message () {
    # $1 : Message
    # $2 : Color
    # return : Message colorized
    local NOW="[$(date +%H:%M:%S)]"

    echo -e "${2}${NOW}${1}${NONE}"
}


check_requirements() {
    # WGET command
    message "[INFO] CHECKING REQUIREMENTS" ${BLUE}
    message "Looking for wget...." ${BLUE}

    if ! type wget 2>/dev/null ; then
        message "[ERROR] wget command not found. Please install it or check your PATH variable" ${RED}
        exit 1
    fi

    # PYTHON version [2.6.x < 3.x]
    message "Looking for the Python Interpreter command..." ${BLUE}

    if ! type python 2>/dev/null ; then
        message "[ERROR] Python interpreter not found. Please install it or check your PATH variable." ${RED}
        exit 1
    fi

    local PVERSION=`python -V 2>&1 | grep 2.[6-9].[0-9]`

    if test "${PVERSION}" ; then
        message "[INFO] Found ${PVERSION}" ${BLUE}
    else
        python -V
        message "[ERROR] Found an Incompatible Python version." ${RED}
        exit 1
    fi

    # PIP COMMAND
    message "-> Looking for PIP command..." ${BLUE}

    # Alternative pip names on Debian/ArchLinux/RedHat based distros:
    local PIP_NAMES="pip pip2 pip-python"
    PIP_NAME=""
    for NAME in ${PIP_NAMES}; do
        if [[ `which ${NAME} 2>/dev/null` ]]; then
            PIP_NAME=${NAME}
            break
        fi
    done

    if [[ ! ${PIP_NAME} ]]; then
        message "[ERROR] PIP command not found. Please install it or check your PATH variable." ${RED}
        exit 1
    fi
    message "[INFO] OK." ${GREEN}
}


install_python_dependencies() {
    local PIP_CMD=$(which $PIP_NAME)
    local PIP_VERSION="$(${PIP_CMD} --version | awk '{print $2}')"

    # TODO: Change for virtualenv support.
    local PIP_ARGS="install --user"

    # Python packages
    local PIP_LXML="lxml==3.2.3"
    local PIP_RELATORIO="relatorio==0.6.0"
    local PIP_DATEUTIL="python-dateutil==2.1"
    local PIP_PSYCOPG2="psycopg2==2.5.1"
    local PIP_PYTZ="pytz==2013.7"
    local PIP_LDAP="python-ldap==2.4.13"
    local PIP_VOBJECT="vobject==0.6.6"
    local PIP_PYWEBDAV="pywebdav==0.9.8"
    local PIP_QRCODE="qrcode==4.0.4"
    local PIP_SIX="six==1.4.1"
    local PIP_PILLOW="PILLOW==2.3.0"
    local PIP_CALDAV="caldav==0.1.12"
    local PIP_POLIB="polib==1.0.3"
    local PIP_SQL="python-sql==0.2"
    
    local PIP_PKGS="$PIP_PYTZ $PIP_LXML $PIP_RELATORIO $PIP_DATEUTIL $PIP_PSYCOPG2 $PIP_LDAP $PIP_VOBJECT $PIP_PYWEBDAV $PIP_QRCODE $PIP_SIX $PIP_PILLOW $PIP_CALDAV $PIP_POLIB $PIP_SQL"

    message "[INFO] Installing python dependencies with pip-${PIP_VERSION} ..." ${YELLOW}

    
    for PKG in ${PIP_PKGS}; do
        message " >> ${PKG}" ${BLUE}
        ${PIP_CMD} ${PIP_ARGS} ${PKG} || exit 1
        message " >> OK" ${GREEN}
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
        mkdir ${TMP_DIR} || exit 1
    fi
    message "[INFO] OK." ${GREEN}

    #
    # Create the destination directories.
    #
    message "[INFO] Creating destination directories..." ${YELLOW}

    BASEDIR="$HOME/gnuhealth"
    TRYTON_BASEDIR="${BASEDIR}/tryton"
    TRYTOND_DIR="${TRYTON_BASEDIR}/server"
    MODULES_DIR="${TRYTOND_DIR}/modules"
    CUSTOM_MODS_DIR="${MODULES_DIR}/custom"
    LOG_DIR="${BASEDIR}/logs"
    ATTACH_DIR="${HOME}/attach"
    
    if [ -e ${BASEDIR} ] ; then
        message "[ERROR] Directory ${BASEDIR} exists. You need to delete it." ${RED}
        exit 1
    else
        mkdir -p ${MODULES_DIR} ${LOG_DIR} ${ATTACH_DIR} ${CUSTOM_MODS_DIR}||  exit 1
    fi
    message "[INFO] OK." ${GREEN}
}


bash_profile () {

    message "[INFO] Creating or Updating the BASH profile for GNU Health" ${BLUE}

    cd $INSTDIR
    
    PROFILE="$HOME/.gnuhealthrc"

    if [ -e ${PROFILE} ] ; then
        # Make a backup copy of the GNU Health BASH profile if it exists
        message "[INFO] GNU Health BASH Profile exists. Making backup to ${PROFILE}.bak ." ${YELLOW}
        cp ${PROFILE} ${PROFILE}.bak || exit 1
    fi

    cp gnuhealthrc ${PROFILE} ||  exit 1

    # Load .gnuhealthrc from .bash_profile . If .bash_profile does not exist, create it.
    if [ -e $HOME/.bash_profile ] ; then
        grep --silent "source ${PROFILE}" $HOME/.bash_profile || echo "[[ -f ${PROFILE} ]] && source ${PROFILE}" >> $HOME/.bash_profile
    else
        echo "[[ -f ${PROFILE} ]] && source ${PROFILE}" >> $HOME/.bash_profile
    fi
   
}

#
# (0) Start.
#
GNUHEALTH_INST_DIR=$PWD
GNUHEALTH_VERSION=`cat version`

message "[INFO] Starting GNU Health ${GNUHEALTH_VERSION} installation..." ${BLUE}

#
# (1) Check requirements.
#
check_requirements

#
# (2) Install directories.
#
install_directories


#
# (3) Download settings.
#
TRYTON_VERSION="3.0"
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
# (4) Install Python dependencies.
#
install_python_dependencies


#
# (5) Download Tryton packages.
#
message "[INFO] Changing to temporary directory." ${BLUE}
cd ${TMP_DIR} || exit 1

message "[INFO] Downloading the Tryton server..." ${YELLOW}
wget ${TRYTOND_URL} || exit 1
message "[INFO] OK." ${GREEN}

message "[INFO] Downloading Tryton modules..." ${YELLOW}
for URL in ${TRYTON_MODULES_URL}; do
    wget ${URL} || exit 1
done
message "[INFO] OK." ${GREEN}


#
# (6) Uncompress the Tryton packages.
#
message "[INFO] Uncompressing the Tryton server..." ${YELLOW}
cd ${TRYTOND_DIR}
tar -xzf ${TMP_DIR}/${TRYTOND_FILE} || exit 1
message "[INFO] OK." ${GREEN}

message "[INFO] Uncompressing the Tryton modules..." ${YELLOW}
cd ${MODULES_DIR} || exit 1
for MODULE in `ls ${TMP_DIR}/trytond_*`; do
    tar -xzf ${MODULE} || exit 1
done
message "[INFO] OK." ${GREEN}


#
# (7) Links to modules.
#
message "[INFO] Changing directory to <../trytond/modules>." ${BLUE}
TRYTOND_FOLDER=$(basename ${TRYTOND_FILE} .tar.gz)
cd "${TRYTOND_DIR}/${TRYTOND_FOLDER}/trytond/modules" || exit 1

message "[INFO] Linking the Tryton modules..." ${YELLOW}
for LNMOD in ${TRYTON_MODULES}; do
    ln -si ${MODULES_DIR}/trytond_${LNMOD}-* ${LNMOD} || exit 1
done
message "[INFO] OK." ${GREEN}

message "[INFO] Copying GNU Health modules to the Tryton modules directory..." ${YELLOW}
cp -a ${GNUHEALTH_INST_DIR}/health* ${MODULES_DIR} || exit 1

EXTRA_FILES="COPYING README version"
for FILE in ${EXTRA_FILES}; do
    cp -a ${GNUHEALTH_INST_DIR}/${FILE} ${BASEDIR} || exit 1
done

ln -si ${MODULES_DIR}/health* .
message "[INFO] OK." ${GREEN}


#
# (8) BASH Profile
#
bash_profile


#
# Clean.
#
message "[INFO] Cleaning Up..." ${YELLOW}
rm -rf ${TMP_DIR} || exit 1

message "[INFO] OK." ${GREEN}


message "[INFO] Installed successfully in ${BASEDIR}." ${BLUE}
