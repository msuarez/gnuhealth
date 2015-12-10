import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class HealthGeneticsTestCase(ModuleTestCase):
    '''
    Test HealthGenetics module.
    '''
    module = 'health_genetics'

def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        HealthGeneticsTestCase))
    return suite
