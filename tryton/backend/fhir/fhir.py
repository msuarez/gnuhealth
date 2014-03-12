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
                besource : resource type
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
