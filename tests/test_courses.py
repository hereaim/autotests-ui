import pytest
from playwright.sync_api import expect
from pages.courses_list_page import CoursesListPage, CheckVisibleCourseCardParams
from pages.create_course_page import CreateCoursePage


@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list(chromium_page_with_state):
    chromium_page_with_state.goto(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses"
    )

    # Получение локаторов
    title_text = chromium_page_with_state.get_by_test_id(
        "courses-list-toolbar-title-text"
    )
    empty_view_icon = chromium_page_with_state.get_by_test_id(
        "courses-list-empty-view-icon"
    )
    empty_title_text = chromium_page_with_state.get_by_test_id(
        "courses-list-empty-view-title-text"
    )
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


@pytest.mark.regression
@pytest.mark.courses
def test_create_courses(create_courses_page, courses_list_page):

    # Переход на страницу создания курса
    create_courses_page.visit(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create"
    )
    # Проверка наличия заголовка "Create course"
    create_courses_page.check_visible_create_course_title()
    # Проверка, что кнопка создания курса недоступна для нажатия
    create_courses_page.check_disabled_create_course_button()
    # Проверка, что отображается пустой блок для предпросмотра изображения
    create_courses_page.check_visible_image_preview_empty_view()
    # Проверка, что блок загрузки изображения отображается в состоянии, когда картинка не выбрана
    create_courses_page.check_visible_image_upload_view()
    # Проверка, что форма создания курса отображается и содержит значения по умолчанию
    create_courses_page.check_visible_create_course_form(
        title="",
        description="",
        estimated_time="",
        max_score="0",
        min_score="0",
    )
    # Проверка наличия заголовка "Exercises"
    create_courses_page.check_visible_exercises_title()
    # Проверка наличия кнопки создания задания
    create_courses_page.check_visible_create_exercise_button()
    # Проверка, что отображается блок с пустыми заданиями
    create_courses_page.check_visible_exercises_empty_view()
    # Загрузка изображения превью курса
    create_courses_page.upload_preview_image("./testdata/files/image.png")
    # Проверка, что блок загрузки изображения отображает состояние, когда картинка успешно загружена
    create_courses_page.check_visible_image_upload_view(True)
    # Заполнение формы создания курса
    create_courses_page.fill_create_course_form(
        title="Playwright",
        estimated_time="2 weeks",
        description="Playwright",
        max_score="100",
        min_score="10",
    )
    # Клик на кнопку создания курса
    create_courses_page.click_create_course_button()

    # Проверка наличия заголовка на странице списка курсов
    courses_list_page.check_visible_courses_title()
    # Проверка на наличие кнопки создания курса
    courses_list_page.check_visible_create_course_button()
    # Проверка корректности отображаемых данных на карточке курса
    courses_list_page.check_visible_course_card(
        CheckVisibleCourseCardParams(
            index=0,
            title="Playwright",
            max_score="100",
            min_score="10",
            estimated_time="2 weeks",
        )
    )
