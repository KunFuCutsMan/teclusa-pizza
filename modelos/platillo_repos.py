from .platillo import Platillo
from .repositorios import RepoPlatillo

from .seccion_menu_repos import RepoSeccionMenu

class RepoPlatilloLocal(RepoPlatillo):

    def __init__(self, secciones: RepoSeccionMenu):
        super().__init__()
        seccion0 = secciones.obtenSecciones()[0]
        self.platillos: dict[int, Platillo] = {
            1: Platillo(1, "Pizza Pepperoni", "Está bien sabrosa", 119, seccion=seccion0)
        }

    def insertaPlatillo(self, platillo):
        nuevo = Platillo(
            id = len(self.platillos.keys()) + 1,
            descripcion = platillo.Descripcion,
            nombre = platillo.Nombre,
            precio = platillo.Precio,
            seccion=platillo.SeccionMenu
        )

        self.platillos.update({nuevo.Id: nuevo})
        return nuevo
    
    def obtenPlatillos(self):
        return list( self.platillos.values() )
    
    def obtenPlatillo(self, id):
        for p in self.platillos.values():
            if p.Id == id:
                return p
        return None
    
    def modificaPlatillo(self, nuevo):
        if nuevo.Id in self.platillos.keys():
            self.platillos[nuevo.Id] = nuevo
    
    def eliminaPlatillo(self, platillo):
        if platillo.Id in self.platillos.keys():
            self.platillos.pop(platillo.Id)