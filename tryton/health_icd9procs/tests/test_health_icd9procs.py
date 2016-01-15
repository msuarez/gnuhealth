import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class HealthICD9ProcsTestCase(ModuleTestCase):
    '''
    Test Health ICD9 Procs module.
    '''
    module = 'health_icd9procs'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        HealthICD9ProcsTestCase))
    return suite
