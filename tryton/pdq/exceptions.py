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

from consts import PDQ_QRY_PARAMS_ALLOWED_CODES, ERRORS


class PDQSupplierException(Exception):
    """
    Base exception class for PDQSupplier
    """
    def __init__(self, error_code=None, segment_id=None, segment_sequence=None):
        self.error_code = error_code
        self.segment_id = segment_id
        self.segment_sequence = segment_sequence


class InvalidPDQMessage(PDQSupplierException):
    """
    Raised when the incoming message is not of the correct type QPB^Q21^QBP_Q21 or QBP^ZV1^QBP_Q21
    """
    def __init__(self, message_type):
        self.message_type = message_type
        self.error_code = ERRORS.UNSUPPORTED_MSG_TYPE
        self.segment_id = 'MSH'
        self.segment_sequence = '9'

    def __str__(self):
        return 'The message type  {0} is not a PDQ request: allowed values are QBP^Q22^QBP_Q21 or QBP^ZV1^QBP_Q21' .\
            format(self.message_type.value)
    
    
class MalformedPDQMessage(PDQSupplierException):
    """
    Raised when the incoming message is not recognized as a valid PDQ Message
    """
    def __init__(self, info=""):
        self.error_code = ERRORS.GENERIC_ERROR
        self.info = info
        
    def __str__(self):
        return 'Malformed message: %s' % self.info 


class PDQMessageProfileNotFound(PDQSupplierException):
    """
    Raised when the incoming message is not recognized as a PDQ Message
    """
    def __init__(self, info=""):
        self.error_code = ERRORS.GENERIC_ERROR
        self.info = info
        
    def __str__(self):
        return 'Message Profile not found for the received message: %s' % self.info 


class InvalidQueryParameterCode(PDQSupplierException):
    """
    Raised when incoming message contains an invalid query parameter code in QBP_3 field
    """
    def __init__(self, parameter_code):
        self.parameter_code = parameter_code
        self.error_code = ERRORS.GENERIC_ERROR
        self.segment_id = 'QPD'
        self.segment_sequence = '3'

    def __str__(self):
        return 'The parameter code {0} is not allowed in the PDQ request message: allowed codes are {1}'.format(self.parameter_code, ','.join(code for code in PDQ_QRY_PARAMS_ALLOWED_CODES ))


class MissingQueryParameters(PDQSupplierException):
    """
    Raised when the incoming message has not any query parameter field (QBP_3 is empty)
    """

    def __init__(self):
        self.error_code = ERRORS.REQ_FIELD_MISSING
        self.segment_id = 'QPD'
        self.segment_sequence = '3'

    def __str__(self):
        return 'The incoming message has not any query parameter'


class MissingQueryParameterValue(PDQSupplierException):
    """
    Raise when a parameter provided in the QPB_3_1 field of the incoming message does not have a value (QBP_3_2 is null)
    """

    def __init__(self):
        self.error_code = ERRORS.REQ_FIELD_MISSING
        self.segment_id = 'QPD'
        self.segment_sequence = '3'

    def __str__(self):
        return 'Missing the reference value for one or more query parameter'


class InvalidDateParameterValue(PDQSupplierException):
    """
    Raised when a query value does not have tproper datatype and format required by hl7
    """

    def __init__(self):
        self.error_code = ERRORS.DATA_TYPE_ERROR
        self.segment_id = 'QPD'
        self.segment_sequence = '3'

    def __str__(self):
        return 'The @PDQ.7.1 parameter in the message does not have an HL7 Datetime datatype allowed format'


class PDQDAOException(PDQSupplierException):
    """
    Raised when Gnuhealth ORM query fails
    """

    def __init__(self):
        self.error_code = ERRORS.GENERIC_ERROR
        self.segment_id = ''
        self.segment_sequence = ''
        
    def __str__(self):

        return "Generic error during PDQ query execution "


class ConnectionPoolException(PDQSupplierException):
    """
    Raised when Tryton connection pool instantiation fails
    """

    def __init__(self):
        self.error_code = ERRORS.GENERIC_ERROR
        self.segment_id = ''
        self.segment_sequence = ''

    def __str__(self):
        return "Gnuhealth database pool creation error "
    
    
class InvalidSendingApplicationParameterValue(PDQSupplierException):
    """
    Raise when the Application Filter is enabled and the content of the MSH_3 field of the incoming message is not included into the Allowed Applications list 
    """

    def __init__(self):
        self.error_code = ERRORS.GENERIC_ERROR
        self.segment_id = 'MSH'
        self.segment_sequence = '3'

    def __str__(self):
        return 'Sending Application value not allowed'
    

