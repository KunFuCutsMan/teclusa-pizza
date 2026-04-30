
class Platillo:

    def __init__(self, id: int, nombre: str, descripcion: str, precio: int):
        self.__id = id
        self.__nombre = nombre
        self.__desc = descripcion
        self.__precio = precio

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

from .repositorios import RepoPlatillo

class RepoPlatilloLocal(RepoPlatillo):

    def __init__(self):
        super().__init__()
        self.platillos: dict[int, Platillo] = {}

    def insertaPlatillo(self, platillo):
        nuevo = Platillo(
            id = len(self.platillos.keys()),
            descripcion = platillo.Descripcion,
            nombre = platillo.Nombre,
            precio = platillo.Precio
        )

        if nuevo.Id not in self.platillos.keys():
            self.platillos[nuevo.Id] = nuevo
            return nuevo
        
        return None
    
    def modificaPlatillo(self, nuevo):
        if nuevo.Id in self.platillos.keys():
            self.platillos[nuevo.Id] = nuevo
    
    def eliminaPlatillo(self, platillo):
        if platillo.Id in self.platillos.keys():
            self.platillos.pop(platillo.Id)