# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    MODULE : Diagnostic Imaging
#
#    Copyright (C) 2008-2019 Luis Falcon <lfalcon@gnuhealth.org>
#    Copyright (C) 2011-2019 GNU Solidario <health@gnusolidario.org>
#    Copyright (C) 2013  Sebastián Marro <smarro@thymbra.com>
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
from trytond.model import Workflow, ModelView, ModelSingleton, ModelSQL, \
    fields, Unique, ValueMixin
from trytond.pyson import Eval
from trytond.pool import Pool
from trytond import backend
from trytond.tools.multivalue import migrate_property


__all__ = [
    'GnuHealthSequences', 'GnuHealthSequenceSetup','ImagingTestType', 
    'ImagingTest', 'ImagingTestRequest', 'ImagingTestResult']

sequences = ['imaging_request_sequence', 'imaging_sequence']


class GnuHealthSequences(ModelSingleton, ModelSQL, ModelView):
    "GNU Health Sequences"
    __name__ = "gnuhealth.sequences"

    imaging_request_sequence = fields.MultiValue(
        fields.Many2One(
            'ir.sequence',
            'Imaging Request Sequence',
            domain=[('code', '=', 'gnuhealth.imaging.test.request')],
            required=True))

    imaging_sequence = fields.MultiValue(
        fields.Many2One(
            'ir.sequence',
            'Imaging Sequence',
            domain=[('code', '=', 'gnuhealth.imaging.test.result')],
            required=True))


    @classmethod
    def multivalue_model(cls, field):
        pool = Pool()

        if field in sequences:
            return pool.get('gnuhealth.sequence.setup')
        return super(GnuHealthSequences, cls).multivalue_model(field)


    @classmethod
    def default_imaging_request_sequence(cls):
        return cls.multivalue_model(
            'imaging_request_sequence').default_imaging_request_sequence()

    @classmethod
    def default_imaging_sequence(cls):
        return cls.multivalue_model(
            'imaging_sequence').default_imaging_sequence()

# SEQUENCE SETUP
class GnuHealthSequenceSetup(ModelSQL, ValueMixin):
    'GNU Health Sequences Setup'
    __name__ = 'gnuhealth.sequence.setup'

    imaging_request_sequence = fields.Many2One('ir.sequence', 
        'Imaging Request Sequence', required=True,
        domain=[('code', '=', 'gnuhealth.imaging.test.request')])


    imaging_sequence = fields.Many2One('ir.sequence', 
        'Imaging Result Sequence', required=True,
        domain=[('code', '=', 'gnuhealth.imaging.test.result')])
  
    @classmethod
    def __register__(cls, module_name):
        TableHandler = backend.get('TableHandler')
        exist = TableHandler.table_exist(cls._table)

        super(GnuHealthSequenceSetup, cls).__register__(module_name)

        if not exist:
            cls._migrate_property([], [], [])

    @classmethod
    def _migrate_property(cls, field_names, value_names, fields):
        field_names.extend(sequences)
        value_names.extend(sequences)
        migrate_property(
            'gnuhealth.sequences', field_names, cls, value_names,
            fields=fields)

    @classmethod
    def default_imaging_request_sequence(cls):
        pool = Pool()
        ModelData = pool.get('ir.model.data')
        return ModelData.get_id(
            'health_imaging', 'seq_gnuhealth_imaging_test_request')

    @classmethod
    def default_imaging_sequence(cls):
        pool = Pool()
        ModelData = pool.get('ir.model.data')
        return ModelData.get_id(
            'health_imaging', 'seq_gnuhealth_imaging_test')
    
# END SEQUENCE SETUP , MIGRATION FROM FIELDS.PROPERTY


class ImagingTestType(ModelSQL, ModelView):
    'Imaging Test Type'
    __name__ = 'gnuhealth.imaging.test.type'

    code = fields.Char('Code', required=True)
    name = fields.Char('Name', required=True)


class ImagingTest(ModelSQL, ModelView):
    'Imaging Test'
    __name__ = 'gnuhealth.imaging.test'

    code = fields.Char('Code', required=True)
    name = fields.Char('Name', required=True)
    test_type = fields.Many2One(
        'gnuhealth.imaging.test.type', 'Type',
        required=True)
    product = fields.Many2One('product.product', 'Service', required=True)

    active = fields.Boolean('Active', select=True)

    @staticmethod
    def default_active():
        return True

