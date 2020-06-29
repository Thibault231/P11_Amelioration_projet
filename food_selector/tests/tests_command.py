# coding: utf-8
"""Unitary Test foodItem.py tables
for food_selector's APP.
"""
from django.test import TestCase
from food_selector.management.commands.foodItem import FoodItemOFF


class ApiToDbTestCase(TestCase):
    """Class TestCase for tests functions.

    Functions:
    -setUp(self)
    -testFoodItemOFFClassArgs(self)
    """
    def setUp(self):
        """Create self objects for running tests
        """
        self.food_item = FoodItemOFF()

    def test_food_itemoff_class_args(self):
        """[summary]Tests the types of
        FoodItemOFF objects attributs.
        """
        food_item = self.food_item
        self.assertIsInstance(food_item.name, str)
        self.assertIsInstance(food_item.brand, str)
        self.assertIsInstance(food_item.category, list)
        self.assertIsInstance(food_item.store, str)
        self.assertIsInstance(food_item.description, str)
        self.assertIsInstance(food_item.allergens, str)
        self.assertIsInstance(food_item.nutriscore, str)
        self.assertIsInstance(food_item.url_id, str)
        self.assertIsInstance(food_item.picture, str)
