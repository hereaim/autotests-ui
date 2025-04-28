from elements.base_element import BaseElement


class FileInput(BaseElement):
    def set_input_file(self, nth: int = 0, file: str, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        locator.set_input_files(file)
