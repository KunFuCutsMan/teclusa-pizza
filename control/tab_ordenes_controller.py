from PyQt5.QtWidgets import QTableView
from PyQt5.QtCore import QModelIndex
from PyQt5.QtGui import QStandardItemModel, QStandardItem

from modelos.platillo import Platillo
from modelos.platillo_table import PlatilloTableModel
from modelos.repositorios import RepoPlatillo
from modelos.menu_actual_model import MenuActualModel
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
        self.textoNotas = ""
        self.cantidadPlatillos = 1

        self.modeloOrden = MenuActualModel(self.ui.tbl_orden_actual)

        self.setupEvents()

    def setupEvents(self):
        self.ui.btn_ver_imagen.clicked.connect(self.onVerImagenClick)
        self.ui.txt_notas_cliente.textEdited.connect(self.onNotasClientesChange)
        self.ui.spin_cantidad.valueChanged.connect(self.onCantidadChange)
        self.ui.btn_add_platillo.clicked.connect(self.onAddPlatilloClick)
        self.ui.btn_eliminar_platillo.clicked.connect(self.onEliminarPlatilloClick)
        self.ui.btn_crear_orden.clicked.connect(self.onCrearOrdenClick)

        self.ui.tbl_menu_disponible.clicked.connect(self.onMenuDisponibleRowClick)
        self.ui.tbl_orden_actual.clicked.connect(self.onOrdenActualRowClick)
    
    def onVerImagenClick(self):
        pass

    def onNotasClientesChange(self, texto: str):
        self.textoNotas = texto

    def onCantidadChange(self, value: int):
        self.cantidadPlatillos = value

    def onAddPlatilloClick(self):
        if self.cantidadPlatillos < 1:
            return
        
        if self.platilloSeleccionado.Id == 0:
            return
        
        self.modeloOrden.insertaPlatillo(
            platillo=self.platilloSeleccionado,
            cantidad=self.cantidadPlatillos,
            notas=self.textoNotas)
    
        self.ui.txt_notas_cliente.setText("")
        self.ui.spin_cantidad.setValue(1)

        self.actualizaLabelTotal()

    def onEliminarPlatilloClick(self):

        self.actualizaLabelTotal()
        pass

    def onCrearOrdenClick(self):
        pass

    def onMenuDisponibleRowClick(self, selected: QModelIndex):
        indexID = self.platilloTableModel.createIndex( selected.row(), 0 )
        platillo = self.platilloRepo.obtenPlatillo(indexID.data())
        if platillo is None:
            return

        self.platilloSeleccionado = platillo

    def onOrdenActualRowClick(self, selected: QModelIndex):
        item = self.modeloOrden.itemFromIndex(selected)
        
        if item.isEditable():
            self.modeloOrden.setData(item.index(), item.text())

        self.actualizaLabelTotal()

    def actualizaLabelTotal(self):
        total = self.modeloOrden.obtenTotal()
        self.ui.lbl_total.setText(f"Total a Pagar: ${total:<.2f}")
        pass