from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        # Локаторы
        self.title_text = page.get_by_test_id('dashboard-toolbar-title-text')
    
    def check_visible_dashboard_title(self):
        expect(self.title_text).to_be_visible()
