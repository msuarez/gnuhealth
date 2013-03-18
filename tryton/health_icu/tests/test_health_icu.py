#!/usr/bin/env python

import sys, os
DIR = os.path.abspath(os.path.normpath(os.path.join(__file__,
    '..', '..', '..', '..', '..', 'trytond')))
if os.path.isdir(DIR):
    sys.path.insert(0, os.path.dirname(DIR))

import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import test_view, test_depends


class HealthIcuTestCase(unittest.TestCase):
    '''
    Test Healthicu module.
    '''

    def setUp(self):
        trytond.tests.test_tryton.install_module('health_icu')

    def test0005views(self):
        '''
        Test views.
        '''
        test_view('health_icu')

    def test0006depends(self):
        '''
        Test depends.
        '''
        test_depends()

def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        HealthIcuTestCase))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
