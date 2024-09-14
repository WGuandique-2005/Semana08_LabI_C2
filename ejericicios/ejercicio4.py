"""
Ejercicio 4
__________________________________________________________

CONSTRUIR UN PROGRAMA QUE MUESTRE UNA VENTANA A TRAVEZ 
DE LA CUAL SE PUEDA LEER TRES SATOS BASICOS DE 3 MASCOTAS DIFERENTES
todo\ usando PyQt5
__________________________________________________________

"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt # esta libreria es para la alineacion de texto

class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        
        # Configuramos nuestra ventana
        self.setWindowTitle("Datos de Mascotas")
        self.setGeometry(100, 100, 400, 400)
        
        # Datos de la primera mascota
        self.label_mascota1 = QLabel("--------------- MASCOTA 1 ---------------")
        self.label_mascota1.setAlignment(Qt.AlignCenter) 
        self.label_nombre1 = QLabel("Nombre:")
        self.input_nombre1 = QLineEdit(self)
        self.input_nombre1.setText("Chispitas")  # Nombre 
        self.label_edad1 = QLabel("Edad:")
        self.input_edad1 = QLineEdit(self)
        self.input_edad1.setText("5 meses")  # Edad 
        self.label_tipo1 = QLabel("Tipo de animal:")
        self.input_tipo1 = QLineEdit(self)
        self.input_tipo1.setText("Perro")  # Tipo de animal 
        
        # Datos de la segunda mascota
        self.label_mascota2 = QLabel("-------------- MASCOTA 2 ---------------")
        self.label_mascota2.setAlignment(Qt.AlignCenter) 
        self.label_nombre2 = QLabel("Nombre:")
        self.input_nombre2 = QLineEdit(self)
        self.input_nombre2.setText("Rubi")  # Nombre 
        self.label_edad2 = QLabel("Edad:")
        self.input_edad2 = QLineEdit(self)
        self.input_edad2.setText(" 2 años y 6 meses")  # Edad 
        self.label_tipo2 = QLabel("Tipo de animal:")
        self.input_tipo2 = QLineEdit(self)
        self.input_tipo2.setText("Gata")  # Tipo de animal 
        
        # Datos de la tercera mascota
        self.label_mascota3 = QLabel("-------------- MASCOTA 3 ---------------")
        self.label_mascota3.setAlignment(Qt.AlignCenter) 
        self.label_nombre3 = QLabel("Nombre:")
        self.input_nombre3 = QLineEdit(self)
        self.input_nombre3.setText("Saltarina")  # Nombre 
        self.label_edad3 = QLabel("Edad:")
        self.input_edad3 = QLineEdit(self)
        self.input_edad3.setText("1 años y 2 meses")  # Edad 
        self.label_tipo3 = QLabel("Tipo de animal:")
        self.input_tipo3 = QLineEdit(self)
        self.input_tipo3.setText("Conejo")  # Tipo de animal 
        
        # Botón para mostrar los datos
        self.boton = QPushButton("Mostrar Datos", self)
        self.boton.clicked.connect(self.mostrar_datos)
        
        # Creamos un layout vertical para almacenar los elementos
        layout = QVBoxLayout()
        layout.addWidget(self.label_mascota1)
        layout.addWidget(self.label_nombre1)
        layout.addWidget(self.input_nombre1)
        layout.addWidget(self.label_edad1)
        layout.addWidget(self.input_edad1)
        layout.addWidget(self.label_tipo1)
        layout.addWidget(self.input_tipo1)
        layout.addWidget(self.label_mascota2)
        layout.addWidget(self.label_nombre2)
        layout.addWidget(self.input_nombre2)
        layout.addWidget(self.label_edad2)
        layout.addWidget(self.input_edad2)
        layout.addWidget(self.label_tipo2)
        layout.addWidget(self.input_tipo2)
        layout.addWidget(self.label_mascota3)
        layout.addWidget(self.label_nombre3)
        layout.addWidget(self.input_nombre3)
        layout.addWidget(self.label_edad3)
        layout.addWidget(self.input_edad3)
        layout.addWidget(self.label_tipo3)
        layout.addWidget(self.input_tipo3)
        layout.addWidget(self.boton)
        
        # Asignar el layout a nuestra ventana
        self.setLayout(layout)

    def mostrar_datos(self):
        nombre1 = self.input_nombre1.text()
        edad1 = self.input_edad1.text()
        tipo1 = self.input_tipo1.text()
        
        nombre2 = self.input_nombre2.text()
        edad2 = self.input_edad2.text()
        tipo2 = self.input_tipo2.text()
        
        nombre3 = self.input_nombre3.text()
        edad3 = self.input_edad3.text()
        tipo3 = self.input_tipo3.text()
        
        # Imprimir los datos de las mascotas
        print(f"Mascota 1 - Nombre: {nombre1}, Edad: {edad1}, Tipo: {tipo1}")
        print(f"Mascota 2 - Nombre: {nombre2}, Edad: {edad2}, Tipo: {tipo2}")
        print(f"Mascota 3 - Nombre: {nombre3}, Edad: {edad3}, Tipo: {tipo3}")

# Creamos la aplicación
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    ventana = Ventana()
    ventana.show()
    
    # Aquí cerramos la aplicación
    sys.exit(app.exec_())
