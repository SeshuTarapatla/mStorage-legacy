from typing import Callable

import flet as ft



class SideBar(ft.NavigationRail):
    def __init__(self, on_change: Callable[[ft.ControlEvent], None]):
        super().__init__()
        self.width = 80
        self.label_type = ft.NavigationRailLabelType.ALL
        self.destinations = [
            ft.NavigationRailDestination(
                ft.Icons.ARCHIVE_OUTLINED, ft.Icons.ARCHIVE, "Encode"
            ),
            ft.NavigationRailDestination(
                ft.Icons.VIDEO_FILE_OUTLINED, ft.Icons.VIDEO_FILE, "Decode"
            ),
            ft.NavigationRailDestination(
                ft.Icons.PLAY_ARROW_OUTLINED, ft.Icons.PLAY_ARROW, "Player"
            ),
            ft.NavigationRailDestination(
                ft.Icons.LOCAL_MOVIES_OUTLINED, ft.Icons.LOCAL_MOVIES, "Gallery"
            ),
            ft.NavigationRailDestination(
                ft.Icons.SETTINGS_OUTLINED, ft.Icons.SETTINGS, "Settings"
            ),
            ft.NavigationRailDestination(ft.Icons.INFO_OUTLINED, ft.Icons.INFO, "Info"),
        ]
        self.selected_index = 0
        self.on_change = on_change

