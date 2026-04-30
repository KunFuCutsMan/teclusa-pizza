from PyQt5.QtWidgets import QApplication
from control.tab_menu_controller import TabMenuController
from vistas.app import Ui_Teclusa
from modelos.platillo import RepoPlatilloLocal

import sys

class TeclusaApp(QApplication):
    """
    # Teclusa App

    El punto de entrada de la aplicación.
    """

    def __init__(self):
        super().__init__([])

        self.ui = Ui_Teclusa(
            title="TECLUSA Pizzeria"
        )

        self.tabMenuController = TabMenuController(
            ui=self.ui.tabMenu,
            platilloRepo= RepoPlatilloLocal(),
        )

    def show(self):
        self.ui.show()


if __name__ == "__main__":
    app = TeclusaApp()
    app.show()
    sys.exit(app.exec())