import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class HealthNTDChagasTestCase(ModuleTestCase):
    '''
    Test Health NTD Chagas module.
    '''
    module = 'health_ntd_chagas'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        HealthNTDChagasTestCase))
    return suite
