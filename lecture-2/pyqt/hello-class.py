from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class window(QWidget):
   def __init__(self,title):
      super().__init__()
      self.resize(640,480)
      self.setWindowTitle(title)
      self.label = QLabel(self)
      self.label.setText("Hello World")
      self.show()    

app = QApplication([])
title='My window'
ex = window(title)
app.exec()