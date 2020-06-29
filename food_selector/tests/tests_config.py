# coding: utf-8
"""[summary]Unitary Test config.py constants
for food_selector's APP.
"""
from django.test import TestCase
from ..config import TESTS, CATEGORIES_LIST


class DataBaseTestCase(TestCase):
    """Class TestCase for tests functions.

    Functions:
    -setUp(self)
    -testsTestsConstant(self)
    -testsCategoriesListConstant(self)
    """
    def setUp(self):
        """Create self objects for running tests
        """
        self.test_const = TESTS
        self.cat_list_const = CATEGORIES_LIST

    def tests_tests_constants(self):
        """[summary]Test that constants for
        unitest exist and are not empty.
        """
        test_const = self.test_const
        self.assertIsInstance(test_const, dict)
        self.assertIsNotNone(test_const['name1'])
        self.assertIsNotNone(test_const['name2'])
        self.assertIsNotNone(test_const['RightStatus'])
        self.assertIsNotNone(test_const['UnfoundStatus'])
        self.assertIsNotNone(test_const['WrongStatus'])

    def tests_categories_list_constants(self):
        """[summary]Test that constants for
        implementing food_selector's DB exist and
        are the good types and good sizes.
        """
        cat_list_const = self.cat_list_const
        self.assertIsInstance(cat_list_const, list)
        self.assertEqual(len(cat_list_const), 2)
