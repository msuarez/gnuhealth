import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class HealthGeneticsUniprotTestCase(ModuleTestCase):
    '''
    Test HealthGeneticsUniprot module.
    '''
    module = 'health_genetics_uniprot'

def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        HealthGeneticsUniprotTestCase))
    return suite
