from playwright.sync_api import Page, expect
from pages.base_page import BasePage

from components.authentication.registration_form_component import RegistrationFormComponent


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.registration_form = RegistrationFormComponent(page)
        
        # Локаторы
        self.registration_button = page.get_by_test_id('registration-page-registration-button')
    
    # Метод для нажатия на кнопку "Registration"
    def click_registration_button(self):
        self.registration_button.click()
