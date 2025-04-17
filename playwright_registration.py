from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Открытие страницы регистрации
    page.goto(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration"
    )

    # Локаторы для полей ввода
    email_input = page.get_by_test_id("registration-form-email-input").locator("input")
    username_input = page.get_by_test_id("registration-form-username-input").locator(
        "input"
    )
    password_input = page.get_by_test_id("registration-form-password-input").locator(
        "input"
    )

    # Проверка видимости полей
    expect(email_input).to_be_visible()
    expect(username_input).to_be_visible()
    expect(password_input).to_be_visible()

    # Заполнение полей
    email_input.fill("user.name@gmail.com")
    username_input.fill("username")
    password_input.fill("password")

    # Локатор и проверка кнопки регистрации
    registration_button = page.get_by_test_id("registration-page-registration-button")
    expect(registration_button).to_be_enabled()

    # Нажатие на кнопку регистрации
    registration_button.click()

    # Проверка перенаправления на страницу Dashboard
    expect(page).to_have_url(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard"
    )
    expect(page.get_by_test_id("dashboard-toolbar-title-text")).to_have_text(
        "Dashboard"
    )
