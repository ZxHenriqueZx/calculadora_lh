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
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '⌫', '='],
        ]

        self._equation = ''
        self.display = display
        self.info = info
        self._left= None
        self._right = None
        self._op = None
        self._make_grid()

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
                    self._config_special_button(button)


                self.addWidget(button, i, j)
                button_slot = self._make_slot(self._insert_text, button)
                self._connect_button_clicked(button, button_slot)

    def _config_special_button(self, button):
        text = button.text()
        font = button.font()
        font.setPixelSize(30)
        button.setFont(font)

        if text == 'C':
            self._connect_button_clicked(button, self._clear)

        if text in '+-*/':
            self._connect_button_clicked(
                button,
                self._make_slot(self._operator_clicked, button)
            )

        if text == '=':
            self._connect_button_clicked(button, self._equal)
        
    def _connect_button_clicked(self, button, slot):
        button.clicked.connect(slot)

    def _make_slot(self, func, *args, **kwargs):
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

    def _clear(self):
        self._left = None
        self._rigth = None
        self._op = None
        self.equation = 'X ? X = X'
        self.display.clear()

    def _operator_clicked(self, button):
        button_text = button.text()
        display_text = self.display.text()
        self.display.clear()

        if not is_valid_number(display_text) and self._left is None:
            print('Não a nada a Fazer')
            return

        if self._left is None:
            self._left = float(display_text)

        self._op = button_text
        self.equation = f'{self._left} {self._op} INSERT'

    def _equal(self):
        display_text = self.display.text()
        
        if not is_valid_number(display_text):
            print('Não a nada a fazer')
            return

        self._rigth = float(display_text)
        self.equation = f'{self._left} {self._op} {self._rigth}'
        result = 0.0

        try:
            result = eval(self.equation)
        except ZeroDivisionError:
            print('Não é possível dividir por zero')

        self.display.clear()
        self.info.setText(f'{self.equation} = {result}')
        self._left = result
        self._right = None
