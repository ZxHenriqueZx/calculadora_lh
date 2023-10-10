from PySide6.QtWidgets import QPushButton
from variables import MID_SIZE, MAX_SIZE, MIN_SIZE


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config_style()

    def config_style(self):
        font = self.font()
        font.setPixelSize(MID_SIZE)
        self.setFont(font)
        self.setMinimumSize(75,75)
