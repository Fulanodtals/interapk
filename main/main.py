import sys
import socket
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

        self.label['ip'] = QLabel('ip') 
        self.label['port'] = QLabel('port') 
        self.userInput['ip'] = QLineEdit('0.0.0.0')
        self.userInput['port'] = QLineEdit('12345')
        

        self.list = QListWidget()

        
        layout.addWidget(title,                  0,0,1,2)
        layout.addWidget(self.label['ip'],       1,0,1,1)
        layout.addWidget(self.label['port'],     1,1,1,1)
        layout.addWidget(self.userInput['ip'],   2,0,1,1)
        layout.addWidget(self.userInput['port'], 2,1,1,1)
        layout.addWidget(self.list,              3,0,1,2)
        

        self.conectCF
        
    def conectCF(self):
        ip = self.userInput['ip'].text()
        port = self.userInput['port'].text()
        
        print('iniciando server')
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('0.0.0.0', port))
        server.listen()

        while True:
            print('analizando')
            running, addr = server.accept()
            mensage = running.recv(1024).decode('utf-8')

            print(f'decodificando: {mensage}')
            
            if mensage == 'desligar':
                print('desligando')

            running.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = MainApp()
    Window.show()
    try:
        sys.exit(app.exec())
    except SystemExit:
        print("closing")