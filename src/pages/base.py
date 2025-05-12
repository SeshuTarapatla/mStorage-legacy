import flet as ft


class BasePage(ft.Container):
    def __init__(self, page: ft.Page) -> None:
        super().__init__()
        self.page = page
        self.expand = True
        self.alignment = ft.alignment.center
        self.border_radius = 10

