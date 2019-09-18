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
#    Copyright (C) 2008-2019 Luis Falcon <falcon@gnuhealth.org>
#    Copyright (C) 2011-2019 GNU Solidario <health@gnusolidario.org>
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
from flask import Flask, redirect, request, jsonify, render_template, url_for
from flask_restful import Resource, Api, abort
from flask_cors import CORS

import psycopg2
from psycopg2 import sql

from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, SubmitField, \
    validators

from flask_httpauth import HTTPBasicAuth
import json
import bcrypt
import logging

__all__ = ["People","Person","Book","Page", "Login", "PasswordForm","Password"]

app = Flask(__name__)

# Allow CORS requests from JS frontends, such as the GH Federation Portal
CORS(app)

app.config.from_pyfile('etc/thalamus.cfg')

api = Api(app)

auth = HTTPBasicAuth()

ACL = json.load(open(app.config['ACL'],'r'))

# Use Gunicorn logging system when Thalamus is run through it
# use the gunicorn argument --log-level to specify the starting
# level of the application (eg, --log-level=debug)
if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)


#Open a connection to PG Server
conn = psycopg2.connect(app.config['POSTGRESQL_URI'])

def check_id(table, resid):
    """
    Checks if the Federation ID exists on the GNU Health HIS
    Returns the instance or null
    """
    cur = conn.cursor()
    cur.execute (
        sql.SQL("SELECT id from {} where id = %s limit(1)").format(sql.Identifier(table)), \
            (resid,))
    try:
        res, = cur.fetchone()
    except:
        res = None

    return res

# Authentication

@auth.verify_password
def verify_password(username, password):
    """
    Takes the username and password from the client
    and checks them against the entry on the people db collection
    The password is bcrypt hashed
    """
    cur = conn.cursor()
    cur.execute ('SELECT data from people \
        where id = %s limit(1)', (username,))
    try:
        user, = cur.fetchone()
    except:
        user = None

    if (user):
        person = user['id']
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
    """Collection resource for demographic information"""

    decorators = [auth.login_required] # Use the decorator from httpauth
    def get(self):
        """
        Retrieves all the people on the person collection
        """
        cur = conn.cursor()
        cur.execute ('SELECT data from people')
        people = cur.fetchall()

        return jsonify(people)

# Person
class Person(Resource):
    """Class that manages the person demographics.
    """

    decorators = [auth.login_required] # Use the decorator from httpauth

    def get(self, person_id):
        """
        Retrieves the person instance
        """
        cur = conn.cursor()
        cur.execute ('SELECT data from people \
            where id = %s limit(1)', (person_id,))

        try:
            person, = cur.fetchone()
        except:
            person = None

        # Return a 404 if the person ID is not found
        if not person:
            return '', 404

        return jsonify(person)

    def post(self, person_id):
        """
        Create a new instance on the Person resource
        Initially just the Federation ID and the bcrypted
        hashed password
        """

        #Grab the data coming from the client, in JSON format
        values = json.loads(request.data)

        # Initialize to inactive the newly created person
        #values['active'] = False
        pw = None

        bcrypt_prefixes = ["$2b$", "$2y$"]

        if check_id('people', person_id):
            abort (422, error="User already exists")

        if (person_id):
            if (type(person_id) is str):
                #Use upper case on the person federation account
                person_id = person_id.upper()
                values['id'] = person_id
        else:
            abort (422, error="wrong format on person ID")

        #If no roles are supplied, assign "end_user"
        if not ('roles' in values.keys()):
            values['roles'] = ["end_user"]


        if ('password' in values.keys()):
            pw = values['password']

        if (pw):
            if (len(pw) > 64):
                abort (422, error="Password is too long")

            # Check if the password is already in bcrypt format
            if (pw[0:4] in bcrypt_prefixes):
                hashed_pw = pw
            else:
                hashed_pw = (bcrypt.hashpw(pw.encode('utf-8'),
                    bcrypt.gensalt())).decode('utf-8')

            values['password'] = hashed_pw

        # Insert the newly created person
        cur = conn.cursor()
        cur.execute("INSERT INTO people (ID, DATA) VALUES (%(id)s, \
            %(data)s)", {'id': person_id, 'data':json.dumps(values)})
        res = conn.commit()

        return res


    def patch(self, person_id):
        """
        Updates the person instance
        """

        #Grab all the data coming from the node client, in JSON format
        values = json.loads(request.data)

        if 'id' in values:
            # Avoid changing the user ID
            print ("Not allowed to change the person ID")
            abort(422, error="Not allowed to change the person ID")
            # TO be discussed...
            # Check if the new ID exist in the Federation, and if it
            # does not, we may be able to update it.

        if check_id('people',person_id):
            jdata = json.dumps(values)
            # UPDATE the information from the person
            # associated to the federation ID
            cur = conn.cursor()
            cur.execute("UPDATE PEOPLE SET data = data || %s where id = %s", \
                (jdata,person_id))
            conn.commit()

        else:
            abort (404, error="User not found")

    def delete(self, person_id):
        """
        Delete the user instance. This will be
        used in exceptional cases only, and the
        instance must be inactive.
        """
        person = check_id('people', person_id)
        if not person:
            abort (404, error="User does not exist")

        else:
           if person['active']:
            abort (422, error="The user is active.")

        #Delete the person
        cur = conn.cursor()
        cur.execute("DELETE FROM people WHERE id = %s", (person_id,))
        conn.commit()

