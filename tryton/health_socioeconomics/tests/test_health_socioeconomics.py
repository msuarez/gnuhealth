import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class HealthSocioeconomicsTestCase(ModuleTestCase):
    '''
    Test Health Socioeconomics module.
    '''
    module = 'health_socioeconomics'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        HealthSocioeconomicsTestCase))
    return suite
