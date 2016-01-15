import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class HealthQRcodesTestCase(ModuleTestCase):
    '''
    Test Health QR codes module.
    '''
    module = 'health_qrcodes'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        HealthQRcodesTestCase))
    return suite
