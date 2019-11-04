#!/usr/bin/env bash
# Script to download/unpack and locally install the GNU Health demo database

URL="https://www.gnuhealth.org/downloads/postgres_dumps/gnuhealth-$1-demo.sql.gz"
DB="ghdemo$1"

help()
{
    cat << EOF

GNU Health HMIS demo database installer

usage: `basename $0` <db_version>

    Example:
    $ bash ./install_demo_dabase.sh 36

    will install the latest demo db for version 3.6.x
EOF
    exit 0
}

bailout () {
    echo "Error"
    echo "Cleaning up..."
    cleanup
    exit 1
    }


if [ $# -eq 0 ]; then
    help
fi

cleanup () {
    rm -f gnuhealth_demo_database.sql.gz
    rm -f gnuhealth_demo_database.sql
    }


if psql -l | grep -wq "$DB"; then
    echo "$DB database already exists"
    echo "    delete it/change target database before proceeding"
    bailout
fi



echo -n "Downloading the demo database..."
wget "$URL" -O gnuhealth_demo_database.sql.gz || bailout
echo 'SUCCESS...'

echo -n "Unpacking the database..."
gunzip -q gnuhealth_demo_database.sql.gz || bailout
echo 'SUCCESS...'

echo -n "Initializing empty database..."
createdb $DB
echo 'SUCCESS...'

echo "Importing demo database..."
psql -q "$DB" < gnuhealth_demo_database.sql > /dev/null 2>&1 || bailout
echo "IMPORT OF DEMO DATABASE $DB COMPLETED SUCCESFULLY !"

echo "Login Info:"
echo "    Database: $DB"
echo "    Username: admin"
echo "    Password: gnusolidario"
exit 0


