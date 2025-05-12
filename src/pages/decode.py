from pages.common import DragAndDropVideo
from .base import BasePage, ft


class DecodePage(BasePage):
    def __init__(self, page: ft.Page) -> None:
        super().__init__(page)
        self.content = ft.Text("Decode", size=30)
        self.theme = ft.Theme(ft.Colors.GREEN)
        self.content = ft.Column(
            [
                DragAndDropVideo(self.theme),
                ft.Container(bgcolor=ft.Colors.BLACK, height=200, opacity=0),
            ]
        )
