from playwright.sync_api import Page, expect

from components.courses.course_view_component import \
    CheckVisibleCourseCardParams
from pages.base_page import BasePage
from components.navigation.sidebar_component import SidebarComponent
from components.navigation.navbar_component import NavbarComponent
from components.view.empty_view_component import EmptyViewComponent
from components.courses.course_view_component import CourseViewComponent
from components.courses.courses_list_toolbar_view_component import CoursesListToolbarViewComponent


class CoursesListPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        # Добавление компонента Navbar
        self.navbar = NavbarComponent(page)

        # Добавление компонента Sidebar
        self.sidebar = SidebarComponent(page)

        # Добавление компонента EmptyView
        self.empty_view = EmptyViewComponent(page, "courses-list")

        # Добавление компонента CourseView
        self.course_view = CourseViewComponent(page)

        # Добавление компонента CoursesListToolbarView
        self.toolbar_view = CoursesListToolbarViewComponent(page)

    def check_visible_empty_view(self):
        self.empty_view.check_visible(
            title="There is no results",
            description="Results from the load test pipeline will be displayed here",
        )
