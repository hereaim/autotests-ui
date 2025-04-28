import pytest
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage


@pytest.mark.regression
@pytest.mark.registration
class TestRegistration:
    def test_successful_registration(
        self, registration_page: RegistrationPage, dashboard_page: DashboardPage
    ):
        # Посещение страницы регистрации
        registration_page.visit(
            "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration"
        )
        # Заполнение формы регистрации
        registration_page.registration_form.fill(
            "user@gmail.com", "username", "password"
        )
        registration_page.registration_form.check_visible(
            "user@gmail.com", "username", "password"
        )
        registration_page.click_registration_button()
        # Проверка видимости заголовка
        dashboard_page.dashboard_toolbar_view.check_visible()
