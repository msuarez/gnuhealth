# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2008-2019 Luis Falcon <lfalcon@gnusolidario.org>
#    Copyright (C) 2011-2019 GNU Solidario <health@gnusolidario.org>
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
from tryton.common import RPCExecute, warning, message, sur
from tryton.gui.window.form import Form
from tryton.common import MODELACCESS
from gi.repository import Gtk

import gettext
import os
import ssl
import requests

_ = gettext.gettext

class FederationResourceLocator():
    # Import person information from Federation

    # Map the resource with the local model
    modinfo = {'people':'party.party'}

    # Callback method to access Thalamus and retrieve the records
    def search_resource(self, widget, *data):
        resource, query, fuzzy_search = data[0].get_text(), \
            data[1].get_text(), data[2].get_active()

        query = query.upper()
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
                self.federation_data = requests.get(res, params=query,
                    auth=(user, password), verify=verify_ssl)

                if not self.federation_data:
                    not_found_msg = "The ID "+ query +\
                        " does not exist on Federation"
                    message(_(not_found_msg))

                else:
                    #Cleanup the results liststore at every search
                    self.results.clear()

                    #Populate and pack the result
                    r = []
                    fields = ['id','name', 'lastname', 'gender',
                        'dob', 'phone', 'address']

                    record = self.federation_data.json()

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
        Gtk.main_quit()

    def create_local_record(self, model, values):
        # Create local record from the information
        # gathered from the Federation
        create_local =rpc.execute(
            'model', model , 'create',
            [values],
            rpc.CONTEXT)
        return create_local


    def update_local_record(self, model, local_record, values):
        # Update local record from the information
        # gathered from the Federation

        update_local =rpc.execute(
            'model', model , 'write', local_record,
            values,
            rpc.CONTEXT)
        return update_local

    # Check if the Federation ID exists in the local node
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

    def set_local_data(self,local_model, fed_data):
        # Retrieve the fields mapping from the federation
        # resource and local model.

        model_fields = \
            rpc.execute('model', 'gnuhealth.federation.object', \
            'get_object_fields',local_model,rpc.CONTEXT)

        if (model_fields):
            #Remove spaces and newlines from fields
            model_fields = model_fields.replace(" ","").replace("\n","")

        #Initialize dictionary values for model-specific fields
        #needed locally only.
        if local_model == 'party.party':
            local_vals = {'federation_account':fed_data['id'], 'is_person':True}

        local_vals['fsync'] = False
        field_mapping = model_fields.split(',')
        resources = []
        fedvals = []
        fed_key = {}
        n=0
        for val in field_mapping:
            #Retrieve the field name, the federation resource name
            #and the associated federation resource field .
            #string of the form field:fed_resource:fed_field
            field, fed_resource, fed_field = val.split(':')

            local_vals[field] = fed_data[fed_field]
        return local_vals

    # Get the values from the selection on the FRL list view
    def get_values(self, treeview, row, column):
        treemod = treeview.get_model()
        tree_iter = treemod.get_iter(row)
        # Get GNU Health Federation ID (column 0)
        federation_id = treemod.get_value(tree_iter,0)

        #Federation Resource name
        resource = self.resource.get_text()

        #local model associated to federation resource
        model = self.modinfo[resource]

        local_vals = self.set_local_data(model,
            self.federation_data.json())

        local_record = self.check_local_record (federation_id)
        if (local_record):
            already_exists_msg= \
                "A record exists LOCALLY with this ID \n\n" \
                "Would you like to update it \n" \
                "with the data from the Federation ?"

            resp_update = sur (_(already_exists_msg))
            # Create the record locally from the information
            # retrieved from the Federation
            if (resp_update):
                local_record = \
                    self.update_local_record (model, local_record, local_vals)

        else:
            not_found_locally_msg= \
                "The person exists on the Federation" \
                " but not locally...  \n" \
                "Would you like to transfer it ?"
            resp_create = sur (_(not_found_locally_msg))

            # Create the record locally from the information
            # retrieved from the Federation
            if (resp_create):
                local_record = self.create_local_record (model, local_vals)

    def __init__(self):

        self.columns = ["ID","Name","Lastname","Gender","DoB","Phone","Address"]

        icon = os.path.join(os.path.dirname(os.path.realpath(__file__)), \
                            "icons/federation.svg")

        self.window = Gtk.Window(Gtk.WindowType.TOPLEVEL)
        self.window.set_icon_from_file(icon)

        self.window.connect("delete_event", self.delete_event)
        self.window.connect("destroy", self.destroy)

        # Border and title
        self.window.set_border_width(10)
        self.window.set_title("GNU Health Federation Resource Locator")

        # Entry for the resource (eg, people)
        self.resource = Gtk.Entry()
        self.resource.set_max_length(30)

        self.resource.set_text("people")

        # Entry to find Federation ID or other info when using fuzzy srch
        self.query = Gtk.Entry()
        self.query.set_max_length(100)

        # Search Button
        self.search_button = Gtk.Button(stock=Gtk.STOCK_FIND)
        self.search_button.set_label("Search")

        # Fuzzy search
        self.fuzzy_search = Gtk.CheckButton(label="Fuzzy")

        # Call method search_resource upon receiving the clicked signal
        self.search_button.connect("clicked", self.search_resource,
            self.resource, self.query, self.fuzzy_search)

        self.hbox = Gtk.HBox (True, 10)
        self.hbox.pack_start (self.resource,
                              expand=False, fill=False, padding=0)
        self.hbox.pack_start (self.query,
                              expand=False, fill=False, padding=0)
        self.hbox.pack_start (self.search_button,
                              expand=False, fill=False, padding=0)
        self.hbox.pack_start (self.fuzzy_search,
                              expand=False, fill=False, padding=0)
        self.resource.show()
        self.query.show()
        self.search_button.show()
        self.fuzzy_search.show()

        self.search_frame = Gtk.Frame()
        self.search_frame.add (self.hbox)

        self.main_table = Gtk.Table(rows=2, columns=2, homogeneous=False)

        # Create the main tree view for the results
        self.results = Gtk.ListStore(str, str, str, str, str, str, str)
        self.treeview = Gtk.TreeView(self.results)

        # Let pick at most one row
        self.treeselection = self.treeview.get_selection()
        self.treeselection.set_mode(Gtk.SelectionMode(1))
        # Process once the row is activated (double-click or enter)
        self.treeview.connect('row-activated', self.get_values)

        # Add and render the columns
        for n in range(len(self.columns)):
            self.cell = Gtk.CellRendererText()
            self.col = Gtk.TreeViewColumn(self.columns[n], self.cell, text=n)
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
        Gtk.main()

def frl_main(data):
    frl = FederationResourceLocator()
    args = frl.main()

def get_plugins(model):
    return [
        (_('Federation Resource Locator'), frl_main),
        ]
