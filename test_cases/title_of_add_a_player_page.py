import os
import unittest
from selenium import webdriver
from pages.add_a_player_form import AddPlayerForm
from pages.dashboard import Dashboard
from test_cases.SCOUT_01_login_to_the_system import TestLogInToSystem
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
import time

class TitleOfAddPlayerPage(unittest.TestCase):
    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts.futbolkolektyw.pl/en/')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)
    def test_title_of_page_add_player_form(self):
        # user_login = LoginPage(self.driver)
        # user_login.type_in_email('user01@getnada.com')
        # user_login.type_in_password('Test-1234')
        # user_login.click_on_the_sign_button() <---zamiast tego wszystkiego od góry jest to:
        TestLogInToSystem.test_log_in_to_system(self)
        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_on_the_add_player_button()
        add_player = AddPlayerForm(self.driver)
        add_player.title_of_page_add_player_form()
    @classmethod
    def tearDown(self):
        self.driver.quit()