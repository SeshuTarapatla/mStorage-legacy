from .base import BasePage, ft


class GalleryPage(BasePage):
    def __init__(self, page: ft.Page) -> None:
        super().__init__(page)
        self.content = ft.Text("Gallery", size=30)

