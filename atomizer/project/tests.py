'''
Mock tests to test pytest
'''
from django.test import TestCase


class AliasTest(TestCase):
    '''
    Tests alias creation/matching/resetting
    '''

    def setUp(self):
        print("Setting up testcase....")

    def test_pytest(self):
        print("Running {} test file".format(__name__))
        test_bool = True
        self.assertTrue(test_bool)
