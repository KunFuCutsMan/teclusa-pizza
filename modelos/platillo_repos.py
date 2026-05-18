from sqlite3 import Cursor

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

class RepoPlatilloDB(RepoPlatillo):
    
    def __init__(self, cur: Cursor, secciones: RepoSeccionMenu):
        super().__init__()
        self.secciones = secciones
        self.cur = cur
        self.cur.row_factory = self.__platillo_factory

    def __platillo_factory(self, cursor, row):
        id, nombre, desc, precio, seccionID = row
        seccion = self.secciones.obtenSeccion(seccionID)
        return Platillo(
            id=id,
            nombre=nombre,
            descripcion=desc,
            precio=precio,
            seccion=seccion
        )
    
    def insertaPlatillo(self, platillo):
        return super().insertaPlatillo(platillo)
    
    def modificaPlatillo(self, nuevo):
        return super().modificaPlatillo(nuevo)

    def eliminaPlatillo(self, platillo):
        return super().eliminaPlatillo(platillo)
    
    def obtenPlatillo(self, id):
        res = self.cur.execute("SELECT * FROM Platillos WHERE PlatilloID = ?", (id,))
        return res.fetchone()
    
    def obtenPlatillos(self):
        res = self.cur.execute("SELECT * FROM Platillos")
        return res.fetchall()