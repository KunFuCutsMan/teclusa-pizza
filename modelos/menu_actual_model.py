from PyQt5.QtCore import Qt, QModelIndex
from PyQt5.QtGui import QStandardItemModel, QStandardItem

from .platillo import Platillo

class MenuActualModel(QStandardItemModel):
    
    def __init__(self):
        super().__init__(0, 2)

        self.setHeaderData(0, Qt.Orientation.Horizontal, "")
        self.root = self.invisibleRootItem()

    def insertaPlatillo(self, platillo: Platillo, cantidad: int, notas: str):

        item = ItemOrden(platillo, cantidad, notas)

        empty = QStandardItem()
        empty.setEnabled(False)
        empty.setEditable(False)

        self.root.appendRow([item, empty])
        self.dataChanged.emit(item.index(), item.index())

    def setData(self, index, value, role = ...):
        match index.row():
            case 0:
                self.editaNotas(value, index)
                self.dataChanged.emit(index, index)
                return True
            case 1:
                self.editaCantidad(value, index)
                self.dataChanged.emit(index, index)
                return True
        
        return False


    def headerData(self, section, orientation, role = ...):
        return ""
    
    def editaNotas(self, text: str, index: QModelIndex):
        parentIndex = index.parent()
        if not parentIndex.isValid():
            return
        
        alimentoItem: ItemOrden = self.root.child(parentIndex.row(), parentIndex.column())
        alimentoItem.notas = text

    def editaCantidad(self, value: str, index: QModelIndex):
        if not value.isdecimal() or value.find('.') != -1 or value.find(',') != -1:
            return
    
        cantidad = int(value)
        if cantidad < 1:
            return
        
        parentIndex = index.parent()
        if not parentIndex.isValid():
            return
        
        alimentoItem: ItemOrden = self.root.child(parentIndex.row(), parentIndex.column())
        alimentoItem.cantidad = cantidad

class ItemOrden(QStandardItem):

    def __init__(self, platillo: Platillo, cantidad: int, notas: str):
        super().__init__()

        self.__platillo = platillo
        self.__cantidad = cantidad
        self.__notas = notas

        self.txtNotas = QStandardItem(self.notas)
        self.txtCantidad = QStandardItem(str(self.cantidad))
        self.txtPrecio = QStandardItem(str(self.__platillo.Precio))
        self.txtSubtotal = QStandardItem(str(self.subtotal))
        self.txtSubtotal.setEditable(False)

        self.setup()

    @property
    def platillo(self): return self.__platillo

    @property
    def subtotal(self): return self.platillo.Precio * self.cantidad

    @property
    def cantidad(self): return self.__cantidad

    @property
    def notas(self): return self.__notas

    @cantidad.setter
    def cantidad(self, value: int):
        self.__cantidad = value
        self.txtCantidad.setText(str(value))
        self.txtSubtotal.setText(str(self.subtotal))

    @notas.setter
    def notas(self, value: str):
        self.__notas = value
        self.txtNotas.setText(value)

    def setup(self):
        self.setText(self.platillo.Nombre)
        self.setEditable(False)
        self.setRowCount(4)
        self.setColumnCount(2)

        self.setChild(0, 0, self.__labelItem("Notas:"))
        self.setChild(0, 1, self.txtNotas)

        self.setChild(1, 0, self.__labelItem("Cantidad:"))
        self.setChild(1, 1, self.txtCantidad)

        self.setChild(2, 0, self.__labelItem("Precio:"))
        self.setChild(2, 1, self.txtPrecio)

        self.setChild(3, 0, self.__labelItem("Subtotal:"))
        self.setChild(3, 1, self.txtSubtotal)

    def __labelItem(self, text: str) -> QStandardItem:
        item = QStandardItem(text)
        item.font().setBold(True)
        item.setFlags(Qt.ItemFlag.ItemIsEnabled)
        return item