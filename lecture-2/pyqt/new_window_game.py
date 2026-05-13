from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from client_transport import GameClient
from json import loads

dices_images={
    1:"dice-six-faces-one.png",
    2:"dice-six-faces-two.png",
    3:"dice-six-faces-three.png",
    4:"dice-six-faces-four.png",
    5:"dice-six-faces-five.png",
    6:"dice-six-faces-six.png"
}

class NewWindow(QMainWindow):
    def __init__(self,name):
        super().__init__()       
        self.setWindowTitle("Parchís - Jugador: "+name)

        self.display_width = 640
        self.display_height = 480
        # create the label that holds the image
        self.image_label = QLabel()
        pixmap=QPixmap("parchis.png")        
        # Asigna la imagen al pixmap, antes reduciendo el tamaño 
        self.image_label.setPixmap(pixmap.scaled(int(pixmap.width()/2),int(pixmap.height()/2)))
        
        self.image_label.resize(self.display_width, self.display_height)

        button=QPushButton('Lanzar dados')
        button.clicked.connect(self.roll_dice)
        
        self.dice0_label=QLabel()
        self.dice1_label=QLabel()
        
        layout=QGridLayout()

        layout.addWidget(self.image_label, 0, 0, 2, 2)
        layout.addWidget(button, 2, 0,2,2,Qt.AlignCenter)
        layout.addWidget(self.dice0_label, 4, 0,1,1,Qt.AlignCenter)
        layout.addWidget(self.dice1_label, 4, 1,1,1,Qt.AlignCenter)

        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

        self.client = GameClient("ws://127.0.0.1:8765", self.handle_response)
        self.client.connect()
        self.client.send_action("join", player_name=name)

    def roll_dice(self):
        # Implementation for rolling dice
        self.client.send_action("roll_dice")

    def handle_response(self, response):
        # Handle the response from the server
        print("Received response:", response)
        data = response
        dices_value=data["board_state"]["dices_value"]

        if dices_value[0]!=0:
            self.dice0_label.setPixmap(QPixmap(dices_images[dices_value[0]]).scaled(100, 100))
        if dices_value[1]!=0:
            self.dice1_label.setPixmap(QPixmap(dices_images[dices_value[1]]).scaled(100, 100))