from .platillo import Platillo
from .repositorios import RepoPlatillo

class RepoPlatilloLocal(RepoPlatillo):

    def __init__(self):
        super().__init__()
        self.platillos: dict[int, Platillo] = {
            1: Platillo(1, "Pizza Pepperoni", "Está bien sabrosa", 119)
        }

    def insertaPlatillo(self, platillo):
        nuevo = Platillo(
            id = len(self.platillos.keys()) + 1,
            descripcion = platillo.Descripcion,
            nombre = platillo.Nombre,
            precio = platillo.Precio
        )

        self.platillos.update({nuevo.Id: nuevo})
        return nuevo
    
    def obtenPlatillos(self):
        return list( self.platillos.values() )
    
    def modificaPlatillo(self, nuevo):
        if nuevo.Id in self.platillos.keys():
            self.platillos[nuevo.Id] = nuevo
    
    def eliminaPlatillo(self, platillo):
        if platillo.Id in self.platillos.keys():
            self.platillos.pop(platillo.Id)