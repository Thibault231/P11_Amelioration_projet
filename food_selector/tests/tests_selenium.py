# coding: utf-8
"""[summary]Fonctionals tests on the Heroku platform for
nutella_project.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from django.test import LiveServerTestCase
from ..config import TESTS


class TestUserTakesTheTest(LiveServerTestCase):
    """Class LiveServerTestCase for tests functions.
    Functions:
    -setUp(self)
    -tearDown(self)
    -test_user_unlog(self)
    -test_user_add_product(self)
    -test_user_log(self)

    """
    def setUp(self):
        """Create self objects for running tests
        """
        self.driver = webdriver.Firefox()

    def tearDown(self):
        """delete self objects after the running tests
        """
        self.driver.quit()

    def test_user_unlog(self):
        """The user start on the index page.
        It search for a substitute of the fooditem 'cassoulet'.
        Once the result dusplayed, the user click on the wikilink
        for more informations.
        At least the user goes to the account_creation page and quit.
        """
        driver = self.driver

        wait = WebDriverWait(self.driver, 40)
        driver.get(TESTS['UrlApp'])
        driver.find_element(
            By.NAME, "item_name").send_keys("cassoulet" + Keys.RETURN)

        wait.until(EC.presence_of_element_located((By.ID, "resultBox")))
        first_url = driver.current_url
        driver.find_element_by_class_name('itemResult').click()

        wait.until(EC.presence_of_element_located((By.ID, "itemBox")))
        second_url = driver.current_url
        driver.find_element(By.ID, "create").click()
        WebDriverWait(self.driver, 2)
        third_url = driver.current_url

        wait.until(EC.presence_of_element_located((By.ID, "creationBox")))
        driver.find_element(By.ID, "index").click()
        last_url = driver.current_url

        self.assertEqual(TESTS['UrlResult'], first_url)
        self.assertEqual(TESTS['UrlItem'], second_url)
        self.assertEqual(TESTS['UrlCreation'], third_url)
        self.assertEqual(TESTS['UrlApp'], last_url)

    def test_user_add_product(self):
        """The user create an account, go to its account page
        and search a substitute for the fooditem'cassoulet'.
        Once the result displayed, it's save and the user logout.
        """
        driver = self.driver
        wait = WebDriverWait(self.driver, 10)
        driver.get(TESTS['UrlApp'])
        wait.until(EC.presence_of_element_located((By.ID, "create")))
        driver.find_element(By.ID, 'create').click()
        wait.until(EC.presence_of_element_located((By.ID, "id_password2")))
        driver.find_element(By.ID, "id_username").send_keys("azerty")
        driver.find_element(By.ID, "id_first_name").send_keys("azerty")
        driver.find_element(By.ID, "id_last_name").send_keys("azerty")
        driver.find_element(By.ID, "id_email").send_keys("azerty@gmail.com")
        driver.find_element(
            By.ID, "id_password1").send_keys("azerty")
        driver.find_element(
            By.ID, "id_password2").send_keys("azerty" + Keys.RETURN)

        wait.until(EC.presence_of_element_located((By.ID, "myaccount")))
        first_url = driver.current_url
        driver.find_element(
            By.NAME, "item_name").send_keys("cassoulet" + Keys.RETURN)

        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "saveItem")))
        second_url = driver.current_url
        driver.find_element(By.CLASS_NAME, "saveItem").click()

        wait.until(EC.element_to_be_clickable((By.ID, "logout")))
        third_url = driver.current_url
        driver.find_element(By.ID, "logout").click()
        wait.until(EC.presence_of_element_located((By.ID, "portfolio")))
        forth_url = driver.current_url

        self.assertEqual(TESTS['UrlCreation'], first_url)
        self.assertEqual(TESTS['UrlResult'], second_url)
        self.assertEqual(TESTS['UrlSave'], third_url)
        self.assertEqual(TESTS['UrlDeconnexion'], forth_url)

    def test_user_log(self):
        """[summary]The user loging, go on its history page,
        then its account page. Finally it delte its account.
        """
        driver = self.driver
        wait = WebDriverWait(self.driver, 10)
        driver.get(TESTS['UrlApp'])
        wait.until(EC.presence_of_element_located((By.ID, "login")))
        driver.find_element(By.ID, 'login').click()
        wait.until(EC.presence_of_element_located((By.ID, "accountBox")))
        first_url = driver.current_url

        driver.find_element(By.ID, "id_email").send_keys("azerty@gmail.com")
        driver.find_element(
            By.ID, "id_password").send_keys("azerty" + Keys.RETURN)

        wait.until(EC.element_to_be_clickable((By.ID, "logout")))
        second_url = driver.current_url
        driver.find_element(By.ID, 'historical').click()

        wait.until(EC.presence_of_element_located((By.ID, "myaccount")))
        third_url = driver.current_url
        driver.find_element(By.ID, 'myaccount').click()

        wait.until(EC.presence_of_element_located((By.ID, "delete")))
        forth_url = driver.current_url
        driver.find_element(By.ID, 'delete').click()

        wait.until(EC.presence_of_element_located((By.ID, "delete2")))
        fifth_url = driver.current_url
        driver.find_element(By.ID, 'delete2').click()

        wait.until(EC.element_to_be_clickable((By.ID, 'index')))
        driver.find_element(By.ID, 'index').click()
        wait.until(EC.element_to_be_clickable((By.ID, 'create')))
        sixth_url = driver.current_url

        self.assertEqual(TESTS['UrlConnexion'], first_url)
        self.assertEqual(TESTS['UrlConnexion'], second_url)
        self.assertEqual(TESTS['UrlHistory'], third_url)
        self.assertEqual(TESTS['UrlAccount'], forth_url)
        self.assertEqual(TESTS['UrlDeleteConfirm'], fifth_url)
        self.assertEqual(TESTS['UrlApp'], sixth_url)

    def test_user_modify_informations(self):
        """[summary]User create a new account, then change the
        password from its space account and log out. 
        After loging out, the user go to the login page
        and ask for losing its password. Finally the user login and
        delete its account.
        """
        driver = self.driver

        # Create account
        driver = self.driver
        wait = WebDriverWait(self.driver, 10)
        driver.get(TESTS['UrlApp'])
        wait.until(EC.presence_of_element_located((By.ID, "create")))
        driver.find_element(By.ID, 'create').click()
        wait.until(EC.presence_of_element_located((By.ID, "id_password2")))
        driver.find_element(By.ID, "id_username").send_keys(TESTS["name1"])
        driver.find_element(By.ID, "id_first_name").send_keys(TESTS["name1"])
        driver.find_element(
            By.ID, "id_last_name").send_keys(TESTS["name1"])
        driver.find_element(
            By.ID, "id_email").send_keys(TESTS["name1"]+"@gmail.com")
        driver.find_element(
            By.ID, "id_password1").send_keys(TESTS["name1"])
        driver.find_element(
            By.ID, "id_password2").send_keys(TESTS["name1"] + Keys.RETURN)
        # first_url = driver.current_url

        # Change password
        wait.until(EC.element_to_be_clickable((By.ID, "myaccount")))
        driver.find_element(By.ID, 'myaccount').click()

        wait.until(EC.element_to_be_clickable((By.ID, "changepassword")))
        driver.find_element(By.ID, "changepassword").click()
        # second_url = driver.current_url

        wait.until(EC.presence_of_element_located((By.ID, "id_new_password2")))
        driver.find_element(By.ID, "id_old_password").send_keys(TESTS["name1"])
        driver.find_element(
            By.ID, "id_new_password1").send_keys(TESTS["name4"])
        driver.find_element(
            By.ID, "id_new_password2").send_keys(TESTS["name4"] + Keys.RETURN)
        third_url = driver.current_url

        wait.until(EC.element_to_be_clickable((By.ID, 'logout')))
        driver.find_element(By.ID, 'logout').click()
        # Reset password
        wait.until(EC.element_to_be_clickable((By.ID, 'login')))
        driver.find_element(By.ID, 'login').click()

        wait.until(EC.element_to_be_clickable((By.ID, 'resetpass')))
        driver.find_element(By.ID, 'resetpass').click()
        forth_url = driver.current_url

        wait.until(EC.presence_of_element_located((By.ID, "id_email")))
        driver.find_element(
            By.ID, "id_email").send_keys(
                TESTS["name1"]+"@gmail.com" + Keys.RETURN)
        # fifth_url = driver.current_url

        # Delete account
        wait.until(EC.element_to_be_clickable((By.ID, "login")))
        driver.find_element(By.ID, 'login').click()
        wait.until(EC.presence_of_element_located((By.ID, "accountBox")))
        driver.find_element(
            By.ID, "id_email").send_keys(TESTS["name1"]+"@gmail.com")
        driver.find_element(
            By.ID, "id_password").send_keys(TESTS["name4"] + Keys.RETURN)
        wait.until(EC.element_to_be_clickable((By.ID, "logout")))
        driver.find_element(By.ID, 'historical').click()
        wait.until(EC.element_to_be_clickable((By.ID, "myaccount")))
        driver.find_element(By.ID, 'myaccount').click()
        wait.until(EC.element_to_be_clickable((By.ID, "delete")))
        driver.find_element(By.ID, 'delete').click()
        wait.until(EC.element_to_be_clickable((By.ID, "delete2")))
        driver.find_element(By.ID, 'delete2').click()
        wait.until(EC.element_to_be_clickable((By.ID, 'index')))
        sixth_url = driver.current_url

        # self.assertEqual(TESTS['UrlCreation'], first_url)
        # self.assertEqual(TESTS['UrlPasswordChange'], second_url)
        self.assertEqual(TESTS['UrlPasswordChange'], third_url)
        self.assertEqual(TESTS['UrlPasswordReset'], forth_url)
        # self.assertEqual(TESTS['UrlPasswordReset'], fifth_url)
        self.assertEqual(TESTS['UrlDeleteDone'], sixth_url)
