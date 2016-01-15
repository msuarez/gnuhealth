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

import logging
import os
from datetime import datetime
from sql import Join
from sql.operators import Like
from hl7apy.core import Message
from hl7apy.utils import check_date
from hl7apy.parser import parse_message, get_message_type
from hl7apy import load_message_profile
from hl7apy.validation import VALIDATION_LEVEL
from hl7apy.exceptions import ParserError, HL7apyException, ValidationError, MessageProfileNotFound
from trytond.transaction import Transaction
from consts import TIMESTAMP, PDQ_MSH_9, PDQV_MSH_9, MESSAGE_ID, COUNTRY_CODE, LANGUAGE, PDQ_QRY_PARAMS_ALLOWED_CODES, \
    PDQV_QRY_PARAMS_ALLOWED_CODES, ASSIGNING_AUTHORITY_NMSP_ID, ASSIGNING_AUTHORITY_UNI_ID, \
    ASSIGNING_AUTHORITY_UNI_ID_TP, PDQ_MESSAGE_STRUCTURE, PDQV_MESSAGE_STRUCTURE, \
    APPLICATION_ERROR_CODE, APPLICATION_REJECT_CODE, APPLICATION_ACCEPT_CODE, ERRORS, CHARACTER_SET
from exceptions import InvalidPDQMessage, MissingQueryParameters, MalformedPDQMessage, \
    InvalidQueryParameterCode, MissingQueryParameterValue, InvalidDateParameterValue, \
    PDQDAOException, ConnectionPoolException, InvalidSendingApplicationParameterValue, \
    PDQMessageProfileNotFound

logger = logging.getLogger(__name__)


