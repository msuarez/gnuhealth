# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2008-2017 Luis Falcon <lfalcon@gnusolidario.org>
#    Copyright (C) 2011-2017 GNU Solidario <health@gnusolidario.org>
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
import os
import ssl

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

_ = gettext.gettext

class FederationResourceLocator():

    # Callback method to access MongoDB and retrieve the records
    def search_resource(self, widget, *data):
        resource, fuzzy_search = data[0].get_text(), data[1].get_active()
        
        if resource:
            model='gnuhealth.federation.config'
            # Retrieve the connection params for MongoDB
            fconn=rpc.execute(
                'model', model , 'read',
                [0],
                ['host','port','database','user','password','ssl'],
                rpc.CONTEXT)
            fconn = fconn[0]
        
            host, port, database, user, password, ssl_conn = fconn['host'],\
                fconn['port'], fconn['database'], fconn['user'], \
                fconn['password'], fconn['ssl']
            
            
            dbconn = MongoClient(host, port, ssl=ssl_conn, \
                ssl_cert_reqs=ssl.CERT_NONE)
            
            db = dbconn[database]
            
            # Use the Demographics collection
            demographics = db.demographics
            
            try:
                auth = db.authenticate(user, password)
      
            except:
                warning("ERROR authenticating to Server")
            
            if fuzzy_search:
                # Find the federation ID using fuzzy search
                msg = "Coming up"
                message(_(msg))
                
            else:
                # Find the federation ID using deterministic algorithm
                # (exact match, return at most one record)

                record = demographics.find_one({'_id':resource})
            
                if not record:
                    not_found_msg = "The ID "+ resource +\
                        " does not exist on Federation"
                    message(_(not_found_msg))
                
                else:
                    fed_id, name, gender, dob, phone, address = \
                        record["_id"], \
                        record["name"], record["gender"], record["dob"], \
                        record["phone"], record["address"]
                        
                    self.results.append([fed_id,name,gender,dob,phone,address])
            

    def delete_event(self, widget, event, data=None):
        # Generate an destroy signal when closing the window
        return False

    # Quit the application
    def destroy(self, widget, data=None):
        gtk.main_quit()
        
    # Get the values from the selection
    def get_values(self, treeview, row, column):
        model = treeview.get_model()
        tree_iter = model.get_iter(row)
        # Get GNU Health Federation ID (column 0)
        federation_id = model.get_value(tree_iter,0)
        
    def __init__(self):
        
        self.columns = ["ID","Name","Gender","DoB","Phone","Address"]

        icon = os.path.expanduser("~") + \
            '/gnuhealth_plugins/frl/icons/gnuhealth_icon.svg'

        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_icon_from_file(icon)

        self.window.connect("delete_event", self.delete_event)
        self.window.connect("destroy", self.destroy)
    
        # Border and title
        self.window.set_border_width(10)
        self.window.set_title("GNU Health Federation Resource Locator")
    
        # Entry to find Federation ID or other info when using fuzzy srch
        self.resource = gtk.Entry(max=100)
        
        # Search Button
        self.search_button = gtk.Button(label=None, stock=gtk.STOCK_FIND)

        # Fuzzy search
        self.fuzzy_search = gtk.CheckButton(label="Fuzzy")
    
        # Call method search_resource upon receiving the clicked signal
        self.search_button.connect("clicked", self.search_resource,
            self.resource, self.fuzzy_search)
    
        
        self.hbox = gtk.HBox (True, 10)
        
        self.hbox.pack_start (self.resource)
        self.hbox.pack_start (self.search_button)
        self.hbox.pack_start (self.fuzzy_search)

        self.resource.show()
        self.search_button.show()
        self.fuzzy_search.show()

        self.search_frame = gtk.Frame()
        self.search_frame.add (self.hbox)
        
        
        self.main_table = gtk.Table(rows=2, columns=2, homogeneous=False)

        # Create the main tree view for the results
        self.results = gtk.ListStore(str, str, str, str, str, str)
        self.treeview = gtk.TreeView(self.results)

        # Let pick at most one row
        self.treeselection = self.treeview.get_selection ()
        self.treeselection.set_mode (gtk.SELECTION_SINGLE)
        
        # Process once the row is activated (double-click or enter)
        self.treeview.connect('row-activated', self.get_values)
        
        
        
        # Add and render the columns
        for n in range(len(self.columns)):
            self.cell = gtk.CellRendererText()
            self.col = gtk.TreeViewColumn(self.columns[n], self.cell, text=n)
            self.treeview.append_column(self.col)

        # attach the query box on the table
        self.main_table.attach(self.search_frame,0,1,0,1)

        # attach the query box on the table
        self.main_table.attach(self.treeview,0,1,1,2)
        
        self.window.add (self.main_table)
        
        # Display the objects
        self.hbox.show()
        self.search_frame.show()
        self.treeview.show()
        self.main_table.show()
        self.window.show()

        
    def main(self):
        gtk.main()


def frl_main(tdata):
    
    frl = FederationResourceLocator()
    args = frl.main()

def get_plugins(model):
    return [
        (_('Federation Resource Locator'), frl_main),
    ]
