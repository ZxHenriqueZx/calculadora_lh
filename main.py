from PySide6.QtWidgets import QApplication
from main_window import MyWindow


if __name__ == '__main__':
    app = QApplication()
    window = MyWindow()

    window.setWindowTitle('Calculadora')

    window.size_fixed()
    window.show()
    app.exec()

