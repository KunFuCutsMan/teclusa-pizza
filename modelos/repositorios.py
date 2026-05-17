from abc import ABC, abstractmethod

from .platillo import Platillo
from .seccion_menu import SeccionMenu
from .estado_orden import EstadoOrden
from .orden import OrdenMenu

class RepoPlatillo(ABC):
    """
    # RepoPlatillo

    Interfaz de repositorio de platillos en el menú del restaurante.

    Un repositorio es un patrón de programación que permite a la capa de lógica
    interactuar con la capa de datos, sin tener que saber de dónde viene dicha
    información. Cambiar la fuente de información solo depende en tener que
    intercambiar el repositorio cuando se entrega a la capa de lógica.
    """
    
    @abstractmethod
    def insertaPlatillo(self, platillo: Platillo) -> Platillo | None:
        """
        Inserta el platillo provisto, y regresa una copia que contiene la ID
        objeto insertado, si la operación fue exitosa.
        """
        pass

    @abstractmethod
    def obtenPlatillos(self) -> list[Platillo]:
        pass

    @abstractmethod
    def obtenPlatillo(self, id: int) -> Platillo | None:
        "Obten el platillo que tiene dicha ID"
        pass

    @abstractmethod
    def modificaPlatillo(self, nuevo: Platillo) -> None:
        pass

    @abstractmethod
    def eliminaPlatillo(self, platillo: Platillo) -> None:
        pass

class RepoSeccionMenu(ABC):
    """
    # RepoSeccionMenu

    Interfaz de repositorio de las secciones del menú del restaurante.

    Un repositorio es un patrón de programación que permite a la capa de lógica
    interactuar con la capa de datos, sin tener que saber de dónde viene dicha
    información. Cambiar la fuente de información solo depende en tener que
    intercambiar el repositorio cuando se entrega a la capa de lógica.
    """
    
    @abstractmethod
    def insertaSeccion(self, seccion: SeccionMenu) -> SeccionMenu | None:
        """
        Inserta la sección provista, y regresa una copia que contiene la ID
        objeto insertado, si la operación fue exitosa.
        """
        pass

    @abstractmethod
    def modificaSeccion(self, nuevo: SeccionMenu) -> None:
        pass

    @abstractmethod
    def eliminaSeccion(self, seccion: SeccionMenu) -> None:
        pass

    @abstractmethod
    def obtenSecciones(self) -> list[SeccionMenu]:
        pass

class RepoEstadoOrden(ABC):
    """
    # RepoEstadoOrden

    Interfaz de repositorio de los estados de una orden.

    Un repositorio es un patrón de programación que permite a la capa de lógica
    interactuar con la capa de datos, sin tener que saber de dónde viene dicha
    información. Cambiar la fuente de información solo depende en tener que
    intercambiar el repositorio cuando se entrega a la capa de lógica.
    """

    @abstractmethod
    def obtenEstado(self, id: int) -> EstadoOrden | None:
        "Obten el estado que tiene dicha ID"
        pass

    @abstractmethod
    def obtenEstados(self) -> list[EstadoOrden]:
        pass

class RepoOrdenMenu(ABC):
    """
    # RepoOrdenMenu

    Interfaz de repositorio de las ordenes registradas

    Un repositorio es un patrón de programación que permite a la capa de lógica
    interactuar con la capa de datos, sin tener que saber de dónde viene dicha
    información. Cambiar la fuente de información solo depende en tener que
    intercambiar el repositorio cuando se entrega a la capa de lógica.
    """

    @abstractmethod
    def insertaOrden(self, orden: OrdenMenu) -> OrdenMenu | None:
        pass

    @abstractmethod
    def obtenOrdenes(self) -> list[OrdenMenu]:
        pass

    @abstractmethod
    def obtenOrden(self, id: int) -> OrdenMenu | None:
        pass

    @abstractmethod
    def modificaOrden(self, orden: OrdenMenu) -> None:
        pass

    @abstractmethod
    def eliminaOrden(self, orden: OrdenMenu) -> None:
        pass