"""
* Ejercicio 1

? Contruir un programa que muestre una ventana en la cual
! aparezca su nombre completo y su edad centrados,
todo\ usando PyQt5
"""

# se importan los módulos necesarios para crear una aplicación gráfica con PyQt5
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel

# se define la clase que hereda de QMainWindow

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # se configura la ventana principal
        self.setGeometry(100, 100, 300, 275)
        self.setWindowTitle("Ejercicio 1")
        
        # Esta etiqueta se utilizará para mostrar el nombre y la edad en la ventana
        label = QLabel("William Josue Guandique Rivera, 18 años")
        
        # Se establece la etiqueta creada como el widget central de la ventana principal utilizando el método setCentralWidget
        self.setCentralWidget(label)

# se muestra la aplicacion
app = QApplication(sys.argv)
window = MyApp()
window.show()
app.exec()
