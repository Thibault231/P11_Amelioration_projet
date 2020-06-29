# coding: utf-8
"""[summary]Unitary Test models.py tables
for food_selector's APP.
"""
from django.contrib.auth.models import User
from django.test import TestCase
from ..models import Account, FoodItem, Category
from ..config import TESTS


class DataBaseTestCase(TestCase):
    """Class TestCase for tests functions.

    Functions:
    -setUp(self)
    -test_fooditem_table_args(self)
    -test_fooditem_table_args(self)
    -test_category_table_args(self)
    -test_links_food_category_tables(self)
    -test_account_table_args(self)
    """

    def setUp(self):
        """Create self objects for running tests
        """
        self.food = FoodItem.objects.create(
            name=TESTS['name1'], allergens=TESTS['name2'])
        self.category = Category.objects.create(name=TESTS['name2'])
        self.food.linked_cat.add(self.category)
        self.user = User.objects.create_user(
            username=TESTS['name2'],
            email=TESTS['name2']+'@gmail.com',
            password=TESTS['name2'])
        self.account = Account.objects.create(user=self.user)

    def test_fooditem_table_args(self):
        """[summary]Tests the types of
        FoodItem objects attributs.
        """
        food = self.food
        self.assertEqual(food.name, TESTS['name1'])
        self.assertEqual(food.allergens, TESTS['name2'])
        self.assertIsInstance(food.brand, str)
        self.assertIsInstance(food.description, str)
        self.assertIsInstance(food.nutriscore, str)
        self.assertIsInstance(food.store, str)
        self.assertIsInstance(food.url_OpenFF, str)

    def test_category_table_args(self):
        """[summary]Tests the types of
        Category objects attributs.
        """
        category = self.category
        self.assertEqual(category.name, TESTS['name2'])

    def test_links_food_category_tables(self):
        """[summary]Tests the link between tables
        FoodItem and Category.
        """
        food = self.food
        select = FoodItem.objects.get(
            linked_cat__name__startswith=TESTS['name2'])
        self.assertEqual(select, food)

    def test_account_table_args(self):
        """[summary]Tests the types of
        Account objects attributs.
        """
        user = self.user
        account = self.account
        food = self.food
        account.history.add(food)
        history_list = list(account.history.all())
        self.assertEqual(account.user, user)
        self.assertEqual(history_list[0], food)
