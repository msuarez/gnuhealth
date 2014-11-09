# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2008-2014 Luis Falcon <falcon@gnu.org>
#    Copyright (C) 2011-2014 GNU Solidario <health@gnusolidario.org>
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
from datetime import date
from trytond.report import Report
from trytond.pool import Pool
from trytond.transaction import Transaction
from dateutil.relativedelta import relativedelta

__all__ = ['InstitutionSummaryReport']

class InstitutionSummaryReport(Report):
    __name__ = 'gnuhealth.summary.report'


    @classmethod
    def get_population(cls,date1,date2,sex):
        """ Return Total Number of people in the system 
        segmented by age group and sex"""
        cursor = Transaction().cursor

        cursor.execute("SELECT COUNT(dob) \
            FROM party_party \
            WHERE dob BETWEEN %s and %s AND \
            sex = %s" ,(date2, date1, sex))
       
        res = cursor.fetchone()[0]
    
        return(res)

    @classmethod
    def get_new_people(cls, start_date, end_date):
        """ Return Total Number of new registered persons """
        cursor = Transaction().cursor
        cursor.execute("SELECT COUNT(activation_date) \
            FROM party_party \
            WHERE activation_date BETWEEN \
            %s AND %s and is_person=True",(start_date, end_date))
       
        res = cursor.fetchone()
        return(res)


    @classmethod
    def get_new_health_users(cls, start_date, end_date):
        """ Return Total Number of new registered patients """
        cursor = Transaction().cursor
        cursor.execute("SELECT COUNT(activation_date) \
            FROM party_party \
            WHERE activation_date BETWEEN \
            %s AND %s and is_patient=True",(start_date, end_date))
       
        res = cursor.fetchone()
        return(res)

    @classmethod
    def get_total_health_users(cls):
        """ Return Total Number of registered people in
        health care system """
        cursor = Transaction().cursor
        cursor.execute("SELECT COUNT(activation_date) \
            FROM party_party \
            WHERE is_patient=True")
       
        res = cursor.fetchone()
        return(res)

    @classmethod
    def parse(cls, report, objects, data, localcontext):
        Patient = Pool().get('gnuhealth.patient')
        Evaluation = Pool().get('gnuhealth.patient.evaluation')

        start_date = data['start_date']
        end_date = data['end_date']

        localcontext['start_date'] = data['start_date']
        localcontext['end_date'] = data['end_date']

        # Demographics
        today = date.today()
        
        for age_group in range (0,20):
            date1 = today - relativedelta(years=(age_group*5))
            date2 = today - relativedelta(years=((age_group*5)+4))
            
            localcontext[''.join(['p',str(age_group),'f'])] = cls.get_population (date1,date2,'f')
            localcontext[''.join(['p',str(age_group),'m'])] = (-1) * cls.get_population (date1,date2,'m')
            
            print age_group*5, date1,'-', age_group*5 + 4, date2
            
        #localcontext['population'] = \
        #    InstitutionSummaryReport().get_population()

        
        return super(InstitutionSummaryReport, cls).parse(report,
            objects, data, localcontext)

