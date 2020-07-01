# coding: utf-8
"""[summary]Unitary tests for views.py functions which don't need
user's loging.
"""
from django.contrib.auth.models import User
from django.test import RequestFactory, TestCase
from django.urls import reverse
from food_selector.models import Account, FoodItem, Category
from food_selector.config import TESTS


class accountTestCase(TestCase):
    """Class TestCase for tests functions.

    Functions:
    -setUp(self)
    -test_right_connexion_log_page(self)
    -test_wrong_connexion_log_page(self)
    -test_connexion_page(self)
    -test_deconnexion_log_page(self)
    -test_deconnexion_unlog_page(self)
    -test_myaccount_log_page(self)
    -test_myaccount_unlog_page(self)
    -test_account_creation_account_page(self)
    -test_right_account_creation_page(self):

    """
    def setUp(self):
        """Create self objects for running tests
        """
        self.food2 = FoodItem.objects.create(
            name=TESTS['name2'],
            allergens=TESTS['name1'])
        self.category2 = Category.objects.create(name=TESTS['name1'])
        self.food2.linked_cat.add(self.category2)
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username=TESTS['name1'],
            email=TESTS['name1']+'@gmail.com',
            password=TESTS['name1'],
            first_name=TESTS['name1'], last_name=TESTS['name1'])
        self.account = Account.objects.create(user=self.user)
        self.account.history.add(self.food2)

    def test_right_connexion_log_page(self):
        """Test login method with right args.
        """
        response = self.client.login(
            email=TESTS['name1']+'@gmail.com',
            password=TESTS['name1'])
        self.assertIs(response, True)

    def test_wrong_connexion_log_page(self):
        """Test login method with wrong args.
        """
        response = self.client.login(
            email=TESTS['name1']+'@gmail.com',
            password=TESTS['name2'])
        self.assertIsNot(response, True)

    def test_connexion_page(self):
        """Test account to the page Connexion with
        GET method and right args.
        """
        response = self.client.get(reverse('account:connexion'))
        self.assertEqual(response.status_code, TESTS['RightStatus'])

    def test_deconnexion_log_page(self):
        """Test deaccount of a loged user with the view deconnexion
        with GET method and right args.
        """
        self.client.login(
            email=TESTS['name1']+'@gmail.com',
            password=TESTS['name1'])
        response = self.client.get(reverse('account:deconnexion'))
        self.assertEqual(response.status_code, TESTS['RightStatus'])

    def test_deconnexion_unlog_page(self):
        """Test deaccount of an unloged user with the view deconnexion
        with GET method and right args.
        """
        response = self.client.get('account:deconnexion')
        self.assertEqual(response.status_code, TESTS['UnfoundStatus'])

    def test_myaccount_log_page(self):
        """Test account to the page Myaccount of a connected user
        with GET method and right args.
        """
        self.client.login(
            email=TESTS['name1']+'@gmail.com',
            password=TESTS['name1'])
        response = self.client.get(reverse('account:myaccount'))
        self.assertEqual(response.status_code, TESTS['RightStatus'])

    def test_myaccount_unlog_page(self):
        """Test account to the page Myaccount of an anonymous
        user with GET method and right args.
        """
        response = self.client.get('account:deconnexion')
        self.assertEqual(response.status_code, TESTS['UnfoundStatus'])

    def test_account_creation_account_page(self):
        """Test account creation on the page Account_creation of an
        anonymous user with GET method and right args.
        """
        response = self.client.get(reverse('account:account_creation'))
        self.assertEqual(response.status_code, TESTS['RightStatus'])

    def test_right_account_creation_page(self):
        """Test account creation on the page Account_creation of an
        anonymous user with GET method and wrong args.
        """
        response = self.client.post(reverse('account:account_creation'), {
            'username': TESTS['name2'],
            'email': TESTS['name2']+'@gmail.com',
            'password1': TESTS['name2'],
            'password2': TESTS['name2']})
        self.assertEqual(response.status_code, TESTS['RightStatus'])
