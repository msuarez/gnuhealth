/*
# GNU HEALTH : The Free Health and Hospital Information System
# (c) 2008-2017 Luis Falcon <falcon@gnuhealth.org>
# (c) 2008-2017 GNU Solidario <info@gnusolidario.org>

# Program name : upgrade_32.sql

# Script to fix the institution assignment on the appointment model

# Versions affected : Any UPGRADE to 3.2 series from previous releases 
# New installations starting in 2.6 are not affected

# INSTRUCTIONS :
#
# 1) Run the script via psql your_db_name < upgrade_32.sql
#
# Execute this script ONLY once !


# Notes from https://discuss.tryton.org/t/migration-from-3-8-to-4-0/96

*/



ALTER TABLE product_template DROP COLUMN category;


UPDATE account_tax_template SET credit_note_base_sign = credit_note_base_sign * -1, credit_note_tax_sign = credit_note_tax_sign * -1;
UPDATE account_tax SET credit_note_base_sign = credit_note_base_sign * -1, credit_note_tax_sign = credit_note_tax_sign * -1;

/* Set the new active attribute to the following models */

/* Patient */
update gnuhealth_patient set active=True;

/* Medicament */
update gnuhealth_medicament set active=True;

/* Health Professional */
update gnuhealth_healthprofessional set active=True;

/* Lab tests */
update gnuhealth_lab_test_type  set active=True;

/* Dx Imaging */
update gnuhealth_imaging_test set active=True;

/* Ambulances */
update gnuhealth_ambulance set active=True;
