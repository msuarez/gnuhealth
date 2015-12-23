import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class HealthDisabilityTestCase(ModuleTestCase):
    '''
    Test Health Disability module.
    '''
    module = 'health_disability'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        HealthDisabilityTestCase))
    return suite
