import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.text import Text
from elements.icon import Icon


class EmptyViewComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.icon = Icon(page, f"{identifier}-empty-view-icon",
                         'Empty view icon')
        self.title = Text(page, f"{identifier}-empty-view-title-text",
                          'Empty view text')
        self.description = Text(page,
                                f"{identifier}-empty-view-description-text",
                                'Empty view description'
                                )

    @allure.step("Chck visible empty view '{title}'")
    def check_visible(self, title: str, description: str):
        # Проверяем видимость иконки
        self.icon.check_visible()

        # Проверяем видимость заголовка и его текст
        self.title.check_visible()
        self.title.check_have_value(title)

        # Проверяем видимость описания и его текст
        self.description.check_visible()
        self.description.check_have_value(description)
