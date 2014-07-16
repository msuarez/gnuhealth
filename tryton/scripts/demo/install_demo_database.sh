#!/usr/bin/env bash
# Script to download/unpack and locally install the GNU Health demo database

URL="http://health.gnu.org/downloads/postgres_dumps/gnuhealth-2.6.0-demo.sql.gz"

if [[ $USER != "gnuhealth" ]]; then
    echo "Run script as gnuhealth user"
    exit 1
fi

echo -n 'Downloading the demo database...'
wget -q "$URL" -O demo_database.sql.gz
echo 'Finished the download.'

echo -n 'Unpacking the database...'
gunzip -q demo_database.sql.gz
echo 'Finished unpacking.'

echo -n 'Initializing empty database...'
psql -q -d template1 -c "create database gnuhealth_demo"
echo 'Empty database initialized.'

echo -n 'Importing demo database...'
psql -q gnuhealth_demo < demo_database.sql
echo 'Imported successfully.'

echo 'Use Tryton to access...'
echo '    Database: gnuhealth_demo'
echo '    Username: admin'
echo '    Password: gnusolidario'
exit 0
