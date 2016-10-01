# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2008-2016 Luis Falcon <lfalcon@gnusolidario.org>
#    Copyright (C) 2011-2016 GNU Solidario <health@gnusolidario.org>
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


__all__ = ['InsurancePlanProductPolicy','InsurancePlan']


class InsurancePlanProductPolicy(ModelSQL, ModelView):
    'Policy associated to the product on the insurance plan'
    __name__ = "gnuhealth.insurance.plan.product.policy"

    plan = fields.Many2One('gnuhealth.insurance.plan',
        'Plan', )

    product = fields.Many2One('product.product',
        'Product', )
        
    discount = fields.Integer('Discount', )


class InsurancePlan(ModelSQL, ModelView):
    __name__ = "gnuhealth.insurance.plan"

    product_policy = fields.One2Many('gnuhealth.insurance.plan.product.policy',
        'plan','Policy')
