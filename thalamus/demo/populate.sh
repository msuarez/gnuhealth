#!/bin/bash
mongoimport -d federation -c people -u gnuhealth people.json -v
