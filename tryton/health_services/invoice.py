#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta
from trytond import backend

__all__ = ['Invoice', 'InvoiceLine']

class Invoice(metaclass=PoolMeta):
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


class InvoiceLine(metaclass=PoolMeta):
    __name__ = 'account.invoice.line'

    @classmethod
    def _get_origin(cls):
        return super(InvoiceLine, cls)._get_origin() + [
            'gnuhealth.health_service.line'
            ]
