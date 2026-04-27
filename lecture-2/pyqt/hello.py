from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MyFirstWindow(QWidget):
   def __init__(self):
      super().__init__()
      self.resize(640,480)
      self.setWindowTitle("Mi primer ventana")
      self.label = QLabel(self)
      self.label.setText("Hello Cruel World")
      
      font = QFont()
      font.setFamily("Times New Roman")
      font.setPointSize(26)
      self.label.setFont(font)
      self.label.move(320,240)      
      
      self.show() 

app = QApplication([])
ex = MyFirstWindow()
app.exec()