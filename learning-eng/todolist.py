import sys
import os
from time import sleep
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QListWidget, QAbstractItemView, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt

class MainApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("main")
        self.setFixedSize(400, 450)

        layout = QVBoxLayout()
        self.setLayout(layout)
        
        label = QLabel('To-do list')
        label.setStyleSheet('font-size: 20px;font-weight:bold;')
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.list = QListWidget(self)
        self.list.addItems(['tarefa 1', 'tarefa 2', 'tarefa 3'])
        #self.list.currentItemChanged.connect(self.changedItem)
        self.list.setStyleSheet('font-size:15px;')
        addItemButton = QPushButton('add item')
        addItemButton.clicked.connect(self.addItem)

        deleteItemButton = QPushButton('delete item')
        deleteItemButton.clicked.connect(self.deleteItem)


        #adicionando widgets na tela
        widgets = [label, self.list, addItemButton, deleteItemButton]
        for widget in widgets:
            layout.addWidget(widget)
        
    def addItem(self):
        self.additem = AddItem(self)
        self.additem.show()

    def deleteItem(self):
        if len(self.list)>0:
            self.list.takeItem(self.list.currentRow())


    def changedItem(self, item):
        if len(self.list)>0:
            print(f'item selecionado: {item.text()}')

class AddItem(QWidget):
    def __init__(self, mainWindow):
        super().__init__()
        self.mainWindow = mainWindow
        self.setWindowTitle("main")
        self.setFixedSize(300, 400)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    Window = MainApp()
    Window.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print("closing")