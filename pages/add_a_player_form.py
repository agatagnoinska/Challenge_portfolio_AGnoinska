import time

from pages.base_page import BasePage


class AddPlayerForm(BasePage):
    menu_scouts_panel_button_xpath = "//*[@aria-label='menu']"
    main_page_button_xpath = "//div/div/div/ul[1]/div[1]"
    players_button_xpath = "//div/div/div/ul[1]/div[2]"
    language_button_xpath = "//div/div/div/ul[3]/div[1]"
    sign_out_button_xpath = "//div/div/div/ul[3]/div[2]"
    email_field_xpath = '//*[@name="email"]'
    name_field_xpath = '//*[@name="name"]'
    surname_field_xpath = '//*[@name="surname"]'
    phone_field_xpath = '//*[@name="phone"]'
    weight_field_xpath = '//*[@name="weight"]'
    age_field_xpath = '//*[@name="age"]'
    main_position_field_xpath = '//*[@name="mainPosition"]'
    submit_button_xpath = '//*[@type="submit"]'
    add_a_player_form_url = ("https://scouts-test.futbolkolektyw.pl/en/players/add")
    expected_title = "Add player"
    # def type_in_email(self, email):
    #     self.field_send_keys(self.login_field_xpath, email)
    #
    # def type_in_password(self, password):
    #     self.field_send_keys(self.password_field_xpath, password)
    # def field_send_keys(self, selector, value, locator_type=By.XPATH):
    #     return self.driver.find_element(locator_type, selector).send_keys(value)
    # def click_on_the_sign_button(self):
    #     self.click_on_the_element(self.sign_in_button_xpath)
    # def click_on_the_element(self, selector, selector_type=By.XPATH):
    #     return self.driver.find_element(selector_type, selector).click()

    def title_of_page_add_player_form(self):
        time.sleep(6)
        assert self.get_page_title(self.add_a_player_form_url) == self.expected_title
pass