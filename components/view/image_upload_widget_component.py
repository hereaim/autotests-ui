from playwright.sync_api import Page

from components.base_component import BaseComponent
from components.view.empty_view_component import EmptyViewComponent
from elements.image import Image
from elements.icon import Icon
from elements.file_input import FileInput
from elements.text import Text
from elements.button import Button


class ImageUploadWidgetComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.preview_empty_view = EmptyViewComponent(page, identifier)

        # Кнопка загрузки, удаления картинки предпросмотра курса и блок с информацией о загружаемой картинке
        self.preview_image = Image(page,
                                   f"{identifier}-image-upload-widget-preview-image",
                                   'Preview image'
                                   )
        self.image_upload_icon = Icon(page,
                                      f"{identifier}-image-upload-widget-info-icon",
                                      'Info icon'
                                      )
        self.image_upload_title = Text(page,
                                       f"{identifier}-image-upload-widget-info-title-text",
                                       'Title text'
                                       )
        self.image_upload_description = Text(page,
                                             f"{identifier}-image-upload-widget-info-description-text",
                                             'Description text'
                                             )
        self.image_upload_button = Button(page,
                                          f"{identifier}-image-upload-widget-upload-button",
                                          'Upload button'
                                          )
        self.image_remove_button = Button(page,
                                          f"{identifier}-image-upload-widget-remove-button",
                                          "Remove button"
                                          )
        self.image_upload_input = FileInput(page,
                                            f"{identifier}-image-upload-widget-input",
                                            'Upload input'
                                            )

    def check_visible(self, is_image_uploaded: bool = False):
        self.image_upload_icon.check_visible()

        self.image_upload_title.check_visible()
        self.image_upload_title.check_have_text(
            'Tap on "Upload image" button to select file'
        )

        self.image_upload_description.check_visible()
        self.image_upload_description.check_have_text(
            "Recommended file size 540X300"
        )

        self.image_upload_button.check_visible()

        if is_image_uploaded:
            self.image_remove_button.check_visible()
            self.preview_image.check_visible()

        if not is_image_uploaded:
            self.preview_empty_view.check_visible(
                title="No image selected",
                description="Preview of selected image will be displayed here",
            )

    def click_remove_image_button(self):
        self.image_remove_button.click()

    def upload_preview_image(self, file: str):
        self.image_upload_input.set_input_file(file)
