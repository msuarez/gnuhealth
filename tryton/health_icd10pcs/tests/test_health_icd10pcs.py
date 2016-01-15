import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class HealthICD10PCSTestCase(ModuleTestCase):
    '''
    Test Health ICD10PCS module.
    '''
    module = 'health_icd10pcs'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        HealthICD10PCSTestCase))
    return suite
