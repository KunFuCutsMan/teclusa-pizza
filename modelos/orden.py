from .platillo import Platillo
from .estado_orden import EstadoOrden

class OrdenMenu:

    def __init__(self, id: int, estado: EstadoOrden, alimentos: list[Platillo]):
        self.__id = id
        self.__alimentos = alimentos
        self.__estado = estado

    @property
    def Id(self): return self.__id

    @Id.setter
    def Id(self, value): self.__id = value

    @property
    def Alimentos(self): return self.__alimentos

    @property
    def Estado(self): return self.__estado

    def copy(self):
        return OrdenMenu(
            id=self.Id,
            estado=self.Estado,
            alimentos=[a.copy() for a in self.Alimentos],
        )