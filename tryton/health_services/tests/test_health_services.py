import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class HealthServicesTestCase(ModuleTestCase):
    '''
    Test Health Services module.
    '''
    module = 'health_services'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        HealthServicesTestCase))
    return suite
