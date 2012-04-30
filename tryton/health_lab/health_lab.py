# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2008-2012  Luis Falcon <lfalcon@gnusolidario.org>
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
from datetime import datetime
from trytond.model import ModelView, ModelSingleton, ModelSQL, fields
from trytond.transaction import Transaction

from trytond.pool import Pool


class GnuHealthSequences(ModelSingleton, ModelSQL, ModelView):
    "Standard Sequences for GNU Health"

    _description = __doc__
    _name = "gnuhealth.sequences"

    lab_sequence = fields.Property(fields.Many2One('ir.sequence',
        'Lab Sequence', domain=[('code', '=', 'gnuhealth.lab')],
        required=True))

GnuHealthSequences()

class PatientData(ModelSQL, ModelView):
    'Patient lab tests'
    _name = 'gnuhealth.patient'
    _description = __doc__

    lab_test_ids = fields.One2Many('gnuhealth.patient.lab.test', 'patient_id',
        'Lab Tests Required')

PatientData()


class TestType(ModelSQL, ModelView):
    'Type of Lab test'
    _name = 'gnuhealth.lab.test_type'
    _description = __doc__

    name = fields.Char('Test', 
        help="Test type, eg X-Ray, hemogram,biopsy...", required=True, select=True)
    code = fields.Char('Code', 
        help="Short name - code for the test", required=True, select=True)
    info = fields.Text('Description')
    product_id = fields.Many2One('product.product', 'Service', required=True)
    critearea = fields.One2Many('gnuhealth.lab.test.critearea', 'test_type_id',
        'Test Cases')

    def __init__(self):
        super(TestType, self).__init__()
        self._sql_constraints = [
            ('code_uniq', 'unique(name)', 'The Lab Test code must be unique'),
        ]

TestType()


class Lab(ModelSQL, ModelView):
    'Lab Test'
    _name = 'gnuhealth.lab'
    _description = __doc__

    name = fields.Char('ID', help="Lab result ID",readonly=True)
    test = fields.Many2One('gnuhealth.lab.test_type', 'Test type',
        help="Lab test type", required=True, select=True)
    patient = fields.Many2One('gnuhealth.patient', 'Patient',
     help="Patient ID", required=True, select=True)
    pathologist = fields.Many2One('gnuhealth.physician', 'Pathologist',
        help="Pathologist", select=True)
    requestor = fields.Many2One('gnuhealth.physician', 'Physician',
        help="Doctor who requested the test", select=True)
    results = fields.Text('Results')
    diagnosis = fields.Text('Diagnosis')
    critearea = fields.One2Many('gnuhealth.lab.test.critearea', 'gnuhealth_lab_id',
        'Lab Test Critearea')
    date_requested = fields.DateTime('Date requested', required=True, select=True)
    date_analysis = fields.DateTime('Date of the Analysis', select=True)

    def __init__(self):
        super(Lab, self).__init__()
        self._sql_constraints += [
            ('id_uniq', 'unique (name)', 'The test ID code must be unique'),
        ]

    def default_date_requested(self):
        return datetime.now()

    def default_analysis(self):
        return datetime.now()

    def create(self, values):
        sequence_obj = Pool().get('ir.sequence')
        config_obj = Pool().get('gnuhealth.sequences')

        values = values.copy()
        if not values.get('name'):
            config = config_obj.browse(1)
            values['name'] = sequence_obj.get_id(
            config.lab_sequence.id)

        return super(Lab, self).create(values)

Lab()


class GnuHealthLabTestUnits(ModelSQL, ModelView):
    'Lab Test Units'
    _name = 'gnuhealth.lab.test.units'
    _description = __doc__

    name = fields.Char('Unit', select=True)
    code = fields.Char('Code', select=True)

    def __init__(self):
        super(GnuHealthLabTestUnits, self).__init__()
        self._sql_constraints = [
            ('name_uniq', 'unique(name)', 'The Unit name must be unique'),
        ]

GnuHealthLabTestUnits()


class GnuHealthTestCritearea(ModelSQL, ModelView):
    'Lab Test Critearea'
    _name = 'gnuhealth.lab.test.critearea'
    _description = __doc__

    name = fields.Char('Analyte', required=True, select=True)
    excluded = fields.Boolean('Excluded',help='Select this option when' \
        ' this analyte is excluded from the test')
    result = fields.Float('Value')
    result_text = fields.Char('Result - Text',help='Non-numeric results. For example '\
        'qualitative values, morphological, colors ...')
    remarks = fields.Char('Remarks')
    normal_range = fields.Text('Reference')
    lower_limit = fields.Float ('Lower Limit')
    upper_limit = fields.Float ('Upper Limit')
    warning = fields.Boolean('Warn',help='Warns the patient about this analyte result' \
        ' It is useful to contextualize the result to each patient status ' \
        ' like age, sex, comorbidities, ...',
         on_change_with=['result', 'lower_limit', 'upper_limit'])
    units = fields.Many2One('gnuhealth.lab.test.units', 'Units')
    test_type_id = fields.Many2One('gnuhealth.lab.test_type', 'Test type',
     select=True)
    gnuhealth_lab_id = fields.Many2One('gnuhealth.lab', 'Test Cases', select=True)
    sequence = fields.Integer('Sequence')

    def __init__(self):
        super(GnuHealthTestCritearea, self).__init__()
        self._order.insert(0, ('sequence', 'ASC'))

    def default_sequence(self):
        return 1

    def default_excluded(self):
        return False
        
    def on_change_with_warning(self, vals):
        lower_limit = vals.get('lower_limit')
        upper_limit = vals.get('upper_limit')
        result = vals.get ('result')
        if (result < lower_limit or result > upper_limit):
            warning = True
        else:
            warning = False
        return warning
        

GnuHealthTestCritearea()


class GnuHealthPatientLabTest(ModelSQL, ModelView):
    'Patient Lab Test'
    _name = 'gnuhealth.patient.lab.test'
    _description = __doc__

    name = fields.Many2One('gnuhealth.lab.test_type', 'Test Type', required=True,
     select=True)
    date = fields.DateTime('Date', select=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('tested', 'Tested'),
        ('ordered', 'Ordered'),       
        ('cancel', 'Cancel'),
        ], 'State', readonly=True, select=True)
    patient_id = fields.Many2One('gnuhealth.patient', 'Patient', required=True,
     select=True)
    doctor_id = fields.Many2One('gnuhealth.physician', 'Doctor',
        help="Doctor who Request the lab test.", select=True)

    def default_date(self):
        return datetime.now()

    def default_state(self):
        return 'draft'

    def default_doctor_id(self):
        user_obj = Pool().get('res.user')
        user = user_obj.browse(Transaction().user)
        uid = int(user.id)

        party_id = Pool().get('party.party').search([
                ('internal_user', '=', uid)])
        if party_id:
            dr_id = Pool().get('gnuhealth.physician').search([
                    ('name', '=', party_id[0])])
            if dr_id:
                return dr_id[0]
            else:
                raise Exception('There is no physician defined ' \
                                'for current user.')
        else:
            return False

GnuHealthPatientLabTest()
