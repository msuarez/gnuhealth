import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class HealthGynecoTestCase(ModuleTestCase):
    '''
    Test Health Gyneco module.
    '''
    module = 'health_gyneco'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        HealthGynecoTestCase))
    return suite
