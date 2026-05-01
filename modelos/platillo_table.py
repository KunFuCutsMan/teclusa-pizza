from PyQt5.QtCore import QAbstractTableModel, QVariant, Qt

from .repositorios import RepoPlatillo

class PlatilloTableModel(QAbstractTableModel):

    def __init__(self, platilloRepo: RepoPlatillo):
        super().__init__(None)
        self.repo = platilloRepo

        self.headers = [
            "Nombre", "Descripción", "Categoría", "Precio"
        ]
    
    def rowCount(self, parent = ...):
        return len(self.repo.obtenPlatillos())
    
    def columnCount(self, parent = ...):
        return len(self.headers)
    
    def data(self, index, role = ...):
        return super().data(index, role)
    
    def headerData(self, section, orientation, role = ...):
        if role != Qt.ItemDataRole.DisplayRole or orientation != Qt.Orientation.Horizontal:
            return QVariant()
        return self.headers[section]