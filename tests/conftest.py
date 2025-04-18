import pytest
from playwright.sync_api import Playwright, Page, expect

@pytest.fixture(scope='session')
def chromium_page(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page()
    browser.close()
    
@pytest.fixture(scope='session')
def initialize_browser_state(chromium_page: Page) -> None:
    chromium_page.goto(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration"
    )

    email_input = chromium_page.get_by_test_id("registration-form-email-input").locator("input")
    email_input.fill("user.name@gmail.com")

    username_input = chromium_page.get_by_test_id("registration-form-username-input").locator(
        "input"
    )
    username_input.fill("username")

    password_input = chromium_page.get_by_test_id("registration-form-password-input").locator(
        "input"
    )
    password_input.fill("password")

    registration_button = chromium_page.get_by_test_id("registration-page-registration-button")
    registration_button.click()
    chromium_page.context.storage_state(path="browser-state.json")
    chromium_page.close()

@pytest.fixture
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:  
    # Использование авторизованного состояния для доступа к страницам
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json")  # Загрузка состояния
    page = context.new_page()
    yield page
    browser.close()   