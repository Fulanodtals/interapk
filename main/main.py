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
        self.resize(300, 400)
        
        layout = QVBoxLayout()
        gridWidget = QWidget()
        gridLayout = QGridLayout()

        title = QLabel('Remote Control')
        title.setStyleSheet('font-size: 20px;font-weight:bold;')
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label = {}
        self.userInput = {}

        self.label['ip'] = QLabel() 
        self.label['port'] = QLabel() 
        self.userInput['ip'] = QLineEdit().setValidator(QIntValidator())
        self.userInput['port'] = QLineEdit().setValidator(QIntValidator())

        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.userInput['ip'].text(), self.userInput['port'].text()))
        server.listen()

        
        gridLayout.setLayout(gridWidget)

        self.layout.addWidget(self.gridWidget)
        self.setLayout(layout)

        self.list = QListWidget()

        vWidgets = [title, self.list]
        for vwidget in vWidgets:
            layout.addWidget(vwidget)

        gridLayout.addWidget(self.label['ip'],       )
        gridLayout.addWidget(self.label['port'],     )
        gridLayout.addWidget(self.userInput['ip'],   )
        gridLayout.addWidget(self.userInput['port'], )



if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = MainApp()
    Window.show()
    try:
        sys.exit(app.exec())
    except SystemExit:
        print("closing")