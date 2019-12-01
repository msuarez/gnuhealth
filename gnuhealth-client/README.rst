The GNU Health GTK Client
=======================================================================

The GTK client allows to connect to the GNU Health HMIS server from the
desktop.


Installation
------------
You can install the GNU Health HMIS client via pip::

 $ pip3 install --user --upgrade gnuhealth-client


Technology
----------
The GNU Health GTK client is a Python 3 application that derives from the Tryton GTK client, with specific
features of GNU Health and healthcare sector.

The default profile
-------------------
The GNU Health client comes with a pre-defined profile, which points to
the GNU Health community demo server::

 Server : federation.gnuhealth.org
 Port : 8000
 User : admin
 Passwd : gnusolidario


GNU Health Plugins
------------------
You can download GNU Health plugins for specific functionality.

For example:

* The GNU Health **Crypto** plugin to digitally sign documents using GNUPG
* The GNU Health **Camera** to use cameras and store them directly 
  on the system (person registration, histological samples, etc..)
* The **Federation Record Locator**, that communicates with **thalamus**
  and interacts with the GNU Health Information System and Person Master Index.

More information about the GNU Health plugins at :

https://en.wikibooks.org/wiki/GNU_Health/Plugins
  

The GNU Health client configuration file
----------------------------------------
The default configuration file resides in::

 $HOME/.config/gnuhealth/<version>/gnuhealth-client.conf

Using a custom greeter / banner
-------------------------------
You can customize the login greeter banner to fit your institution.

In the section [client] include the banner param with the absolute path
of the png file.

Something like::

 [client]
 banner = /home/yourlogin/myhospitalbanner.png

The default resolution of the banner is 500 x 128 pixels. Adjust yours
to approximately this size.

Development
-----------
The development of the GNU Health client will be done on GNU Savannah, 
using the Mercurial repository.

Tasks, bugs and mailing lists will be on health-dev@gnu.org , for development.

General questions can be done on health@gnu.org mailing list.

Homepage
--------
https://www.gnuhealth.org


Documentation
-------------
The GNU Health GTK documentation will be at the corresponding
chapter in the GNU Health Wikibook

https://en.wikibooks.org/wiki/GNU_Health
