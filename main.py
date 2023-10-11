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
    my_info = Info('TESTE')
    window.add_widget_to_layout(my_info)

    #display
    my_display = Display()
    window.add_widget_to_layout(my_display)

    #Grid
    grid_buttons = GridButtons()
    window.vertical_layout.addLayout(grid_buttons)

    #Button
    grid_buttons.addWidget(Button('1'), 0, 0)
    grid_buttons.addWidget(Button('2'), 0, 1)
    grid_buttons.addWidget(Button('3'), 0, 2)
    grid_buttons.addWidget(Button('4'), 0, 3)
    grid_buttons.addWidget(Button('5'), 1, 0)
    grid_buttons.addWidget(Button('6'), 1, 1)
    grid_buttons.addWidget(Button('7'), 1, 2)
    grid_buttons.addWidget(Button('8'), 1, 3)

    #Exexuta a aplicação
    window.size_fixed()
    window.show()
    app.exec()

