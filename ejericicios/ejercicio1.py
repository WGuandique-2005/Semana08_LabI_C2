"""
* Ejercicio 1

? Contruir un programa que muestre una ventana en la cual
! aparezca su nombre completo y su edad centrados,
todo\ usando PyQt5
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(100, 100, 300, 275)
        self.setWindowTitle("Ejercicio 1")
        
        label = QLabel("William Josue Guandique Rivera, 18 años")
        
        self.setCentralWidget(label)

app = QApplication(sys.argv)
window = MyApp()
window.show()
app.exec()
