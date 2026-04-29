from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTabWidget

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