class ImagingTestRequest(Workflow, ModelSQL, ModelView):
    'Imaging Test Request'
    __name__ = 'gnuhealth.imaging.test.request'

    patient = fields.Many2One('gnuhealth.patient', 'Patient', required=True)
    date = fields.DateTime('Date', required=True)
    requested_test = fields.Many2One(
        'gnuhealth.imaging.test', 'Test',
        required=True)
    doctor = fields.Many2One('gnuhealth.healthprofessional', 'Doctor', required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('requested', 'Requested'),
        ('done', 'Done'),
        ], 'State', readonly=True)
    comment = fields.Text('Comment')
    request = fields.Char('Request', readonly=True)
    urgent = fields.Boolean('Urgent')

    @classmethod
    def __setup__(cls):
        super(ImagingTestRequest, cls).__setup__()
        cls._transitions |= set((
            ('draft', 'requested'),
            ('requested', 'done')
        ))
        cls._buttons.update({
            'requested': {
                'invisible': ~Eval('state').in_(['draft']),
                },
            'generate_results': {
                'invisible': ~Eval('state').in_(['requested'])
                }
            })
        cls._order.insert(0, ('date', 'DESC'))
        cls._order.insert(1, ('request', 'DESC'))

    @staticmethod
    def default_date():
        return datetime.now()

    @staticmethod
    def default_state():
        return 'draft'

    @staticmethod
    def default_doctor():
        pool = Pool()
        HealthProf= pool.get('gnuhealth.healthprofessional')
        hp = HealthProf.get_health_professional()
        return hp

    @classmethod
    def create(cls, vlist):
        Sequence = Pool().get('ir.sequence')
        Config = Pool().get('gnuhealth.sequences')

        vlist = [x.copy() for x in vlist]
        for values in vlist:
            if not values.get('request'):
                config = Config(1)
                values['request'] = Sequence.get_id(
                    config.imaging_request_sequence.id)

        return super(ImagingTestRequest, cls).create(vlist)

    @classmethod
    def copy(cls, tests, default=None):
        if default is None:
            default = {}
        default = default.copy()
        default['request'] = None
        default['date'] = cls.default_date()
        return super(ImagingTestRequest, cls).copy(tests, default=default)

    @classmethod
    @ModelView.button
    @Workflow.transition('requested')
    def requested(cls, requests):
        pass

    @classmethod
    @ModelView.button_action('health_imaging.wizard_generate_result')
    def generate_results(cls, requests):
        pass

    @classmethod
    @Workflow.transition('done')
    def done(cls, requests):
        pass


class ImagingTestResult(ModelSQL, ModelView):
    'Imaging Test Result'
    __name__ = 'gnuhealth.imaging.test.result'

    patient = fields.Many2One('gnuhealth.patient', 'Patient', readonly=True)
    number = fields.Char('Number', readonly=True)
    date = fields.DateTime('Date', required=True)
    request_date = fields.DateTime('Requested Date', readonly=True)
    requested_test = fields.Many2One(
        'gnuhealth.imaging.test', 'Test',
        required=True)
    request = fields.Many2One(
        'gnuhealth.imaging.test.request', 'Request',
        readonly=True)
    doctor = fields.Many2One('gnuhealth.healthprofessional', 'Doctor', required=True)
    comment = fields.Text('Comment')
    images = fields.One2Many('ir.attachment', 'resource', 'Images')

    @classmethod
    def create(cls, vlist):
        Sequence = Pool().get('ir.sequence')
        Config = Pool().get('gnuhealth.sequences')

        vlist = [x.copy() for x in vlist]
        for values in vlist:
            if not values.get('name'):
                config = Config(1)
                values['number'] = Sequence.get_id(
                    config.imaging_sequence.id)

        return super(ImagingTestResult, cls).create(vlist)

    @classmethod
    def search_rec_name(cls, name, clause):
        if clause[1].startswith('!') or clause[1].startswith('not '):
            bool_op = 'AND'
        else:
            bool_op = 'OR'
        return [bool_op,
            ('patient',) + tuple(clause[1:]),
            ('number',) + tuple(clause[1:]),
            ]

    @classmethod
    def __setup__(cls):
        super(ImagingTestResult, cls).__setup__()
        t = cls.__table__()
        cls._sql_constraints = [
            ('number_uniq', Unique(t, t.number),
             'The test ID code must be unique')
        ]
        cls._order.insert(0, ('date', 'DESC'))
