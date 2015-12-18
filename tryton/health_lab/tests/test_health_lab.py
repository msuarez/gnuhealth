import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class HealthLabTestCase(ModuleTestCase):
    '''
    Test Health Lab module.
    '''
    module = 'health_lab'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        HealthLabTestCase))
    return suite
