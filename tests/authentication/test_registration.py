import allure
import pytest
from allure_commons.types import Severity

from config import settings
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from tools.routes import AppRoute


@pytest.mark.regression
@pytest.mark.registration
@allure.tag(AllureTag.REGRESSION, AllureTag.REGISTRATION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.REGISTRATION)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.AUTHENTICATION)
@allure.sub_suite(AllureStory.REGISTRATION)
class TestRegistration:
    @allure.title("Registration with correct email, username and password")
    @allure.severity(Severity.CRITICAL)
    def test_successful_registration(
            self, registration_page: RegistrationPage,
            dashboard_page: DashboardPage
    ):
        # Посещение страницы регистрации
        registration_page.visit(
            AppRoute.REGISTRATION
        )
        # Заполнение формы регистрации
        registration_page.registration_form.fill(
            settings.test_user.email, settings.test_user.username,
            settings.test_user.password
        )
        registration_page.registration_form.check_visible(
            settings.test_user.email, settings.test_user.username,
            settings.test_user.password
        )
        registration_page.click_registration_button()
        # Проверка видимости заголовка
        dashboard_page.dashboard_toolbar_view.check_visible()
