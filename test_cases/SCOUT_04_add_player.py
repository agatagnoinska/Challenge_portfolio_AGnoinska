import os
import time
import unittest
from selenium import webdriver
from pages.add_a_player_form import AddPlayerForm
from pages.dashboard import Dashboard
from test_cases.SCOUT_01_login_to_the_system import TestLogInToSystem
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestAddingPlayer(unittest.TestCase):
    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_adding_player(self):
        TestLogInToSystem.test_log_in_to_system(self)
        time.sleep(3)
        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_on_the_add_player_button()
        add_player = AddPlayerForm(self.driver)
        add_player.fill_name('Adam')
        add_player.fill_surname('Nawałka')
        add_player.fill_age('12121988')
        add_player.fill_main_position('strzelec')
        add_player.click_on_the_submit_button()
        time.sleep(3)
    @classmethod
    def tearDown(self):
        self.driver.quit()
