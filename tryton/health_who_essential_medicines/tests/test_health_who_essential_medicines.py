import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class HealthWHOEssentialMedicinesTestCase(ModuleTestCase):
    '''
    Test Health WHO Essential Medicines module.
    '''
    module = 'health_who_essential_medicines'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        HealthWHOEssentialMedicinesTestCase))
    return suite
