"""
Ejercicio 3
__________________________________________________________

CONSTRUIR UN PROGRAMA QUE MUESTRE UNA VENTANA A TRAVEZ 
DE LA CUAL SE PUEDA LEER SU NUMERO DE CEDULA Y NOMBRE
todo\ usando PyQt5
__________________________________________________________

"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        
        # Configuramos nuestra ventana
        self.setWindowTitle("Formulario de Cédula y Nombre")
        self.setGeometry(100, 100, 300, 200)
        
        # Creamos los elementos dde nuestra interfaz
        self.label_cedula = QLabel("Número de Cédula:")
        self.input_cedula = QLineEdit(self)
        self.input_cedula.setText("06784507-1")  # numero de la cédula que se mostrara
        
        self.label_nombre = QLabel("Nombre Completo:")
        self.input_nombre = QLineEdit(self)
        self.input_nombre.setText("Briseily Yamileth Solorzano Hernandez")  # el nombre que se mostrara
        
        self.boton = QPushButton("Mostrar Datos", self)
        
        # Conectamos el botón para la función que nos mostrara los datos
        self.boton.clicked.connect(self.mostrar_datos)
        
        # Creamos un layout vertical donde se almacenaran los elementos
        layout = QVBoxLayout()
        layout.addWidget(self.label_cedula)
        layout.addWidget(self.input_cedula)
        layout.addWidget(self.label_nombre)
        layout.addWidget(self.input_nombre)
        layout.addWidget(self.boton)
        
        # Asignamos el layout a nuestra ventana
        self.setLayout(layout)

    def mostrar_datos(self):
        cedula = self.input_cedula.text()
        nombre = self.input_nombre.text()
        print(f"Cédula: {cedula}, Nombre Completo: {nombre}")

# Creamos la aplicación
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    ventana = Ventana()
    ventana.show()

    # Aqui cerramos la aplicacion
    sys.exit(app.exec_())
