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