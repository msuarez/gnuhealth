import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class HealthProfileTestCase(ModuleTestCase):
    '''
    Test Health Profile module.
    '''
    module = 'health_profile'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        HealthProfileTestCase))
    return suite
