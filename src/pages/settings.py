from .base import BasePage, ft


class SettingsPage(BasePage):
    def __init__(self, page: ft.Page) -> None:
        super().__init__(page)
        self.content = ft.Text("Settings", size=30)

