from time import sleep
from typing import cast
import flet as ft

from pages import Pages


class AppBar(ft.AppBar):
    def __init__(self, title: str) -> None:
        super().__init__()
        self.title = ft.Text(title)


class NavigationRailDestination(ft.NavigationRailDestination):
    def __init__(
        self,
        label: str,
        icon: ft.Icons | None = None,
        selected_icon: ft.Icons | None = None,
    ):
        super().__init__()
        self.label = label
        if isinstance(icon, ft.Icons):
            self.icon = icon
        if isinstance(selected_icon, ft.Icons):
            self.selected_icon = selected_icon


class NavigationRail(ft.NavigationRail):
    def __init__(self, height: int | None = None) -> None:
        super().__init__()
        self.selected_index = 1
        self.label_type = ft.NavigationRailLabelType.ALL
        if height:
            self.height = height
        else:
            self.expand = True

class DecodePage(ft.Container):
    def __init__(self) -> None:
        super().__init__()
        self.expand = True
        self.content = ft.Text("DECODE", size=30)
        self.alignment = ft.alignment.center


class TabThemes:
    RED = ft.Theme(ft.Colors.RED)
    BLUE = ft.Theme(ft.Colors.BLUE)
    GREEN = ft.Theme(ft.Colors.GREEN)
    PURPLE = ft.Theme(ft.Colors.PURPLE)


class MainPage:
    def __init__(self, page: ft.Page) -> None:
        self.page = page
        self.page.title = "Flet testing"
        self.app_bar = AppBar("mStorage")

        self.page.add(
            self.app_bar,
            ft.Container(
                content=ft.ProgressRing(), expand=True, alignment=ft.alignment.center
            ),
        )
        self.page.update()
        sleep(1)

        self.pages = Pages(self.page)
        self.navigation_rail = NavigationRail()
        self.navigation_rail.destinations = [
            NavigationRailDestination(
                "Encode", ft.Icons.ARCHIVE_OUTLINED, ft.Icons.ARCHIVE
            ),
            NavigationRailDestination(
                "Decode", ft.Icons.VIDEO_FILE_OUTLINED, ft.Icons.VIDEO_FILE
            ),
            NavigationRailDestination(
                "Player", ft.Icons.PLAY_ARROW_OUTLINED, ft.Icons.PLAY_ARROW
            ),
            NavigationRailDestination(
                "Gallery", ft.Icons.LOCAL_MOVIES_OUTLINED, ft.Icons.LOCAL_MOVIES
            ),
            NavigationRailDestination(
                "Settings", ft.Icons.SETTINGS_OUTLINED, ft.Icons.SETTINGS
            ),
            NavigationRailDestination("Info", ft.Icons.INFO_OUTLINED, ft.Icons.INFO),
        ]
        self.navigation_rail.on_change = self.handle_tabs
        self.main_container = ft.Container(expand=True, padding=ft.Padding(0,0,30,0))

        self.reset()
        self.page.add(
            self.app_bar,
            ft.Row(
                [
                    ft.Column(
                        [
                            self.navigation_rail,
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        width=70,
                    ),
                    self.main_container,
                    # ft.Column(
                    #     [
                    #         ft.Container(expand=True)
                    #     ],
                    #     alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    #     width=30,
                    # )
                ],
                expand=True,
            ),
        )
        self.handle_tabs()

    def reset(self) -> None:
        if controls := self.page.controls:
            controls.clear()

    def handle_tabs(self, e: ft.ControlEvent = cast(ft.ControlEvent, None)) -> None:
        match self.navigation_rail.selected_index:
            case 0:
                self.page.theme = TabThemes.BLUE
                self.main_container.content = self.pages.encode_page
            case 1:
                self.page.theme = TabThemes.GREEN
                self.main_container.content = self.pages.decode_page
            case 2:
                self.page.theme = TabThemes.RED
                self.main_container.content = self.pages.player_page
            case 3:
                self.page.theme = TabThemes.PURPLE
                self.main_container.content = self.pages.gallery_page
            case 4:
                self.main_container.content = self.pages.settings_page
            case 5:
                self.main_container.content = self.pages.info_page
        self.page.update()


ft.app(MainPage)
