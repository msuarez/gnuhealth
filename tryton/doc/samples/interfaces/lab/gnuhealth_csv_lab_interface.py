#  gnuhealth_csv_lab_interface.py
#  
#  Copyright 2017 Luis Falcon <falcon@gnu.org>
#  Copyright 2011-2017 GNU Solidario <health@gnusolidario.org>
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
import csv
import sys

dbname = 'sandbox32'
user = 'admin'
password = 'gnusolidario'
hostname = 'localhost'
port = '8069'

health_server = \
    'http://'+user+':'+password+'@'+hostname+':'+port+'/'+dbname

def check_lab_test():
    LabTest = Model.get('gnuhealth.lab')
    LabTestLine = Model.get('gnuhealth.lab.test.critearea')

    # Verify that each test exists at the DB before trying 
    # to upload the results
    csv_file = csv.reader(open(sys.argv[1], 'rb'))
    for line in csv_file:
        test_id = line[0]
        analyte = line[1]
        if not (LabTest.find(['name','=',test_id])):
            exit("ERROR: Test %s not found" %test_id)
            
        if  not (LabTestLine.find([('name','=',analyte), \
            ('gnuhealth_lab_id','=',test_id)])):
            exit("ERROR: Analyte %s not found on %s" %(analyte, test_id))

    print "Basic check on test ID and analytes succeeded"
            
def input_results():
    LabTestLine = Model.get('gnuhealth.lab.test.critearea')
    csv_file = csv.reader(open(sys.argv[1], 'rb'))
    for line in csv_file:
        test_id = line[0]
        analyte = line[1]
        result = line[2]
        # Update the model with the result values
        for result_line in LabTestLine.find([('name','=',analyte), \
            ('gnuhealth_lab_id','=',test_id)]):
            result_line.result = float(result)
            result_line.save()

if (len(sys.argv) < 2):
    exit ("You need to specify a CSV file with the lab results")
    
print "Connecting to GNU Health Server ..."
conf = config.set_xmlrpc(health_server)
print "Connected !"

print "Checking integrity of the batch file ..."
check_lab_test()
print "Updating lab results from batch file ..."
input_results()
print "Done !"
