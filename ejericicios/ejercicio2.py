"""
* Ejercicio 2

? Construir un programa que muestre una ventana y que lea
! una clave secreta sin mostra los caracteres que la componen,
todo\ en PyQt5
"""

# Se importan los módulos necesarios para crear una aplicación gráfica con PyQt5

import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QLineEdit, QLabel,
                            QPushButton, QWidget, QVBoxLayout)

# Clase que hereda de QMainWindow para crear la ventana principal
class myAPP(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(100,100,300,100)
        self.setWindowTitle("Ejercicio 2")
        
        self.label = QLabel("Ingrese la clave:")
        # Crear un campo de texto para ingresar la clave
        self.editxt = QLineEdit()
        # Establecer el modo de eco del campo de texto para ocultar los caracteres
        self.editxt.setEchoMode(QLineEdit.Password)
        self.btn = QPushButton("Ingresar")
        self.btn.clicked.connect(self.clicked_btn)
        self.lbl = QLabel()
        
        central = QWidget()
        
        # Crear un layout vertical para organizar los widgets
        layout = QVBoxLayout()
        
        # Agregar los widgets al layout
        layout.addWidget(self.label)
        layout.addWidget(self.editxt)
        layout.addWidget(self.btn)
        layout.addWidget(self.lbl)
        
        # Establecer el layout en el widget central
        central.setLayout(layout)
        # Establecer el widget central en la ventana
        self.setCentralWidget(central)
        
    # Función que se llama cuando se hace clic en el botón
    def clicked_btn(self):
        # Obtener el texto ingresado en el campo de texto
        clave = self.editxt.text()
        if not clave:
            self.lbl.setText("Ingrese una clave")
        else:
        # Imprimir la clave en la consola
            print(f"La clave es: {clave}")

# Crear una aplicación de PyQt5
app = QApplication(sys.argv)
# Crear una instancia de la clase myAPP
window = myAPP()
# Mostrar la ventana
window.show()
app.exec()