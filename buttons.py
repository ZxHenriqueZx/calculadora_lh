import math
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
    def __init__(self, display, info, window, *args, **kwargs):
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
        self.window = window
        self.info = info
        self._left = None
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
        self.display.enter_signal.connect(self._equal)
        self.display.backspace_signal.connect(self.display.backspace)
        self.display.esc_signal.connect(self._clear)
        self.display.number_signal.connect(self._insert_text)
        self.display.operator_signal.connect(self._operator_clicked)

        for i, row in enumerate(self._grid_cal):
            for j, button_text in enumerate(row):
                button = Button(button_text)

                if button_text not in '0123456789.':
                    button.setProperty('cssClass', 'specialButton')
                    self._config_special_button(button)


                self.addWidget(button, i, j)
                button_slot = self._make_slot(self._insert_text, button_text)
                self._connect_button_clicked(button, button_slot)

    def _config_special_button(self, button):
        text = button.text()
        font = button.font()
        font.setPixelSize(30)
        button.setFont(font)

        if text == 'C':
            self._connect_button_clicked(button, self._clear)

        if text == '⌫':
            self._connect_button_clicked(button, self.display.backspace)

        if text in '+-*/^':
            self._connect_button_clicked(
                button,
                self._make_slot(self._operator_clicked, text)
            )

        if text == '=':
            self._connect_button_clicked(button, self._equal)
        
    def _connect_button_clicked(self, button, slot):
        button.clicked.connect(slot)

    def _make_slot(self, func, *args, **kwargs):
        @Slot(bool)
        def real_slot(_):
            func(*args, **kwargs)
        return real_slot


    @Slot()
    def _insert_text(self, text):
        new_display_value = self.display.text() + text

        if not is_valid_number(new_display_value):
            return

        self.display.insert(text)
        self.display.setFocus()

    def _clear(self):
        self._left = None
        self._right = None
        self._op = None
        self.equation = 'X ? X = X'
        self.display.clear()
        self.display.setFocus()

    def _operator_clicked(self, text):
        display_text = self.display.text()
        self.display.clear()

        if not is_valid_number(display_text) and self._left is None:
            self._show_error('Digite o primeiro numero da operação')
            return

        if self._left is None:
            self._left = float(display_text)

        self._op = text
        self.equation = f'{self._left} {self._op} INSERT'
        self.display.setFocus()

    def _equal(self):
        display_text = self.display.text()
        
        if not is_valid_number(display_text) or self._left is None:
            self._show_error('Não a conta a Fazer!') 
            return

        self._right = float(display_text)
        self.equation = f'{self._left} {self._op} {self._right}'
        result = 0.0

        try:
            if self._op == '^':
                result = math.pow(self._left, self._right)
            else:
                result = eval(self.equation)
        except ZeroDivisionError:
            self._show_error('Não é possivel dividir por zero')
            self._clear()
        except OverflowError:
            result = 'error'
            self._show_error('Esta conta excede o limite permitido!')

        self.display.clear()
        self.info.setText(f'{self.equation} = {result}')
        self._left = result
        self._right = None
        self.display.setFocus()

    def _show_error(self, msg):
        msg_box = self.window._make_msg_box()
        msg_box.setText(msg)
        msg_box.setIcon(msg_box.Icon.Warning)
        msg_box.exec()

