#!/usr/bin/python2
#  gnuhealth_product_uploader.py
#  
#  Copyright 2017 - 2018 Luis Falcon <falcon@gnu.org>
#  Copyright 2011-2018 GNU Solidario <health@gnusolidario.org>
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

# Requirements
# Proteus version : 4.2.x
# pip2 install --user "proteus>=4.2,<4.3"

# ##### Usage ########
# python2 ./gnuhealth_product_uploader.py products_file_name.csv

# Product CSV Format
# Name,List Price,Cost Price,Type,UOM
# Sample csv content
# "Rapid urease test",15,12,"service","Unit"

from proteus import config, Model
import csv
import sys

from decimal import Decimal

dbname = 'health32'
user = 'admin'
password = 'gnusolidario'
hostname = 'localhost'
port = '8000'

health_server = \
    'http://'+user+':'+password+'@'+hostname+':'+port+'/'+dbname+'/'

            
def input_results():
    ProductInfo = Model.get('product.template')
    ProductUOM = Model.get('product.uom')
    csv_file = csv.reader(open(sys.argv[1], 'rb'))
    for line in csv_file:
        name = line[0]
        list_price = line[1]
        cost_price = line[2]
        product_type = line[3]
        uom = line[4]
        # Update the model with the result values
        product = ProductInfo ()
        product.name = name
        product.list_price = Decimal(list_price)
        product.cost_price = Decimal(cost_price)
        uom_val, = ProductUOM.find([('name','=',uom)])
        product.default_uom = uom_val
        
        product.save()

if (len(sys.argv) < 2):
    exit ("You need to specify a CSV file with the product list")
    
print "Connecting to GNU Health Server ..."
conf = config.set_xmlrpc(health_server)
print "Connected !"

print "Updating products from batch file ..."
input_results()
print "Done !"
