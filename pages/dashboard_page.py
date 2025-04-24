from playwright.sync_api import Page, expect

from pages.base_page import BasePage

from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from components.dashboard.dashboard_toolbar_view_component import DashboardToolbarViewComponent
from components.charts.chart_view_component import ChartViewComponent


class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        # Добавление компонента Navbar
        self.navbar = NavbarComponent(page)

        # Добавление компонента Sidebar
        self.sidebar = SidebarComponent(page)

        # Добавление компонента DashboardToolbarView
        self.dashboard_toolbar_view = DashboardToolbarViewComponent(page)

        self.scores_chart_view = ChartViewComponent(page, "scores", "scatter")
        self.courses_chart_view = ChartViewComponent(page, "courses", "pie")
        self.students_chart_view = ChartViewComponent(page, "students", "bar")
        self.activities_chart_view = ChartViewComponent(page, "activities", "line")
