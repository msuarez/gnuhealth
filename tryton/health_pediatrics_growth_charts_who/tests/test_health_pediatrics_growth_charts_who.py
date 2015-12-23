import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class HealthPediatricsGrowthChartsWHOTestCase(ModuleTestCase):
    '''
    Test Health Pediatrics Growth Charts WHO module.
    '''
    module = 'health_pediatrics_growth_charts_who'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        HealthPediatricsGrowthChartsWHOTestCase))
    return suite
