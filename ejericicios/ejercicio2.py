"""
* Ejercicio 2

? Construir un programa que muestre una ventana y que lea
! una clave secreta sin mostra los caracteres que la componen,
todo\ en PyQt5
"""

import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QLineEdit, QLabel,
                            QPushButton, QWidget, QVBoxLayout)

class myAPP(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(100,100,300,100)
        self.setWindowTitle("Ejercicio 2")
        
        self.label = QLabel("Ingrese la clave:")
        self.editxt = QLineEdit()
        self.editxt.setEchoMode(QLineEdit.Password)
        self.btn = QPushButton("Ingresar")
        self.btn.clicked.connect(self.clicked_btn)
        
        central = QWidget()
        layout = QVBoxLayout()
        
        layout.addWidget(self.label)
        layout.addWidget(self.editxt)
        layout.addWidget(self.btn)
        central.setLayout(layout)
        self.setCentralWidget(central)
        
    def clicked_btn(self):
        clave = self.editxt.text()
        print(f"La clave es: {clave}")

app = QApplication(sys.argv)
window = myAPP()
window.show()
app.exec()