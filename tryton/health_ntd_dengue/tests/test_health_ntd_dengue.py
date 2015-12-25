import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class HealthNTDDengueTestCase(ModuleTestCase):
    '''
    Test Health NTD Dengue module.
    '''
    module = 'health_ntd_dengue'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        HealthNTDDengueTestCase))
    return suite
