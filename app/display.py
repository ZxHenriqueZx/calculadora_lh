from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import Qt, Signal
from app.variables import MAX_SIZE, TEXT_MARGIN, MIN_WIDTH, MID_SIZE
from app.utils import is_empyt, is_num_or_dot

class Display(QLineEdit):
    enter_signal = Signal()
    backspace_signal = Signal()
    esc_signal = Signal()
    number_signal = Signal(str)
    operator_signal = Signal(str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config_size()

    def config_size(self):
        margins = [TEXT_MARGIN for i in range(4)]
        self.setStyleSheet(f'font-size: {MAX_SIZE}px;')
        self.setMinimumHeight(MAX_SIZE * 2)
        self.setMinimumWidth(MIN_WIDTH)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*margins)

    def keyPressEvent(self, event):
        text = event.text().strip()
        key = event.key()
        KEYS = Qt.Key
        
        is_enter = key in [KEYS.Key_Enter, KEYS.Key_Return, KEYS.Key_Equal]
        is_backspace = key in [KEYS.Key_Backspace, KEYS.Key_Delete]
        is_esc = key == KEYS.Key_Escape
        is_operator = text in '/*-+p'

        if is_enter:
            self.enter_signal.emit()
            return event.ignore()
        
        if is_backspace:
            self.backspace_signal.emit()
            return event.ignore()

        if is_esc:
            self.esc_signal.emit()
            return event.ignore()

        if is_operator:
            if text.lower() == 'p':
                text = '^'
            self.operator_signal.emit(text)
            return event.ignore()

        if is_empyt(text):
            return event.ignore()

        if is_num_or_dot(text):
            self.number_signal.emit(text)
            return event.ignore()

