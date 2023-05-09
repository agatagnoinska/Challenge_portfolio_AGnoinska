import os
import unittest
from selenium import webdriver
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from test_cases.SCOUT_01_login_to_the_system import TestLogInToSystem
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT

class TestLogOut(unittest.TestCase):
    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts.futbolkolektyw.pl/en/')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_log_out(self):
        TestLogInToSystem.test_log_in_to_system(self)
        dashboard_page = Dashboard(self.driver)
        dashboard_page.sign_out()
        login_page = LoginPage(self)
        #login_page.title_of_page()
    @classmethod
    def tearDown(self):
        self.driver.quit()