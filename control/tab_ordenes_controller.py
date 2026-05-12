from PyQt5.QtWidgets import QTableView

from modelos.platillo_table import PlatilloTableModel
from vistas.app import TabTomarOrden

class TabOrdenesController:

    def __init__(self, ui: TabTomarOrden, platilloTableModel: PlatilloTableModel):
        self.ui = ui

        self.platilloTableModel = platilloTableModel

        self.ui.tbl_menu_disponible.setSelectionMode( QTableView.SelectionMode.SingleSelection )
        self.ui.tbl_menu_disponible.setSelectionBehavior( QTableView.SelectionBehavior.SelectRows )
        self.ui.tbl_menu_disponible.setModel(self.platilloTableModel)

    def setupEvents(self):
        pass