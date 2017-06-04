# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2008-2017 Luis Falcon <falcon@gnu.org>
#    Copyright (C) 2011-2017 GNU Solidario <health@gnusolidario.org>
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
from datetime import date, datetime
from trytond.report import Report
from trytond.pool import Pool
from trytond.transaction import Transaction
from dateutil.relativedelta import relativedelta

__all__ = ['InstitutionSummaryReport']

class InstitutionSummaryReport(Report):
    __name__ = 'gnuhealth.summary.report'


    @classmethod
    def get_population_with_no_dob(cls):
        """ Return Total Number of living people in the system 
        without a date of birth"""
        cursor = Transaction().connection.cursor()

        # Check for entries without date of birth
        cursor.execute("SELECT COUNT(id) \
            FROM party_party WHERE is_person is TRUE and \
            deceased is not TRUE and dob is null")

        res = cursor.fetchone()[0]
    
        return(res)

    @classmethod
    def get_population(cls,date1,date2,gender,total):
        """ Return Total Number of living people in the system 
        segmented by age group and gender"""
        cursor = Transaction().connection.cursor()

        if (total):
            cursor.execute("SELECT COUNT(id) \
                FROM party_party WHERE \
                gender = %s and deceased is not TRUE",(gender))

        else:
            cursor.execute("SELECT COUNT(id) \
                FROM party_party \
                WHERE dob BETWEEN %s and %s AND \
                gender = %s  \
                and deceased is not TRUE" ,(date2, date1, gender))

       
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
            
        cursor = Transaction().connection.cursor()
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
            
        cursor = Transaction().connection.cursor()
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
            
        cursor = Transaction().connection.cursor() 
        cursor.execute(query,(start_date, end_date))
       
        res = cursor.fetchone()
        return(res)

    @classmethod
    def get_evaluations(cls, start_date, end_date, dx):
        """ Return evaluation info """
        
        Evaluation = Pool().get('gnuhealth.patient.evaluation')
        start_date = datetime.strptime(str(start_date), '%Y-%m-%d')
        end_date = datetime.strptime(str(end_date), '%Y-%m-%d')
        end_date += relativedelta(hours=+23,minutes=+59,seconds=+59)
        
        clause = [
            ('evaluation_start', '>=', start_date),
            ('evaluation_start', '<=', end_date),
            ]
                
        if dx:
            clause.append(('diagnosis', '=', dx))
            
        res = Evaluation.search(clause)
        
        return(res)

    @classmethod
    def count_evaluations(cls, start_date, end_date, dx):
        """ count diagnoses by groups """
        
        Evaluation = Pool().get('gnuhealth.patient.evaluation')
        start_date = datetime.strptime(str(start_date), '%Y-%m-%d')
        end_date = datetime.strptime(str(end_date), '%Y-%m-%d')
        end_date += relativedelta(hours=+23,minutes=+59,seconds=+59)
        
        clause = [
            ('evaluation_start', '>=', start_date),
            ('evaluation_start', '<=', end_date),
            ('diagnosis', '=', dx),
            ]

        res = Evaluation.search_count(clause)
        
        return(res)


    @classmethod
    def get_context(cls, records, data):
        Patient = Pool().get('gnuhealth.patient')
        Evaluation = Pool().get('gnuhealth.patient.evaluation')

        context = super(InstitutionSummaryReport, cls).get_context(records, data)

        start_date = data['start_date']
        end_date = data['end_date']

        demographics = data['demographics']
        context['demographics'] = data['demographics']

        patient_evaluations = data['patient_evaluations']
        context['patient_evaluations'] = data['patient_evaluations']
        
        context['start_date'] = data['start_date']
        context['end_date'] = data['end_date']

        # Demographics
        today = date.today()

        context[''.join(['p','total_','f'])] = \
            cls.get_population (None,None,'f', total=True)

        context[''.join(['p','total_','m'])] = \
            cls.get_population (None,None,'m', total=True)
        
        # Living people with NO date of birth
        context['no_dob'] = \
            cls.get_population_with_no_dob()

        # Build the Population Pyramid for registered people

        for age_group in range (0,21):
            date1 = today - relativedelta(years=(age_group*5))
            date2 = today - relativedelta(years=((age_group*5)+5), days=-1)
            
            context[''.join(['p',str(age_group),'f'])] = \
                cls.get_population (date1,date2,'f', total=False)
            context[''.join(['p',str(age_group),'m'])] = \
                cls.get_population (date1,date2,'m', total=False)


        # Count those lucky over 105 years old :)
        date1 = today - relativedelta(years=105)
        date2 = today - relativedelta(years=200)

        context['over105f'] = \
            cls.get_population (date1,date2,'f', total=False)
        context['over105m'] = \
            cls.get_population (date1,date2,'m', total=False)

        
        # Count registered people, and those within the system of health
        context['new_people'] = \
            cls.get_new_people(start_date, end_date, False)
        context['new_in_health_system'] = \
            cls.get_new_people(start_date, end_date, in_health_system=True)

        # New births
        context['new_births'] = \
            cls.get_new_births(start_date, end_date)
        
        # New deaths
        context['new_deaths'] = \
            cls.get_new_deaths(start_date, end_date)

        # Get evaluations within the specified date range
        
        context['evaluations'] = \
            cls.get_evaluations(start_date, end_date, None)
        
        evaluations = cls.get_evaluations(start_date, end_date, None)
        
        eval_dx =[]
        non_dx_eval = 0
        non_age_eval = 0
        eval_f = 0
        eval_m = 0
        
        # Global Evaluation info
        for evaluation in evaluations:
            if evaluation.diagnosis:
                eval_dx.append(evaluation.diagnosis)
            else:
                # Increase the evaluations without Dx counter
                non_dx_eval += 1
            if (evaluation.gender == 'f'):
                eval_f +=1
            else:
                eval_m +=1

            if not evaluation.computed_age:
                non_age_eval +=1
        
        context['non_dx_eval'] = non_dx_eval
        context['eval_num'] = len(evaluations)
        context['eval_f'] = eval_f
        context['eval_m'] = eval_m
        context['non_age_eval'] = non_age_eval
        
        # Create a set to work with single diagnoses
        # removing duplicate entries from eval_dx
        
        unique_dx = set(eval_dx)
        
        summary_dx = []
        # Traverse the evaluations with Dx to get the key values
        for dx in unique_dx:
            # unique_evaluations holds the evaluations with
            # the same diagnostic
            unique_evaluations = cls.get_evaluations(start_date, end_date, dx)

            group_1 = group_2 = group_3 = group_4 = group_5 = 0
            group_1f = group_2f = group_3f = group_4f = group_5f = 0

            total_evals = len(unique_evaluations)
            
            new_conditions = 0
            
            for unique_eval in unique_evaluations:
                
                if (unique_eval.computed_age):
                    
                    #Strip to get the raw year
                    age = int(unique_eval.computed_age.split(' ')[0][:-1])
                    
                    
                    # Age groups in this diagnostic
                    if (age < 5):
                        group_1 += 1
                        if (unique_eval.gender == 'f'):
                            group_1f += 1
                    if (age in range(5,14)):
                        group_2 += 1
                        if (unique_eval.gender == 'f'):
                            group_2f += 1
                    if (age in range(15,45)):
                        group_3 += 1
                        if (unique_eval.gender == 'f'):
                            group_3f += 1
                    if (age in range(46,60)):
                        group_4 += 1
                        if (unique_eval.gender == 'f'):
                            group_4f += 1
                    if (age > 60):
                        group_5 += 1
                        if (unique_eval.gender == 'f'):
                            group_5f += 1

                # Check for new conditions vs followup / chronic checkups 
                # in the evaluation with a particular diagnosis
                
                if (unique_eval.visit_type == 'new'):
                    new_conditions += 1
                    
            eval_dx = {'diagnosis': unique_eval.diagnosis.rec_name,
                'age_group_1': group_1, 'age_group_1f': group_1f,
                'age_group_2': group_2, 'age_group_2f': group_2f,
                'age_group_3': group_3, 'age_group_3f': group_3f,
                'age_group_4': group_4, 'age_group_4f': group_4f,
                'age_group_5': group_5, 'age_group_5f': group_5f,
                'total': total_evals, 'new_conditions' : new_conditions,
                }
                
            # Append into the report list the resulting
            # dictionary entry
            
            summary_dx.append(eval_dx)
        
        context['summary_dx'] = summary_dx

        return context
