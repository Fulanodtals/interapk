import sys
import socket
import threading
import os
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QVBoxLayout, QListWidget, QGridLayout
from PyQt6.QtGui import QIntValidator
from PyQt6.QtCore import Qt

class MainApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("main")
        self.setFixedSize(300,400)
        
        layout = QGridLayout()
        self.setLayout(layout)

        title = QLabel('Remote Control')
        title.setStyleSheet('font-size: 20px;font-weight:bold;')
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label = {}
        self.userInput = {}

        self.label['ip'] = QLabel('your ip') 
        self.label['port'] = QLabel('select port') 
        self.label['myip'] = QLabel()
        self.userInput['port'] = QLineEdit('12345')
        self.list = QListWidget()

        
        layout.addWidget(title,                  0,0,1,2)
        layout.addWidget(self.label['ip'],       1,0,1,1)
        layout.addWidget(self.label['port'],     1,1,1,1)
        layout.addWidget(self.label['myip'],     2,0,1,1)
        layout.addWidget(self.userInput['port'], 2,1,1,1)
        layout.addWidget(self.list,              3,0,1,2)
        
        
        threading.Thread(target=self.conectCF, daemon=True).start()
        threading.Thread(target=self.getIpAdress, daemon=True).start()
        
    def conectCF(self):
        port = int(self.userInput['port'].text())
        
        print('iniciando server')
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('0.0.0.0', port))
        server.listen()

        while True:
            print('analizando')
            running, addr = server.accept()
            mensage = running.recv(1024).decode('utf-8')

            if mensage == 'desligar':
                print('desligando')

            running.close()



    def getIpAdress(self):
        try:
            getip = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            getip.connect(("8.8.8.8", 80))  # O IP 8.8.8.8 é do Google DNS, qualquer IP externo serve
            ip = getip.getsockname()[0]
            getip.close()
            self.label['myip'].setText(f'{ip}')
            self.label['myip'].adjustSize()
        except:
            self.label['myip'].setText('ip nao encontrado')
            self.label['myip'].adjustSize()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = MainApp()
    Window.show()
    try:
        sys.exit(app.exec())
    except SystemExit:
        print("closing")