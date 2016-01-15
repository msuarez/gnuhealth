import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class HealthInpatientCalendarTestCase(ModuleTestCase):
    '''
    Test Health Inpatient Calendar module.
    '''
    module = 'health_inpatient_calendar'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        HealthInpatientCalendarTestCase))
    return suite
