from typing import Callable
import flet as ft

from components.videopicker import VideoPicker


class EncodePage(ft.Container):
    def __init__(self, picker_func: Callable) -> None:
        super().__init__()
        self.expand = True
        self.content = ft.Column(
            [
            VideoPicker("#132738", picker_func),
            ft.Container(expand=3)
            ],
            expand=True
        )