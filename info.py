from PySide6.QtWidgets import QLabel, QWidget
from PySide6.QtCore import Qt
from variables import MID_SIZE

class Info(QLabel):
    def __init__(self, text: str, parent: QWidget | None = None):
        super().__init__(text, parent)
        self.config_style()

    def config_style(self):
        self.setStyleSheet(f'font-size: {MID_SIZE}px;')
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
