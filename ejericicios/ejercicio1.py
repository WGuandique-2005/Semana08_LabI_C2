"""
* Ejercicio 1

? Contruir un programa que muestre una ventana en la cual
! aparezca su nombre completo y su edad centrados,
todo\ usando PyQt5
"""

# se importan los módulos necesarios para crear una aplicación gráfica con PyQt5
import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QLabel, QVBoxLayout, QWidget)
from PyQt5.QtCore import Qt


# se define la clase que hereda de QMainWindow

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # se configura la ventana principal
        self.setGeometry(100, 100, 300, 275)
        self.setWindowTitle("Ejercicio 1")
        
        center = QWidget()
        layout = QVBoxLayout()
        
        # Esta etiqueta se utilizará para mostrar el nombre y la edad en la ventana
        label = QLabel("William Josue Guandique Rivera, 18 años")
        
        # Se centra la etiqueta
        layout.addWidget(label)
        layout.setAlignment(Qt.AlignCenter)
        
        # Se establece la etiqueta creada como el widget central de la ventana principal utilizando el método setCentralWidget
        center.setLayout(layout)
        self.setCentralWidget(center)

# se muestra la aplicacion
app = QApplication(sys.argv)
window = MyApp()
window.show()
app.exec_()