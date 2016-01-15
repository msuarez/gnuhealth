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

from datetime import datetime
import uuid

# constants for PDQ supplier_new message values
SENDING_APPLICATION = 'gnuhealth'
SENDING_FACILITY = 'gnuhealth'
TIMESTAMP = datetime.strftime(datetime.now(), '%Y%m%d%H%M%S')
MESSAGE_ID = uuid.uuid4().hex
CHARACTER_SET = 'utf-8'
ASSIGNING_AUTHORITY_NMSP_ID = 'gnuhealth'
ASSIGNING_AUTHORITY_UNI_ID = '1'
ASSIGNING_AUTHORITY_UNI_ID_TP = 'ISO'
PDQ_5_NAME_TYPE = 'L'
PDQ_QRY_PARAMS_ALLOWED_CODES = ['@PID.3.1', '@PID.5.1.1', '@PID.5.2', '@PID.7.1', '@PID.8', '@PID.11.1.1', '@PID.11.3',
                                '@PID.11.4', '@PID.11.5', '@PID.18.1']
PDQV_QRY_PARAMS_ALLOWED_CODES = PDQ_QRY_PARAMS_ALLOWED_CODES + ['@PV1.3.1']

PDQ_MSH_9 = 'RSP^K22^RSP_K21'
PDQV_MSH_9 = 'RSP^ZV2^RSP_ZV2' 

PDQ_MESSAGE_STRUCTURE = 'RSP_K21'
PDQV_MESSAGE_STRUCTURE = 'RSP_ZV2'
PROCESSING_ID = 'P'
COUNTRY_CODE = 'ITA'
LANGUAGE = 'EN'
PDQ_RESULTS_FOUND_CODE = 'OK'
PDQ_NO_RESULTS_FOUND_CODE = 'NF'
APPLICATION_ACCEPT_CODE = 'AA'
APPLICATION_ERROR_CODE = 'AE'
APPLICATION_REJECT_CODE = 'AR'


# constants for errors
class ERRORS:
    SEVERITY_ERROR_CODE = 'E'
    SEGMENTS_SEQUENCE_ERROR = '100'
    REQ_FIELD_MISSING = '101'
    DATA_TYPE_ERROR = '102'
    UNSUPPORTED_MSG_TYPE = '200'
    GENERIC_ERROR = '207'

