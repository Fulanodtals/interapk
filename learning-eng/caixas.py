import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit

program = QApplication(sys.argv)#cria a variavel mae que recebe todos os argumentos


window = QWidget()#cria a janela
window.resize(500, 400)#da a janera um tamanho x e y
window.setWindowTitle("first window")# da um titulo a janela

button = QPushButton("botao", window) #cria um botao
button.setGeometry(100, 100, 50, 50) #coloca o tamanho e a posicao do botao
button.setStyleSheet('''
    color: white;
    background-color: black;'''
) #estiliza o botao



def lerValor():
    value = getInput.text()
    label.setText(value)
    label.adjustSize()

def BotaoClickado():#funcao a ser executada
    label.setText()#muda o texto
    label.adjustSize()#ajusta o label para a mudanca
button.released.connect( lerValor)#executa a funcao apardir do click


label = QLabel("texto", window)#cria uma label (texto)
label.move(300, 100)
label.setStyleSheet('font-size:30px;')

getInput = QLineEdit("", window)
getInput.setGeometry(100, 200, 150, 50)


window.show()#mostrar elementos na tela

program.exec()#executa o programa