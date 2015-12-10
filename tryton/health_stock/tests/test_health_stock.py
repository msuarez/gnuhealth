import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class HealthStockTestCase(ModuleTestCase):
    '''
    Test HealthStock module.
    '''
    module = 'health_stock'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        HealthStockTestCase))
    return suite
