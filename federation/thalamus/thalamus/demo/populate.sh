#!/bin/bash
echo "Importing Demographics information..."
mongoimport -d federation -c people -u gnuhealth people.json -v

echo "Importing pages of lives (pols)....." 
mongoimport -d federation -c pols -u gnuhealth pols.json -v
