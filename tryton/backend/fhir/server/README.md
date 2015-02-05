### Installation

The server requires Flask and a few of its addons. And, of course, a working GNU Health installation. GNU Health needs Python 2.x!

It is recommended to install the packages into a virtual environment using virtualenv.

Setup the environment (as the gnuhealth user):

    $ pip install virtualenv                # Install virtualenv using python (may require root)
    $ cd my_work_folder                     # Wherever you want to put the virtual enviroment folder
    $ virtualenv -p /usr/bin/python2 venv   # Create the environment, with the Python 2.x interpreter
    $ source venv/bin/activate              # Active the environment

Now install the packages:

    $ pip install Flask Flask-Login Flask-Tryton Flask-Restful Flask-WTF        # Flask, and the addons
    $ pip install Tornado psycopg2                                              # HTTP server and database driver
    $ pip install pywebdav vobject qrcode                                       # Various packages required by Tryton
    $ pip install defusedxml                                                    # Safer XML parsing

Some of these packages (like pywebdav) are already installed on the system. However, it's usually easier to administrate and debug the Flask server when working in a virtual environment.

More help with [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/).

### Configuration

The server ships with a simple production config file. However, it needs to be edited.

    server/config.py
    ----------------
    TRYTON_DATABASE = ''    # GNU Health database
    SERVER_NAME = ''        # Domain name of the server (e.g., fhir.example.com)
    SECRET_KEY = ''         # Set this value to a long and random string

There are other options available for Flask and its addons:
* [Flask](http://flask.pocoo.org/docs/0.10/config/)
* [Flask-Login](https://flask-login.readthedocs.org/en/latest/)
* [Flask-Tryton](https://code.google.com/p/flask-tryton/)
* [Flask-Restful](http://flask-restful.readthedocs.org/en/latest/quickstart.html)
* [Flask-WTF](https://flask-wtf.readthedocs.org/en/latest/)

### Security

Use TLS. Sensitive medical information must be protected and confidential.

By default, all FHIR endpoints except the Conformance statement require user authentication. The user authentication and access follows Tryton's model, respecting model and field access rights.

The same credentials used to sign into GNU Health are used to access the FHIR REST server.

### Running the server

The server ships with a simple script (run_server.py) to run the server using [Tornado](http://www.tornadoweb.org/en/stable/).

With the virtual environment activated and as the gnuhealth user, run the server.

    $ python run_server.py

However, most production servers use nginx, lighttpd, or apache in front of the Tornado server. For example, a common practice is to have nginx sit in front of multiple Tornado instances, acting as a load balancer, handling SSL, and serving static content (like images and common javascript). How to configure an nginx/lighttpd + tornado + flask setup is beyond this document, although it is not complicated, especially with nginx.

### Troubleshooting

#### Cannot connect to database

Flask-Tryton should automatically find and parse the Tryton config file. If it is not found:

    server/config.py
    ----------------
    TRYTON_CONFIG = ''      # Set this to the path of the Tryton configuration file (e.g., '/weird/tryton/weird-tryton.conf')
