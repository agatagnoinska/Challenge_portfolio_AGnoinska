import time
from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    password_label_xpath = '//*[@id="password-label"]'
    sign_in_button_xpath = "//*[contains(@class, 'MuiButton-label')]"
    sign_in_button_label_xpath = '//div/div[2]/button/span[1]'
    remind_password_hyperlink_xpath = "//*[@id='__next']/form/div/div[1]/a"
    remind_password_label_xpath = '//div/div[1]/a'
    language_selection_dropdown_xpath = "//*[@aria-haspopup='listbox']"
    language_English_button_xpath = "//*[@data-value='en']"
    language_Polish_button_xpath = "//*[@data-value='pl']"
    header_text_element_xpath = '//*[text()="Scouts Panel"]'
    validation_wrong_login_xpath = '//div/div[1]/div[3]/span'
    login_url = ("https://scouts.futbolkolektyw.pl/en/")
    expected_title = "Scouts panel - sign in"
    expected_text = "Scouts Panel"
    expected_validation_wrong_login = 'Identifier or password invalid.'
    expected_password_label_polish = 'Hasło'
    expected_remind_password_polish = 'Przypomnij hasło'
    expected_sign_in_button_polish = 'ZALOGUJ'

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    # def field_send_keys(self, selector, value, locator_type=By.XPATH):
    #     return self.driver.find_element(locator_type, selector).send_keys(value)
    def click_on_the_sign_button(self):
        self.wait_for_element_to_be_clickable(self.sign_in_button_xpath)
        self.click_on_the_element(self.sign_in_button_xpath)

    # def click_on_the_element(self, selector, selector_type=By.XPATH):
    #     return self.driver.find_element(selector_type, selector).click()
    def click_on_the_dropdown_language(self):
        self.wait_for_element_to_be_clickable(self.language_selection_dropdown_xpath)
        self.click_on_the_element(self.language_selection_dropdown_xpath)

    def click_on_the_polish(self):
        self.wait_for_element_to_be_clickable(self.language_Polish_button_xpath)
        self.click_on_the_element(self.language_Polish_button_xpath)

    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.header_text_element_xpath)
        assert self.get_page_title(self.login_url) == self.expected_title

    def assert_elements(self):
        self.wait_for_presence_of_element(self.header_text_element_xpath)
        self.assert_element_text(self.driver, self.header_text_element_xpath, self.expected_text)

    def assert_element_validation(self):
        self.wait_for_presence_of_element(self.validation_wrong_login_xpath)
        self.assert_element_text(self.driver, self.validation_wrong_login_xpath, self.expected_validation_wrong_login)

    def assert_polish_translation_password(self):
        self.wait_for_presence_of_element(self.password_label_xpath)
        self.assert_element_text(self.driver, self.password_label_xpath, self.expected_password_label_polish)

    def assert_polish_translation_signin(self):
        self.wait_for_presence_of_element(self.sign_in_button_label_xpath)
        self.assert_element_text(self.driver, self.sign_in_button_label_xpath, self.expected_sign_in_button_polish)

    def assert_polish_translation_remind_password(self):
        self.wait_for_presence_of_element(self.remind_password_label_xpath)
        self.assert_element_text(self.driver, self.remind_password_label_xpath, self.expected_remind_password_polish)

