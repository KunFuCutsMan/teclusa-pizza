from PyQt5.QtWidgets import QApplication
from vistas.app import Ui_Teclusa

import sys

class TeclusaApp(QApplication):

    def __init__(self):
        super().__init__([])
        
        self.ui = Ui_Teclusa(
            title="TECLUSA Pizzeria"
        )

    def show(self):
        self.ui.show()


if __name__ == "__main__":
    app = TeclusaApp()
    app.show()
    sys.exit(app.exec())