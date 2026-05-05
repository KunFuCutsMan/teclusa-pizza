from PyQt5.QtCore import QAbstractTableModel, QVariant, Qt, QObject, QModelIndex

from .repositorios import RepoPlatillo

class PlatilloTableModel(QAbstractTableModel):

    def __init__(self, platilloRepo: RepoPlatillo, parent: QObject | None = None):
        super().__init__(parent)
        self.repo = platilloRepo

        self.headers = [
            "ID", "Nombre", "Descripción", "Categoría", "Precio"
        ]
    
    def rowCount(self, parent = ...):
        return len(self.repo.obtenPlatillos())
    
    def columnCount(self, parent = ...):
        return len(self.headers)
    
    def data(self, index, role = ...):
        if role != Qt.ItemDataRole.DisplayRole:
            return QVariant()
        
        data = list( map( lambda p: (p.Id, p.Nombre, p.Descripcion, p.SeccionMenu.Nombre, p.Precio),
        self.repo.obtenPlatillos() ) )

        return data[index.row()][index.column()]
    
    def headerData(self, section, orientation, role = ...):
        if role != Qt.ItemDataRole.DisplayRole or orientation != Qt.Orientation.Horizontal:
            return QVariant()
        return self.headers[section]
    
    def flags(self, index):
        return Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled
    
    def actualizaVista(self):
        # Notify the view that the entire model has changed
        top_left = self.index(0, 0)
        bottom_right = self.index(self.rowCount() - 1, self.columnCount() - 1)
        self.dataChanged.emit(top_left, bottom_right)
        self.layoutChanged.emit()