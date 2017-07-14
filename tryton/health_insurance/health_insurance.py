# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2008-2017 Luis Falcon <lfalcon@gnusolidario.org>
#    Copyright (C) 2011-2017 GNU Solidario <health@gnusolidario.org>
#
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

from trytond.model import ModelView, ModelSQL, ModelSingleton, fields
from datetime import datetime
from trytond.pool import Pool
from trytond.transaction import Transaction
from trytond.pyson import Eval, Not, Bool, PYSONEncoder, Equal, And, Or, If


__all__ = ['InsurancePlanProductPolicy','InsurancePlan','HealthService']


class InsurancePlanProductPolicy(ModelSQL, ModelView):
    'Policy associated to the product on the insurance plan'
    __name__ = "gnuhealth.insurance.plan.product.policy"

    plan = fields.Many2One('gnuhealth.insurance.plan',
        'Plan', required=True)

    product = fields.Many2One('product.product',
        'Product', )

    product_category = fields.Many2One('product.category',
        'Category', )
        
    discount = fields.Float('Discount', digits=(3,2), 
        help="Discount in Percentage", required=True)

    @classmethod
    def validate(cls, policies):
        super(InsurancePlanProductPolicy, cls).validate(policies)
        for policy in policies:
            policy.validate_discount()
            policy.validate_policy_elements()

    def validate_discount(self):
        if (self.discount < 0 or self.discount > 100):
            self.raise_user_error('discount_pct_out_of_range')

    def validate_policy_elements(self):
        if (not self.product and not self.product_category):
            self.raise_user_error('discount_need_and_element')

    @classmethod
    def __setup__(cls):
        super(InsurancePlanProductPolicy, cls).__setup__()

        cls._error_messages.update({
            'discount_pct_out_of_range':
                'Percentage out of range [0-100]',
                    'discount_need_and_element':
                'You need a product or category',
        })


class InsurancePlan(ModelSQL, ModelView):
    __name__ = "gnuhealth.insurance.plan"
    _rec_name = 'name'

    product_policy = fields.One2Many('gnuhealth.insurance.plan.product.policy',
        'plan','Policy')

class HealthService(ModelSQL, ModelView):
    __name__ = 'gnuhealth.health_service'

    insurance_holder = fields.Many2One('party.party','Insurance Holder',
        help="Insurance Policy Holder")

    insurance_plan = fields.Many2One('gnuhealth.insurance',
            'Plan', 
            domain=[('name', '=', Eval('insurance_holder'))],
            depends=['insurance_holder'])

 
    # Set the insurance holder upon entering the 
    @fields.depends('patient')
    def on_change_patient(self):
        insurance_holder=None
        if self.patient:
            self.insurance_holder = self.patient.name
