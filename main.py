from PySide6.QtWidgets import QApplication, QLabel
from PySide6.QtGui import QIcon
from main_window import MyWindow
from display import Display
from variables import ICON_PATH
from info import Info
from theme import setup_theme_app
from buttons import Button, GridButtons


if __name__ == '__main__':
    #Cria a Aplicação
    app = QApplication()
    setup_theme_app()
    window = MyWindow()

    #Nome da Aplicação
    window.setWindowTitle('Calculadora')

    #Define o icone
    icon = QIcon(str(ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    #Info
    my_info = Info('X ? X = X')
    window.add_widget_to_layout(my_info)

    #display
    my_display = Display()
    window.add_widget_to_layout(my_display)

    #Grid
    grid_buttons = GridButtons(my_display, my_info, window)
    window.vertical_layout.addLayout(grid_buttons)

    #Button

    #Exexuta a aplicação
    window.size_fixed()
    window.show()
    app.exec()

