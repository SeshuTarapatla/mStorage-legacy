from pages.common import DragAndDropVideo
from .base import BasePage, ft


class EncodePage(BasePage):
    def __init__(self, page: ft.Page) -> None:
        super().__init__(page)
        self.content = ft.Text("Encode", size=30)
        self.theme = ft.Theme(ft.Colors.BLUE)
        self.content = ft.Column(
            [
                DragAndDropVideo(self.theme),
                ft.Container(bgcolor=ft.Colors.BLACK, height=200, opacity=0),
            ]
        )