class GnuHealthPdqDAO():
    """
    Class for Gnuhealth database connection. It provides all the methods for Patient Demographics
    Query execution, according to query parameters coming from the request HL7 message.
    """
    def __init__(self, pool):
        """
        @param pool: the HL7 Pool Manager
        """
        
        self.pool = pool
        self.patient_table = self.pool.get_table('gnuhealth.patient')
        self.party_table = self.pool.get_table('party.party')
        self.address_table = self.pool.get_table('party.address')
        
        # tables used for PDQV 
        self.hospital_bed_table = self.pool.get_table('gnuhealth.hospital.bed')
        self.hospital_ward_table = self.pool.get_table('gnuhealth.hospital.ward')
        self.inpatient_registration_table = self.pool.get_table('gnuhealth.inpatient.registration')
        
        # HL7 Configuration tables
        self.hl7_conf_table = self.pool.get_table('hl7.hl7')
        
        # PDQ Configuration tables
        self.pdq_conf_table = self.pool.get_table('pdq.pdq')
        self.pdq_allowed_apps_table = self.pool.get_table('pdq.allowed_applications')
        
        # PDQ Configuration parameters dictionary
        self.pdq_conf_dict = self._load_pdq_configuration_dict()

    def _get_pdq_fields(self, is_pdqv=False):
        """
        Provides the Gnuhealth database fields which provide PDQ (or PDQV) information needed to fill the HL7 message
        response. All the fields are ordered in a list, each of the fields refer to a specific
        PID (or PV1)  segment field.

        :return: An array containing the Gnuhealth Column objects referred to the fields
        """
        pdq_fields = [
            # change the first parameter to self.patient_table.identifier_code for gnuhealth 2.4
            self.party_table.code,            # pid_3_1       - PATIENT IDENTIFIER
            self.party_table.lastname,        # pid_5_1       - PATIENT LAST NAME
            self.party_table.name,            # pid_5_2       - PATIENT_ NAME
            # NOT SUPPORTED:                  # pid_6_1       - MOTHER_MAIDEN_NAME
            # NOT SUPPORTED:                  # pid_6_1_7     - NAME_TYPE_CODE
            self.party_table.dob,             # pid_7_1       - DATETIME_OF_BIRTH,
            self.party_table.sex,             # pid_8         - ADMINISTRATIVE_SEX
            self.address_table.street,        # pid_11_1      - STREET_ADDRESS
            self.address_table.city,          # pid_11_3      - CITY
            self.address_table.country,       # pid_11_4      - STATE_OR_PROVINCE
            self.address_table.zip,           # pid_11_5      - ZIP_CODE
            # NOT SUPPORTED:                  # pid_11_9      - COUNTY_CODE
            # SEEM NOT SUPPORTED              # pid_13_1      - TELEPHONE_NUMBER
            # SEEM NOT SUPPORTED              # pid_13_1_2    - PHONE_USE_CODE
            # SEEM NOT SUPPORTED              # pid_13_1_3    - PHONE_EQP_TYPE
            # SEEM NOT SUPPORTED              # pid_13_1_6    - PHONE_AREA
            self.party_table.ref,             # pid_18_1      - ACCOUNT_NUMBER
            self.party_table.ref,             # pid_19_1      - SSN
            self.party_table.marital_status,  # pid_16        - MARITAL_STATUS
            # SEEM NOT SUPPORTED              # pid_23        - BIRTH_CITY
        ]
      
        if is_pdqv:
            pdq_fields.append(self.hospital_ward_table.name)  # pv1_3_1 - WARD NAME # problems with PDQ calls
       
        logger.debug("PDQ FIELDS LEN:%d" % len(pdq_fields))
        return pdq_fields

    def _get_params_table_mappings(self):
        """
        Defines the mapping between the HL7 Query search parameters and the Column Gnuealth objects they refer to
        :return: A dictionary mapping the HL7 query search parameter keys with the Column objects
        """
        return {
            'patient_identifier': self.patient_table.name,
            'patient_surname': self.party_table.lastname,
            'patient_name': self.party_table.name,
            'patient_dob': self.party_table.dob,
            'patient_sex': self.party_table.sex,
            'patient_address': self.address_table.street,
            'patient_account_number': self.party_table.ref,
            'patient_ward_name': self.hospital_ward_table.name
        }
        
    def _get_pdq_allowed_applications(self):
        transaction = Transaction()
        transaction.start(self.pool.get_domain(), 0)
        query = self.pdq_allowed_apps_table.select(*[self.pdq_allowed_apps_table.allowed_application])
        cursor = transaction.cursor
        cursor.execute(*query)
        results = cursor.fetchall()  # return all results
        transaction.stop()  # cursor.close()
        
        if results is not None and len(results) > 0:
            allowed_apps = [res[0] for res in results]
            logger.debug("Allowed APPS:%s" % allowed_apps)
            return allowed_apps
        else:
            logger.debug("NO allowed applications found")
            return []
        
    def _get_sending_application(self):
        transaction = Transaction()
        transaction.start(self.pool.get_domain(), 0)
        query = self.hl7_conf_table.select(*[self.hl7_conf_table.application_code])
        cursor = transaction.cursor
        cursor.execute(*query)
        results = cursor.fetchall()  # return all results
        transaction.stop()
        
        if results is not None and len(results) > 0:
            return results[0][0]
        else:
            return "gnuhealth"
        
    def is_pdq_module_enabled(self):
        return self.pdq_conf_dict["ENABLED"]
    
    def is_sending_application_filter_enabled(self):
        return self.pdq_conf_dict["FILTER_BY_ALLOWED_APP"]
    
    def get_allowed_applications(self):
        return self.pdq_conf_dict["ALLOWED_APPLICATIONS"]
    
    def get_sending_application(self):
        return self.pdq_conf_dict["SENDING_APPLICATION"]
    
    def get_sending_facility(self):
        return self.pdq_conf_dict["SENDING_FACILITY"]
    
    def get_character_set(self):
        return self.pdq_conf_dict["CHARACTER_SET"]
    
    def get_language_code(self):
        return self.pdq_conf_dict["LANGUAGE"]
    
    def get_country_code(self):
        return self.pdq_conf_dict["COUNTRY"]
    
    def _load_pdq_configuration_dict(self):
        """
        Load the pdq configuration dict from the database, based on the current content of the hl7 and pdq tables
        """
  
        conf = {
            "ENABLED": False,
            "ALLOWED_APPLICATIONS": [],
            "FILTER_BY_ALLOWED_APP": False,
            "SENDING_FACILITY": "gnuhealth",
            "SENDING_APPLICATION": "gnuhealth",
            "CHARACTER_SET": CHARACTER_SET,
            "LANGUAGE": LANGUAGE,
            "COUNTRY": COUNTRY_CODE
        }
        
        transaction = Transaction()
        transaction.start(self.pool.get_domain(), 0)
        query = self.pdq_conf_table.select(*[self.pdq_conf_table.enabled, self.pdq_conf_table.facility_name,
                                           self.pdq_conf_table.filter_by_allowed_app, self.pdq_conf_table.encoding_char,
                                           self.pdq_conf_table.country, self.pdq_conf_table.language])
        cursor = transaction.cursor
        cursor.execute(*query)
        results = cursor.fetchall()  # return all results
        logger.debug("PDQ CONFIGURATION Query results: %s" % results)
        
        transaction.stop()
        
        if results:
            conf["ENABLED"] = results[0][0]   
            conf["SENDING_FACILITY"] = results[0][1]   
            conf["FILTER_BY_ALLOWED_APP"] = results[0][2]
            conf["CHARACTER_SET"] = results[0][3]
            conf["COUNTRY"] = results[0][4]
            conf["LANGUAGE"] = results[0][5]
            conf["ALLOWED_APPLICATIONS"] = self._get_pdq_allowed_applications()
            conf["SENDING_APPLICATION"] = self._get_sending_application()
            
        return conf
    
    def _get_pdq_where_clause(self, query_params):
        """
        Builds the where clause of the Gnuhealth ORM query, according to the HL7 parameters provided in the dictionary
        at input. PDQ supplier may decide some rules of the query, according to the way it decides to provide data.
        The main rules are the following:

         - Surname, name and address parameter use a LIKE operator and they allow also the usage of the '*' character
         in the parameter value of the PDQ request HL7 message. This special character has the same behaviour
         of '%' in SQL

         - All the other parameters use an EQUAL operator, and usage of special character is not supported.

         :type:  query_params ``dictionary``
         :param: query_params A dictionary providing the parameter values coming from the PDQ HL7 message request

         :return: The Where clause used by the Gnuhealth ORM methods to perform the query
        """
        logger.debug(query_params.iteritems())
        where = None
        mappings = self._get_params_table_mappings()
        for param, value in query_params.iteritems():
            if param in ('patient_surname', 'patient_name', 'patient_address'):
                if not where:
                    # % is the magic character for the LIKE operator
                    where = Like(mappings[param], value.replace('*', '%'))
                else:
                    # % is the magic character for the LIKE operator
                    where &= Like(mappings[param], value.replace('*', '%'))
            else:
                if not where:
                    where = mappings[param] == value
                else:
                    where &= mappings[param] == value
        return where

    def _get_pdq_results_table(self):
        logger.debug("PQQ building query...")
        patient_party_join = Join(self.patient_table, self.party_table)
        patient_party_join.type_ = 'LEFT'
        patient_party_join.condition = patient_party_join.left.name == self.party_table.id
        # Second join, with address table
        patient_party_addr_join = Join(patient_party_join, self.address_table)
        patient_party_addr_join.type_ = 'LEFT'
        patient_party_addr_join.condition = patient_party_addr_join.right.party == patient_party_join.right.id
        
        logger.debug("PDQ JOIN TABLE CREATED")
        return patient_party_addr_join
    
    def _get_pdqv_results_table(self):
        logger.debug("PQQV building query")
        
        # JOIN 1, party table with patient table
        # LEFT JOIN gnuhealth_patient on gnuhealth_patient.name=party_party.id 
        patient_party_join = Join(self.patient_table, self.party_table)
        patient_party_join.type_ = 'LEFT'
        patient_party_join.condition = patient_party_join.left.name == self.party_table.id
        
        # JOIN 2, with address table
        patient_party_addr_join = Join(patient_party_join, self.address_table)
        patient_party_addr_join.type_ = 'LEFT'
        patient_party_addr_join.condition = patient_party_addr_join.right.party == patient_party_join.right.id
        
        # JOIN 3 , with inpatient_registration table
        # LEFT JOIN gnuhealth_inpatient_registration ON gnuhealth_inpatient_registration.patient = gnuhealth_patient.id
        patient_party_reg_join = Join(patient_party_addr_join, self.inpatient_registration_table)
        patient_party_reg_join.type_ = 'LEFT'
        patient_party_reg_join.condition = self.inpatient_registration_table.patient == self.patient_table.id
        
        # JOIN 4, with hospital_bed table
        # LEFT JOIN gnuhealth_hospital_bed ON gnuhealth_hospital_bed.id = gnuhealth_inpatient_registration.bed
        patient_party_bed_join = Join(patient_party_reg_join, self.hospital_bed_table)
        patient_party_bed_join.type_ = "LEFT"
        patient_party_bed_join.condition = self.hospital_bed_table.id == self.inpatient_registration_table.bed
        
        # JOIN 5, with hospital_ward table
        # LEFT JOIN gnuhealth_hospital_ward ON gnuhealth_hospital_ward.id = gnuhealth_hospital_bed.ward
        # where gnuhealth_hospital_ward.name='Maternity'
        patient_party_ward_join = Join(patient_party_bed_join, self.hospital_ward_table)
        patient_party_ward_join.type_ = "LEFT"
        patient_party_ward_join.condition = self.hospital_ward_table.id == self.hospital_bed_table.ward
        logger.debug("PDQV JOIN TABLE CREATED")
       
        return patient_party_ward_join
        
    def search_patient(self, transaction, query_parameters, is_pdqv=False):
        """
        Performs the query to search for patient results, according to the parameters provided at input. It uses the
        ORM objects in order to define all the Join clauses needed to retrieve all fields required to build the message
        response. It instantiates a connection to the Gnuhealth server in order to perform the query.

        :type: transaction ``Transaction``
        :param: transaction The Gnuhealth Trytond transaction object
        :type is_pdqv: boolean
        :param is_pdqv: true if the message is a Patient Demographics And Visit Query Message, false otherwise
            (it is a PDQ message)
        :return: A list of tuples containing all the found results

        :raises: :exc:`PDQDAOException` if an exception occurs during query execution

        """
        try:
            if is_pdqv:
                patients_table = self._get_pdqv_results_table()
            else:
                patients_table = self._get_pdq_results_table()
        
            logger.debug("Patients Result Table:%s" % str(patients_table))
            transaction.start(self.pool.get_domain(), 0)
            query = patients_table.select(*self._get_pdq_fields(is_pdqv),
                                          where=self._get_pdq_where_clause(query_parameters))
            cursor = transaction.cursor
            logger.debug("Executing Patients Search query: %s" % query)
            cursor.execute(*query)
            
            results = cursor.fetchall()  # return all results
            logger.debug('Query results: %s' % results)
            transaction.stop()
            return results
        except Exception as e:
            logger.error('An error occurred performing the query: %s' % e)
            raise PDQDAOException


