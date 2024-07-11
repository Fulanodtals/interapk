import sys#importacao para gerenciamento do programa
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QLabel#importacoes que serao usadas 
from PyQt6.QtGui import QIcon #importacao para utilizar icones


class MyApp(QWidget):#classe principal do aplicativo
    def __init__(self):#construtor da classe
        super().__init__()#declara essa classe como mae
        self.setWindowTitle("main")#colocando nome para janela
        self.setWindowIcon(QIcon('maps.png'))#inserindo um icone
        self.resize(500, 400)#alterando tamanho da tela

        #conteiner
        layout = QVBoxLayout()#opcao de layout para organizar os widgets(elementos)
        self.setLayout(layout)#instanciando o container(layout)

        self.label = QLabel('what is your name:')#texto
        self.input = QLineEdit()#caixa de texto
        self.button = QPushButton('click here')#botao
        self.button.released.connect(self.seyHello)#conecta com a funcao a executa
        self.output = QTextEdit()#caixa de saida de texto

        #colocando os widgets no container:
        layout.addWidget(self.label)
        layout.addWidget(self.input)
        layout.addWidget(self.button)
        layout.addWidget(self.output)

    def seyHello(self):
        self.getText = self.input.text()
        print(self.getText)
        self.output.setText(f'hello {self.getText}')
        




app = QApplication(sys.argv)#isso gerencia o fluxo de controle

window = MyApp()#instancia da classe
window.show()#mostrar elementos da classe


app.exec()#executa o aplicativo