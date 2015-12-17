import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class HealthSurgeryTestCase(ModuleTestCase):
    '''
    Test Health Surgery module.
    '''
    module = 'health_surgery'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        HealthSurgeryTestCase))
    return suite
