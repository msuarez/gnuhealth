import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class HealthImagingTestCase(ModuleTestCase):
    '''
    Test Health Imaging module.
    '''
    module = 'health_imaging'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        HealthImagingTestCase))
    return suite
