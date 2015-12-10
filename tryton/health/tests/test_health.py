import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class HealthTestCase(ModuleTestCase):
    '''
    Test Health module.
    '''
    module = 'health'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        HealthTestCase))
    return suite
