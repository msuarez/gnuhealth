#!/usr/bin/env python

##############################################################################
#
#    T-Logon Manager
#    Copyright (C) 2006-2014  Luis Falcon <falcon@gnu.org>
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


""" Program : tlogon

T-Logon Manager 

Description: Tlogon is a single point of entry to multiple Tryton instances 
( Development - QA - Training - Production, ...).

Initially, Tlogon was "T"inyERP Logon, now "T"ryton Logon .

"""

#The tryton client program name
TRYTON = "tryton"

import pygtk
pygtk.require('2.0')
import gtk
import os, sys
from xml.dom import minidom, Node

def getnode(node):
    leaf = {}
    attribs = []
    if node.nodeType == Node.ELEMENT_NODE:
        for (name,value) in node.attributes.items():
                leaf [name] = value
    return leaf 

def parse_tlogonrc (init_tlogon):
    instance_values = []
    doc = minidom.parseString(init_tlogon)
    node = doc.documentElement
    getnode(node)

    for child in node.childNodes:
        contents = getnode(child)
        if len (contents) > 0:
            attribs = [contents["id"],contents["description"],
            contents["appserver"],contents["port"],
            contents["url"],contents["role"]]
            instance_values.append (attribs)
    return instance_values


def init_tlogonrc ():
    ''' Checks whether $HOME/.tlogonrc exists
    if it doesn't creates one with a demo
    entry.

    '''
    try:
        tlogonrc = open (os.environ['HOME']+"/.tlogonrc")
        tlogonrc_data = tlogonrc.read()

    except IOError:
        tlogonrc_data = u'''<?xml version="1.0" encoding="UTF-8" ?>
        <!-- Automatically generated. Do not edit by hand -->
        <tlogon>
        <instance id='1' 
            description='GNU Health Demo Server' 
            appserver='health.gnusolidario.org' 
            port='8000'
            database='health26'
            role='Demo'
            url='tryton://localhost:8000/health26/'/>
        </tlogon>
'''
        
        tlogonrc = open (os.environ['HOME']+"/.tlogonrc","w")
        tlogonrc.write (tlogonrc_data)
        tlogonrc.close()

    return tlogonrc_data



