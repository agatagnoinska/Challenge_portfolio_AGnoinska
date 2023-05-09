from pages.base_page import BasePage
import time

class Dashboard(BasePage):
    menu_scouts_panel_button_xpath = "//*[@aria-label='menu']"
    main_page_button_xpath = "//div/div/div/ul[1]/div[1]"
    players_button_xpath = "//div/div/div/ul[1]/div[2]"
    language_button_xpath = "//div/div/div/ul[2]/div[1]"
    sign_out_button_xpath = "//div/div/div/ul[2]/div[2]"
    dev_team_contact_button_xpath = "//*[contains(@href, 'app.slack')]"
    logo_scouts_panel_xpath = "//*[@title='Logo Scouts Panel']"
    add_player_button_xpath = "//div[2]/div/div/a/button"
    last_created_player_button_xpath = "//div[3]/div/div/a[1]/button/span[1]"
    lats_updated_player_button_xpath = "//div[3]/div[3]/div/div/a[2]/button"
    last_created_match_button_xpath = "//div[3]/div[3]/div/div/a[3]/button"
    last_updated_match_button_xpath = "//div[3]/div[3]/div/div/a[4]/button"
    last_updated_report_button_xpath = "//div[3]/div[3]/div/div/a[5]/button"
    dashboard_url = ("https://scouts.futbolkolektyw.pl/en/")
    expected_title = "Scouts panel"
    dashboard_title_xpath='//*[@id="__next"]/div[1]/header/div/h6'
    expected_added_player = 'Adam Nawałka'
    def title_of_page(self):
        time.sleep(5)
        assert self.get_page_title(self.dashboard_url) == self.expected_title
    def click_on_the_add_player_button(self):
        self.wait_for_element_to_be_clickable(self.add_player_button_xpath)
        self.click_on_the_element(self.add_player_button_xpath)

    def sign_out(self):
        self.wait_for_element_to_be_clickable(self.sign_out_button_xpath)
        self.click_on_the_element(self.sign_out_button_xpath)

    def assert_last_added_player(self):
        last_added_player = self.find_last_player(self.last_created_player_button_xpath).text
        assert self.expected_added_player == last_added_player
pass