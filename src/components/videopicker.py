from typing import Callable
import flet as ft

from ui import border


class VideoPicker(ft.Container):
    def __init__(self, accent: ft.ColorValue, on_click: Callable) -> None:
        super().__init__()
        self.expand = 7
        self.border = border(accent, 10)
        self.border_radius = 10
        self.content = ft.Text(
            "Drag and Drop Video Here",
            size=30,
            opacity=0.4
        )
        self.alignment = ft.alignment.center
        self.ink = True
        self.ink_color = accent
        self.on_click = on_click
        self.on_hover = None

