#!/usr/bin/env python3
import json
import sys
import psycopg2

try:
    conn = psycopg2.connect("postgresql://localhost/federation")
except:
    print ("Unable to connect to the database")

people_file = open('people.json', 'r')
people_data = json.load(people_file)

pols_file = open('pols.json', 'r')
pols_data = json.load(pols_file)

cur = conn.cursor()

# Create the schemas
print ("Creating the people schema...")
cur.execute("""CREATE TABLE IF NOT EXISTS \
    people (ID VARCHAR PRIMARY KEY, DATA JSONB);""")
conn.commit()

print ("Creating the POLS schema...")
cur.execute("""CREATE TABLE IF NOT EXISTS \
    pols (id VARCHAR PRIMARY KEY, DATA JSONB);""")
conn.commit()

for person in people_data:
    id = person['id']
    print ("Inserting", id)
    cur.execute("INSERT INTO people (ID, DATA) VALUES (%(id)s, \
        %(data)s)", {'id': id, 'data':json.dumps(person)})
    conn.commit()

for pol in pols_data:
    id = pol['id']
    print ("Inserting", id)
    cur.execute("INSERT INTO pols (ID, DATA) VALUES (%(id)s, \
        %(data)s)", {'id': id, 'data':json.dumps(pol)})
    conn.commit()