# Book of Life Resource
class Book(Resource):
    """Collection resource for a person life information"""

    decorators = [auth.login_required] # Use the decorator from httpauth

    def get(self, person_id):
        """
        Retrieves the pages of life from the person
        """
        cur = conn.cursor()
        cur.execute ('SELECT data from pols where book = %s', (person_id,))
        pages = cur.fetchall()

        return jsonify(pages)


        # Return a 404 if the person ID is not found
        if not pages:
            return '', 404

        return jsonify(pages)


# Page of Life
class Page(Resource):
    """Information and events that make and shape a person life"""

    decorators = [auth.login_required] # Use the decorator from httpauth

    def get(self, person_id, page_id):
        """
        Retrieves the page instance
        """
        cur = conn.cursor()
        cur.execute ('SELECT data from pols \
            where id = %s limit(1)', (page_id,))
        try:
            page, = cur.fetchone()
        except:
            page = None


        # Return a 404 if the page ID is not found
        if not page:
            abort (404, error="Book or page or not found")

        return jsonify(page)

    def post(self, person_id, page_id):
        """
        Create a new instance on the Page resource
        """
        #Grab the data coming from the client, in JSON format
        values = json.loads(request.data)

        # Basic validation on page ID exsistance and string type
        if (person_id and 'id' in values):
            if (type(person_id) is str and type(values['id'])):

                # Insert the newly created Page of Life from the person Book
                cur = conn.cursor()
                cur.execute("INSERT INTO pols (ID, BOOK, DATA) \
                    VALUES (%(id)s, %(book)s, %(data)s)", \
                    {'id': page_id, 'book': person_id, \
                    'data':json.dumps(values)})
                res = conn.commit()

        else:
            print ("wrong format on person or page ID")
            abort (422, error="wrong format on person or page ID")

        return jsonify(res)

    def patch(self, person_id, page_id):
        """
        Updates the Page of Life
        """
        #Grab all the data coming from the node client, in JSON format
        values = json.loads(request.data)

        if 'id' in values:
            # Avoid changing the page ID
            abort(422, error="Not allowed to change the page ID")

        if check_id('pols',page_id):

            jdata = json.dumps(values)
            # UPDATE the information from the page
            # associated to the federation ID book
            cur = conn.cursor()
            cur.execute("UPDATE pols SET data = data || %s where id = %s", \
                (jdata,page_id))
            conn.commit()

        else:
            abort (404, error="Page not found")

