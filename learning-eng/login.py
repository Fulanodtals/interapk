import sys
import os
import time
from PyQt6.QtWidgets import QApplication, QWidget,QPushButton, QLineEdit, QLabel, QGridLayout, QSizePolicy
from PyQt6.QtSql import QSqlDatabase, QSqlQuery #blibliotecas para mecher com o banco de dados (microsoft acess)

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
        layout.addWidget(loginButton,               4, 3, 1, 5)

        self.status = QLabel('')
        self.status.setStyleSheet('font-size:20px; color:red;')
        layout.addWidget(self.status, 4, 0, 1, 1)

        def conectDB(self):
            #https://doc.qt.io/qt-5/sql-driver.html
            db = QSqlDatabase.addDatabase('QODBC')#coloque o tipo de database disponivel no link acima
            #definindo a string de conexao para conectar com o banco de dados
            db.setDatabaseName('DRIVER={{Microsoft Acess Driver(*.mdb, *.accdb)}};DBQ={0}'.format(os.path.join(os.getcwd(), 'MyDatabase.accdb')))

            if not db.open():#aplicando uma execao para caso nao funcione 
                print('error in database conection')
                self.status.setText('conecion failed, try again later.')

    
        def UserCheck(self):
            #pegando o input do usuario
            username = self.LineEdit['Username'].text()
            password = self.LineEdit['Password'].text()
            
            query = QSqlQuery()#variavel para consulta da database
            #abaixo ele verifica no banco de dados se tem input correto
            query.prepare('SELECT * FROM Users WHERE Username=:username')#para todos da lista usuarios onde Usuario = input 
            
            query.exec()
            

if __name__ == "__main__":

    app = QApplication(sys.argv)
    
    LoginWindow = LoginApp()
    LoginWindow.show()

    #execao para o fechamento do aplicativo
    try:
        sys.exit(app.exec())
    except SystemExit:
        print("closing")