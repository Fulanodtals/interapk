import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QGridLayout, QSizePolicy, QVBoxLayout
from PyQt6.QtCore import Qt
import pandas as pd

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
        self.setFixedSize(350, 200)

        layout = QGridLayout()
        self.setLayout(layout)

        label = {}
        self.LineEdit = {}

        label["login"] = QLabel('Login')
        label['login'].setStyleSheet('font-size:20px;')


        label["Username"] = QLabel('Username: ')
        label["Password"] = QLabel('Password: ')

        label["Username"].setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        label["Password"].setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)   
        
        self.LineEdit["Username"] = QLineEdit()
        self.LineEdit["Password"] = QLineEdit()
        self.LineEdit["Password"].setEchoMode(QLineEdit.EchoMode.Password)
        
        layout.addWidget(label['login'],            0, 0, 1, 3, Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(label["Username"],         1, 0, 1, 1)
        layout.addWidget(self.LineEdit['Username'], 2, 0, 1, 3)
        layout.addWidget(label["Password"],         3, 0, 1, 1)
        layout.addWidget(self.LineEdit["Password"], 4, 0, 1, 3)

        loginButton = QPushButton('log-in')
        loginButton.released.connect(self.UserCheck)
        layout.addWidget(loginButton,               5, 2, 1, 1)


        self.status = QLabel('')
        self.status.setStyleSheet('font-size:12px; color:red;')
        layout.addWidget(self.status, 5, 0, 1, 1)


    def UserCheck(self):
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

    try:
        sys.exit(app.exec())
    except SystemExit:
        print("closing")