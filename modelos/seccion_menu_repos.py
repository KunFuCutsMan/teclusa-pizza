from .seccion_menu import SeccionMenu
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

