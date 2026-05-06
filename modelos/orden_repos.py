from .repositorios import RepoOrdenMenu
from .orden import OrdenMenu

class RepoOrdenMenuLocal(RepoOrdenMenu):

    def __init__(self):
        super().__init__()
        self.ordenes: dict[int, OrdenMenu] = {}

    def obtenOrden(self, id):
        for o in self.ordenes.values():
            if o.Id == id:
                return o
        return None
    
    def obtenOrdenes(self):
        return list(self.ordenes.values())
    
    def insertaOrden(self, orden):
        nuevo = orden.copy()
        nuevo.Id = len(self.ordenes.keys()) + 1

        self.ordenes.update({ nuevo.Id: nuevo })
        return nuevo
    
    def modificaOrden(self, orden):
        if orden.Id in self.ordenes.keys():
            self.ordenes[orden.Id] = orden
    
    def eliminaOrden(self, orden):
        if orden.Id in self.ordenes.keys():
            self.ordenes.pop(orden.Id)