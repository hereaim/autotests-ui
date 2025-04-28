import pytest
from pages.courses.courses_list_page import CoursesListPage, CheckVisibleCourseCardParams
from pages.courses.create_course_page import CreateCoursePage


@pytest.mark.regression
@pytest.mark.courses
class TestCourses:
    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
        courses_list_page.visit(
            "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses"
        )
        courses_list_page.navbar.check_visible('username')
        courses_list_page.sidebar.check_visible()
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.check_visible_empty_view()

    def test_create_course(self, create_courses_page: CreateCoursePage, courses_list_page: CoursesListPage):
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

    def test_edit_course(self,
                         create_courses_page: CreateCoursePage,
                         courses_list_page: CoursesListPage):
        # переход на страницу создания курса
        create_courses_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
        # заполнение формы создания курса
        # Проверка, что отображается пустой блок для предпросмотра изображения
        create_courses_page.image_upload_widget.check_visible(is_image_uploaded=False)
        create_courses_page.image_upload_widget.upload_preview_image(
            "./testdata/files/image.png"
        )
        create_courses_page.create_course_form.fill(
            title="Playwright",
            estimated_time="2 weeks",
            description="Playwright",
            max_score="100",
            min_score="10",)
        # клик по кнопке создания курса
        create_courses_page.create_course_toolbar_view.click_create_course_button()
        # проверка, что курс создан с изначальными данными
        courses_list_page.course_view.check_visible(
            CheckVisibleCourseCardParams(
                index=0,
                title="Playwright",
                max_score="100",
                min_score="10",
                estimated_time="2 weeks",
            ))
        # клик на кнопку редактирования курса
        courses_list_page.course_view.menu.click_edit(index=0)
        # заполнение формы редактирования курса
        create_courses_page.create_course_form.fill(
            title="Not Playwright",
            estimated_time="1 weeks",
            description="Not Playwright",
            max_score="20",
            min_score="1",)
        # клик по кнопке редактирования курса
        create_courses_page.create_course_toolbar_view.click_create_course_button()
        # проверка, что курс изменен
        courses_list_page.course_view.check_visible(
            CheckVisibleCourseCardParams(
                index=0,
                title="Not Playwright",
                max_score="20",
                min_score="1",
                estimated_time="1 weeks",
            ))
