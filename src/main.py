import flet as ft

from components import AppBar, SideBar
from pages.decode import DecodePage
from pages.encode import EncodePage
from pages.gallery import GalleryPage
from pages.info import InfoPage
from pages.player import PlayerPage
from pages.settings import SettingsPage
from ui import Themes
from vars import TITLE


class MainPage:
    def __init__(self, page: ft.Page) -> None:
        self.page = page
        self.page.title = TITLE
        # self.page.theme_mode = ft.ThemeMode.LIGHT

        self.app_bar = AppBar(TITLE)
        self.side_bar = SideBar(self.page_change)
        self.current_page = ft.Container(expand=True)

        self.file_picker = ft.FilePicker(on_result=self.pick_files)
        self.page.overlay.append(self.file_picker)

        self.encode_page = EncodePage(
            lambda _: self.file_picker.pick_files(
                dialog_title="Select a video to encode",
                allowed_extensions=["mp4", "mkv"],
            )
        )
        self.decode_page = DecodePage(
            lambda _: self.file_picker.pick_files(
                dialog_title="Select a video to encode", allowed_extensions=["mp4"]
            )
        )
        self.player_page = PlayerPage(
            lambda _: self.file_picker.pick_files(
                dialog_title="Select a video to encode",
                allowed_extensions=["mp4", "mkv"],
            )
        )
        self.gallery_page = GalleryPage()
        self.settings_page = SettingsPage()
        self.info_page = InfoPage()
        self.current_page.content = self.encode_page

        self.page_change()

    def refresh(self) -> None:
        if controls := self.page.controls:
            controls.clear()
        self.main_layout = ft.Row(
            [
                self.side_bar,
                self.current_page,
            ],
            expand=True,
        )
        self.page.add(self.app_bar, self.main_layout)
        self.page.update()

    def page_change(self, e: ft.ControlEvent | None = None) -> None:
        match self.side_bar.selected_index:
            case 0:
                self.page.theme = Themes.BLUE
                self.current_page.content = self.encode_page
            case 1:
                self.page.theme = Themes.GREEN
                self.current_page.content = self.decode_page
            case 2:
                self.page.theme = Themes.RED
                self.current_page.content = self.player_page
            case 3:
                self.page.theme = Themes.PURPLE
                self.current_page.content = self.gallery_page
            case 4:
                self.current_page.content = self.settings_page
            case 5:
                self.current_page.content = self.info_page
        self.refresh()

    def pick_files(self, e: ft.ControlEvent) -> None:
        print(f"File picker invoked: {e}")


ft.app(MainPage)
