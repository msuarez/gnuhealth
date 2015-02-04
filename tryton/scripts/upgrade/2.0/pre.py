#!/usr/bin/env python
# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2008-2015 Luis Falcon <lfalcon@gnusolidario.org>
#    Copyright (C) 2011-2015 GNU Solidario <health@gnusolidario.org>
#
#                             Bruno M. Villasanti <bvillasanti@thymbra.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
import optparse
import psycopg2


def main(pg_cursor):
    pg_cursor.execute('UPDATE "ir_model_data" '
        'SET inherit = %s '
        'WHERE fs_id like \'prod_em%%\' '
        '  AND model = %s AND module = %s ',
        (False, 'product.template', 'health',))

if __name__ == '__main__':
    parser = optparse.OptionParser(version='0.1')
    parser.add_option('--pg', dest='dsn', help='dsn for PostgreSQL')

    opt, args = parser.parse_args()
    pg_conn = None
    pg_cursor = None
    try:
        print ">> Attempting to connect..."
        pg_conn = psycopg2.connect(opt.dsn)
        print ">> Connected!"
        pg_cursor = pg_conn.cursor()
        main(pg_cursor)
        pg_conn.commit()
        print ">> Successfully prepared for migration!"
    finally:
        if pg_cursor:
            pg_cursor.close()
        if pg_conn:
            pg_conn.close()
