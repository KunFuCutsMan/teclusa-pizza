from PyQt5.QtWidgets import QApplication
from control.tab_menu_controller import TabMenuController
from control.tab_ordenes_controller import TabOrdenesController
from vistas.app import Ui_Teclusa
from modelos.seccion_menu_repos import RepoSeccionMenuDB
from modelos.platillo_repos import RepoPlatilloDB
from modelos.platillo_table import PlatilloTableModel

from db.conn import con

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

        repoSecciones = RepoSeccionMenuDB(con.cursor())
        repoPlatillos = RepoPlatilloDB(cur=con.cursor(), secciones=repoSecciones)

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
            repoPlatillo=repoPlatillos,
            platilloTableModel=platilloTableModel,
        )

    def show(self):
        self.ui.show()


if __name__ == "__main__":
    app = TeclusaApp()
    app.show()
    sys.exit(app.exec())