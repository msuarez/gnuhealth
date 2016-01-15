#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta
from trytond.transaction import Transaction
from trytond import backend

__all__ = ['Invoice', 'InvoiceLine']
__metaclass__ = PoolMeta


class Invoice:
    __name__ = 'account.invoice'

    patient = fields.Function(
            fields.Many2One('gnuhealth.patient', 'Patient',
                help="Patient in the invoice"),
                'get_patient')

    health_service = fields.Function(
            fields.Many2One('gnuhealth.health_service', 'Health Service',
                help="The service entry"),
                'get_health_service', searcher='search_health_service')

    def get_patient(self, name):
        try:
            return self.lines[0].origin.name.patient.id
        except:
            return None

    def get_health_service(self, name):
        try:
            return self.lines[0].origin.name.id
        except:
            return None

    @classmethod
    def search_health_service(cls, name, clause):
        return [('lines.origin.name.id',
                    clause[1],
                    clause[2],
                    'gnuhealth.health_service.line')]


    @classmethod
    def __setup__(cls):
        super(Invoice, cls).__setup__()

    @classmethod
    def __register__(cls, module_name):
        cursor = Transaction().cursor
        TableHandler = backend.get('TableHandler')
        table = TableHandler(cursor, cls, module_name)

        # We retrieve the patient
        # from the invoice line origin
        if table.column_exist('patient'):
            table.drop_column('patient')

        # Similarly, we retrieve the health_service
        # from the invoice line origin
        if table.column_exist('health_service'):
            table.drop_column('health_service')

        super(Invoice, cls).__register__(module_name)

class InvoiceLine:
    __name__ = 'account.invoice.line'

    @classmethod
    def _get_origin(cls):
        return super(InvoiceLine, cls)._get_origin() + [
            'gnuhealth.health_service.line'
            ]
