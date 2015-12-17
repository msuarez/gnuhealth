import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class HealthLifestyleTestCase(ModuleTestCase):
    '''
    Test Health Lifestyle module.
    '''
    module = 'health_lifestyle'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        HealthLifestyleTestCase))
    return suite
