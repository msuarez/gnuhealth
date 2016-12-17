import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class HealthArchivesTestCase(ModuleTestCase):
    '''
    Test Health Archives module.
    '''
    module = 'health_archives'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        HealthArchivesTestCase))
    return suite
