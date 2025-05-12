from datetime import datetime
from .base import ft


class DragAndDropVideo(ft.Container):
    def __init__(self, theme: ft.Theme) -> None:
        super().__init__()
        self.expand = True
        self.theme: ft.Theme = theme
        self.content = ft.Column(
            [ft.Text("Drag and Drop Video Here", size=25, opacity=0.3)],
            alignment=ft.MainAxisAlignment.CENTER
        )
        self.alignment = ft.alignment.center
        self.border_radius = 10
        self.border = ft.Border(*[ft.BorderSide(10, color=self.border_color())] * 4)
        self.on_click = self.pick_file
        print(f"UPDATED: {datetime.now()}")

    def border_color(self) -> str | None:
        match self.theme.color_scheme_seed:
            case ft.Colors.GREEN:
                return "#151b14"
            case ft.Colors.BLUE:
                return "#161b21"
            case ft.Colors.RED:
                return "#231716"
        return None

    def pick_file(self, e) -> None:
        print("File picker to be implemented")
