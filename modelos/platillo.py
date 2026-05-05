from .seccion_menu import SeccionMenu

class Platillo:

    def __init__(self, id: int, nombre: str, descripcion: str, precio: int, seccion: SeccionMenu | None):
        self.__id = id
        self.__nombre = nombre
        self.__desc = descripcion
        self.__precio = precio
        self.__seccion = seccion

    @property
    def Id(self): return self.__id

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

    @property
    def SeccionMenu(self): return self.__seccion

    @SeccionMenu.setter
    def SeccionMenu(self, value): self.__seccion = value

    def copy(self):
        return Platillo(
            id=self.Id,
            nombre=self.Nombre,
            descripcion=self.Descripcion,
            precio=self.Precio,
            seccion=self.SeccionMenu
        )