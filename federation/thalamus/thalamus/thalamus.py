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
#    Copyright (C) 2008-2018 Luis Falcon <lfalcon@gnusolidario.org>
#    Copyright (C) 2011-2018 GNU Solidario <health@gnusolidario.org>
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
from flask_restful import Resource, Api, abort
from flask_pymongo import PyMongo
from flask_httpauth import HTTPBasicAuth
import json
from ast import literal_eval
import bcrypt
import logging

__all__ = ["People","Person"]

app = Flask(__name__)
app.config.from_pyfile('etc/thalamus.cfg')

api = Api(app)

mongo = PyMongo(app)

auth = HTTPBasicAuth()

ACL = json.load(open(app.config['ACL'],'r'))

def check_person(person_id):
    """
    Checks if the Federation ID exists on the GNU Health HIS
    Returns the instance or null
    """
    person = mongo.db.people.find_one({'_id' : person_id})

    return person

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
        # account = mongo.db.people.find_one({'_id' : username})
        person = user['_id']
        hashed_password = user['password']
        roles = user['roles']
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

    def post(self, person_id):
        """
        Create a new instance on the Person resource 
        Initially just the Federation ID and the bcrypted
        hashed password
        """
        if check_person(person_id):
            abort (422, error="User already exists")

        pw = request.args.get('password',type=str)
        if (request.args.get('active') == "True"):
            active= True
        else:
            active= False

        roles = request.args.getlist('roles')

        if (pw):
            if (len(pw) > 64):
                abort (422, error="Password is too long")

            hashed_pw = bcrypt.hashpw(pw.encode('utf-8'), 
                    bcrypt.gensalt())
            person = mongo.db.people.insert({'_id' : person_id,
                'password' : hashed_pw.decode('utf-8'),
                'roles' : roles,
                'active' : active})
            return jsonify(person)

        else:
            abort (422, error="No password provided")

    def patch(self, person_id):
        """
        Updates the person instance 
        """

        # Convert from bytes to dictionary the information
        # coming from the node (Python Requests library)
        values = literal_eval(request.data.decode())

        if '_id' in values:
            # Avoid changing the user ID
            abort(422, error="Not allowed to change the person ID")
            # TO be discussed...
            # Check if the new ID exist in the Federation, and if it
            # does not, we may be able to update it.
            
        if check_person(person_id): 
            update_person = mongo.db.people.update_one({"_id":person_id},
                {"$set": values})
        else:
            abort (404, error="User not found")

    def delete(self, person_id):
        """
        Delete the user instance. This will be 
        used in exceptional cases only, and the 
        instance must be inactive.
        """
        person = check_person(person_id)
        if not person:
            abort (404, error="User does not exist")

        else:
           if person['active']:
            abort (422, error="The user is active.") 

        delete_person = mongo.db.people.delete_one({"_id":person_id})
 
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

# Institutions resource
class Institutions(Resource):
    "Health and other institutions"
    
    decorators = [auth.login_required] # Use the decorator from httpauth

    def get(self):
        institutions = list(mongo.db.institution.find())
        return jsonify(institutions)

api.add_resource(Institutions, '/institutions')


if __name__ == '__main__':
    app.run()
