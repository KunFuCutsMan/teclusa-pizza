
class EstadoOrden:

    def __init__(self, id: int, nombre: str):
        self.__id = id
        self.__nombre = nombre

    @property
    def Id(self): return self.__id

    @property
    def Nombre(self): return self.__nombre