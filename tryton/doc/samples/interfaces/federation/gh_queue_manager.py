#  gh_queue_manager.py
#  
#  Copyright 2019 Luis Falcon <falcon@gnu.org>
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

def check_federation_queue():
    Queue = Model.get('gnuhealth.federation.queue')

    mqueued = Queue.find ([('state', '=', 'queued')])
    queued_messages = len(mqueued)
    
    print ("Number of messages in the queue", queued_messages)

            
    
print ("Connecting to GNU Health Server ...")
conf = config.set_xmlrpc(health_server)
print ("Connected !")
check_federation_queue()
