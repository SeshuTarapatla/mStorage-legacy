from .base import BasePage, ft


class InfoPage(BasePage):
    def __init__(self, page: ft.Page) -> None:
        super().__init__(page)
        self.content = ft.Text("Info", size=30)

