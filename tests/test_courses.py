from playwright.sync_api import sync_playwright, expect
import pytest

@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list():
    # Авторизация и сохранение состояния браузера
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto(
            "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration"
        )

        email_input = page.get_by_test_id("registration-form-email-input").locator("input")
        email_input.fill("user.name@gmail.com")

        username_input = page.get_by_test_id("registration-form-username-input").locator(
            "input"
        )
        username_input.fill("username")

        password_input = page.get_by_test_id("registration-form-password-input").locator(
            "input"
        )
        password_input.fill("password")

        registration_button = page.get_by_test_id("registration-page-registration-button")
        registration_button.click()

        # Сохраняем состояние браузера (куки и localStorage) в файл для дальнейшего использования
        context.storage_state(path="browser-state.json")

    # Использование авторизованного состояния для доступа к страницам
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state="browser-state.json")
        page = context.new_page()

        page.goto(
            "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses"
        )

        # Получение локаторов
        title_text = page.get_by_test_id("courses-list-toolbar-title-text")
        empty_view_icon = page.get_by_test_id("courses-list-empty-view-icon")
        empty_title_text = page.get_by_test_id("courses-list-empty-view-title-text")
        empty_description_text = page.get_by_test_id(
            "courses-list-empty-view-description-text"
        )

        # Проверка видимости элементов
        expect(title_text).to_be_visible()
        expect(empty_view_icon).to_be_visible()
        expect(empty_title_text).to_be_visible()
        expect(empty_description_text).to_be_visible()
        # Проверка текста элементов
        expect(title_text).to_have_text("Courses")
        expect(empty_title_text).to_have_text("There is no results")
        expect(empty_description_text).to_have_text(
            "Results from the load test pipeline will be displayed here"
        )
