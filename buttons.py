from PySide6.QtWidgets import QPushButton, QGridLayout
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

class GridButtons(QGridLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._grid_cal = [
            ['C', '^', '/', ' '],
            ['7', '8', '9', 'x'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '<', '='],
        ]
