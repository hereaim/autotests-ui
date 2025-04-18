import pytest
from playwright.sync_api import expect, Page

@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list(chromium_page_with_state):
    chromium_page_with_state.goto(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses"
    )

    # Получение локаторов
    title_text = chromium_page_with_state.get_by_test_id("courses-list-toolbar-title-text")
    empty_view_icon = chromium_page_with_state.get_by_test_id("courses-list-empty-view-icon")
    empty_title_text = chromium_page_with_state.get_by_test_id("courses-list-empty-view-title-text")
    empty_description_text = chromium_page_with_state.get_by_test_id(
        "courses-list-empty-view-description-text"
    )

    # Проверка видимости элементов
    expect(title_text).to_be_visible()
    expect(empty_view_icon).to_be_visible()
    expect(empty_title_text).to_be_visible()
    expect(empty_description_text).to_be_visible()
    # Проверка текста элементов
    expect(title_text).to_have_text("Courses")
    expect(empty_title_text).to_have_text("There is no results")
    expect(empty_description_text).to_have_text(
        "Results from the load test pipeline will be displayed here"
    )
    chromium_page_with_state.wait_for_timeout(2000)