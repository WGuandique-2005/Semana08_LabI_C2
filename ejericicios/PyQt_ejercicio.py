"""
* Ejercicio con PyQt5

? Haremos una calculadora que puede realizar las opreaciones basicas
! que tenga dos LineEdit u que muestre el resultado en un label,
todo\ usando PyQt5
"""
# Se importan los módulos necesarios para crear una aplicación gráfica con PyQt5

import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QLineEdit, QLabel,
                            QPushButton, QWidget, QVBoxLayout, QComboBox)
class myCalc(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(30,300,430,300)
        self.setWindowTitle("Calculadora_basica")
        self.setContentsMargins(40,10,40,40)
        self.setStyleSheet("background-color: lightblue;")
        
        label1 = QLabel("Esocoja una opcion:")
        self.op = QComboBox()
        self.op.addItem("Suma")
        self.op.addItem("Resta")
        self.op.addItem("Multiplicacion")
        self.op.addItem("Division")
        
        label2 = QLabel("Ingrese los valores:")
        self.txt1 = QLineEdit()
        self.txt2 = QLineEdit()
        
        self.btn = QPushButton("Calcular")
        self.btn.clicked.connect(self.click_calc)
        self.resp = QLabel()
        
        center = QWidget()
        layout = QVBoxLayout()
        
        layout.addWidget(label1)
        layout.addWidget(self.op)
        layout.addWidget(label2)
        layout.addWidget(self.txt1)
        layout.addWidget(self.txt2)
        layout.addWidget(self.btn)
        layout.addWidget(self.resp)
        
        center.setLayout(layout)
        self.setCentralWidget(center)
    
    def click_calc(self):
        try:
            num1 = float(self.txt1.text())
            num2 = float(self.txt2.text())
            suma = num1 + num2
            resta = num1 - num2
            multiplicacion = num1 * num2
            division = num1 / num2
            if self.op.currentText() == "Suma":
                self.resp.setText("La suma es: " + str(suma))
            elif self.op.currentText()== "Resta":
                self.resp.setText("La resta es: " + str(resta))
            elif self.op.currentText() == "Division":
                if num2 == 0:
                    self.resp.setText("Error, no se puede dividir entre cero")
                else:
                    self.resp.setText("La division es: " + str(division))
            elif self.op.currentText() == "Multiplicacion":
                self.resp.setText("La multiplicacion es: " + str(multiplicacion))
        except:
            self.resp.setText("Error, ingrese valores validos")

app = QApplication(sys.argv)
calc = myCalc()
calc.show()
app.exec()