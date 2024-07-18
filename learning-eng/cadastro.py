import sys
import os
from time import sleep
from PyQt6.QtWidgets import QApplication, QWidget,QPushButton, QLineEdit, QLabel, QGridLayout, QSizePolicy, QRadioButton
from PyQt6.QtCore import Qt
import _mysql_connector

class LoginApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("main")
        self.setFixedSize(300, 300)

        layout = QGridLayout()
        self.setLayout(layout)

        label = {}
        self.LineEdit = {}

        label["Codigo"] = QLabel('Codigo: ')
        label["Descricao"] = QLabel('Descrição: ')
        label["Preco"] = QLabel('Preço: ')
        label['categoria'] = QLabel('Categoria:')

        label["Codigo"].setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        label["Descricao"].setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)   
        label["Preco"].setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)   
        
        self.LineEdit["Codigo"] = QLineEdit()
        self.LineEdit["Descricao"] = QLineEdit()
        self.LineEdit["Preco"] = QLineEdit()

        self.button = {}
        self.button['informatica'] = QRadioButton('informatica')
        self.button['alimentos'] = QRadioButton('alimentos')
        self.button['eletronicos'] = QRadioButton('eletronicos')
        
        sendButton = QPushButton('log-in')
        sendButton.clicked.connect(self.send)
        
        layout.addWidget(label["Codigo"],            1, 0, 1, 1)
        layout.addWidget(self.LineEdit['Codigo'],    1, 1, 1, 3)
        layout.addWidget(label['Descricao'],         2, 0, 1, 1)
        layout.addWidget(self.LineEdit['Descricao'], 2, 1, 1, 3)
        layout.addWidget(label['Preco'],             3, 0, 1, 1)
        layout.addWidget(self.LineEdit['Preco'],     3, 1, 1, 3)
        layout.addWidget(label['categoria'],          5, 0, 1, 1)
        layout.addWidget(self.button['informatica'],  5, 1, 1, 3)
        layout.addWidget(self.button['alimentos'],    6, 1, 1, 3)
        layout.addWidget(self.button['eletronicos'],  7, 1, 1, 3)
        layout.addWidget(sendButton,                  8, 2, 1, 2)
 

    def send(self):
        pass
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    LoginWindow = LoginApp()
    LoginWindow.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print("closing")