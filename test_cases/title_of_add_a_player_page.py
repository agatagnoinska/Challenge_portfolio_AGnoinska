import os
import unittest
from selenium import webdriver

from pages.add_a_player_form import AddPlayerForm
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
import time
class TitleOfAddPlayerPage(unittest.TestCase):
    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/')
        # nie wiem jaki adres dać:formularza dodawania czy głównej
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)
    def test_title_of_page_add_player_form(self):
        user_login = LoginPage(self.driver)
        # user_login.title_of_page()
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_button()
        time.sleep(8)
        dashboard_page = Dashboard(self.driver)
        # dashboard_page.title_of_page()
        dashboard_page.click_on_the_add_player_button()
        add_player = AddPlayerForm(self.driver)
        add_player.title_of_page_add_player_form()
        time.sleep(8)
    # dlaczego jak nie daję wierszy 19-29 to test działą? jak to się samo loguje?
    @classmethod
    def tearDown(self):
        self.driver.quit()