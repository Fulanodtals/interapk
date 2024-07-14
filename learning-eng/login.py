import sys
import os
from time import sleep
from PyQt6.QtWidgets import QApplication, QWidget,QPushButton, QLineEdit, QLabel, QGridLayout, QSizePolicy
import pandas as pd #biblioteca para ver exel

#classe da tela principal
class MainApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("main")
        self.resize(600, 500)
        label = QLabel('main app', parent=self)

#classe da tela de login
class LoginApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("main")
        self.setFixedSize(450, 150)

        layout = QGridLayout()
        self.setLayout(layout)

        label = {}#chaves pq vai criar varias dessa
        self.LineEdit = {}#chaves pq vai criar varias dessa
        
        #pode acessar essa variavel por label["nome"]
        label["Username"] = QLabel('Username: ')#criando a label username
        label["Password"] = QLabel('Password: ')#criando a label password

        #definindo o tamanho x e z com o padrao de fixado 
        label["Username"].setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        label["Password"].setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)   
        
        self.LineEdit["Username"] = QLineEdit()#definindo um input
        self.LineEdit["Password"] = QLineEdit()
        self.LineEdit["Password"].setEchoMode(QLineEdit.EchoMode.Password)#escondendo os caracteres da senha
        
        #coloca na tela e define a posicao da linha, da coluna, depois do tamanho da linha e coluna
        layout.addWidget(label["Username"],         0, 0, 1, 1)
        layout.addWidget(self.LineEdit['Username'], 0, 1, 1, 3)#coloca na tela e define a posicao x, y depois o tamanho x, y
 
        layout.addWidget(label["Password"],         1, 0, 1, 1)
        layout.addWidget(self.LineEdit["Password"], 1, 1, 1, 3)#coloca na tela e define a posicao x, y depois o tamanho x, y

        loginButton = QPushButton('log-in')
        loginButton.released.connect(self.UserCheck)#conectando metodo ao botao
        layout.addWidget(loginButton,               4, 3, 1, 1)

        self.status = QLabel('')
        self.status.setStyleSheet('font-size:12px; color:red;')
        layout.addWidget(self.status, 4, 0, 1, 1)

        #self.conectDB()#aplicando metodo no main

    def conectDB(self):#trocar database
        #https://doc.qt.io/qt-5/sql-driver.html
        self.db = QSqlDatabase.addDatabase('QODBC')#coloque o tipo de database disponivel no link acima
        #definindo a string de conexao para conectar com o banco de dados
        self.db.setDatabaseName('DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=MyDatabase.accdb')

        if not self.db.open():#aplicando uma execao para caso nao funcione 
            print('error in database conection')
            self.status.setText('conecion failed, try again later.')


    def UserCheck(self):
        #pegando o input do usuario
        username = self.LineEdit['Username'].text()
        password = self.LineEdit['Password'].text()
        users = pd.read_excel('./Users.xlsx')

        for user in users['Username']:
            if user == username:
                for code in users['Password']:
                    if code == password:
                        self.mainApp = MainApp()
                        self.mainApp.show()
                        LoginWindow.close()
                    else:
                        self.status.setText('password incorrect')
            else:
                self.status.setText('username not found')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    LoginWindow = LoginApp()
    LoginWindow.show()

    #execao para o fechamento do aplicativo
    try:
        sys.exit(app.exec())
    except SystemExit:
        print("closing")