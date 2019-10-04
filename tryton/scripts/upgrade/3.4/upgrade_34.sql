/*
# GNU HEALTH : The Free Health and Hospital Information System
# (c) 2008-2017 Luis Falcon <falcon@gnuhealth.org>
# (c) 2008-2017 GNU Solidario <info@gnusolidario.org>

# Program name : upgrade_34.sql

# Script to update from GNU Health 3.2 to 3.4 (tryton 4.6)

# Versions affected : Any UPGRADE to 3.4 series from previous releases 

# INSTRUCTIONS :
#
# 1) Run the script via psql your_db_name < upgrade_34.sql
#
# Execute this script ONLY once !



*/

UPDATE party_address_format SET format_ = REPLACE(format_, '${district}', '${subdivision}');

DELETE FROM ir_model_data WHERE model = 'ir.property';

DELETE from ir_property where res like 'party.party,%' and SUBSTRING(res, POSITION(',' IN res) + 1)::integer not in (select id from party_party);
