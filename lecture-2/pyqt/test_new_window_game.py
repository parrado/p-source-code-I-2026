from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from new_window_doctor import NewWindow


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Médico")
       
        # Se crean los labels
        l1=QLabel('ID: ')
        l2=QLabel('Contraseña: ')

        # Se crean los campos de entrada
        self.e1=QLineEdit()
        self.e2=QLineEdit()

        b1=QPushButton('Iniciar sesión')
        b1.clicked.connect(self.newWindow)
        
        
        gridLayout=QGridLayout()
        
         # Se añaden los widgets al layout
        gridLayout.addWidget(l1,0,0)
        gridLayout.addWidget(l2,1,0)
        
        gridLayout.addWidget(self.e1,0,1)
        gridLayout.addWidget(self.e2,1,1)

        gridLayout.addWidget(b1,2,0,1,2)
        


        widget = QWidget()
        widget.setLayout(gridLayout)
        #QMainWindow requiere un widget central
        self.setCentralWidget(widget)

        
        # Deshabilita el botón de maximizar
        self.setWindowFlags( Qt.MSWindowsFixedSizeDialogHint)
    
    def newWindow(self):
        id=self.e1.text()
        password=self.e2.text()
        if len(id) and len(password):           
            self.nw=NewWindow(id, password)
            self.nw.show()
        else:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("Por favor ingresar ID y Contraseña")
            msgBox.setWindowTitle("Alerta")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()

       
app = QApplication([])
ex = MainWindow()
ex.show()
app.exec()