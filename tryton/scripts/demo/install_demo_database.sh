#!/usr/bin/env bash
# Script to download/unpack and locally install the GNU Health demo database

URL="http://health.gnu.org/downloads/postgres_dumps/gnuhealth-2.6.0-demo.sql.gz"
DB="gnuhealth_demo"

if [[ $USER != "gnuhealth" ]]; then
    echo "Run script as gnuhealth user"
    exit 1
fi


if psql -l | grep -q "$DB"; then
    echo "$DB database already exists"
    echo "    delete it/change target database before proceeding"
    exit 1
fi

function cleanup {
    rm -f demo_database.sql.gz
    rm -f demo_database.sql
    exit
    }

trap cleanup SIGHUP SIGINT SIGTERM EXIT

echo -n 'Downloading the demo database...'
wget -q "$URL" -O demo_database.sql.gz
echo 'Finished the download.'

echo -n 'Unpacking the database...'
gunzip -q demo_database.sql.gz
echo 'Finished unpacking.'

echo -n 'Initializing empty database...'
psql -q -d template1 -c "create database $DB"
echo 'Empty database initialized.'

echo -n 'Importing demo database...'
psql -q "$DB" < demo_database.sql > /dev/null 2>&1
echo 'Imported successfully.'

echo 'Use Tryton to access (with non-gnuhealth user!)...'
echo "    Database: $DB"
echo '    Username: admin'
echo '    Password: gnusolidario'
exit 0
