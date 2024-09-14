"""
* Ejercicio 5

? Contruir un programa que muestre una ventana a través de la cual
! se pueden leer 10 datos característicos de una persona,
todo\ usando PyQt5
"""

# Se importan los módulos necesarios para crear una aplicación gráfica con PyQt5

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLineEdit, QPushButton,
                            QLabel, QTextEdit, QComboBox, QWidget, QFormLayout, QInputDialog)

class myApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,400,650)
        self.setWindowTitle("Ejercicio 5")
        self.setContentsMargins(30,20,30,20)
        
        center = QWidget()
        layout = QFormLayout()
        
        lbl1 = QLabel("Ingrese sus datos:")
        
        lbl_nombre = QLabel("Su nombre:")
        self.txt_nombre = QLineEdit()
        lbl_apellido = QLabel("Su apellido:")
        self.txt_apellido = QLineEdit()
        
        lbl_nacionalidad = QLabel("Escriba su nacionalidad:")
        self.txt_nacionalidad = QLineEdit()
        
        lbl_genero = QLabel("Su género:")
        self.combo_genero = QComboBox()
        self.combo_genero.addItem("Hombre cisgenero")
        self.combo_genero.addItem("Mujer cisgenero")
        self.combo_genero.addItem("Prefiero no decirlo")
        
        lbl_estatura = QLabel("Su estatura: (en cm)")
        self.txt_estatura = QLineEdit()
        lbl_tez = QLabel("Su tez de piel:")
        self.txt_tez = QLineEdit()
        
        lbl_pelo = QLabel("Su tipo de pelo:")
        self.combo_pelo = QComboBox()
        self.combo_pelo.addItem("Lacio")
        self.combo_pelo.addItem("Ondulado")
        self.combo_pelo.addItem("Rizado")
        self.combo_pelo.addItem("Afro")
        
        lbl_peloC = QLabel("Su color de pelo:")
        self.combo_peloC = QComboBox()
        self.combo_peloC.addItem("Negro")
        self.combo_peloC.addItem("Castaño")
        self.combo_peloC.addItem("Rubio")
        
        lbl_ojos = QLabel("Su color de ojos:")
        self.combo_ojo = QComboBox()
        self.combo_ojo.addItem("Marrones")
        self.combo_ojo.addItem("Azules")
        self.combo_ojo.addItem("Verdes")
        
        lbl_rostro = QLabel("Su tipo de rostro:")
        self.combo_rostro = QComboBox()
        self.combo_rostro.addItem("Cuadrado")
        self.combo_rostro.addItem("Redondo")
        self.combo_rostro.addItem("Ovalado")
        self.combo_rostro.addItem("Alargado")
        
        # Crear un botón para guardar los datos.
        self.btn_guardar = QPushButton("Guardar datos")
        self.btn_guardar.clicked.connect(self.clicked_btn)
        
        # Crear un text edit para ver los datos
        self.txt_output = QTextEdit()
        
        # Añade todo al layout
        layout.addWidget(lbl1)
        layout.addWidget(lbl_nombre)
        layout.addWidget(self.txt_nombre)
        layout.addWidget(lbl_apellido)
        layout.addWidget(self.txt_apellido)
        layout.addWidget(lbl_nacionalidad)
        layout.addWidget(self.txt_nacionalidad)
        layout.addWidget(lbl_genero)
        layout.addWidget(self.combo_genero)
        layout.addWidget(lbl_estatura)
        layout.addWidget(self.txt_estatura)
        layout.addWidget(lbl_tez)
        layout.addWidget(self.txt_tez)
        layout.addWidget(lbl_pelo)
        layout.addWidget(self.combo_pelo)
        layout.addWidget(lbl_peloC)
        layout.addWidget(self.combo_peloC)
        layout.addWidget(lbl_ojos)
        layout.addWidget(self.combo_ojo)
        layout.addWidget(lbl_rostro)
        layout.addWidget(self.combo_rostro)
        
        layout.addWidget(self.btn_guardar)
        layout.addWidget(self.txt_output)
        
        # Se hace que el layout sea el central widget
        center.setLayout(layout)
        self.setCentralWidget(center)
        
    def clicked_btn(self):
        # Cree un cuadro de diálogo para preguntar al usuario si desea guardar los datos.
        respuesta, ok = QInputDialog.getItem(self, "Guardar datos", "¿Desea guardar los datos?", ["Sí", "No"], 0, False)
        if ok and respuesta == "Sí":
            # Obtenerlos datos de los campos de entrada y crear una cadena
            datos = f"Nombre: {self.txt_nombre.text()}\n"
            datos += f"Apellido: {self.txt_apellido.text()}\n"
            datos += f"Nacionalidad: {self.txt_nacionalidad.text()}\n"
            datos += f"Género: {self.combo_genero.currentText()}\n"
            datos += f"Estatura: {self.txt_estatura.text()} cm\n"
            datos += f"Tez de piel: {self.txt_tez.text()}\n"
            datos += f"Tipo de pelo: {self.combo_pelo.currentText()}\n"
            datos += f"Color de pelo: {self.combo_peloC.currentText()}\n"
            datos += f"Color de ojos: {self.combo_ojo.currentText()}\n"
            datos += f"Tipo de rostro: {self.combo_rostro.currentText()}\n"
            self.txt_output.setText(datos)
        else:
            # Limpiar la salida si no se ingresa nada
            self.txt_output.setText("")

# Create the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = myApp()
    ventana.show()
    sys.exit(app.exec_())