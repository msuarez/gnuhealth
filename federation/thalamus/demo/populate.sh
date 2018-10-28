#!/bin/bash
echo "Importing Demographics information..."
mongoimport -d federation -c people -u gnuhealth people.json -v

echo "Importing pages of lives....." 
mongoimport -d federation -c lives -u gnuhealth lives.json -v
