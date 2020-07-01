# coding: utf-8
"""[summary]Unitary tests for views.py functions which don't need
user's loging.
"""
from django.test import TestCase
from django.urls import reverse
from ..models import FoodItem, Category
from ..config import TESTS


class ViewsTestCase(TestCase):
    """Class TestCase for tests functions.

    Functions:
    -setUp(self):
    -test_index_page(self):
    -test_legal_page(self):
    -test_wrong_result_page(self):
    -test_right_result_page(self):
    -test_right_item_page(self):
    -test_wrong_item_page(self):

    """
    def setUp(self):
        """Create self objects for running tests
        """
        self.food1 = FoodItem.objects.create(
            name=TESTS['name2'], allergens=TESTS['name1'])
        self.category1 = Category.objects.create(name=TESTS['name1'])
        self.food1.linked_cat.add(self.category1)

    def test_index_page(self):
        """Test account to the page Index
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, TESTS['RightStatus'])

    def test_legal_page(self):
        """Test account to the page Legal
        """
        response = self.client.get(reverse('food_selector:legal'))
        self.assertEqual(response.status_code, TESTS['RightStatus'])

    def test_wrong_result_page(self):
        """Test account to the page Result with
        POST method and wrong args.
        """
        response = self.client.post(
            reverse('food_selector:result'),
            {'item_name': TESTS['name1']})
        self.assertEqual(response.status_code, TESTS['UnfoundStatus'])

    def test_right_result_page(self):
        """Test account to the page Result with
        POST method and right args.
        """
        right_name = self.food1.name
        response = self.client.post(
            reverse('food_selector:result'),
            {'item_name': right_name})
        self.assertEqual(response.status_code, TESTS['RightStatus'])

    def test_right_item_page(self):
        """Test account to the page Item with
        GET method and right args.
        """
        right_id = self.food1.id
        response = self.client.get(reverse('food_selector:item', args=(right_id,)))
        self.assertEqual(response.status_code, TESTS['RightStatus'])

    def test_wrong_item_page(self):
        """Test account to the page Item with
        GET method and wrong args.
        """
        response = self.client.get(reverse('food_selector:item', args=(10000,)))
        self.assertEqual(response.status_code, TESTS['UnfoundStatus'])
