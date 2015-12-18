import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class HealthCalendarTestCase(ModuleTestCase):
    '''
    Test Health Calendar module.
    '''
    module = 'health_calendar'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        HealthCalendarTestCase))
    return suite
