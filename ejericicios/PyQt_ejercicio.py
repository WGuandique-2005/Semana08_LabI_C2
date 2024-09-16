"""
* Ejercicio con PyQt5

? Haremos una calculadora que puede realizar las operaciones básicas,
? como suma, resta, multiplicación y división;
* que permita seleccionar que se desea realizar con un combo box
! que tenga dos LineEdit que muestre el resultado en un label,
todo usando PyQt5

! Con la utilización de <RadioButton> <ComboBox> <SpinBox> 
"""
# Se importan los módulos necesarios para crear una aplicación gráfica con PyQt5

import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QLineEdit, QLabel, QDialog,
                            QPushButton, QWidget, QVBoxLayout, QComboBox, QRadioButton)

class myCalc(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(30,300,430,300)
        self.setWindowTitle("Calculadora_basica")
        
        # Establecer los márgenes de contenido
        self.setContentsMargins(40,10,40,40)
        
        label1 = QLabel("Escoja una opción:")
        # Crear un combobox para seleccionar la operación
        self.op = QComboBox()
        self.op.addItem("Suma")
        self.op.addItem("Resta")
        self.op.addItem("Multiplicación")
        self.op.addItem("División")
        
        label2 = QLabel("Ingrese los valores:")
        # Crear dos LineEdit para ingresar los valores
        self.txt1 = QLineEdit()
        self.txt2 = QLineEdit()
        
        # Crear un botón para calcular el resultado
        self.btn = QPushButton("Calcular")
        self.btn.clicked.connect(self.click_calc)
        
        # Crear un label para mostrar el resultado
        self.resp = QLabel()
        
        # Crear un botón para cerrar la aplicación
        self.exit = QPushButton("Cerrar")
        self.exit.clicked.connect(self.clicked_exit)
        
        # Crear un widget central
        center = QWidget()
        # Crear un layout vertical
        layout = QVBoxLayout()
        
        # Agregar los widgets al layout
        layout.addWidget(label1)
        layout.addWidget(self.op)
        layout.addWidget(label2)
        layout.addWidget(self.txt1)
        layout.addWidget(self.txt2)
        layout.addWidget(self.btn)
        layout.addWidget(self.resp)
        layout.addWidget(self.exit)
        
        # Establecer el layout en el widget central
        center.setLayout(layout)
        
        # Establecer el widget central en la ventana
        self.setCentralWidget(center)
    
    def click_calc(self):
        try:
            # Convertir los valores ingresados a números
            num1 = float(self.txt1.text())
            num2 = float(self.txt2.text())
            
            # Realizar las operaciones
            suma = num1 + num2
            resta = num1 - num2
            multiplicacion = num1 * num2
            division = num1 / num2
            
            # Mostrar el resultado según la operación seleccionada
            if self.op.currentText() == "Suma":
                self.resp.setText("La suma es: " + str(suma))
            elif self.op.currentText()== "Resta":
                self.resp.setText("La resta es: " + str(resta))
            elif self.op.currentText() == "División":
                if num2 == 0:
                    self.resp.setText("Error, no se puede dividir entre cero")
                else:
                    self.resp.setText("La división es: " + str(division))
            elif self.op.currentText() == "Multiplicación":
                self.resp.setText("La multiplicación es: " + str(multiplicacion))
        except:
            # Mostrar un mensaje de error si se ingresa un valor inválido
            self.resp.setText("Error, ingrese valores válidos")
            
    def clicked_exit(self):
        # Crear un dialogo de confirmación
        confirm_dialog = QDialog()
        confirm_dialog.setWindowTitle("Confirmar cierre")

        label = QLabel("¿Está seguro de cerrar la aplicación?")
        btn_yes = QRadioButton("Sí")
        btn_no = QRadioButton("No")

        # Set the initial checked state of the radio buttons
        btn_no.setChecked(True)

        btn_yes.clicked.connect(lambda: self.close(exit()))
        btn_no.clicked.connect(lambda: confirm_dialog.reject())

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(btn_yes)
        layout.addWidget(btn_no)

        confirm_dialog.setLayout(layout)

        if confirm_dialog.exec_() == QDialog.Accepted:
            self.close()

# Crear una aplicación
app = QApplication(sys.argv)
calc = myCalc()
calc.show()
# Ejecutar la aplicación
app.exec()