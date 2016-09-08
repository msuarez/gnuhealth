import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class HealthISSTestCase(ModuleTestCase):
    '''
    Test Health ISS module.
    '''
    module = 'health_iss'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        HealthISSTestCase))
    return suite
