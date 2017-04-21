# -*- coding: utf-8 -*-
##############################################################################
#
#    Thalamus, the GNU Health Message and Authentication Server
#
#           Thalamus is part of the GNU Health project
#
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2008-2017 Luis Falcon <lfalcon@gnusolidario.org>
#    Copyright (C) 2011-2017 GNU Solidario <health@gnusolidario.org>
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
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_pymongo import PyMongo
from flask_httpauth import HTTPBasicAuth
import json
import bcrypt

import logging

__all__ = ["People","Person"]

app = Flask(__name__)
app.config.from_pyfile('etc/thalamus.cfg')

api = Api(app)

mongo = PyMongo(app)

auth = HTTPBasicAuth()

ACL = json.load(open(app.config['ACL'],'r'))

# Authentication

@auth.verify_password
def verify_password(username, password):
    """
    Takes the username and password from the client
    and checks them against the entry on the people db collection
    The password is bcrypt hashed
    """ 
    user = mongo.db.people.find_one({'_id' : username})
    if (user):
        account = mongo.db.people.find_one({'_id' : username})
        person = account['_id']
        hashed_password = account['password']
        roles = account['roles']
        if bcrypt.checkpw(password.encode('utf-8'), 
            hashed_password.encode('utf-8')):
            """ Authentication OK
            Now check the access level for the resource
            """
            method = request.method
            endpoint = request.endpoint
            view_args = request.view_args
            return access_control(username,roles, method, endpoint, view_args)
                
        else:
            return False
        
    else:
       return False



# Authorization
def access_control(username, roles, method, endpoint, view_args):
    """
    Takes the logged in user roles, method and endpoint as arguments
    Verifies them against the ACL and returns either True or False
    """
    for user_role in roles:
        for acl_entry in ACL:
            if (acl_entry["role"] == user_role):
                actions = acl_entry["permissions"]
                if (endpoint in actions[method]):
                    """Check if the method allows to access the endpoint"""
                    if view_args:
                        """If there are arguments (eg, person_id), check 
                            whether the user role has global access
                            or just can see his/her records"""
                        if (username == view_args["person_id"] or
                            actions["global"] == "True"):
                                return True
                    else:
                        return True
    return False
        
# People Resource
class People(Resource):
    "Holds the person demographics information"
    
    decorators = [auth.login_required] # Use the decorator from httpauth
    def get(self):
        """
        Retrieves all the people on the person collection
        """
        
        people = list(mongo.db.people.find())

        return jsonify(people)

# Person 
class Person(Resource):
    "Holds the person demographics information"
    
    decorators = [auth.login_required] # Use the decorator from httpauth
    def get(self, person_id):
        """
        Retrieves the person instance 
        """
        person = mongo.db.people.find_one({'_id' : person_id})

        return jsonify(person)


api.add_resource(People, '/people') #Add resource for People

api.add_resource(Person, '/people/<person_id>') #Add person instance


# Personal Documents resource
class PersonalDocs(Resource):
    "Documents associated to the person (scanned info, birth certs, ..)"
    def get(self):
        documents = list(mongo.db.personal_document.find())
        return jsonify(documents)

api.add_resource(PersonalDocs, '/personal-documents')

# Domiciliary Units resource
class DomiciliaryUnits(Resource):
    "Domiciliary Units"
    def get(self):
        dus = list(mongo.db.domiciliary_unit.find())
        return jsonify(dus)

api.add_resource(DomiciliaryUnits, '/domiciliary-units')

# Health Encounters resource
class Encounters(Resource):
    "Events related to person"
    def get(self):
        events = list(mongo.db.encounter.find())
        return jsonify(encounters)

api.add_resource(Encounters, '/encounters')

# Vital signs, anthropometrics and other measurements
class Measurements(Resource):
    "Vital signs and anthropometrics"
    def get(self):
        events = list(mongo.db.measurements.find())
        return jsonify(measurements)

api.add_resource(Measurements, '/measurements')


# Hospitalizations resource
class Hospitalizations(Resource):
    "Hospitalization history"
    def get(self):
        hospitalizations = list(mongo.db.hospitalization.find())
        return jsonify(hospitalizations)

api.add_resource(Hospitalizations, '/hospitalizations')

    
if __name__ == '__main__':
    app.run()
