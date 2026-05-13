from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from new_window_game import NewWindow


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Jugador")
       
        # Se crea el label
        l1=QLabel('Nombre jugador: ')

        # Se crea el campo de entrada
        self.e1=QLineEdit()
        
        b1=QPushButton('Entrar al juego')
        b1.clicked.connect(self.newWindow)
        
        
        gridLayout=QGridLayout()
        
         # Se añaden los widgets al layout
        gridLayout.addWidget(l1,0,0)
        
        gridLayout.addWidget(self.e1,0,1)
        
        gridLayout.addWidget(b1,2,0,1,2)
        


        widget = QWidget()
        widget.setLayout(gridLayout)
        #QMainWindow requiere un widget central
        self.setCentralWidget(widget)

        
        # Deshabilita el botón de maximizar
        self.setWindowFlags( Qt.MSWindowsFixedSizeDialogHint)
    
    def newWindow(self):
        name=self.e1.text()
        if len(name):           
            self.nw=NewWindow(name)
            self.nw.show()
        else:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText("Por favor ingresar nombre de jugador")
            msgBox.setWindowTitle("Alerta")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()

       
app = QApplication([])
ex = MainWindow()
ex.show()
app.exec()