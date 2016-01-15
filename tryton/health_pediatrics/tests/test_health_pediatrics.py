import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class HealthPediatricsTestCase(ModuleTestCase):
    '''
    Test Health Pediatrics module.
    '''
    module = 'health_pediatrics'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        HealthPediatricsTestCase))
    return suite
