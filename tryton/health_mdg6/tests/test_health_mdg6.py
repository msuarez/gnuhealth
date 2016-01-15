import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class HealthMDG6TestCase(ModuleTestCase):
    '''
    Test Health MDG6 module.
    '''
    module = 'health_mdg6'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        HealthMDG6TestCase))
    return suite
