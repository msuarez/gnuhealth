# -*- coding: utf-8 -*-
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
from flask import Flask, request, jsonify, render_template
from flask_restful import Resource, Api
from flask_pymongo import PyMongo

import bcrypt
import logging

app = Flask(__name__)
app.config.from_pyfile('thalamus.cfg')

api = Api(app)

mongo = PyMongo(app)

# People Resource
class People(Resource):
    "Holds the person demographics information"
    def get(self):
        """
        Retrieves all the people on the person collection
        """
        people = list(mongo.db.people.find())

        return jsonify(people)

api.add_resource(People, '/people')


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


@app.route('/login', methods=['GET','POST'])
def login():  
    """
    Login method that takes the user credentials
    and checks against a bcrypt hashed password

    TODO: Needs work to get the roles and avoid passing the
    credentials as arguments
    """
    
    if request.method == 'POST':
        federation_account = request.form['fedaccount']
    
        # Do validation first...
        # id_ : Holds the unique federation account code :
        user = mongo.db.people.find_one({'_id' : federation_account})
        if (user):
            form_password = request.form['password']
            account = mongo.db.people.find_one({'_id' : federation_account})
            person = account['_id']
            hashed_password = account['password']
            if bcrypt.checkpw(form_password.encode('utf-8'), 
                hashed_password.encode('utf-8')):
                msg = "User logged in correctly"
            else:
                msg = "Wrong user or password"
            
            return msg
        else:
           return "Wrong user or password" 
    return render_template('login.html')
    
if __name__ == '__main__':
    app.run()
