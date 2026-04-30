
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