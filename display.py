from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import Qt
from variables import MAX_SIZE, TEXT_MARGIN, MIN_WIDTH

class Display(QLineEdit):
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
