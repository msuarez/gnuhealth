# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2011  Adrián Bernardi, Mario Puntin
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
from datetime import timedelta
from trytond.model import ModelView, ModelSQL, fields
from trytond.pyson import Eval, Equal


class PatientData(ModelSQL, ModelView):
    _name = 'gnuhealth.patient'
    _description = __doc__

    # TODO: Trytonize field type
    #receivable = fields.Related('name', 'credit', type='float', string='Receivable',
        #help='Total amount this patient owes you', readonly=True)

PatientData()


class Appointment(ModelSQL, ModelView):
    'Add Invoicing information to the Appointment'
    _name = 'gnuhealth.appointment'
    _description = __doc__

    def copy(self, ids, default=None):
        if default is None:
            default = {}
        default.update({'validity_status': 'tobe'})
        return super(Appointment, self).copy(ids, default=default)

    def on_change_appointment_date(self, apt_date):
        if apt_date:
            validity_date = apt_date['appointment_date']
            validity_date += timedelta(days=7)
            return {'appointment_validity_date': validity_date}
        return {}

    no_invoice = fields.Boolean('Invoice exempt',
        states={'invisible': Equal(Eval('validity_status'), 'invoiced')},
        depends=['validity_status'])
    appointment_date = fields.DateTime('Date and Time',
        on_change=['appointment_date'])
    appointment_validity_date = fields.DateTime('Validity Date')
    validity_status = fields.Selection([
        ('invoiced', 'Invoiced'),
        ('tobe', 'To be Invoiced'),
        ], 'Status')

    def default_no_invoice(self):
        return True

    def default_validity_status(self):
        return 'tobe'

Appointment()


class LabTest(ModelSQL, ModelView):
    'Add Invoicing information to the Lab Test'
    _name = 'gnuhealth.patient.lab.test'
    _description = __doc__

    no_invoice = fields.Boolean('Invoice exempt',
        states={'invisible': Equal(Eval('invoice_status'), 'invoiced')},
        depends=['invoice_status'])
    invoice_status = fields.Selection([
        ('invoiced', 'Invoiced'),
        ('tobe', 'To be Invoiced'),
        ], 'Invoice Status')

    def default_no_invoice(self):
        return True

    def default_invoice_status(self):
        return 'tobe'

LabTest()


class PatientPrescriptionOrder(ModelSQL, ModelView):
    'Add Invoicing information to the Patient Prescription Order'
    _name = 'gnuhealth.prescription.order'
    _description = __doc__

    no_invoice = fields.Boolean('Invoice exempt',
        states={'invisible': Equal(Eval('invoice_status'), 'invoiced')},
        depends=['invoice_status'])
    invoice_status = fields.Selection([
        ('invoiced', 'Invoiced'),
        ('tobe', 'To be Invoiced'),
        ], 'Invoice Status')

    def default_no_invoice(self):
        return True

    def default_invoice_status(self):
        return 'tobe'

PatientPrescriptionOrder()
