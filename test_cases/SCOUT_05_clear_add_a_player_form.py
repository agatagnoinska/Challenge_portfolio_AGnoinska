import os
import unittest
from selenium import webdriver
from pages.add_a_player_form import AddPlayerForm
from pages.dashboard import Dashboard
from test_cases.SCOUT_01_login_to_the_system import TestLogInToSystem
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestClearButton(unittest.TestCase):
    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts.futbolkolektyw.pl/en/')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_clear_button(self):
        TestLogInToSystem.test_log_in_to_system(self)
        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_on_the_add_player_button()
        add_player = AddPlayerForm(self.driver)
        add_player.fill_name('Adam')
        add_player.fill_surname('Nawałka')
        add_player.click_on_clear_button()
        add_player.assert_text_name_after_clear()
        add_player.assert_text_surname_after_clear()

    @classmethod
    def tearDown(self):
        self.driver.quit()
