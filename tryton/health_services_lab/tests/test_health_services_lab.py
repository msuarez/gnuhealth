import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class HealthServicesLabTestCase(ModuleTestCase):
    '''
    Test Health Services module.
    '''
    module = 'health_services_lab'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        HealthServicesLabTestCase))
    return suite
