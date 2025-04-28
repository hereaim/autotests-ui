import re

import allure
from playwright.sync_api import Page
from pages.base_page import BasePage

from components.authentication.login_form_component import LoginFormComponent
from elements.button import Button
from elements.link import Link
from elements.text import Text


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.login_form = LoginFormComponent(page)
        # Локаторы
        self.login_button = Button(page, 'login-page-login-button', 'Login')
        self.registration_link = Link(page, 'login-page-registration-link',
                                      'Link')
        self.wrong_email_or_password_alert = Text(page,
                                                  'login-page-wrong-email-or-password-alert',
                                                  'Wrong email or password')

    # Метод для нажатия на кнопку "Login"
    def click_login_button(self):
        self.login_button.click()

    # Метод для нажатия на ссылку "Registration"
    def click_registration_link(self):
        self.registration_link.click()
        self.check_current_url(re.compile(".*/#/auth/registration"))

    # Метод для проверки отображения алерта с ошибкой
    @allure.step("Check visible wring email or password allert")
    def check_visible_wrong_email_or_password_alert(self):
        self.wrong_email_or_password_alert.check_visible()
        self.wrong_email_or_password_alert.check_have_value(
            'Wrong email or password')
