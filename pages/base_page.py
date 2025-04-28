from typing import Pattern

from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page
    
    def visit(self, url: str): # Метод для открытия ссылок
        self.page.goto(url, wait_until='networkidle')
    
    def reload(self): # Метод для перезагрузки страницы
        self.page.reload(wait_until='domcontentloaded')

    def check_current_url(self, expected_url: Pattern[str]): # Метод для проверки текущей ссылки
        expect(self.page).to_have_url(expected_url)