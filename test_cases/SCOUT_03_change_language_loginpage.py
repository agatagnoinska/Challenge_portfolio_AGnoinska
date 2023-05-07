import os
import unittest
from selenium import webdriver
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
import time

class TestChangeLanguageLoginPage(unittest.TestCase):
    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts.futbolkolektyw.pl/en/')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)
    def test_changing_language(self):
        language = LoginPage (self.driver)
        language.click_on_the_dropdown_language()
        language.click_on_the_polish()
        language.assert_polish_translation_password()
        language.assert_polish_translation_remind_password()
        language.assert_polish_translation_signin()
    @classmethod
    def tearDown(self):
        self.driver.quit()