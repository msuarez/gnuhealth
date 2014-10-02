/*
# GNU HEALTH : The Free Health and Hospital Information System
# (c) 2008-2014 Luis Falcon <falcon@gnu.org>
# (c) 2008-2014 GNU Solidario <info@gnusolidario.org>

# Program name : fix_appointments_instituion.sql

# Script to fix the institution assignment on the appointment model

# Versions affected : Any UPGRADE to 2.6 series previous to 2.6.4
# New installations starting in 2.6 are not affected

# INSTRUCTIONS :
#
# 1) Run the script via psql your_db_name < fix_appointments_instituion.sql
# 2) Update the health module : 
#   $ cdexe
#   $ ./trytond --update=health --database=your_db_name
#
# Execute this script ONLY once !

*/

ALTER TABLE gnuhealth_appointment DROP CONSTRAINT IF EXISTS gnuhealth_appointment_institution_fkey;

UPDATE GNUHEALTH_APPOINTMENT SET INSTITUTION = GNUHEALTH_INSTITUTION.ID FROM GNUHEALTH_INSTITUTION WHERE GNUHEALTH_APPOINTMENT.INSTITUTION = GNUHEALTH_INSTITUTION.NAME
