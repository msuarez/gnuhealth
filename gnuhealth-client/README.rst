The GNU Health GTK Client
=======================================================================

The GTK client allows to connect to the GNU Health server from the
desktop.

Starting from GNU Health version 3.2, you can directly download the
gnuhealth client from GNU.org or pypi.

Installation
------------

For a system-wide installation (you need to be root)

  # pip install gnuhealth-client

Alternatively, you can do a local installation :

  $ pip install --user gnuhealth-client


Technology
----------
The GNU Health GTK client derives from the Tryton GTK client, with specific
features of GNU Health and healthcare sector

GNU Health client series 3.2.x use GTK2+ and Python2 . This is a 
transition series for the upcoming 3.4, that will use GTK3+ and Python3

The default profile
-------------------
The GNU Health client comes with a pre-defined profile, which points to
the GNU Health community demo server 

| Server : health.gnusolidario.org
| Port : 8000
| User : admin
| Passwd : gnusolidario

GNU Health Plugins
------------------
You can download GNU Health plugins for specific functionality.

For example:

* The GNU Health **Crypto** plugin to digitally sign documents using GNUPG
* The GNU Health **Camera** to use cameras and store them directly 
  on the system (person registration, histological samples, etc..)

More information about the GNU Health plugins at :

https://en.wikibooks.org/wiki/GNU_Health/Plugins
  

The GNU Health client configuration file
----------------------------------------
The default configuration file resides in

$HOME/.config/gnuhealth/gnuhealth-client.conf

Using a custom greeter / banner
-------------------------------
You can customize the login greeter banner to fit your institution.

In the section [client] include the banner param with the absolute path
of the png file.

Something like

| [client]
| banner = /home/yourlogin/myhospitalbanner.png

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
http://health.gnu.org


Documentation
-------------
The GNU Health GTK documentation will be at the corresponding
chapter in the GNU Health Wikibook

https://en.wikibooks.org/wiki/GNU_Health
