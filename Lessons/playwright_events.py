from playwright.sync_api import sync_playwright, Request, Response

def log_request(request: Request):
    print(f"Request: {request.url}")
    
def log_response(response: Response):
    print(f"Response: {response.url}")

# Фильтрация событий
def log_specific_request(request):
    if "googleapis.com" in request.url:
        print(f"Filtered Request: {request.url}")
        
#Получение доп.информации о содержимом ответа
def log_response_body(response):
    if response.ok:
        print(f"Response Body: {response.body()}")
    
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    
    # page.on("request", log_request)
    # page.on("response", log_response)
    
    # Динамическое добавление обработчиков событий через анонимные функции
    listener = lambda request: print(f"Request: {request.url}")
    page.on("request", listener) # Добавление обработчика события запроса
    page.remove_listener("request", listener) # Удаление обработчика события запроса
    
    # Фильтрованные события
    page.on("request", log_specific_request)
    
    # Дополнительная информация о содержимом ответа
    page.on("response", log_response_body)
    
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
    
    page.wait_for_timeout(5000)

