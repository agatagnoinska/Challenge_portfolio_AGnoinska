import os
import unittest
from selenium import webdriver
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
import time

class TestLogInToSystem(unittest.TestCase):
    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_log_in_to_system_wrong_login(self):
        user_login = LoginPage(self.driver)
        user_login.type_in_email('user01@ge')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_button()
        user_login.assert_element_validation()
    @classmethod
    def tearDown(self):
        self.driver.quit()