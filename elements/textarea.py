import allure
from playwright.sync_api import Locator, expect

from elements.base_element import BaseElement
from ui_coverage_tool import ActionType
from tools.logger import get_logger


logger = get_logger("TEXTAREA")


class Textarea(BaseElement):
    @property
    def type_of(self) -> str:
        return "textarea"

    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        return super().get_locator(nth, **kwargs).locator("textarea").first

    def get_raw_locator(self, nth: int = 0, **kwargs) -> str:
        return (
            f"{super().get_raw_locator(nth, **kwargs)}//textarea"
        )

    def fill(self, value: str, nth: int = 0, **kwargs):
        step = f'Fill {self.type_of} "{self.name}" to value "{value}"'
        with allure.step(step):
            logger.info(step)
            locator = self.get_locator(nth, **kwargs)
            locator.fill(value)
        self.tracker_coverage(ActionType.FILL, nth, **kwargs)

    def check_have_value(self, value: str, nth: int = 0, **kwargs):
        step = f'Check {self.type_of} "{self.name}" have value "{value}"'
        with allure.step(step):
            logger.info(step)
            locator = self.get_locator(nth, **kwargs)
            expect(locator).to_have_value(value)
        self.tracker_coverage(ActionType.VALUE, nth, **kwargs)
