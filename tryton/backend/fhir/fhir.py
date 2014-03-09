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
    
    def search(self, base, resource, params):
        """Search FHIR Resources with specific criteria
            Base : Service Root URL
            Resource : resource type
            Parames : extra search criteria
        """
        fhir_query = str(base) +'/'+ str(resource) +'?'+ str(params)
        response = requests.get (fhir_query)
        return response
                
    
