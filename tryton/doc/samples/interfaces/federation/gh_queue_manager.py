#  gh_queue_manager.py
#  
#  Copyright 2019 Luis Falcon <falcon@gnuhealth.org>
#  Copyright 2011-2019 GNU Solidario <health@gnusolidario.org>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

# Check the README file for documentation on how to use this program

from proteus import config, Model
import sys

dbname = 'health34'
user = 'admin'
password = 'gnusolidario'
hostname = 'localhost'
port = '8000'

health_server = \
    'http://'+user+':'+password+'@'+hostname+':'+port+'/'+dbname+'/'


usage = """
   Usage : gh_queue_manager <action> [args]
    Actions:
        * check: View messages in queue
        * push: Send messages to the federation
    """
def federation_queue(action):
    Queue = Model.get('gnuhealth.federation.queue')

    mqueued = Queue.find ([('state', '=', 'queued')])
    queued_messages = len(mqueued)
    
    print ("Number of messages in the queue", queued_messages)
    if (action == "check"):
        exit (0)

    if (action == "push"):
        print ("Sending messages with status Queued...")
        for msg in mqueued:
            print (msg.msgid, msg.federation_locator, msg.time_stamp, msg.model, msg.node)
            try:
                msg.click('send')
            except:
                print ("Failed to send message ", msg.msgid)



if (len(sys.argv) < 2):
    exit (usage)
    
print ("Connecting to GNU Health Server ...")
conf = config.set_xmlrpc(health_server)
print ("Connected !")

federation_queue(action=sys.argv[1])
