import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class HealthInsuranceTestCase(ModuleTestCase):
    '''
    Test Health Insurance module.
    '''
    module = 'health_insurance'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        HealthInsuranceTestCase))
    return suite
