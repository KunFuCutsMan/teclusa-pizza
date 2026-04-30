
class SeccionMenu:

    def __init__(self, nombre: str, id: int = 0):
        self.__id = id
        self.__nombre = nombre
    
    @property
    def Id(self): return self.__id

    @property
    def Nombre(self): return self.__nombre

    @Nombre.setter
    def Nombre(self, value: str): self.__nombre = value

from .repositorios import RepoSeccionMenu

class RepoSeccionMenuLocal(RepoSeccionMenu):

    def __init__(self):
        super().__init__()
        self.secciones: dict[SeccionMenu] = {
            1: SeccionMenu(id=1, nombre="Platos principales"),
            2: SeccionMenu(id=2, nombre="Entradas"),
            3: SeccionMenu(id=3, nombre="Aperitivos"),
            4: SeccionMenu(id=4, nombre="Bebidas"),
        }
    
    def insertaSeccion(self, seccion):
        return super().insertaSeccion(seccion)
    
    def modificaSeccion(self, nuevo):
        return super().modificaSeccion(nuevo)
    
    def eliminaSeccion(self, seccion):
        return super().eliminaSeccion(seccion)
    
    def obtenSecciones(self):
        return list(self.secciones.values())

