import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class HealthReportingTestCase(ModuleTestCase):
    '''
    Test Health Reporting module.
    '''
    module = 'health_reporting'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        HealthReportingTestCase))
    return suite
