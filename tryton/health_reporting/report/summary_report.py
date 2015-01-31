# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2008-2015 Luis Falcon <falcon@gnu.org>
#    Copyright (C) 2011-2015 GNU Solidario <health@gnusolidario.org>
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
    def get_population(cls,date1,date2,sex,total):
        """ Return Total Number of living people in the system 
        segmented by age group and sex"""
        cursor = Transaction().cursor

        if (total):
            cursor.execute("SELECT COUNT(dob) \
                FROM party_party WHERE sex = %s and deceased is not TRUE",(sex))

        else:
            cursor.execute("SELECT COUNT(dob) \
                FROM party_party \
                WHERE dob BETWEEN %s and %s AND \
                sex = %s  and deceased is not TRUE" ,(date2, date1, sex))
       
        res = cursor.fetchone()[0]
    
        return(res)

    @classmethod
    def get_new_people(cls, start_date, end_date, in_health_system):
        """ Return Total Number of new registered persons alive """
        
        query = "SELECT COUNT(activation_date) \
            FROM party_party \
            WHERE activation_date BETWEEN \
            %s AND %s and is_person=True and deceased is not TRUE"
         
        if (in_health_system):
            query = query + " and is_patient=True"
            
        cursor = Transaction().cursor
        cursor.execute(query,(start_date, end_date))
       
        res = cursor.fetchone()
        return(res)

    @classmethod
    def get_new_births(cls, start_date, end_date):
        """ Return birth certificates within that period """
        
        query = "SELECT COUNT(dob) \
            FROM gnuhealth_birth_certificate \
            WHERE dob BETWEEN \
            %s AND %s"
            
        cursor = Transaction().cursor
        cursor.execute(query,(start_date, end_date))
       
        res = cursor.fetchone()
        return(res)

    @classmethod
    def get_new_deaths(cls, start_date, end_date):
        """ Return death certificates within that period """
        """ Truncate the timestamp of DoD to match a whole day"""
    
        query = "SELECT COUNT(dod) \
            FROM gnuhealth_death_certificate \
            WHERE date_trunc('day', dod) BETWEEN \
            %s AND %s"
            
        cursor = Transaction().cursor
        cursor.execute(query,(start_date, end_date))
       
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

        localcontext[''.join(['p','total_','f'])] = \
            cls.get_population (None,None,'f', total=True)

        localcontext[''.join(['p','total_','m'])] = \
            cls.get_population (None,None,'m', total=True)
        
        # Build the Population Pyramid for registered people

        for age_group in range (0,21):
            date1 = today - relativedelta(years=(age_group*5))
            date2 = today - relativedelta(years=((age_group*5)+5), days=-1)
            
            localcontext[''.join(['p',str(age_group),'f'])] = \
                cls.get_population (date1,date2,'f', total=False)
            localcontext[''.join(['p',str(age_group),'m'])] = \
                cls.get_population (date1,date2,'m', total=False)


        # Count those lucky over 105 years old :)
        date1 = today - relativedelta(years=105)
        date2 = today - relativedelta(years=200)

        localcontext['over105f'] = \
            cls.get_population (date1,date2,'f', total=False)
        localcontext['over105m'] = \
            cls.get_population (date1,date2,'m', total=False)

        
        # Count registered people, and those within the system of health
        localcontext['new_people'] = \
            cls.get_new_people(start_date, end_date, False)
        localcontext['new_in_health_system'] = \
            cls.get_new_people(start_date, end_date, in_health_system=True)

        # New births
        localcontext['new_births'] = \
            cls.get_new_births(start_date, end_date)
        
        # New deaths
        localcontext['new_deaths'] = \
            cls.get_new_deaths(start_date, end_date)

        return super(InstitutionSummaryReport, cls).parse(report,
            objects, data, localcontext)

