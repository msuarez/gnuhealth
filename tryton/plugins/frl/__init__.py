# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2008-2018 Luis Falcon <lfalcon@gnusolidario.org>
#    Copyright (C) 2011-2018 GNU Solidario <health@gnusolidario.org>
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
from tryton.common import MODELACCESS

import gettext
import gtk
import os
import ssl
import requests

_ = gettext.gettext

class FederationResourceLocator():

    # Callback method to access Thalamus and retrieve the records
    def search_resource(self, widget, *data):
        resource, query, fuzzy_search = data[0].get_text(), \
            data[1].get_text(), data[2].get_active()

        if resource:
            model='gnuhealth.federation.config'
            # Retrieve the connection params for Thalamus
            fconn,=rpc.execute(
                'model', model , 'read',
                [0],
                ['host','port','user','password','ssl', \
                    'verify_ssl'],
                rpc.CONTEXT)

            host, port, user, password, ssl, verify_ssl = \
                fconn['host'], fconn['port'], fconn['user'], \
                fconn['password'], fconn['ssl'], fconn['verify_ssl']

            if (ssl):
                protocol = 'https://'
            else:
                protocol = 'http://'

            url = protocol + host + ':' + str(port)
            res = url + '/' + resource

            if resource == "people":
                res = res + '/' + query

            try:
                conn = requests.get(res,
                    auth=(user, password), verify=verify_ssl)

            except:
                message(_('Unable to connect to Thalamus'))
                return

            if fuzzy_search:
                # Find the federation ID using fuzzy search
                msg = "Coming up"
                message(_(msg))
            else:
                # Find the federation ID using deterministic algorithm
                # (exact match, return at most one record)
                get_data = requests.get(res, params=query,
                    auth=(user, password), verify=verify_ssl)

                if not get_data:
                    not_found_msg = "The ID "+ query +\
                        " does not exist on Federation"
                    message(_(not_found_msg))

                else:
                    #Populate and pack the result
                    r = []
                    fields = ['_id','name', 'lastname', 'gender',
                        'dob', 'phone', 'address']

                    record = get_data.json()

                    for fname in fields:
                        if fname in record.keys():
                            field= record[fname]
                        else:
                            field= ''
                        r.append(field)

                    self.results.append(r)

    def delete_event(self, widget, event, data=None):
        # Generate an destroy signal when closing the window
        return False

    # Quit the application
    def destroy(self, widget, data=None):
        gtk.main_quit()

    # Check if the Federation ID exists in the local Tryton node
    # Looks for any ID (both the PUID and the alternative IDs)
    def check_local_record(self, federation_id):
        model = 'party.party'
        get_record=rpc.execute(
            'model', model , 'search',
            ['OR',
                ("federation_account", "=", federation_id),
                ("ref", "=", federation_id),
                [("alternative_ids", "=", federation_id)],
            ],
            rpc.CONTEXT)
        res = get_record
        return res

    # Get the values from the selection
    def get_values(self, treeview, row, column):
        model = treeview.get_model()
        tree_iter = model.get_iter(row)
        # Get GNU Health Federation ID (column 0)
        federation_id = model.get_value(tree_iter,0)
        if (self.check_local_record (federation_id)):
            already_exists_msg="At least one record exists LOCALLY " \
                "with this ID.\n"
            message(_(already_exists_msg))
        else:
            not_found_locally_msg="The person exists on the Federation" \
                " but not locally...  \n" \
                "Would you like to transfer it ?"
            message (_(not_found_locally_msg))

    def __init__(self):

        self.columns = ["ID","Name","Lastname","Gender","DoB","Phone","Address"]

        icon = os.path.expanduser("~") + \
            '/gnuhealth_plugins/frl/icons/federation.svg'

        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_icon_from_file(icon)

        self.window.connect("delete_event", self.delete_event)
        self.window.connect("destroy", self.destroy)

        # Border and title
        self.window.set_border_width(10)
        self.window.set_title("GNU Health Federation Resource Locator")

        # Entry for the resource (eg, people)
        self.resource = gtk.Entry(max=20)
        self.resource.set_text("people")

        # Entry to find Federation ID or other info when using fuzzy srch
        self.query = gtk.Entry(max=100)

        # Search Button
        self.search_button = gtk.Button(label=None, stock=gtk.STOCK_FIND)

        # Fuzzy search
        self.fuzzy_search = gtk.CheckButton(label="Fuzzy")

        # Call method search_resource upon receiving the clicked signal
        self.search_button.connect("clicked", self.search_resource,
            self.resource, self.query, self.fuzzy_search)

        self.hbox = gtk.HBox (True, 10)
        self.hbox.pack_start (self.resource)
        self.hbox.pack_start (self.query)
        self.hbox.pack_start (self.search_button)
        self.hbox.pack_start (self.fuzzy_search)
        self.resource.show()
        self.query.show()
        self.search_button.show()
        self.fuzzy_search.show()

        self.search_frame = gtk.Frame()
        self.search_frame.add (self.hbox)

        self.main_table = gtk.Table(rows=2, columns=2, homogeneous=False)

        # Create the main tree view for the results
        self.results = gtk.ListStore(str, str, str, str, str, str, str)
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

def frl_main(data):
    frl = FederationResourceLocator()
    args = frl.main()

def get_plugins(model):
    access = MODELACCESS['gnuhealth.federation.config']

    if access['read']:
        return [
            (_('Federation Resource Locator'), frl_main),]
    else:
        print ("Not enough access. Disabling FRL")

