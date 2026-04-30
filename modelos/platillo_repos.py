from .platillo import Platillo
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