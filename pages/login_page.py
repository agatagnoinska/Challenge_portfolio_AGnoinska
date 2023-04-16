import time

from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[contains(@class, 'MuiButton-label')]"
    remind_password_hyperlink_xpath = "//*[@id='__next']/form/div/div[1]/a"
    language_selection_dropdown_xpath = "//*[@aria-haspopup='listbox']"
    language_English_button_xpath = "//*[@data-value='en']"
    language_Polish_button_xpath = "//*[@data-value='pl']"
    login_url = ("https://scouts-test.futbolkolektyw.pl/en")
    expected_title = "Scouts panel - sign in"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)
    # def field_send_keys(self, selector, value, locator_type=By.XPATH):
    #     return self.driver.find_element(locator_type, selector).send_keys(value)
    def click_on_the_sign_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)
    # def click_on_the_element(self, selector, selector_type=By.XPATH):
    #     return self.driver.find_element(selector_type, selector).click()

    def title_of_page(self):
        time.sleep(7)
        assert self.get_page_title(self.login_url) == self.expected_title

