import allure
import pytest
from allure_commons.types import Severity

from fixtures.pages import login_page
from pages.authentication.login_page import LoginPage
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from tools.routes import AppRoute
from config import settings

auth_data = [
    ("user.name@gmail.com", "password"),
    ("user.name@gmail.com", "  "),
    ("  ", "password"),
]


@pytest.mark.regression
@pytest.mark.authorization
@allure.tag(AllureTag.AUTHORIZATION, AllureTag.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.AUTHORIZATION)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.AUTHENTICATION)
@allure.sub_suite(AllureStory.AUTHORIZATION)
class TestAuthorization:
    @allure.tag(AllureTag.USER_LOGIN)
    @allure.severity(Severity.BLOCKER)
    @allure.title("User login with correct email and password")
    def test_successful_authorization(
        self,
        dashboard_page: DashboardPage,
        registration_page: RegistrationPage,
        login_page: LoginPage,
    ):
        registration_page.visit(
            AppRoute.REGISTRATION
        )
        registration_page.registration_form.fill(
            email=settings.test_user.email,
            username=settings.test_user.username,
            password=settings.test_user.password,
        )
        registration_page.click_registration_button()

        dashboard_page.dashboard_toolbar_view.check_visible()
        dashboard_page.navbar.check_visible(settings.test_user.username)
        dashboard_page.sidebar.check_visible()
        dashboard_page.sidebar.click_logout()

        login_page.login_form.fill(email=settings.test_user.email, password=settings.test_user.password)
        login_page.click_login_button()

        dashboard_page.dashboard_toolbar_view.check_visible()
        dashboard_page.navbar.check_visible(settings.test_user.username)
        dashboard_page.sidebar.check_visible()

    @allure.tag(AllureTag.NAVIGATION)
    @allure.severity(Severity.NORMAL)
    @allure.title("Navigation from login page to registration page")
    def test_navigate_from_authorization_page_to_registration_page(
        self, registration_page: RegistrationPage, login_page: LoginPage
    ):
        login_page.visit(
            AppRoute.LOGIN
        )
        login_page.registration_link.click()
        registration_page.registration_form.check_visible(
            email="", username="", password=""
        )

    @allure.tag(AllureTag.USER_LOGIN)
    @allure.title("User login with wrong email or password")
    @allure.severity(Severity.CRITICAL)
    @pytest.mark.parametrize("email, password", auth_data)
    def test_wrong_email_or_password_authorization(
        self, login_page: LoginPage, email: str, password: str
    ):
        login_page.visit(
            AppRoute.LOGIN
        )
        login_page.login_form.fill(email=email, password=password)
        login_page.login_form.check_visible(email, password)
        login_page.click_login_button()
        login_page.check_visible_wrong_email_or_password_alert()
