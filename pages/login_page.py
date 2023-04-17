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
    header_text_element_xpath= '//*[text()="Scouts Panel"]'
    login_url = ("https://scouts-test.futbolkolektyw.pl/en")
    expected_title = "Scouts panel - sign in"
    expected_text = "Scouts Panel"

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
    def assert_elements(self):
        self.assert_element_text(self.driver, self.header_text_element_xpath, self.expected_text)
    # def assert_element_text(self, driver, xpath, expected_text):
    #     """Comparing expected text with observed value from web element
    #         :param driver: webdriver instance
    #         :param xpath: xpath to element with text to be observed
    #         :param expected_text: text what we expecting to be found
    #         :return: None
    #     """
    #     element = driver.find_element(by=By.XPATH, value=xpath)
    #     element_text = element.text
    #     assert expected_text == element_text