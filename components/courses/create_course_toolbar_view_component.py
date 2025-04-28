from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.text import Text
from elements.button import Button


class CreateCourseToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        # Заголовок и кнопка создания курса
        self.title = Text(page,
            "create-course-toolbar-title-text", 'Title'
        )
        self.create_button = Button(page,
            "create-course-toolbar-create-course-button", 'Create'
        )

    def check_visible(self, is_create_course_disabled=True):
        self.title.check_visible()
        self.title.check_have_value(text="Create course")
        self.create_button.check_visible()
        if is_create_course_disabled:
            self.create_button.check_disabled()
        if not is_create_course_disabled:
            self.create_button.check_enabled()

    def click_create_course_button(self):
        self.create_button.click()
