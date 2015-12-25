import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class HealthNursingTestCase(ModuleTestCase):
    '''
    Test Health Nursing module.
    '''
    module = 'health_nursing'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        HealthNursingTestCase))
    return suite
