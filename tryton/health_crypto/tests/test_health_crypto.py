import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class HealthCryptoTestCase(ModuleTestCase):
    '''
    Test Health Crypto module.
    '''
    module = 'health_crypto'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        HealthCryptoTestCase))
    return suite
