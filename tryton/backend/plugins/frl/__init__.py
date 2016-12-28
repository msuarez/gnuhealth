# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2008-2016 Luis Falcon <lfalcon@gnusolidario.org>
#    Copyright (C) 2011-2016 GNU Solidario <health@gnusolidario.org>
#
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

import tryton.rpc as rpc
from tryton.common import RPCExecute, warning, message
from tryton.gui.window.form import Form
import gettext
import gtk

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure


_ = gettext.gettext

class FederationResourceLocator():

    # Callback method to access MongoDB and retrieve the records
    def search_resource(self, widget, data):
        resource = data.get_text()
        if resource:
            model='gnuhealth.federation.config'
            # Retrieve the connection params for MongoDB
            fconn=rpc.execute(
                'model', model , 'read',
                [0],
                ['host','port','database','user','password','ssl'],
                rpc.CONTEXT)
            fconn = fconn[0]
        return
        
    def delete_event(self, widget, event, data=None):
        # Generate an destroy signal when closing the window
        return False

    # Quit the application
    def destroy(self, widget, data=None):
        gtk.main_quit()
        
    def __init__(self):

        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
    
        self.window.connect("delete_event", self.delete_event)
    
        self.window.connect("destroy", self.destroy)
    
        # Border and title
        self.window.set_border_width(10)
        self.window.set_title("GNU Health Federation Resource Locator")
    
        # Entry to find Federation ID
        self.person_id = gtk.Entry(max=30)
        
        # Search Button
        self.search_button = gtk.Button(label=None, stock=gtk.STOCK_FIND)
    
        # Call method search_resource upon receiving the clicked signal
        self.search_button.connect("clicked", self.search_resource, self.person_id)
    
        self.hbox = gtk.HBox (True, 10)
        
        self.hbox.pack_start (self.person_id)
        self.hbox.pack_start (self.search_button)

        self.person_id.show()
        self.search_button.show()
    
        self.window.add (self.hbox)
        
        # Display the objects
        self.hbox.show()
        self.window.show()

    def main(self):
        gtk.main()


def frl_main(tdata):
    print (tdata)
    
    frl = FederationResourceLocator()
    args = frl.main()

def get_plugins(model):
    return [
        (_('Federation Resource Locator'), frl_main),
    ]
