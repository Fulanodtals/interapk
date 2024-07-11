import sys
from PyQt6.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton, QLineEdit, QFileDialog, QLabel
import pandas as pd #biblioteca para mecher com o exel


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("main")
        self.resize(700, 500)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.table = QTableWidget()#instancia para criar a tabela
        layout.addWidget(self.table)#inserindo a tabela na tela


        self.label = QLabel('digite o nome da planilha:')
        layout.addWidget(self.label)

        self.getSheet_name = QLineEdit()
        layout.addWidget(self.getSheet_name)

        self.loadButton = QPushButton('Load data')
        self.loadButton.released.connect(self.LoadExeldata)
        layout.addWidget(self.loadButton)

    #metodo para carregar o exel
    def LoadExeldata(self):#os parametros é para a pasta do exel e o nome da planilia
        self.getFile = QWidget()#criando janela para procurar o arquivo

        self.sheetName = self.getSheet_name.text()#pegando testo do LineEdit
        #procura o arquivo e dita o titulo da janela
        self.exel_dir, _ = QFileDialog.getOpenFileName(self.getFile, "selecione arquivo")
        df = pd.read_excel(self.exel_dir, self.sheetName)#cria uma instancia que ira ler o exel

        if df.size == 0:#condicao se nao conseguir pegar o exel
            return # vai apenas retornar

        df.fillna(0, inplace=True)#exclui as tabelas vazias
        self.table.setRowCount(df.shape[0])#faz a contagem de linhas
        self.table.setColumnCount(df.shape[1])#faz a contagem das colunas
        self.table.setHorizontalHeaderLabels(df.columns)#coloca o cabecalho no topo

        #retornar os valores da planilha
        for row in df.iterrows(): #para cada linha da planilia
            values = row[1]#pega os valores apartir da linha 2
            for col_index, value in enumerate(values):#pega a coluna principal e seus valores e retorna
                if isinstance(value, (float, int)):#se der certo ele pega os valores tanto float como int
                    value = f'{value:0,.0f}'#limita a virgula
                table_item = QTableWidgetItem(str(value))#e insere na planilia como uma string
                self.table.setItem(row[0], col_index, table_item)#colocando na planilha a linha, com a coluna principal e os itens
    
if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = MyApp()
    window.show()

    #execao para o fechamento do aplicativo
    try:
        sys.exit(app.exec())
    except SystemExit:
        print("closing")