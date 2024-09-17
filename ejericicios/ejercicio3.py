"""
Ejercicio 3
__________________________________________________________

CONSTRUIR UN PROGRAMA QUE MUESTRE UNA VENTANA A TRAVEZ 
DE LA CUAL SE PUEDA LEER SU NUMERO DE CEDULA Y NOMBRE
todo\ usando PyQt5
__________________________________________________________

"""

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit,
                            QTextEdit, QPushButton, QVBoxLayout)

class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        
        # Configuramos nuestra ventana
        self.label = QLabel("Ingrese los siguientes datos: \n")
        self.setWindowTitle("Formulario de Cédula y Nombre")
        self.setGeometry(100, 100, 300, 200)
        
        # Creamos los elementos de la interfaz
        self.label_cedula = QLabel("Número de Cédula:")
        self.input_cedula = QLineEdit(self)
        
        self.label_nombre = QLabel("Nombre Completo:")
        self.input_nombre = QLineEdit(self)
        
        # Comando para mostrar los datos
        self.txt_data = QTextEdit()
        self.boton = QPushButton("Mostrar Datos", self)
        
        # Conectamos el botón para la función que nos mostrara los datos
        self.boton.clicked.connect(self.mostrar_datos)
        
        # Creamos un layout vertical donde se almacenaran los elementos
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.label_cedula)
        layout.addWidget(self.input_cedula)
        layout.addWidget(self.label_nombre)
        layout.addWidget(self.input_nombre)
        layout.addWidget(self.boton)
        layout.addWidget(self.txt_data)
        
        # Asignamos el layout a nuestra ventana
        self.setLayout(layout)

    def mostrar_datos(self):
        cedula = self.input_cedula.text()
        nombre = self.input_nombre.text()
        
        if not cedula and not nombre:
            self.txt_data.setText("Por favor ingresar su número de cédula y su nombre: ")
        elif not cedula:
            self.txt_data.setText("Por favor ingresar su número de cédula: ")
        elif not nombre:
            self.txt_data.setText("Por favor ingresar su nombre completo: ")
        else:
            print(f"Cédula: {cedula}, Nombre Completo: {nombre}")
            self.txt_data.setText(f"Cédula: {cedula}\nNombre Completo: {nombre}")

# Creamos la aplicación
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    ventana = Ventana()
    ventana.show()

    # Este comando nos cierra la aplicacion 
    sys.exit(app.exec_())
