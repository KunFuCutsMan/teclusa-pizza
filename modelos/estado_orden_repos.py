from sqlite3 import Cursor

from .repositorios import RepoEstadoOrden
from .estado_orden import EstadoOrden

class RepoEstadoOrdenLocal(RepoEstadoOrden):

    def __init__(self):
        self.estados = [
            EstadoOrden(1, "En Espera"),
            EstadoOrden(2, "En Proceso"),
            EstadoOrden(3, "Lista"),
            EstadoOrden(4, "Entregada"),
            EstadoOrden(5, "Cancelada"),
        ]

    def obtenEstado(self, id):
        for p in self.estados:
            if p.Id == id:
                return p
        return None

    def obtenEstados(self):
        return list(self.estados)


class RepoEstadoOrdenDB(RepoEstadoOrden):

    def __init__(self, cur: Cursor):
        self.cur = cur
        self.cur.row_factory = self.__estadoOrden_factory

    def __estadoOrden_factory(self, cursor, row):
        id, nombre = row
        return EstadoOrden(id=id, nombre=nombre)

    def obtenEstado(self, id):
        res = self.cur.execute("SELECT * FROM EstadosOrdenes WHERE EstadoOrdenID = ?", (id,))
        return res.fetchone()
    
    def obtenEstados(self):
        res = self.cur.execute("SELECT * FROM EstadosOrdenes")
        return res.fetchall()