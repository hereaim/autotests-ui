from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login",
              wait_until="networkidle")
    
    # Изменение текста через JavaScript и анонимную функцию
    page.evaluate("""
    (text) => {
    const title = document.getElementById('authentication-ui-course-title-text');
    title.textContent = text;
    }
    """,
    'New Text')
    
    page.wait_for_timeout(3000)
    
    # Изменение текста через JavaScript и f-строки
    next_text = 'Another Text'
    page.evaluate(f"""
    const title = document.getElementById('authentication-ui-course-title-text');
    title.textContent = '{next_text}';
    """)
    
    page.wait_for_timeout(5000)
    
    