from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[contains(@class, 'MuiButton-label')]"
    remind_password_hyperlink_xpath = "//*[@id='__next']/form/div/div[1]/a"
    language_selection_dropdown_xpath = "//*[@aria-haspopup='listbox']"
    language_English_button_xpath = "//*[@data-value='en']"
    language_Polish_button_xpath = "//*[@data-value='pl']"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)
