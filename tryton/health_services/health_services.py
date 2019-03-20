# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2008-2019 Luis Falcon <lfalcon@gnusolidario.org>
#    Copyright (C) 2011-2019 GNU Solidario <health@gnusolidario.org>
#
#    Copyright (C) 2011  Adrián Bernardi, Mario Puntin (health_invoice)
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
import datetime
from trytond.model import ModelView, ModelSQL, fields, ModelSingleton, \
    Unique, ValueMixin
from trytond.transaction import Transaction
from trytond.pyson import Eval, Equal
from trytond.pool import Pool
from trytond import backend
from trytond.tools.multivalue import migrate_property


__all__ = ['GnuHealthSequences', 'GnuHealthSequenceSetup',
    'HealthService', 'HealthServiceLine', 'PatientPrescriptionOrder']

sequences = ['health_service_sequence']

class GnuHealthSequences(ModelSingleton, ModelSQL, ModelView):
    "Standard Sequences for GNU Health"
    __name__ = "gnuhealth.sequences"

    health_service_sequence = fields.MultiValue(fields.Many2One('ir.sequence',
        'Health Service Sequence', domain=[
            ('code', '=', 'gnuhealth.health_service')
        ], required=True))


    @classmethod
    def multivalue_model(cls, field):
        pool = Pool()

        if field in sequences:
            return pool.get('gnuhealth.sequence.setup')
        return super(GnuHealthSequences, cls).multivalue_model(field)

    @classmethod
    def default_health_service_sequence(cls):
        return cls.multivalue_model(
            'health_service_sequence').default_health_service_sequence()


# SEQUENCE SETUP
class GnuHealthSequenceSetup(ModelSQL, ValueMixin):
    'GNU Health Sequences Setup'
    __name__ = 'gnuhealth.sequence.setup'

    health_service_sequence = fields.Many2One('ir.sequence', 
        'Health Service Sequence', required=True,
        domain=[('code', '=', 'gnuhealth.health_service')])

  
    @classmethod
    def __register__(cls, module_name):
        TableHandler = backend.get('TableHandler')
        exist = TableHandler.table_exist(cls._table)

        super(GnuHealthSequenceSetup, cls).__register__(module_name)

        if not exist:
            cls._migrate_MultiValue([], [], [])

    @classmethod
    def _migrate_property(cls, field_names, value_names, fields):
        field_names.extend(sequences)
        value_names.extend(sequences)
        migrate_property(
            'gnuhealth.sequences', field_names, cls, value_names,
            fields=fields)

    @classmethod
    def default_health_service_sequence(cls):
        pool = Pool()
        ModelData = pool.get('ir.model.data')
        return ModelData.get_id(
            'health_services', 'seq_gnuhealth_health_service')
    
# END SEQUENCE SETUP , MIGRATION FROM FIELDS.MultiValue


class HealthService(ModelSQL, ModelView):
    'Health Service'
    __name__ = 'gnuhealth.health_service'

    STATES = {'readonly': Eval('state') == 'invoiced'}

    name = fields.Char('ID', readonly=True)
    desc = fields.Char('Description')
    patient = fields.Many2One('gnuhealth.patient',
            'Patient', required=True,
            states=STATES)
    institution = fields.Many2One('gnuhealth.institution', 'Institution')
    company = fields.Many2One('company.company', 'Company')

    service_date = fields.Date('Date')
    service_line = fields.One2Many('gnuhealth.health_service.line',
        'name', 'Service Line', help="Service Line")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('invoiced', 'Invoiced'),
        ], 'State', readonly=True)
    invoice_to = fields.Many2One('party.party', 'Invoice to')

    @classmethod
    def __setup__(cls):
        super(HealthService, cls).__setup__()

        t = cls.__table__()
        cls._sql_constraints = [
            ('name_unique', Unique(t,t.name),
                'The Service ID must be unique'),
            ]
        cls._buttons.update({
            'button_set_to_draft': {'invisible': Equal(Eval('state'),
                'draft')}
            })

        cls._order.insert(0, ('state', 'ASC'))
        cls._order.insert(1, ('name', 'DESC'))

    @staticmethod
    def default_state():
        return 'draft'

    @staticmethod
    def default_company():
        return Transaction().context.get('company')

    @staticmethod
    def default_service_date():
        return datetime.date.today()

    @staticmethod
    def default_institution():
        HealthInst = Pool().get('gnuhealth.institution')
        institution = HealthInst.get_institution()
        return institution

    @classmethod
    @ModelView.button
    def button_set_to_draft(cls, services):
        cls.write(services, {'state': 'draft'})

    @classmethod
    def create(cls, vlist):
        Sequence = Pool().get('ir.sequence')
        Config = Pool().get('gnuhealth.sequences')

        vlist = [x.copy() for x in vlist]
        for values in vlist:
            if not values.get('name'):
                config = Config(1)
                values['name'] = Sequence.get_id(
                    config.health_service_sequence.id)
        return super(HealthService, cls).create(vlist)


class HealthServiceLine(ModelSQL, ModelView):
    'Health Service'
    __name__ = 'gnuhealth.health_service.line'

    name = fields.Many2One('gnuhealth.health_service', 'Service',
        readonly=True)
    desc = fields.Char('Description', required=True)
    appointment = fields.Many2One('gnuhealth.appointment', 'Appointment',
        help='Enter or select the date / ID of the appointment related to'
        ' this evaluation')
    to_invoice = fields.Boolean('Invoice')
    product = fields.Many2One('product.product', 'Product', required=True)
    qty = fields.Integer('Qty')
    from_date = fields.Date('From')
    to_date = fields.Date('To')

    @staticmethod
    def default_qty():
        return 1

    @staticmethod
    def default_to_invoice():
        return True

    @fields.depends('product', 'desc')
    def on_change_product(self, name=None):
        if self.product:
            self.desc = self.product.name


    @classmethod
    def validate(cls, services):
        super(HealthServiceLine, cls).validate(services)
        for service in services:
            service.validate_invoice_status()

    def validate_invoice_status(self):
        if (self.name):
            if (self.name.state == 'invoiced'):
                self.raise_user_error(
                    "This service has been invoiced.\n"
                    "You can no longer modify service lines.")


""" Add Prescription order charges to service model """

class PatientPrescriptionOrder(ModelSQL, ModelView):
    'Prescription Order'
    __name__ = 'gnuhealth.prescription.order'

    service = fields.Many2One(
        'gnuhealth.health_service', 'Service',
        domain=[('patient', '=', Eval('patient'))], depends=['patient'],
        states = {'readonly': Equal(Eval('state'), 'done')},
        help="Service document associated to this prescription")

    @classmethod
    def __setup__(cls):
        super(PatientPrescriptionOrder, cls).__setup__()
        cls._buttons.update({
            'update_service': {
                'readonly': Equal(Eval('state'), 'done'),
            },
            })


    @classmethod
    @ModelView.button
    def update_service(cls, prescriptions):
        pool = Pool()
        HealthService = pool.get('gnuhealth.health_service')

        hservice = []
        prescription = prescriptions[0]

        if not prescription.service:
            cls.raise_user_error("Need to associate a service !")

        service_data = {}
        service_lines = []

        # Add the prescription lines to the service document

        for line in prescription.prescription_line:
            service_lines.append(('create', [{
                'product': line.medicament.name.id,
                'desc': 'Prescription Line',
                'qty': line.quantity
                }]))

            
        hservice.append(prescription.service)
        
        description = "Services including " + \
            prescription.prescription_id
        
        service_data ['desc'] =  description
        service_data ['service_line'] = service_lines
                
        HealthService.write(hservice, service_data)
