#!/usr/bin/env python
# -*- coding: utf-8 -*-
##############################################################################
#
#    HL7 FHIR Python Reference Implementation
#
#    Copyright (C) 2014 Luis Falcon <lfalcon@gnusolidario.org>
#    Copyright (C) 2014 GNU Solidario <health@gnusolidario.org>
#    Copyright (C) 2014 Chris Zimmerman <siv@riseup.net> 
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
import json
import lxml.etree


__all__ = ["RestfulFHIR"]


class RestfulFHIR:
    """General Set of REST Interactions for resources"""

    def __init__(self, base, content_type='json'):
        self.mimes={'xml': {'resource': 'application/xml+fhir; charset=utf-8',
                            'bundle': 'application/atom+xml; charset=utf-8',
                            'taglist': 'application/xml+fhir; charset=utf-8'},
                    'json': {'resource': 'application/json+fhir; charset=utf-8',
                            'bundle': 'application/json+fhir; charset=utf-8',
                            'taglist': 'application/json+fhir; charset=utf-8'}}
        self.validators={'json': json.loads,
                            'xml': lxml.etree.fromstring} 
        self.content_headers=self.mimes[content_type]
        self.validator=self.validators[content_type]
        self.base = base

    def search(self, resource, params):
        """Search FHIR Resources with specific criteria
            PARAMETERS:
                resource : resource type
                params : extra search criteria
            RETURNS:
                response
                    200 : Found
                    403 : Failed
        """

        fhir_query = '/'.join([str(self.base), str(resource)])
        headers={'accept': self.content_headers['resource']}
        response = requests.get(fhir_query, headers=headers, params=params)
        return response

    def read(self, resource, resid):
        """Read current status of the resource
            PARAMETERS:
                resource : resource type
                resid : unique resource identifier
            RETURNS:
                response
                    200 : Found
                    404 : Does not exist
                    410 : Deleted resource
        """

        fhir_query = str(self.base) + '/' + str(resource) + '/' + str(resid)
        headers={'accept': self.content_headers['resource']}
        response = requests.get(fhir_query, headers=headers)
        return response

    def vread(self, resource, resid, vid):
        """Read given version of the resource
            PARAMETERS:
                resource : resource type
                resid : unique resource identifier
                vid : unique version identifier
            RETURNS:
                response
                    200 : Found
                    404 : Does not exist
                    405 : Prohibit previous versions
                    410 : Deleted resource
        """

        fhir_query = '/'.join([str(x) for x in \
                    [self.base, resource, resid, '_history', vid]])
        headers={'accept': self.content_headers['resource']}
        response = requests.get(fhir_query, headers=headers)
        return response

    def update(self, resource, resid, body):
        """Update or create FHIR resource
            PARAMETERS:
                resource : resource type
                resid : unique resource identifier
                body : resource
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

        try:
            self.validator(body)
        except:
            raise TypeError("Body does not have a valid structure")
        fhir_query = '/'.join([str(self.base), str(resource), str(resid)])
        headers={'content-type': self.content_headers['resource']}
        response = requests.put(fhir_query, data=body, headers=headers)
        return response

    def delete(self, resource, resid):
        """Delete existing resource
            PARAMETERS:
                resource : resource type
                resid : unique resource identifier
            RETURNS:
                response
                    204 : Delete successful
                    404 : Does not exist
                    405 : Not allowed
        """

        fhir_query = '/'.join([str(self.base), str(resource), str(resid)])
        response = requests.delete(fhir_query)
        return response

    def create(self, resource, body):
        """Create new resource
            PARAMETERS:
                resource : resource type
                body : resource
            RETURNS:
                response
                    201 : Resource created
                    400 : Bad request
                    404 : Not supported
                    422 : Rejected
                    500 : Incorrect Document
        """

        try:
            self.validator(body)
        except:
            raise TypeError("Body does not have a valid structure")
        fhir_query = '/'.join([str(self.base), str(resource)])
        headers = {'content-type': self.content_headers['resource']}
        response = requests.post(fhir_query, data=body, headers=headers)
        return response

    def transaction(self, bundle):
        """Create, delete, or update multiple resources
            PARAMETERS:
                bundle : resource bundle
            RETURNS:
                response
                    200 : Success
                    400 : Bad request
                    404 : Not supported
                    405 : Not allowed
                    409 : Version conflict
                    412 : Version precondition conflict
                    422 : Rejected
        """

        try:
            self.validator(bundle)
        except:
            raise TypeError("Bundle does not have a valid structure")
        fhir_query = str(self.base)
        headers = {'content-type': self.content_headers['bundle']}
        response = requests.post(fhir_query, data=bundle, headers=headers)
        return response

    def conformance(self, _options=False):
        """Retrieves conformance statement
            PARAMETERS:
                _options : use OPTIONS verb
            RETURNS:
                response
                    200 : Found
                    404 : FHIR not supported
        """

        headers={'accept': self.content_headers['resource']}
        if _options:
            response = requests.options(str(self.base), headers=headers)
        else:
            fhir_query = '/'.join([str(self.base), 'metadata'])
            response = requests.get(fhir_query, headers=headers)
        return response

    def history(self, resource=None, resid=None, params=None):
        """Retrieve history of: specific resource, given type, or all resources
            PARAMETERS:
                resource : resource type
                resid :  unique resource identifier
                params : extra history criteria
            RETURNS:
                response
                    200 : Found
        """
        fhir_query = '/'.join([str(x) for x in \
                        [self.base, resource, resid, '_history'] if x])
        headers={'accept': self.content_headers['resource']}
        response = requests.get(fhir_query, headers=headers, params=params)
        return response

    def validate(self, resource, resid=None, body=None):
        """Check whether content is a valid resource and update
            PARAMETERS:
                resource : resource type
                body : resource
                resid : unique resource identifier
            RETURNS:
                response
                    200 : Valid resource/Valid update
                    400 : Bad request/Invalid
                    422 : Valid resource, but invalid update
        """

        if not body: raise TypeError('Need something to validate! Attach body.')
        try:
            self.validator(body)
        except:
            raise TypeError("Body does not have a valid structure")
        fhir_query = '/'.join([str(x) for x in \
                        [self.base, resource, '_validate', resid] if x])
        headers = {'content-type': self.content_headers['resource']} 
        response = requests.post(fhir_query, data=body, headers=headers)
        return response
