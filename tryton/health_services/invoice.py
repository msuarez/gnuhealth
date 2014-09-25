#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta

__all__ = ['Invoice']
__metaclass__ = PoolMeta


class Invoice:
    __name__ = 'account.invoice'
    health_service = fields.Many2One('gnuhealth.health_service',
            'Health Service')
    patient = fields.Many2One('gnuhealth.patient', 'Patient')

    @classmethod
    def __setup__(cls):
        super(Invoice, cls).__setup__()
