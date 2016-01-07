# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2008-2016 Luis Falcon <lfalcon@gnusolidario.org>
#    Copyright (C) 2011-2016 GNU Solidario <health@gnusolidario.org>
#    Copyright (C) 2015 CRS4
#
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


from trytond.pool import Pool


class PoolManager:
    def __init__(self, database_name):
        self.database_name = database_name
        
        self.pool = Pool(self.database_name)
        self.pool.init()
        self.pool.start()
        
    def get_pool(self):
        return self.pool
    
    def get_domain(self):
        return self.database_name
        
    def get_table(self, table_name):
        """
        Retrieves a table object from the connection pool
    
        :type:  table_name ``str``
        :param: table_name  the name of the table to retrieve from the connection pool
    
        :return: the ``Table`` object corresponding to the name
        """
        return self.pool.get(table_name).__table__()
