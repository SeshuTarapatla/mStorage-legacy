import flet as ft

__all__ = ["Colors", "Themes"]


class Colors:
    RED = ft.Colors.RED
    GREEN = ft.Colors.GREEN
    BLUE = ft.Colors.BLUE
    PURPLE = ft.Colors.PURPLE


class Themes:
    RED = ft.Theme(Colors.RED)
    GREEN = ft.Theme(Colors.GREEN)
    BLUE = ft.Theme(Colors.BLUE)
    PURPLE = ft.Theme(Colors.PURPLE)


def border(color: ft.ColorValue, width: int = 1) -> ft.Border:
    _border = ft.BorderSide(width, color)
    return ft.Border(*[_border] * 4)
