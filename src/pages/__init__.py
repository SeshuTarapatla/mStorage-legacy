from .base import ft
from .decode import DecodePage
from .encode import EncodePage
from .gallery import GalleryPage
from .info import InfoPage
from .player import PlayerPage
from .settings import SettingsPage


class Pages:
    def __init__(self, page: ft.Page) -> None:
        self.empty_page = None
        self.decode_page = DecodePage(page)
        self.encode_page = EncodePage(page)
        self.player_page = PlayerPage(page)
        self.gallery_page = GalleryPage(page)
        self.settings_page = SettingsPage(page)
        self.info_page = InfoPage(page)
