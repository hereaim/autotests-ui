import pytest
from pages.courses_list_page import CoursesListPage, CheckVisibleCourseCardParams
from pages.create_course_page import CreateCoursePage


@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list(courses_list_page: CoursesListPage):
    courses_list_page.visit(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses"
    )
    courses_list_page.navbar.check_visible('username')
    courses_list_page.sidebar.check_visible()
    courses_list_page.toolbar_view.check_visible()
    courses_list_page.check_visible_empty_view()


@pytest.mark.regression
@pytest.mark.courses
def test_create_course(create_courses_page: CreateCoursePage, courses_list_page: CoursesListPage):
    # Переход на страницу создания курса
    create_courses_page.visit(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create"
    )
    # Проверка наличия заголовка "Create course" и что кнопка недоступна для нажатия
    create_courses_page.create_course_toolbar_view.check_visible()
    # Проверка, что отображается пустой блок для предпросмотра изображения
    create_courses_page.image_upload_widget.check_visible(is_image_uploaded=False)
    # Проверка, что форма создания курса отображается и содержит значения по умолчанию
    create_courses_page.create_course_form.check_visible(
        title="",
        description="",
        estimated_time="",
        max_score="0",
        min_score="0",
    )
    # Проверка наличия заголовка "Exercises" и кнопки создания задания
    create_courses_page.create_exercises_toolbar_view.check_visible()
    # Проверка, что отображается блок с пустыми заданиями
    create_courses_page.check_visible_exercises_empty_view()
    # Загрузка изображения превью курса
    create_courses_page.image_upload_widget.upload_preview_image("./testdata/files/image.png")
    # Проверка, что блок загрузки изображения отображает состояние, когда картинка успешно загружена
    create_courses_page.image_upload_widget.check_visible(is_image_uploaded=True)
    # Заполнение формы создания курса
    create_courses_page.create_course_form.fill(
        title="Playwright",
        estimated_time="2 weeks",
        description="Playwright",
        max_score="100",
        min_score="10",
    )
    # Проверка наличия заголовка "Create course" и что кнопка доступна для нажатия
    create_courses_page.create_course_toolbar_view.check_visible(is_create_course_disabled=False)
    # Клик на кнопку создания курса
    create_courses_page.create_course_toolbar_view.click_create_course_button()

    # Проверка наличия заголовка на странице списка курсов
    courses_list_page.toolbar_view.check_visible()
    courses_list_page.course_view.check_visible(
        CheckVisibleCourseCardParams(
            index=0,
            title="Playwright",
            max_score="100",
            min_score="10",
            estimated_time="2 weeks",
        )
    )
