#!/usr/bin/env python3
import json
import sys
import psycopg2

#Modify to meet your needs
PG_URI = "postgresql://localhost/federation"

try:
    conn = psycopg2.connect(PG_URI)
except:
    print ("Unable to connect to the database")

people_file = open('people.json', 'r')
people_data = json.load(people_file)

pols_file = open('pols.json', 'r')
pols_data = json.load(pols_file)

cur = conn.cursor()

for person in people_data:
    id = person['id']
    print ("Inserting", id)
    cur.execute("INSERT INTO people (ID, DATA) VALUES (%(id)s, \
        %(data)s)", {'id': id, 'data':json.dumps(person)})
    conn.commit()


for pol in pols_data:
    id = pol['id']
    book = pol['book']
    print ("Inserting", id, book)
    cur.execute("INSERT INTO pols (ID, BOOK, DATA) VALUES (%(id)s, %(book)s, %(data)s)", {'id': id, 'book': book, 'data':json.dumps(pol)})
    conn.commit()
