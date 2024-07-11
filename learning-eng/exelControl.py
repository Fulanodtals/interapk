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

        self.welcome = QLabel('(: Welcome to exel editor :)')
        self.welcome.setStyleSheet('font-size:15px; align-itens:center;')
        layout.addWidget(self.welcome)

        self.table = QTableWidget()#instancia para criar a tabela
        layout.addWidget(self.table)#inserindo a tabela na tela


        self.label = QLabel('digite o nome da planilha:')
        layout.addWidget(self.label)

        self.getSheet_name = QLineEdit()
        layout.addWidget(self.getSheet_name)

        self.button = QPushButton('Load data')
        self.button.released.connect(self.LoadExeldata)
        layout.addWidget(self.button)

        self.fileLabel = QLabel('digite o nome do arquivo')
        layout.addWidget(self.fileLabel)

        self.getFileName = QLineEdit()
        layout.addWidget(self.getFileName)

        self.saveButton = QPushButton('save as a new file')
        self.saveButton.released.connect(self.ExportExelData)
        layout.addWidget(self.saveButton)
    
        
    #metodo para carregar o exel
    def LoadExeldata(self):#os parametros é para a pasta do exel e o nome da planilia
        self.getFile = QWidget()#criando janela para procurar o arquivo

        self.sheetName = self.getSheet_name.text()#pegando testo do LineEdit
        #procura o arquivo e dita o titulo da janela
        self.exel_dir, _ = QFileDialog.getOpenFileName(self.getFile, "selecione arquivo")
        df = pd.read_excel(self.exel_dir, self.sheetName)#cria uma instancia que ira ler o exel
        print('asdqw')
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
    
    def ExportExelData(self):#funcao para exportar a planilha
        columnHeaders = []#lista da coluna do topos

        for abc in range(self.table.model().columnCount()):#loop da lista de colunas
            columnHeaders.append(self.table.horizontalHeaderItem(abc).text())#adiciona os itens do cabecalio na variavel
        
        df = pd.DataFrame(columns=columnHeaders)#adiciona o cabecalho no banco de dados do pandas na variavel

        for row in range(self.table.rowCount()):#para cada linha na contagem de linhas
            for col in range(self.table.columnCount()):#para cada coluna na contagem de colunas
                #abaixo adiciona a linha e colunas da planilha dentro da table com as linhas e colunas
                df.at[row, columnHeaders[col]] = self.table.item(row, col).text()
        
        df.to_excel(f'{self.getFileName.text()}.xlsx', index=False)#cria o arquivo exel
        print("pasta criada")


if __name__ == "__main__":

    app = QApplication(sys.argv)
    
    window = MyApp()
    window.show()

    #execao para o fechamento do aplicativo
    try:
        sys.exit(app.exec())
    except SystemExit:
        print("closing")