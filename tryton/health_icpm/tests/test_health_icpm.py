import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class HealthICPMTestCase(ModuleTestCase):
    '''
    Test Health ICPM module.
    '''
    module = 'health_icpm'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        HealthICPMTestCase))
    return suite
