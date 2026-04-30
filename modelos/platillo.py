
class Platillo:

    def __init__(self, nombre: str, descripcion: str, precio: int):
        self.__nombre = nombre
        self.__desc = descripcion
        self.__precio = precio

    @property
    def Nombre(self): return self.__nombre
    
    @Nombre.setter
    def Nombre(self, value: str):
        self.__nombre = value

    @property
    def Descripcion(self):
        return self.__desc
    
    @Descripcion.setter
    def Descripcion(self, value: str):
        self.__desc = value

    @property
    def Precio(self): return self.__precio

    @Precio.setter
    def Precio(self, value: int):
        if value >= 0:
            self.__precio = value