class GnuHealthPDQSupplier():
    """
    This class implements the IHE Patient Demographics Supplier (PDS) actor for Gnuhealth. It is the actor responsible
    to receive all the HL7 PDQ requests, transform each one in a Gnuhealth ORM query, retrieve the results and then
    send them back to the client in a HL7 acknowledge response message
    """
    def __init__(self, pool_manager, msg):
        self.raw_msg = msg
        self.msg = None  # the PQD raw message has not been parsed yet
        self.pool = pool_manager
        self.dao = GnuHealthPdqDAO(self.pool)

    def _nvl(self, value):
        return value if value else u''
    
    def is_pdq_message(self):
        try:
            return get_message_type(self.raw_msg) == "QBP^Q22^QBP_Q21"
        except Exception, e:
            logger.debug("Invalid message type: %s: %s" % (self.raw_msg, str(e)))
            return False
    
    def is_pdqv_message(self):
        try:
            return get_message_type(self.raw_msg) == "QBP^ZV1^QBP_Q21"
        except Exception, e:
            logger.debug("Invalid message: %s: %s" % (self.raw_msg, str(e)))
            return False
    
    def is_pdq_module_enabled(self):
        return self.dao.is_pdq_module_enabled()
    
    def is_sending_application_filter_enabled(self):
        return self.dao.is_sending_application_filter_enabled()
    
    def get_allowed_applications(self):
        return self.dao.get_allowed_applications()

    def _check_incoming_message(self):
        """
        Controls the incoming HL7 message, after parsing, according to some IHE PDQ message request rules.
        It checks that:

          - All query parameters codes and values are correct in the request message

          - The incoming message contains at least one query parameter

          - For the birth date query parameter, the date value format is HL7 - compliant
          
          - If the Allowed Application Filter is enabled. checks if the MSH_3 field contains a value included in the
            Allowed_application list table

        :raises: :exc:`MissingQueryParameters` if the incoming message has not any query parameters
            (QPD_3 hl7 message field is empty)
        :raises: :exc:`InvalidQueryParameterCode` if the incoming message has a query parameter code
            (QPD_3_1) in a not-allowed format
        :raises: :exc:`MissingQueryParameterValue` if the incoming message has a query parameter
            (QPD_3_1) correct but without the corrispondent value (QPD_3_2)
        :raises: :exc:`InvalidDateParameterValue` if the incoming message has a query parameter (QPD_3_1) asking for
            the patient birth date, but providing a not allowed date format in the value
        :raise:  :exc:`InvalidSendingApplicationParameterValue if the Application Filter is enabled and  the MSH_3
            field of the incoming message is not included into the Allowed Applications list`
        """
        
        try:
            message_profiles_dir = _get_message_profiles_dir()
            logger.debug("Checking for message profile from dir: %s" % message_profiles_dir)
            
            if self.is_pdq_message():
                message_profile = load_message_profile(os.path.join(message_profiles_dir, 'pdq_request'))
            elif self.is_pdqv_message():
                message_profile = load_message_profile(os.path.join(message_profiles_dir, 'pdqv_request'))
            else:
                raise MessageProfileNotFound()
            self.msg = parse_message(self.raw_msg, validation_level=VALIDATION_LEVEL.STRICT,
                                     message_profile=message_profile)
        except MessageProfileNotFound, e:  # NO PDQ
            logger.error("No message profile found for message: %s -> %s" % (self.raw_msg, str(e)))
            raise PDQMessageProfileNotFound
        except ParserError, e:  # INVALID HL7
            logger.error("Error parsing incoming  message: %s -> %s" % (self.raw_msg, str(e)))
            raise MalformedPDQMessage(str(e))
        except HL7apyException, e:  # INVALID PDQ
            logger.error("Error parsing incoming PDQ message: %s -> %s" % (self.raw_msg, str(e)))
            raise MalformedPDQMessage(str(e))
        
        try:
            self.msg.validate()
        except ValidationError, ve:
            logger.error("Error validating incoming PDQ message: %s -> %s" % (self.raw_msg, str(ve)))
            raise MalformedPDQMessage(str(ve))

        if self.is_sending_application_filter_enabled():
            allowed_apps = self.get_allowed_applications()
            msh_3 = self.msg.msh.msh_3
            logger.debug("MSH_3 VALUE:%s" % msh_3.value)
            if msh_3.value not in allowed_apps:
                raise InvalidSendingApplicationParameterValue
        
        qpd_3 = self.msg.qpd.qpd_3
        if len(qpd_3) == 0:
            raise MissingQueryParameters
        # check parameters codes correctness
        else:
            if self.is_pdq_message():
                qry_params_allowed_codes = PDQ_QRY_PARAMS_ALLOWED_CODES
            elif self.is_pdqv_message():
                qry_params_allowed_codes = PDQV_QRY_PARAMS_ALLOWED_CODES
            else:
                raise InvalidPDQMessage(self.msg.MSH.MSH_9.value)
                
            for qpd3_instance in qpd_3:
                if qpd3_instance.qpd_3_1.value not in qry_params_allowed_codes:
                    raise InvalidQueryParameterCode(qpd3_instance.qpd_3_1.value)
                elif qpd3_instance.qpd_3_2.value == '':
                    raise MissingQueryParameterValue
                # check that the PID.7.1, if passed, is a date in one of the allowed HL7 formats
                elif qpd3_instance.qpd_3_1.value == '@PID.7.1':
                    if not check_date(qpd3_instance.qpd_3_2.value):
                        raise InvalidDateParameterValue
        return True

    def _create_query_parameters(self):
        """
        This method is called after HL7 request message check and fills the dictionary object, used later to build the
        where clause of the Gnu Health ORM query, with the required values.

        :return: A dictionary containing all name-> value pairs for query parameters provided in the message
        """
        params = {}
        mapping = {
            '@PID.3.1': 'patient_identifier',
            '@PID.5.1.1': 'patient_surname',
            '@PID.5.2': 'patient_name',
            '@PID.7.1': 'patient_dob',
            '@PID.8': 'patient_sex',
            '@PID.11.1.1': 'patient_address',
            '@PID.18': 'patient_account_number',
            '@PV1.3.1': 'patient_ward_name'
            }
        
        for qpd_instance in self.msg.qpd.qpd_3:
            try:
                param_name = mapping[qpd_instance.qpd_3_1.value]
                params[param_name] = qpd_instance.qpd_3_2.value
            except KeyError, ke:
                logger.error("Query parameter %s not supported yet:%s . Ignored..." % (qpd_instance, ke))
            
        return params

    def _set_msh(self, message, is_pdqv=False):
        """
        Fills the MSH segment of the response message

        :type: message ``Message``
        :params: message The incoming HL7 request parsed message
        """
        
        message.msh.msh_3 = self.dao.get_sending_application()
        message.msh.msh_4 = self.dao.get_sending_facility()
        message.msh.msh_5 = self.msg.msh.msh_3
        message.msh.msh_6 = self.msg.msh.msh_4
        message.msh.msh_7 = TIMESTAMP
        
        if is_pdqv:
            message.msh.msh_9 = PDQV_MSH_9
        else:
            message.msh.msh_9 = PDQ_MSH_9
            
        message.msh.msh_10 = MESSAGE_ID
        message.msh.msh_17 = self.dao.get_country_code()
        message.msh.msh_18 = self.dao.get_character_set()
        message.msh.msh_19 = self.dao.get_language_code()
       
    def _create_pdq_res_list(self, message, message_structure, results):
        """
        Iterates the results tuple coming from the Gnuhealth ORM query execution, and provides a list of PDQ Segment
        objects, filled with the value results. These segments will be part of the response message.
        If the query had no results, an empty list is returned.
         
        :type:  results  ``list``
        :param: results a list providing the Gnuhealth ORM query results

        :return: the original message with a list of PDQ hl7apy ``Segment`` instances valued with the results

        """
        if len(results) == 0:
            return message
        else:
            pid_seq = 1
            character_set = self.dao.get_character_set()
            
            if message_structure == PDQV_MESSAGE_STRUCTURE:
                g0 = message.add_group('%s_query_response' % message_structure)
                g = g0.add_group('%s_PATIENT' % message_structure)
                
            else:
                g = message.add_group('%s_query_response' % message_structure)
                
            logger.debug("group created")
                
            for result in results:
                pid = g.add_segment("pid")
                # pid = message.add_segment("pid")
                # pid = m.rsp_k21_query_result.pid
                pid.pid_1.pid_1_1 = '%s' % pid_seq
                pid.pid_3.pid_3_1 = '%s' % self._nvl(result[0])
                pid.pid_3.pid_3_4.hd_1 = ASSIGNING_AUTHORITY_NMSP_ID
                pid.pid_3.pid_3_4.hd_2 = ASSIGNING_AUTHORITY_UNI_ID
                pid.pid_3.pid_3_4.hd_3 = ASSIGNING_AUTHORITY_UNI_ID_TP
                pid.pid_5.pid_5_1 = self._nvl(result[1]).encode(character_set)
                pid.pid_5.pid_5_2 = self._nvl(result[2]).encode(character_set)
                pid.pid_7 = datetime.strftime(result[3], '%Y%m%d') if result[3] else ''
                pid.pid_8 = self._nvl(result[4]).encode(character_set)
                pid.pid_11.xad_1 = self._nvl(result[5]).encode(character_set)
                pid.pid_11.xad_3 = self._nvl(result[6]).encode(character_set)
                pid.pid_11.xad_4 = self._nvl(result[7]).encode(character_set)
                pid.pid_11.pid_11_5 = self._nvl(result[8]).encode(character_set)
                pid.pid_18.pid_18_1 = self._nvl(result[9]).encode(character_set)
                pid.pid_16.pid_16_1 = self._nvl(result[10]).encode(character_set)
                pid_seq += 1
            return message

    def build_error_response(self, error_msg):
        m = Message("ACK") 
        m.MSH.MSH_9 = "ACK^ACK"
        m.MSA.MSA_1 = "AR"
        m.MSA.MSA_2 = self.msg.MSH.MSH_10 if self.msg else ""
        m.ERR.ERR_1 = "100"
        m.ERR.ERR_2 = error_msg
        
        return m.to_mllp()
    
    def _create_error_message(self):
        m = Message("ACK",  version='2.5', validation_level=VALIDATION_LEVEL.STRICT) 
        m.MSH.MSH_9 = "ACK^ACK"
        m.MSA.MSA_1 = "AR"
        m.MSA.MSA_2 = self.msg.MSH.MSH_10 if self.msg else ""
        return m
        
    def _create_message(self, results, ack_code):
        """
        Creates the final RSP_K21 response message. If no errors occurred and some results have been found, the message
        will carry as many different PID segments as the number of the results.

        :type:  results  ``list``
        :param: results a list providing the Gnuhealth ORM query results

        :type:  ack_code  ``str``
        :param: ack_code it is the ack:code to be put in the MSA segment. If no errors occurred, the code wull be of
            positive ACK (AA); else, one of the negative acks (AE, AR)

        :return: an hl7apy ``Message`` class instance, which is the final RSP_K21 message
        """
        try:
            qry_ack_code = 'OK'
            if len(results) == 0:
                qry_ack_code = 'NF'
            
            is_pdqv = self.is_pdqv_message()
            logger.debug("Creating response message...")
            if is_pdqv:
                message_profile = load_message_profile(os.path.join(_get_message_profiles_dir(), "pdqv_response"))
                message_structure = PDQV_MESSAGE_STRUCTURE
            else:
                message_profile = load_message_profile(os.path.join(_get_message_profiles_dir(), "pdq_response"))
                message_structure = PDQ_MESSAGE_STRUCTURE
                
            message = Message(message_structure, version='2.5', validation_level=VALIDATION_LEVEL.STRICT,
                              reference=message_profile)
            
            self._set_msh(message, is_pdqv)
            
            msa = message.add_segment("MSA")
            msa.msa_1 = ack_code
            msa.msa_2 = self.msg.msh.msh_10.msh_10_1

            qak = message.add_segment("QAK")
            qak.qak_1 = self.msg.qpd.qpd_2
            qak.qak_2 = qry_ack_code
            qak.qak_4.qak_4_1 = str(len(results))  # total results
            qak.qak_5.qak_5_1 = str(len(results))  # sent results
            qak.qak_6.qak_6_1 = "0"  # remaining results
            
            message.add_segment("QPD")
            message.qpd = self.msg.qpd

            message = self._create_pdq_res_list(message, message_structure, results)
            return message
        except Exception, e:
            logger.error('Error during Message Creation, %s' % e)

    def create_pdq_response(self):
        """
        This is the main method of the GnuHealthPDQSupplier class. It receives the HL7 request message from the
        dispatcher, and returns the response message. It first calls the methods to execute parsing and all checks to
        the incoming message. If these operation fails, no query is executed in the Gnuhealth ORM, ad a N-ACK response
        is created and sent back. Else, a GnuHealthPDQDAO object is instantiated, and the query executed.

        :return: The hl7apy Message object, which is the response message object
        """
        logger.debug("CREATING PDQ RESPONSE...")
        err = None
        response = None
        is_generic_incoming_msg_error = False
        try:
            # check if enabled
            self._check_incoming_message()
            logger.debug("INCOMING PDQ MESSAGE CHECKING PASSED")
        except InvalidPDQMessage as e:
            err = (e.error_code, e.segment_id, e.segment_sequence,
                   ERRORS.SEVERITY_ERROR_CODE, str(e))
            is_generic_incoming_msg_error = True
        except PDQMessageProfileNotFound as e:
            err = (e.error_code, None, None,
                   ERRORS.SEVERITY_ERROR_CODE, str(e))
            is_generic_incoming_msg_error = True
        except MalformedPDQMessage as e:
            err = (e.error_code, None, None,
                   ERRORS.SEVERITY_ERROR_CODE, str(e))
            is_generic_incoming_msg_error = True
        except MissingQueryParameters as e:
            err = (e.error_code, e.segment_id, e.segment_sequence,
                   ERRORS.SEVERITY_ERROR_CODE, str(e))
        except InvalidQueryParameterCode as e:
            err = (e.error_code, e.segment_id, e.segment_sequence,
                   ERRORS.SEVERITY_ERROR_CODE, str(e))
        except MissingQueryParameterValue as e:
            err = (e.error_code, e.segment_id, e.segment_sequence,
                   ERRORS.SEVERITY_ERROR_CODE, str(e))
        except InvalidDateParameterValue as e:
            err = (e.error_code, e.segment_id, e.segment_sequence,
                   ERRORS.SEVERITY_ERROR_CODE, str(e))
        except InvalidSendingApplicationParameterValue as e:
            err = (e.error_code, e.segment_id, e.segment_sequence,
                   ERRORS.SEVERITY_ERROR_CODE, str(e))
        except Exception as e:
            logger.error("Unknown exception during pdq incoming message parsing:%s" % e)
            err = (ERRORS.GENERIC_ERROR, None, None, ERRORS.SEVERITY_ERROR_CODE, str(e))
        
        if err:
            logger.error("Error found parsing incoming message. Generic: %s -> %s" %
                         (is_generic_incoming_msg_error, err))
            if is_generic_incoming_msg_error:
                response = self._create_error_message()
                logger.debug("create generic error response: %s" % response)
            else:
                response = self._create_message([], APPLICATION_REJECT_CODE)
                
            logger.debug("Adding error segment: %s" % str(err))  
            error_code, segment_id, segment_sequence, severity, description = err
            err_segment = response.add_segment("err")
            if segment_id is not None:
                err_segment.err_2.err_2_1 = segment_id  # optional field
            if segment_sequence is not None:
                err_segment.err_2.err_2_2 = segment_sequence  # optional field
            err_segment.err_3.err_3_1 = error_code
            if description is not None:
                err_segment.err_3.err_3_2 = description  # optional field
            err_segment.err_4.err_4_1 = severity  
            
            return response.to_mllp()
                
        else:
            logger.debug("Incoming message is valid: building the query")
            # if the message is OK, proceed with the query
            try:
                 
                transaction = Transaction()
                qry_params = self._create_query_parameters()
                
                results = self.dao.search_patient(transaction, qry_params, self.is_pdqv_message())
                logger.debug("Query results: %s" % str(results))
                response = self._create_message(results, APPLICATION_ACCEPT_CODE)
                logger.debug("Response: %s" % str(response))
            except PDQDAOException as e:
                err = (e.error_code, e.segment_id, e.segment_sequence, ERRORS.SEVERITY_ERROR_CODE, str(e))
            except ConnectionPoolException as e:
                err = (e.error_code, e.segment_id, e.segment_sequence, ERRORS.SEVERITY_ERROR_CODE, str(e))
            except Exception as e:
                logger.error("Unknown exception during hl7 response creation:%s" % e)
                err = (ERRORS.GENERIC_ERROR, None, None, ERRORS.SEVERITY_ERROR_CODE, str(e))
        
            if err:
                response = self._create_message([], APPLICATION_ERROR_CODE)
                error_code, segment_id, segment_sequence, severity, description = err
                err_segment = response.add_segment("err")
                if segment_id is not None:
                    err_segment.err_2.err_2_1 = segment_id  # optional field
                if segment_sequence is not None:
                    err_segment.err_2.err_2_2 = segment_sequence  # optional field
                err_segment.err_3.err_3_1 = error_code
                if description is not None:
                    err_segment.err_3.err_3_2 = description  # optional field
                err_segment.err_4.err_4_1 = severity  
           
            return response.to_mllp()


def _get_message_profiles_dir():
    return os.path.join(os.path.dirname(__file__), "message_profiles/")
    
if __name__ == '__main__':
    
    from connection.pool_manager import PoolManager
    pool_mgr = PoolManager("gnuhealth_demo")
    # test search patient, with where clause
    s = GnuHealthPdqDAO(pool_mgr)
    qp = {
        'patient_surname': 'BL*',
        'patient_name': 'BER*',
        'patient_dob': datetime.strptime('19851212', '%Y%m%d'),
        'patient_sex': 'm',
        'patient_address': 'ke*',
        'patient_identifier': '7'
    }
    s.search_patient(Transaction(), qp)


