#!/bin/bash
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2008-2018 Luis Falcon <falcon@gnu.org>
#    Copyright (C) 2011-2018 GNU Solidario <info@gnusolidario.org>
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

message()
{
    local UTC="$(date -u +'%Y-%m-%d %H:%M:%S')"
    
    case $1 in
      ERROR ) echo -e "\e[00;31m${UTC} [ERROR] $2\e[00m";;
      WARNING ) echo -e "\e[0;33m${UTC} [WARNING] $2\e[m" ;;
      INFO ) echo -e "\e[0;36m${UTC} [INFO] $2\e[m" ;;
    esac
}

bailout() 
{
    message "ERROR" "Bailing out !"
    exit 1
}

source $HOME/.gnuhealthrc
message "INFO" "Starting GNU Health Server version ${GNUHEALTH_VERSION} ..."
cd ${GNUHEALTH_DIR}/tryton/server/${TRYTOND}/bin
python3 ./trytond $@ || bailout


