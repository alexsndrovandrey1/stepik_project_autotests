from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(
            *LoginPageLocators.REGISTRATION_EMAIL
        )
        email_input.send_keys(email)

        password_input = self.browser.find_element(
            *LoginPageLocators.REGISTRATION_PASSWORD
        )
        password_input.send_keys(password)

        password_confirm_input = self.browser.find_element(
            *LoginPageLocators.REGISTRATION_PASSWORD_CONFIRM
        )
        password_confirm_input.send_keys(password)

        register_button = self.browser.find_element(
            *LoginPageLocators.REGISTRATION_BUTTON
        )
        register_button.click()