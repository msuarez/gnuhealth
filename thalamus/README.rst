Thalamus: The GNU Health Message and Authentication Server
==========================================================

The Thalamus project provides a RESTful API hub to all the GNU Health 
Federation nodes. The main functions are:

 # Message server: A concentrator and message relay from and to 
 the participating nodes in the GNU Health Federation and the GNU Health
 Information System (MongoDB). Some of the participating nodes include 
 the GNU Health HMIS (Tryton based), MyGNUHealth mobile PHR application,
 laboratories, research institutions and civil offices.
 
 # Authentication Server : Thalamus also serves as an authentication and
 authorization server to interact with the GNUHealth Information System

Thalamus is part of the GNU Health project, but it is a self contained, 
independent server that can be used in different health related scenarios.


Installation
------------
Thalamus is pip-installable.

    >>> pip install thalamus
 

Technology
----------
RESTful API: Thalamus uses a REST (Representional State Transfer) 
architectural style, powered by 
`Flask <https://en.wikipedia.org/wiki/Flask_(web_framework)>`_ technology

Thalamus will perform CRUD (Create, Read, Update, Delete) operations. They
will be achived via the following methods upon resources and their instances.

 # GET : Read
 
 # POST : Create
 
 # PUT / PATCH : Update
  
 # DELETE : Minimal (or even none)
  

JSON: The information will be encoded in `JSON <https://en.wikipedia.org/wiki/JSON>`_ format.


Resources
---------

Some examples of resources and end-points are:

People (/people)

DomiciliaryUnits (/domiciliary-units)

Institutions (/institutions)

Encounters (/encounters)

Events (/events)

PersonalDocs (/personal-documents)


Running Thalamus from a WSGI Container
--------------------------------------
In production settings, for performance reasons you should use a HTTP server.
We have chosen `Gunicorn <http://gunicorn.org>`_ , but you can use any WSGI server.

Gunicorn supports WSGI natively and it comes as Python package. We have 
included a very simple config file (etc/gunicorn.cfg) to run Thalamus from 
Gunicorn with SSL enabled.

For example, you can run the Thalamus application from Gunicorn as follows

    >>> gunicorn --config etc/gunicorn.cfg thalamus:app


Development
-----------
Thalamus is part of the GNU Health project.

The development will be done on GNU Savannah, using the Mercurial repository.

Tasks, bugs and mailing lists will be on health-dev@gnu.org , for development.

General questions can be done on health@gnu.org mailing list.

You can visit http://health.gnu.org


Release Cycle
-------------
Thalamus will follow its own release process, independent from GNU Health HMIS.


Packaging
---------
There will be a tarball, as well as a Python package (pypi)



:Author: Luis Falcon <lfalcon@gnusolidario.org>
