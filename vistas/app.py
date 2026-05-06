from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTabWidget
from vistas.ventana_menu import Ui_VentanaMenu
from vistas.ventana_supervision import Ui_FormSupervision

# NOTA:
#
# Las clases que se utilizan para interactuar con la aplicación son distintas
# a las generadas por `pyuic5` mediante los archivos .ui. Las clases presentes
# en este archivo deben heredar de `QWidget` y la la clase generada de la
# interfaz gráfica respectiva, y exportar los eventos relacionados con ellas.
#
# Esto se hace para no tener problema al modificar los archivos .ui y tener que
# exportarlos a Python.

class Ui_Teclusa(QWidget):
    """
    # Ui_Teclusa

    Clase responsable de UI de la aplicación
    """

    def __init__(self, title: str = "App"):
        super().__init__()

        self.setWindowTitle(title)
        self.setBaseSize(640, 480)
        self.setMinimumSize(640,480)

        self.tabs = QTabWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.tabs)
        self.setLayout(layout)

        # Crea y vincula las tabulaciones
        self.tabMenu = TabMenu()
        self.tabSupervision = TabSupervision()

        self.tabs.addTab(self.tabMenu, "Menú")
        self.tabs.addTab(self.tabSupervision, "Supervisión")

class TabMenu(QWidget, Ui_VentanaMenu):
    """
    # TabMenu

    Clase que representa a la intefaz gráfica `Ui_VentanaMenu`, responsable de
    manejar los eventos presentes en dicha interfaz.
    """
    def __init__(self):
        super().__init__()
        self.setupUi(self)

class TabSupervision(QWidget, Ui_FormSupervision):

    def __init__(self):
        super().__init__()
        self.setupUi(self)