# Add resources and endpoints
# The endpoints are the class names in lower case (eg, people, life, page...)

#People and person
api.add_resource(People, '/people') #Add resource for People
api.add_resource(Person, '/people/<string:person_id>') #Add person instance

#Book and pages of life resources (in pols collection)
api.add_resource(Book, '/pols/<string:person_id>')
api.add_resource(Page, '/pols/<string:person_id>/<string:page_id>')

# Personal Documents resource
class PersonalDocs(Resource):
    "Documents associated to the person (scanned info, birth certs, ..)"

    decorators = [auth.login_required] # Use the decorator from httpauth

    def get(self, person_id):
        """
        Retrieves the documents of a person
        """
        cur = conn.cursor()
        cur.execute ('SELECT fedacct, pol, data, document from personal_docs \
            where fedacct = %s', (person_id,))
        documents = cur.fetchall()

        return jsonify(documents)

api.add_resource(PersonalDocs, '/personal_docs/<string:person_id>')

# Documents associated to a Page of Life
class PolDocs(Resource):
    "Documents associated to the person in the context of a Page of Life"

    decorators = [auth.login_required] # Use the decorator from httpauth

    def get(self, person_id, pol_id):
        """
        Retrieves the documents of a person
        """
        cur = conn.cursor()
        cur.execute ('SELECT fedacct, pol, data, document from personal_docs \
            where fedacct = %s', (person_id,pol_id))
        documents = cur.fetchall()

        return jsonify(documents)

api.add_resource(PolDocs, '/personal_docs/<string:person_id>/<string:pol_id>')

# Domiciliary Units resource
class DomiciliaryUnits(Resource):
    "Domiciliary Units"

    decorators = [auth.login_required] # Use the decorator from httpauth

    def get(self):
        """
        Retrieves the Domiciliary Units
        """
        cur = conn.cursor()
        cur.execute ('SELECT data from dus')
        dus = cur.fetchall()

        return jsonify(dus)

api.add_resource(DomiciliaryUnits, '/domiciliary-units')


# Institutions resource
class Institutions(Resource):
    "Health and other institutions"

    decorators = [auth.login_required] # Use the decorator from httpauth
    def get(self):
        """
        Retrieves the Institutions
        """
        cur = conn.cursor()
        cur.execute ('SELECT data from institutions')
        institutions = cur.fetchall()

        return jsonify(institutions)

api.add_resource(Institutions, '/institutions')

# Login 
class Login(Resource):
    """"
    Main class for loggin in from another resources, such the GH Federation Portal
    At this point, with the decorator auth.login_required is enough
    """
    
    decorators = [auth.login_required] # Use the decorator from httpauth

    def get(self):
        return True 

api.add_resource(Login, '/login')



class PasswordForm(FlaskForm):
    password = PasswordField('Password',
        validators=[validators.DataRequired(),
        validators.Length(min=6, max=30),
        validators.EqualTo('pconfirm', message='Password mistmatch')])
    pconfirm = PasswordField('Confirm Password')
    update = SubmitField('Update')

# Update the password of the user with a form
@app.route('/password/<person_id>', methods=('GET', 'POST'))
@auth.login_required
def password(person_id):
    error = None
    form = PasswordForm()
    if (request.method == 'POST' and form.validate()):
            pwd = form.password.data.encode()
            enc_pwd = bcrypt.hashpw(pwd, bcrypt.gensalt()).decode()
            values = {'password': enc_pwd}

            jdata = json.dumps(values)
            # UPDATE the information from the person
            # associated to the federation ID 
            cur = conn.cursor()
            cur.execute("UPDATE PEOPLE SET data = data || %s where id = %s", \
                (jdata,person_id))
            update_password = cur.rowcount
            conn.commit()

            if update_password > 0:
                return redirect(url_for('index'))
            else:
                error = "Error updating the password"
    return render_template('password.html', form=form, \
        fed_account=person_id, error=error)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.logger.warning("Running Thalamus without gunicorn ...")
    app.run()
