import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class HealthHistoryTestCase(ModuleTestCase):
    '''
    Test Health History module.
    '''
    module = 'health_history'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        HealthHistoryTestCase))
    return suite