class tlogongui:
    ui = '''<ui>
        <menubar name="MenuBar">
          <menu action="Connection">
            <menuitem action="New"/>
            <menuitem action="Connect"/>
            <menuitem action="Edit"/>
            <menuitem action="Delete"/>
            <separator/>
            <menuitem action="Quit"/>
        
          </menu>
          <menu action="Help">
            <menuitem action="About"/>
          </menu>
        </menubar>
        <toolbar name="Toolbar">
          <toolitem action="New"/>
          <toolitem action="Edit"/>
          <toolitem action="Delete"/>
          <toolitem action="Connect"/>
          <toolitem action="Quit"/>
          <separator/>
        </toolbar>
        </ui>'''
      
    
    def __init__(self,instances):

        # Create the toplevel window
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.connect('destroy', lambda w: gtk.main_quit())
        self.window.set_title("Tryton Logon Manager")
        self.window.set_resizable (False)
        self.window.set_border_width(1)

        vbox = gtk.VBox()
        self.window.add(vbox)

        # Create a UIManager instance
        uimanager = gtk.UIManager()

        # Add the accelerator group to the toplevel window
        accelgroup = uimanager.get_accel_group()
        self.window.add_accel_group(accelgroup)

        # Create an ActionGroup
        actiongroup = gtk.ActionGroup('tlogongui')

        # Create actions
        actiongroup.add_actions([('Connection', None, '_Connection'),
             ('Quit', gtk.STOCK_QUIT, '_Quit', None,
                'Exit Tryton Logon Manager', self.quit_program),
             ('Edit', gtk.STOCK_PROPERTIES, '_Edit',None,
                "Edit Selected Instance",self.modify_instance),
             ('Delete', gtk.STOCK_DELETE, '_Delete',None,
                "Delete Selected Instance",self.delete_instance),
             ('Help', None, '_Help'),
             ('About', gtk.STOCK_ABOUT, '_About',None,
                "About Tryton Logon Manager",self.show_about),
             ('Connect', gtk.STOCK_YES, '_Connect',
                None, "Connect to selected Instance",self.activate_row),
             ('New', gtk.STOCK_NEW, '_New',
                None,'Create a new Instance',self.modify_instance)])
     

        # Add the actiongroup to the uimanager
        uimanager.insert_action_group(actiongroup, 0)

        # Add a UI description
        uimanager.add_ui_from_string(self.ui)

        # Create a MenuBar
        menubar = uimanager.get_widget('/MenuBar')
        vbox.pack_start(menubar, False)

        # Create a Toolbar
        toolbar = uimanager.get_widget('/Toolbar')
        vbox.pack_start(toolbar, False)


        # liststore to hold instances data 
        self.liststore = gtk.ListStore(str, str, str, str, str, str, 'gboolean')
        self.framewindow = gtk.ScrolledWindow()
        self.framewindow.set_size_request(400,400)  
        self.treeview = gtk.TreeView(self.liststore)
        self.framewindow.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_ALWAYS)    
        self.framewindow.add (self.treeview)
        
        #Define all the columns
        col_instance_id = gtk.TreeViewColumn('Identifier')
        col_description = gtk.TreeViewColumn('Description')
        col_appserver = gtk.TreeViewColumn('Appserver')
        col_port = gtk.TreeViewColumn('Port')
        col_url = gtk.TreeViewColumn('Url')
        col_role = gtk.TreeViewColumn('Role')


        #Make Columns resizable
        col_description.set_resizable(True)
        col_role.set_resizable(True)

        #Make Description column the larger one
        col_description.set_expand (True)

        #Make invisible some columns
        col_instance_id.set_visible (False)
        col_appserver.set_visible (False)
        col_port.set_visible (False)
        col_url.set_visible (False)

        # We map the array components to the instance elements
        
        for (instance_id, description,appserver,port,url,role) in instances:
            self.liststore.append([instance_id,description,
                appserver,port,url,role, True])


        # Append description and role to the treeview
        self.treeview.append_column(col_description)
        self.treeview.append_column(col_role)

        # Cell rendering 
        cell_id = gtk.CellRendererText()
        cell_desc = gtk.CellRendererText()
        cell_apps = gtk.CellRendererText()
        cell_port = gtk.CellRendererText()
        cell_url = gtk.CellRendererText()
        cell_role = gtk.CellRendererText()

        
        # Add some color to the cells
        cell_role.set_property('cell-background', 'grey')
        cell_desc.set_property('cell-background', 'grey')


        # Pack the columns 
        col_instance_id.pack_start (cell_id, True)
        col_description.pack_start (cell_desc, True)
        col_appserver.pack_start (cell_apps, True)
        col_port.pack_start (cell_port, True)
        col_url.pack_start (cell_url, True)
        col_role.pack_start (cell_role, True)
        
        # Make the list searchable
        self.treeview.set_search_column(1)

        # Make both the description and Role able to classify 
        col_description.set_sort_column_id(0)
        col_role.set_sort_column_id(1)

        # Add some signals 
        self.treeview.connect ('row-activated', self.activate_row)
        self.selection = self.treeview.get_selection()
        self.selection.connect("changed", self.select_item)

        # the number associated to the text param shows the field text 
        # (0 = ID, 1= Description ... )
        col_instance_id.set_attributes(cell_id, text=0)
        col_description.set_attributes(cell_desc, text=1)
        col_appserver.set_attributes(cell_apps, text=2)
        col_port.set_attributes(cell_port, text=3)
        col_url.set_attributes(cell_url, text=4)
        col_role.set_attributes(cell_role, text=5)

        vbox.pack_start (self.framewindow, False)
        self.window.show_all()

        return

    def select_item (self, selection):
        try:
            (data, column) = selection.get_selected ()
            instance_info = [data.get_value(column,0),data.get_value(column,1),
                data.get_value(column,2),data.get_value(column,3),
                data.get_value(column,4),data.get_value(column,5)]
            return instance_info
        except:
            return

    def activate_row (self, *selection):  
        #Pointer to selection ( passing args from treeview.connect
        # !=  action group connect )

        (id, desc, host, port, url, role) = self.select_item (self.selection)

        #Execute the Tryton client
        command = [TRYTON,url]

        pid = os.fork ()

        if pid:  
            try:
                os.execvp (command[0],command)
                sys.exit (0)   # Give back control to the parent
            except OSError, error:
                sys.stderr.write("Couldn't exec %s : %s\n"% (command[0], error))
                sys.exit(1)

        if pid < 0:
            sys.stderr.write ("Couldn't fork a new process.... exiting now")
            sys.exit(1)
                
        return

    def quit_program(self,NULL):
        print 'Have a good one !'
        gtk.main_quit()


    def assign_new_id (self):
        num_records = len (tlogonrc) 

        if num_records > 0:
            last_id = tlogonrc[num_records-1][0] 
        else:
            last_id = 0
        next_id = int(last_id) + 1
        
        return next_id

    def write_tlogonrc (self):
        tlogonrc_data = []
        tlogonrc_header = u'''<?xml version="1.0" encoding="UTF-8" ?>
            <!-- Automatically generated. Do not edit by hand -->
            <tlogon>
            '''
        tlogonrc_footer = u"</tlogon>"

        tlogonrc_data.append (tlogonrc_header)
        
        for buffer in tlogonrc:
            (id, desc, host, port, url, role) = buffer
            line = unicode ("\t<instance id=\'%s\' description=\'%s\' \
                appserver=\'%s\' port=\'%s\' url=\'%s\' role=\'%s\'/>\n"
                % (id, desc,host,port,url,role))
            tlogonrc_data.append (line)

        tlogonrc_data.append (tlogonrc_footer)
        
        new_tlogonrc = open (os.environ['HOME']+"/.tlogonrc","w")
        new_tlogonrc.writelines (tlogonrc_data)
        new_tlogonrc.close()

        return

    def message_window (self,message_type,message):
        message_window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        message_window.set_title (message_type)
        message_window.set_border_width(10)
        message_window.set_resizable (False)
        message_label = gtk.Label(message)
        
        message_frame = gtk.VBox()
        message_window.add(message_frame)

        message_icon = gtk.Button(stock=gtk.STOCK_DIALOG_ERROR)
        message_frame.pack_start (message_icon)
        message_frame.pack_start (message_label)
        message_icon.connect_object("clicked", 
            gtk.Widget.destroy, message_window)
        message_window.show_all()
    
    def show_about (self,control):
        about_window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        about_window.set_title ("About T-Logon Manager")
        about_window.set_border_width(10)
        about_window.set_resizable (False)
        message="""
        T-Logon Manager

        (c) 2006-2014 Luis Falcon 

        License : GPL v3+

        """

        about_label = gtk.Label(message)
        about_label.set_justify (gtk.JUSTIFY_CENTER)    
        separator = gtk.HSeparator()    
        
        about_frame = gtk.VBox()
        about_window.add(about_frame)

        about_icon = gtk.Button(stock=gtk.STOCK_OK)
        about_frame.pack_start (about_label)
        about_frame.pack_start (separator)
        about_frame.pack_start (about_icon, True, False,0)
        about_icon.connect_object("clicked", gtk.Widget.destroy, about_window)
        about_window.show_all()
    
    def search_instance_position (self, id):
        counter=0
        for instance in tlogonrc:
            if instance[0] == id:
                position = counter
            counter=counter+1   
        return position
    
    def save_instance (self,widget, buffer):

        (action, id, desc, host, port, url, role) = buffer 

        # We get the active value in the Role combobox 
        role_model = role.get_model()
        role_active = role.get_active()
        role_txt = role_model [role_active][0]
        
        if not desc.get_text() or not host.get_text():  
            self.message_window ("Error",
                "Description and host can not be empty")
        
        else:
            # Assign a new ID if creating a new instance
            if action == "New":             
                next_id = self.assign_new_id ()
                tlogonrc.append ( [unicode (next_id), 
                    unicode (desc.get_text()),unicode (host.get_text()), 
                    unicode (port.get_text()),unicode (url.get_text()), 
                    unicode (role_txt)])

                self.liststore.append([unicode (next_id), 
                    unicode (desc.get_text()),unicode (host.get_text()), 
                    unicode (port.get_text()),unicode (url.get_text()),
                    unicode (role_txt), True])

            else:   
                # Update Instance contents when modifying it
                position = self.search_instance_position (id)   
                tlogonrc [position] = [unicode (id), 
                    unicode (desc.get_text()),unicode (host.get_text()), 
                    unicode (port.get_text()),unicode (url.get_text()),
                    unicode (role_txt)]

                self.liststore [position] = [unicode (id), 
                    unicode (desc.get_text()),unicode (host.get_text()), 
                    unicode (port.get_text()),unicode (url.get_text()), 
                    unicode (role_txt), True]
        
            self.write_tlogonrc ()

            self.modify_instance_window.destroy()

        return

    # Instance deletion from list
    def delete_instance (self,control):
        if len(tlogonrc) > 0:   
            (id, desc, host, port, url, role) = self.select_item (self.selection)
            position = self.search_instance_position (id)
            del tlogonrc [position]
            self.write_tlogonrc ()
            del self.liststore [position]
        return  

    def modify_instance(self,control):
        ''' We need to input the following fields
        - application server host or IP
        - Tryton Server port
        - Role
        - Description
        - URL
        '''
        # Initialize it to dummy when creating a new instance
        id=-1  

        action = control.get_name()

        if len(tlogonrc) == 0 and action == "Edit":
            return

        if action == "Edit":
            (id, desc, host, port, url, role) = \
                self.select_item(self.selection)

        window_title = "%s Tryton Instance" % action

        buffer = []

        buffer.append (action)
        buffer.append (id)

        self.modify_instance_window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.modify_instance_window.set_title(window_title)
        self.modify_instance_window.set_resizable (False)

        # Vertical Box to hold the entry boxes
        main_box = gtk.VBox (False,0)
        self.modify_instance_window.add(main_box)


        #Create a grid for Labels / Entries
        grid = gtk.Table (6,2, False)
        main_box.pack_start (grid, False, False, 0)

        #Instance Description 
        idesc_label = gtk.Label ("Description")
        #Description <= 60 chars
        idesc = gtk.Entry (max=60)
        idesc_text = idesc.get_text()


        #Instance hostname / IP address
        ihost_label = gtk.Label ("Server")
        #Hostnames <= 40 chars
        ihost = gtk.Entry (max=40)

        #Instance Port 
        iport_label = gtk.Label ("Port")
        #Port <= 5 chars
        iport = gtk.Entry (max=5)

        #Instance url
        iurl_label = gtk.Label ("URL")
        #URL < 100 chars
        iurl = gtk.Entry (max=100)

        # Instance Role ( Combobox )
        irole_label = gtk.Label ("Role")
        irole = gtk.combo_box_new_text()
        irole.append_text("Development")    
        irole.append_text("Quality Assurance")  
        irole.append_text("Training")   
        irole.append_text("Demo")   
        irole.append_text("Production") 

        #Set the default role to Development
        irole.set_active(0)

        #We set the default values depending on editing the instance 
        #or creating a new one

        if action == "New":
            iport.set_text("8000")
            iport.set_text("tryton://localhost:8000/dbname/")
            irole.set_active(0) # Set Development role by default
        else:
            idesc.set_text (desc)
            ihost.set_text (host)
            iport.set_text (port)
            iurl.set_text (url)
            role_id = {
                "Development":0,
                "Quality Assurance":1,
                "Training":2,
                "Demo":3,
                "Production":4}
            irole.set_active(role_id[role]) 

        # We fill the instance information values into the buffer

        buffer.append (idesc)
        buffer.append (ihost)
        buffer.append (iport)
        buffer.append (iurl)
        buffer.append (irole)

        #Description
        grid.attach(idesc_label,0,1,0,1,xpadding=10)
        grid.attach(idesc,1,2,0,1,xpadding=10)

        #Host
        grid.attach(ihost_label,0,1,1,2,xpadding=10)
        grid.attach(ihost,1,2,1,2,xpadding=10)

        #Port
        grid.attach(iport_label,0,1,2,3,xpadding=10)
        grid.attach(iport,1,2,2,3,xpadding=10)

        #URL
        grid.attach(iurl_label,0,1,3,4,xpadding=10)
        grid.attach(iurl,1,2,3,4,xpadding=10)

        #Role
        grid.attach(irole_label,0,1,5,6,xpadding=10)
        grid.attach(irole,1,2,5,6,xpadding=10)

        # Horizontal Box to hold the Save and Cancel Buttons
        botton_box = gtk.HBox (True,0)

        #Separator
        separator = gtk.HSeparator()
        main_box.pack_start (separator)
        main_box.pack_start (botton_box, False, False, 5)

        # Save and Cancel Buttons
        save_button = gtk.Button(stock=gtk.STOCK_SAVE)
        cancel_button = gtk.Button(stock=gtk.STOCK_CANCEL)
        save_button.connect("clicked", self.save_instance,buffer)
        cancel_button.connect_object("clicked", gtk.Widget.destroy,
            self.modify_instance_window)

        botton_box.pack_start (save_button, False, False,0)
        botton_box.pack_start (cancel_button, False, False,0)
        self.modify_instance_window.show_all()

        return  

if __name__ == '__main__':
    
    init_tlogon = init_tlogonrc()
    tlogonrc = parse_tlogonrc (init_tlogon)
    main_gui = tlogongui(tlogonrc)
    gtk.main()


