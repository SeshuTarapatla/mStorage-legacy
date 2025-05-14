from typing import Callable
import flet as ft

from components.videopicker import VideoPicker


class PlayerPage(ft.Container):
    def __init__(self, picker_func: Callable) -> None:
        super().__init__()
        self.expand = True
        self.content = ft.Column(
            [
            VideoPicker("#3a1816", picker_func),
            ft.Container(expand=3)
            ],
            expand=True
        )
