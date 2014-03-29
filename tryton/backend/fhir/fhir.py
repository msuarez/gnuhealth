#!/usr/bin/env python
# -*- coding: utf-8 -*-
##############################################################################
#
#    HL7 FHIR Python Reference Implementation
#    Copyright (C) 2014 Luis Falcon <lfalcon@gnusolidario.org>
#    Copyright (C) 2014 GNU Solidario <health@gnusolidario.org>
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

import requests


__all__ = ["RestfulFHIR"]


class RestfulFHIR:
    """General Set of REST Interactions for resources"""

    def search(self, base, resource, params):
        """Search FHIR Resources with specific criteria
            PARAMETERS:
                base : Service Root URL
                resource : resource type
                params : extra search criteria
            RETURNS:
                response
        """

        fhir_query = str(base) + '/' + str(resource) + '?' + str(params)
        response = requests.get(fhir_query)
        return response

    def read(self, base, resource, resid):
        """Read current status of the resource
            PARAMETERS:
                base : Service Root URL
                besource : resource type
                resid : unique resource identifier
            RETURNS:
                response
                    200 : Found
                    404 : Does not exist
                    410 : Deleted resource
        """

        fhir_query = str(base) + '/' + str(resource) + '/' + str(resid)
        response = requests.get(fhir_query)
        return response

    def update(self, body, base, resource, resid):
        """Update or create FHIR resource
            PARAMETERS:
                body : resource
                base : service root url
                resource : resource type
                resid : unique resource identifier
            RETURNS:
                response
                    200 : Resource updated
                    201 : Resource created
                    400 : Bad request
                    404 : Type not supported
                    405 : Not allowed
                    409 : Version conflict
                    412 : Version precondition failure
                    422 : Rejected
        """

        fhir_query = '/'.join([str(base), str(resource), str(resid)])
        response = requests.put(fhir_query, data=body)
        return response

    def delete(self, base, resource, resid):
        """Delete existing resource
            PARAMETERS:
                base : service root url
                resource : resource type
                resid : unique resource identifier
            RETURNS:
                response
                    204 : Delete successful
                    404 : Does not exist
                    405 : Not allowed
        """

        fhir_query = '/'.join([str(base), str(resource), str(resid)])
        response = requests.delete(fhir_query)
        return response

    def create(self, base, resource, body, headers):
        """Create new resource
            PARAMATERS:
                body : resource
                base : service root url
                resource : resource type
            RETURNS:
                201 : Resource created
                400 : Bad request
                404 : Not supported
                422 : Rejected
                500 : Incorrect Document
        """

        fhir_query = '/'.join([str(base), str(resource)])
        response = requests.post(fhir_query, data=body, headers=headers)
        return response

    def transaction(self, bundle, base):
        """Create, delete, or update multiple resources
            PARAMETERS:
                bundle : resource bundle
                base : service root url
            RETURNS:
                200 : Success
                400 : Bad request
                404 : Not supported
                405 : Not allowed
                409 : Version conflict
                412 : Version precondition conflict
                422 : Rejected
        """

        fhir_query = str(base)
        response = requests.post(fhir_query, data=bundle)
        return response

    def conformance(self, base):
        """Retrieves conformance statement
            PARAMETERS:
                base : service root url
            RETURNS:
                200 : Found
                404 : FHIR not supported
        """
        #TODO Should support OPTIONS verb, too

        fhir_query = '/'.join([str(base), 'metadata'])
        response = requests.get(fhir_query)
        return response
