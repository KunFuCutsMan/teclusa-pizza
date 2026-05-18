from PyQt5.QtWidgets import QTableView
from PyQt5.QtCore import QModelIndex

from modelos.platillo import Platillo
from modelos.repositorios import RepoPlatillo, RepoSeccionMenu
from modelos.platillo_table import PlatilloTableModel
from vistas.app import TabMenu

class TabMenuController:
    
    def __init__(self, ui: TabMenu, platilloRepo: RepoPlatillo, seccionMenuRepo: RepoSeccionMenu, platilloTableModel: PlatilloTableModel):
        self.ui = ui
        self.platilloRepo = platilloRepo
        self.seccionRepo = seccionMenuRepo
        self.tblCatalogoModel = platilloTableModel

        self.ui.nmbPrecio.setMinimum(1)
        self.ui.nmbPrecio.setMaximum(999_999)
        self.ui.nmbPrecio.setPrefix("$")
        self.ui.nmbPrecio.setSuffix(".00")

        self.ui.txtDescripcion.setAcceptRichText(False)

        self.ui.cmbCategoriaPlatillo.addItems(
            list( map(lambda s: s.Nombre, self.seccionRepo.obtenSecciones()) )
        )

        self.ui.tblCatalogoAlimentos.setSelectionMode( QTableView.SelectionMode.SingleSelection )
        self.ui.tblCatalogoAlimentos.setSelectionBehavior( QTableView.SelectionBehavior.SelectRows )
        self.ui.tblCatalogoAlimentos.setModel(self.tblCatalogoModel)

        self.platilloAgregar = Platillo(id=0, nombre="", descripcion="", precio=0, seccion=None)
        self.onCmbCategoriaChange(0)

        self.setupEvents()

    def setupEvents(self):
        self.ui.txtNombrePlatillo.textEdited.connect(self.onNombrePlatilloEdit)
        self.ui.nmbPrecio.valueChanged.connect(self.onPrecioPlatilloChange)
        self.ui.txtDescripcion.textChanged.connect(self.onPlatilloDescripcionChange)
        self.ui.btnAgregar.clicked.connect(self.onBtnAgregarClick)
        self.ui.btnModificar.clicked.connect(self.onBtnModificarClick)
        self.ui.btnEliminar.clicked.connect(self.onBtnEliminarClick)
        self.ui.txtBuscarPlatillo.textEdited.connect(self.onPlatilloBusquedaChange)
        self.ui.cmbCategoriaPlatillo.activated.connect(self.onCmbCategoriaChange)
        self.ui.tblCatalogoAlimentos.clicked.connect(self.onTablaRowSelected)

    def validaPlatilloAgregar(self) -> bool:

        if self.platilloAgregar.Nombre.strip() == "":
            return False

        if self.platilloAgregar.Descripcion.strip() == "":
            return False
        
        if self.platilloAgregar.Precio <= 0:
            return False
        
        if self.platilloAgregar.SeccionMenu is None:
            return False

        return True
    
    def vaciaFormularioPlatillo(self):
        self.ui.txtNombrePlatillo.setText("")
        self.ui.nmbPrecio.setValue(0)
        self.ui.txtDescripcion.clear()

    def rellenaFormularioPlatillo(self, platillo: Platillo):
        self.ui.txtNombrePlatillo.setText(platillo.Nombre)
        self.ui.nmbPrecio.setValue(platillo.Precio)
        self.ui.txtDescripcion.setText(platillo.Descripcion)
        self.ui.cmbCategoriaPlatillo.setCurrentIndex(platillo.SeccionMenu.Id - 1)
        
        self.platilloAgregar = Platillo(
            id=platillo.Id,
            nombre=platillo.Nombre,
            descripcion=platillo.Descripcion,
            precio=platillo.Precio,
            seccion=platillo.SeccionMenu
        )

    def onNombrePlatilloEdit(self, texto: str):
        self.platilloAgregar.Nombre = texto

    def onPrecioPlatilloChange(self, precio: int):
        self.platilloAgregar.Precio = precio

    def onPlatilloDescripcionChange(self):
        self.platilloAgregar.Descripcion = self.ui.txtDescripcion.toPlainText().strip()

    def onBtnAgregarClick(self):

        if not self.validaPlatilloAgregar():
            # Le falta un argumento al botón
            return None
        
        self.platilloRepo.insertaPlatillo(self.platilloAgregar)
        self.tblCatalogoModel.actualizaVista()

        self.vaciaFormularioPlatillo()

    def onBtnModificarClick(self):
        if self.platilloAgregar.Id <= 0:
            # No sabemos que modificar
            return None

        if not self.validaPlatilloAgregar():
            # Le falta un argumento al botón
            return None
        
        self.platilloRepo.modificaPlatillo(self.platilloAgregar.copy())
        self.tblCatalogoModel.actualizaVista()
        self.vaciaFormularioPlatillo()

    def onCmbCategoriaChange(self, index: int):
        seccion = self.seccionRepo.obtenSeccion(index + 1)
        self.platilloAgregar.SeccionMenu = seccion

    def onBtnEliminarClick(self):
        if self.platilloAgregar.Id <= 0:
            # No sabemos que eliminar
            return None
        
        self.platilloRepo.eliminaPlatillo(self.platilloAgregar)
        self.platilloAgregar = Platillo(
            id=0, nombre="", descripcion="",
            precio=0, seccion=None
        )
        self.vaciaFormularioPlatillo()
        self.tblCatalogoModel.actualizaVista()

    def onPlatilloBusquedaChange(self, texto: str):
        self.tblCatalogoModel.filtra(texto)
        self.tblCatalogoModel.actualizaVista()

    def onTablaRowSelected(self, selected: QModelIndex):
        indexID = self.tblCatalogoModel.createIndex( selected.row(), 0 )
        platillo = self.platilloRepo.obtenPlatillo(indexID.data())
        if platillo is None:
            return None

        self.rellenaFormularioPlatillo(platillo)

