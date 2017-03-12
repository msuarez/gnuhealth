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
from datetime import date
from trytond.report import Report
from trytond.pool import Pool
from trytond.transaction import Transaction
from dateutil.relativedelta import relativedelta

__all__ = ['ImmunizationStatusReport']

class ImmunizationStatusReport(Report):
    __name__ = 'gnuhealth.immunization_status_report'


    @classmethod
    def get_context(cls, records, data):
        Sched = Pool().get('gnuhealth.immunization_schedule')
        Patient = Pool().get('gnuhealth.patient')
        patient = Patient(data['patient_id'])
        
        context = super(ImmunizationStatusReport, cls).get_context(records,
            data)
            
        context['patient'] = patient
        sched = Sched(data['immunization_schedule_id'])
        
        context['immunization_schedule'] = sched

        immunizations_to_check = \
            cls.get_immunizations_for_age(patient, sched)
        
        immunization_status = \
            cls.verify_status(immunizations_to_check)
        
        context['immunization_status'] = immunization_status
        
        return context 

    @classmethod
    def get_immunizations_for_age(cls,patient,immunization_schedule):
        
        immunizations_for_age = []
        
        for vaccine in immunization_schedule.vaccines:
            
            for dose in vaccine.doses:
                dose_number, dose_age, age_unit = dose.dose_number, \
                    dose.age_dose, dose.age_unit
                
                #TODO : For 3.2, use the generic raw_age argument
                # from compute_age_from_dates

                p_age = [patient.age.split(' ')[0][:-1], 
                    patient.age.split(' ')[1][:-1], 
                    patient.age.split(' ')[2][:-1]]                

                #Age of the person in years and months
                pyears,pmonths = int(p_age[0]),int(p_age[1])

                pmonths = (pyears*12)+pmonths
                
                if ((age_unit == 'months' and pmonths >= dose_age) or
                    (age_unit == 'years' and pyears >= dose_age)):
                        immunization_info = {
                            'patient' : patient,
                            'vaccine' : vaccine,
                            'dose' : dose_number,
                            'dose_age' : dose_age,
                            'age_unit' : age_unit,
                            'status' : None}
                        
                        # Add to the list of this person immunization check
                        immunizations_for_age.append(immunization_info)

        return immunizations_for_age

    @classmethod
    def verify_status(cls,immunizations_to_check):
        Vaccination = Pool().get('gnuhealth.vaccination')

        result = []
        for immunization in immunizations_to_check:
            immunization['status'] = "missing"
            res = Vaccination.search_count([
                ('name', '=', immunization['patient']),
                ('dose', '=', immunization['dose']),
                ('vaccine.name', '=', immunization['vaccine'].vaccine.name),
                ])
           
            if res:
                immunization['status'] = 'ok'
            
            result.append(immunization)
        
        return result
        

