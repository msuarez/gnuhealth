import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class HealthICD10TestCase(ModuleTestCase):
    '''
    Test Health ICD10 module.
    '''
    module = 'health_icd10'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        HealthICD10TestCase))
    return suite
