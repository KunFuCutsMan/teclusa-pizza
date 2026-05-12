from PyQt5.QtWidgets import QApplication
from control.tab_menu_controller import TabMenuController
from control.tab_ordenes_controller import TabOrdenesController
from vistas.app import Ui_Teclusa
from modelos.seccion_menu_repos import RepoSeccionMenuLocal
from modelos.platillo_repos import RepoPlatilloLocal
from modelos.platillo_table import PlatilloTableModel

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

        repoSecciones = RepoSeccionMenuLocal()
        repoPlatillos = RepoPlatilloLocal(repoSecciones)

        platilloTableModel = PlatilloTableModel(
            platilloRepo=repoPlatillos
        )

        self.tabMenuController = TabMenuController(
            ui=self.ui.tabMenu,
            platilloRepo= repoPlatillos,
            seccionMenuRepo= repoSecciones,
            platilloTableModel=platilloTableModel
        )

        self.tabOrdenesController = TabOrdenesController(
            ui=self.ui.tabTomarOrden,
            platilloTableModel=platilloTableModel,
        )

    def show(self):
        self.ui.show()


if __name__ == "__main__":
    app = TeclusaApp()
    app.show()
    sys.exit(app.exec())