from PyQt5.QtWidgets import QTableView
from PyQt5.QtCore import QModelIndex

from modelos.platillo import Platillo
from modelos.platillo_table import PlatilloTableModel
from modelos.repositorios import RepoPlatillo
from vistas.app import TabTomarOrden

class TabOrdenesController:

    def __init__(self, ui: TabTomarOrden, repoPlatillo: RepoPlatillo, platilloTableModel: PlatilloTableModel):
        self.ui = ui

        self.platilloTableModel = platilloTableModel
        self.platilloRepo = repoPlatillo

        self.ui.tbl_menu_disponible.setSelectionMode( QTableView.SelectionMode.SingleSelection )
        self.ui.tbl_menu_disponible.setSelectionBehavior( QTableView.SelectionBehavior.SelectRows )
        self.ui.tbl_menu_disponible.setModel(self.platilloTableModel)

        self.platilloSeleccionado = Platillo(0, "", "", 0, None)

    def setupEvents(self):
        self.ui.btn_ver_imagen.clicked.connect(self.onVerImagenClick)
        self.ui.txt_notas_cliente.textEdited.connect(self.onNotasClientesChange)
        self.ui.spin_cantidad.valueChanged.connect(self.onCantidadChange)
        self.ui.btn_add_platillo.clicked.connect(self.onAddPlatilloClick)
        self.ui.btn_eliminar_platillo.clicked.connect(self.onEliminarPlatilloClick)
        self.ui.btn_crear_orden.clicked.connect(self.onCrearOrdenClick)

        self.ui.tbl_menu_disponible.clicked.conect(self.onMenuDisponibleRowClick)
        self.ui.tbl_orden_actual.clicked.connect(self.onOrdenActualRowClick)
    
    def onVerImagenClick(self):
        pass

    def onNotasClientesChange(self, texto: str):
        pass

    def onCantidadChange(self, value: int):
        pass

    def onAddPlatilloClick(self):
        pass

    def onEliminarPlatilloClick(self):
        pass

    def onCrearOrdenClick(self):
        pass

    def onMenuDisponibleRowClick(self, selected: QModelIndex):
        indexID = self.tblCatalogoModel.createIndex( selected.row(), 0 )
        platillo = self.platilloRepo.obtenPlatillo(indexID.data())
        if platillo is None:
            return

        self.platilloSeleccionado = platillo

    def onOrdenActualRowClick(self, selected: QModelIndex):
        pass