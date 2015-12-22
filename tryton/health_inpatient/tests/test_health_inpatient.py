import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class HealthInpatientTestCase(ModuleTestCase):
    '''
    Test Health Inpatient module.
    '''
    module = 'health_inpatient'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        HealthInpatientTestCase))
    return suite
