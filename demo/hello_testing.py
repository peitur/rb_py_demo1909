#!/usr/bin/env python3

# python -m unittest hello_testing.py

import unittest

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestSomething1('testing_something_1'))
    suite.addTest(TestSomething2('testing_something_2'))
    return suite

class TestSomething1(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown():
        pass

class TestSomething2(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown():
        pass

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run( suite() )
