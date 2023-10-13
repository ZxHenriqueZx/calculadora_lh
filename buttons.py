from PySide6.QtWidgets import QPushButton, QGridLayout
from PySide6.QtCore import Slot
from variables import MID_SIZE, MAX_SIZE, MIN_SIZE
from utils import is_valid_number


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
    def __init__(self, display, info,  *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._grid_cal = [
            ['C', '^', '/', '🐍'],
            ['7', '8', '9', 'x'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '⌫', '='],
        ]

        self._make_grid()
        self._equation = ''
        self.display = display
        self.info = info

    @property
    def equation(self):
        return self._equation

    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)

    def _make_grid(self):
        for i, row in enumerate(self._grid_cal):
            for j, button_text in enumerate(row):
                button = Button(button_text)

                if button_text not in '0123456789.':
                    button.setProperty('cssClass', 'specialButton')
                    font = button.font()
                    font.setPixelSize(30)
                    button.setFont(font)

                self.addWidget(button, i, j)
                button_slot = self._make_display_slot(self._insert_text, button)
                button.clicked.connect(button_slot)

    def _make_display_slot(self, func, *args, **kwargs):
        @Slot()
        def real_slot(_):
            func(*args, **kwargs)
        return real_slot


    def _insert_text(self, button):
        button_text = button.text()
        new_display_value = self.display.text() + button_text

        if not is_valid_number(new_display_value):
            return

        self.display.insert(button_text)

