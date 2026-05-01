from PyQt5.QtCore import QAbstractTableModel, QVariant, Qt, QObject

from .repositorios import RepoPlatillo

class PlatilloTableModel(QAbstractTableModel):

    def __init__(self, platilloRepo: RepoPlatillo, parent: QObject | None = None):
        super().__init__(parent)
        self.repo = platilloRepo

        self.headers = [
            "Nombre", "Descripción", "Categoría", "Precio"
        ]
    
    def rowCount(self, parent = ...):
        return len(self.repo.obtenPlatillos())
    
    def columnCount(self, parent = ...):
        return len(self.headers)
    
    def data(self, index, role = ...):
        if role != Qt.ItemDataRole.DisplayRole:
            return QVariant()
        
        data = list( map( lambda p: (p.Nombre, p.Descripcion, "", p.Precio),
        self.repo.obtenPlatillos() ) )

        return data[index.row()][index.column()]
    
    def headerData(self, section, orientation, role = ...):
        if role != Qt.ItemDataRole.DisplayRole or orientation != Qt.Orientation.Horizontal:
            return QVariant()
        return self.headers[section]
    
    def flags(self, index):
        return Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled