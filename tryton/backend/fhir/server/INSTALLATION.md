### Configuration

The server ships with a simple production config file. However, it needs to be edited.

    server/config.py
    ----------------
    TRYTON_DATABASE = ''    # GNU Health database
    SERVER_NAME = ''        # Domain name of the server
    SECRET_KEY = ''         # Set this to a long and random string

There are other options available for Flask and its addons:
* [Flask](http://flask.pocoo.org/docs/0.10/config/)
* [Flask-Login](https://flask-login.readthedocs.org/en/latest/)
* [Flask-Tryton](https://code.google.com/p/flask-tryton/)
* [Flask-Restful](http://flask-restful.readthedocs.org/en/latest/quickstart.html)
* [Flask-WTF](https://flask-wtf.readthedocs.org/en/latest/)

### Running the server

The server ships with a simple script (fhir/run_server.py) to run the server using [Tornado](http://www.tornadoweb.org/en/stable/).

However, most production servers use nginx, lighttpd, or apache in front of the Tornado server. For example, a common practice is to have nginx sit in front of multiple Tornado instances, acting as a load balancer, handling SSL, and serving static content (like images and common javascript). How to configure an nginx/lighttpd + tornado + flask setup is beyond this document, although it is not complicated, especially with nginx.
