Thalamus: The GNU Health message and Authentication server
==========================================================

The Thalamus project will provide a hub to all the GNU Health Federation
nodes. The main functions will be:

 # Message server: A concentrator and message relay from and to 
 the participating nodes in the GNU Health Federation and the GNU Health
 Information System (MongoDB). Some of the participating nodes include 
 the GNU Health HMIS (Tryton based), MyGNUHealth mobile PHR application,
 laboratories, research institutions and civil offices, to name a few
 possibilities.

 # Authentication Server : Thalamus will provide an authentication server
 to interact with the GNUHealth Information System

It will also provide a way to query the status of the Federation. 
Current connected nodes, type of nodes, workload, logs, ...

Thalamus will provides a common way to interconnect the heterogeneous
- both from the technical and functional aspects -, nodes within the 
GNU Health federation. 

Technology
----------
 RESTful API: Thalamus uses a REST (Representional State Transfer) 
 architectural style, powered by Flask technology (Flask_(web_framework)_)

 Thalamus will perform CRUD (Create, Read, Update, Delete) operations. They
 will be achived via the following methods upon resources and their instances.

 # GET : Read 
 # POST : Create 
 # PUT / PATCH : Update
 # DELETE : Minimal (or even none)

 JSON: The information will be encoded in JSON_ format.
 

Main resources
--------------

This is work in progress. Some initial resources and end-points

People (/people)

DomiciliaryUnits (/domiciliary-units)

Institutions (/institutions)
 
Encounters (/encounters)

Events (/events)

PersonalDocs (/personal-documents)


Development
-----------
Thalamus is part of the GNU Health project. 

The development will be done on GNU Savannah, using the Mercurial repository.

Tasks, bugs and mailing lists will be on health-dev@gnu.org , for development.

General questions can be done on health@gnu.org mailing list.


Release Cycle
-------------
Thalamus will follow its own release process, independent from GNU Health HMIS.


Packaging
---------
There will be a tarball, as well as a Python package.

