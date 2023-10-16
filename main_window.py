from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QMessageBox

class MyWindow(QMainWindow):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)

        self.vertical_layout = QVBoxLayout()
        self.main_widget.setLayout(self.vertical_layout)

        self.setWindowTitle('Window Title')

    def size_fixed(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def add_widget_to_layout(self, widget):
        self.vertical_layout.addWidget(widget)

    def _make_msg_box(self):
        return QMessageBox(self)
