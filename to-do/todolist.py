import sys
import os
from time import sleep
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QListWidget,QMessageBox, QVBoxLayout, QLabel, QLineEdit
from PyQt6.QtCore import Qt
import pandas as pd

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

        df = pd.read_excel('./notas.xlsx', header=None)
        self.db = df.iloc[:, 0].tolist()
        for item in self.db:
            print(item)
            self.list.addItem(item)
        self.list.setStyleSheet('font-size:15px;')
        self.list.doubleClicked.connect(self.deleteItem)

        addItemButton = QPushButton('Nova tarefa')
        addItemButton.setStyleSheet('padding:10px;font-size:20px;')
        addItemButton.clicked.connect(self.add_item)
 

        #adicionando widgets na tela
        widgets = [label, self.list, addItemButton]
        for widget in widgets:
            layout.addWidget(widget)
        

    def add_item(self):
        self.additem = AddItem(self)
        self.additem.show()

    def addTesk(self, tesk):  
        self.db.append(tesk)
        #self.list.addItem(tesk)

    def deleteItem(self):
        selectItem = self.list.selectedItems()
        if not selectItem:
            QMessageBox.information(self, "No Selection", "Please select an item to delete.")
            return
        for item in selectItem:
            #self.db.remove()
            self.list.takeItem(self.list.currentRow())

    def changedItem(self, item):
        if len(self.list)>0:
            print(f'item selecionado: {item.text()}')

class AddItem(QWidget):
    def __init__(self, main_app):
        super().__init__()
        self.main_app = main_app
        self.setWindowTitle("main")
        self.setFixedSize(200, 300)

        layout = QVBoxLayout()
        self.setLayout(layout)

        label = QLabel('NOVA TAREFA')
        label.setStyleSheet('font-size: 20px;font-weight:bold;')
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        pergunta = QLabel('qual sera a nova tarefa?')
        self.tarefa = QLineEdit()

        button = QPushButton('adicionar')
        button.clicked.connect(self.sendTesk)

        widgets = [label, pergunta, self.tarefa, button]
        for widget in widgets:
            layout.addWidget(widget)

    def sendTesk(self):
        tesk = self.tarefa.text()
        self.main_app.addTesk(tesk)
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    Window = MainApp()
    Window.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print("closing")