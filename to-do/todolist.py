import sys
import os
from time import sleep
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QListWidget, QAbstractItemView, QVBoxLayout, QLabel, QLineEdit
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
        self.additem = AddItem(self, 0)
        self.additem.show()

    def deleteItem(self):
        if len(self.list)>0:
            self.list.takeItem(self.list.currentRow())
    
    def editItem(self):
        pass

    def changedItem(self, item):
        if len(self.list)>0:
            print(f'item selecionado: {item.text()}')

class AddItem(QWidget):
    def __init__(self, mainWindow, choise):
        super().__init__()
        self.mainWindow = mainWindow
        self.setWindowTitle("main")
        self.setFixedSize(200, 300)
        if choise == 0:
            self.addingItem

        layout = QVBoxLayout()
        self.setLayout(layout)

        label = QLabel('NOVA TAREFA')
        label.setStyleSheet('font-size: 20px;font-weight:bold;')
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        pergunta = QLabel('qual sera a nova tarefa?')
        self.tarefa = QLineEdit()

        button = QPushButton('adicionar')
        button.clicked.connect(self.addTask)

        widgets = [label, pergunta, self.tarefa, button]
        for widget in widgets:
            layout.addWidget(widget)

    def addTask(self):
        tesk = self.tarefa.text()
        print(tesk)
        

    

    def addingItem(self):
        pass
        
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    Window = MainApp()
    Window.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print("closing")