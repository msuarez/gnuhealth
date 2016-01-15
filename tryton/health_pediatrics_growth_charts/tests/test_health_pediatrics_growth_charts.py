import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class HealthPediatricsGrowthChartsTestCase(ModuleTestCase):
    '''
    Test Health Pediatrics Growth Charts module.
    '''
    module = 'health_pediatrics_growth_charts'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        HealthPediatricsGrowthChartsTestCase))
    return suite
