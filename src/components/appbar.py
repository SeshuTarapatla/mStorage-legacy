import flet as ft


class AppBar(ft.AppBar):
    def __init__(self, title: str) -> None:
        super().__init__()
        self.title = ft.Text(title)
