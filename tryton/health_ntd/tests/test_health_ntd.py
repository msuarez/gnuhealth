import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class HealthNTDTestCase(ModuleTestCase):
    '''
    Test Health NTD module.
    '''
    module = 'health_ntd'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        HealthNTDTestCase))
    return suite
