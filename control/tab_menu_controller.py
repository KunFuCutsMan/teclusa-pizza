from modelos.platillo import Platillo
from modelos.repositorios import RepoPlatillo, RepoSeccionMenu
from vistas.app import TabMenu

class TabMenuController:
    
    def __init__(self, ui: TabMenu, platilloRepo: RepoPlatillo, seccionMenuRepo: RepoSeccionMenu):
        self.ui = ui
        self.platilloRepo = platilloRepo
        self.seccionRepo = seccionMenuRepo

        self.ui.nmbPrecio.setMinimum(1)
        self.ui.nmbPrecio.setPrefix("$")
        self.ui.nmbPrecio.setSuffix(".00")

        self.ui.txtDescripcion.setAcceptRichText(False)

        self.platilloAgregar = Platillo(id=0, nombre="", descripcion="", precio=0)

        self.setupEvents()

    def setupEvents(self):
        self.ui.txtNombrePlatillo.textEdited.connect(self.onNombrePlatilloEdit)
        self.ui.nmbPrecio.valueChanged.connect(self.onPrecioPlatilloChange)
        self.ui.txtDescripcion.textChanged.connect(self.onPlatilloDescripcionChange)
        self.ui.btnAgregar.clicked.connect(self.onBtnAgregarClick)
        self.ui.btnModificar.clicked.connect(self.onBtnModificarClick)
        self.ui.btnEliminar.clicked.connect(self.onBtnEliminarClick)
        self.ui.txtBuscarPlatillo.textEdited.connect(self.onPlatilloBusquedaChange)

    def onNombrePlatilloEdit(self, texto: str):
        self.platilloAgregar.Nombre = texto

    def onPrecioPlatilloChange(self, precio: int):
        self.platilloAgregar.Precio = precio

    def onPlatilloDescripcionChange(self):
        self.platilloAgregar.Descripcion = self.ui.txtDescripcion.toPlainText().strip()

    def onBtnAgregarClick(self):
        pass

    def onBtnModificarClick(self):
        pass

    def onBtnEliminarClick(self):
        pass

    def onPlatilloBusquedaChange(self, texto: str):
        pass