import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QComboBox

program = QApplication(sys.argv)

def lerComboBox():
    boxText = box.currentText()#pega texto do elemento e insere na variavel
    labelPrint.setText(boxText)
    labelPrint.adjustSize()


window = QWidget()
window.resize(600, 400)
window.setWindowTitle("comboBox")

button = QPushButton("ver", window)
button.setGeometry(400, 100, 100, 50)
button.clicked.connect(lerComboBox)

label = QLabel("text: ", window)
label.move(100, 200)
label.setStyleSheet('font-size:20px;')

labelPrint = QLabel(window)
labelPrint.move(150, 200)
labelPrint.setStyleSheet('font-size:20px;')


box = QComboBox(window)#instanciando a combo box#dando um titulo
box.addItems(['linguagens de programacao','java','python', 'php'])#adicionando os itens(o primeiro sera o titulo)
box.move(50, 50)


window.show()
program.exec()