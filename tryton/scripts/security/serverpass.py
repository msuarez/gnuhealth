#!/usr/bin/env python

##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2008-2015 Luis Falcon <falcon@gnu.org>
#    Copyright (C) 2011-2015 GNU Solidario <health@gnusolidario.org>
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

import argparse
import getpass
import os
import sys
import crypt
import random
import string
import ConfigParser

try:
    import cracklib
except ImportError:
    print "Cracklib not installed. Please install the library and try again"
    sys.exit(-1)

config_file = ""
  
parser = argparse.ArgumentParser()

parser.add_argument("-c", "--config",
    help="Specify alternative Tryton configuration file")

args = parser.parse_args()

try: 
    config_file = os.environ['TRYTOND_CONFIG']
except:
    pass

if args.config:
    config_file = args.config

if not config_file:
    print "TRYTOND_CONFIG variable not set and No configuration file specified"
    sys.exit(-1)



    
print "Using Tryton configuration file ", config_file
        
def validate_password():
    passwd = getpass.getpass()
    print "Again"
    passwd2 = getpass.getpass()
    
    if (passwd != passwd2):
        print "Password mismatch"
        return validate_password()
        
    """Check against cracklib to avoid simple passwords"""
    try: 
        cracklib.VeryFascistCheck (passwd)
    except ValueError as msg:
        print msg
        return validate_password()
      
    return passwd    

config = ConfigParser.RawConfigParser()
config.read(config_file)

if not 'session' in config.sections():
    config.add_section('session')

trytond_pass = validate_password()

salt =  "".join(random.sample(string.ascii_letters + string.digits, 8))

encrypted_passwd = crypt.crypt(trytond_pass, salt)

config.set ('session','super_pwd',encrypted_passwd)

output_file = open(config_file,'w')
config.write(output_file)

print "Configuration file updated with new password !"
