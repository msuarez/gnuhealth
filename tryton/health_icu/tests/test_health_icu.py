import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class HealthICUTestCase(ModuleTestCase):
    '''
    Test Health ICU module.
    '''
    module = 'health_icu'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        HealthICUTestCase))
    return suite
