from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import Qt, Signal
from variables import MAX_SIZE, TEXT_MARGIN, MIN_WIDTH, MID_SIZE

class Display(QLineEdit):
    enter_signal = Signal()
    backspace_signal = Signal()
    esc_signal = Signal()

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
        key = event.key()
        KEYS = Qt.Key
        
        is_enter = key in [KEYS.Key_Enter, KEYS.Key_Return]
        is_backspace = key in [KEYS.Key_Backspace, KEYS.Key_Delete]
        is_esc = key == KEYS.Key_Escape

        if is_enter:
            self.enter_signal.emit()
            return event.ignore()
        
        if is_backspace:
            self.backspace_signal.emit()
            return event.ignore()

        if is_esc:
            self.esc_signal.emit()
            return event.ignore()
