import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class HealthOphthalmologyTestCase(ModuleTestCase):
    '''
    Test Health module.
    '''
    module = 'health_ophthalmology'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        HealthOphthalmologyTestCase))
    return suite
