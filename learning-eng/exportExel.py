import sys
from PyQt6.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QPushButton, QVBoxLayout, QHBoxLayout
import pandas as pd


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("main")
        self.resize(700, 500)

        layout = QVBoxLayout()
        self.setLayout(layout)
         
        self.table = QTableWidget()
        layout.addWidget(self.table)
        
        self.button = QPushButton('export to exel')
        self.button.released.connect(self.ExportExelData)
        layout.addWidget(self.button)

        self.LoadData()

    def ExportExelData(self):#funcao para exportar a planilha
        columnHeaders = []#lista da coluna do topos

        for abc in range(self.table.model().columnCount()):#loop da lista de colunas
            columnHeaders.append(self.table.horizontalHeaderItem(abc).text())#adiciona os itens do cabecalio na variavel
        
        df = pd.DataFrame(columns=columnHeaders)#adiciona o cabecalho no banco de dados do pandas na variavel

        for row in range(self.table.rowCount()):#para cada linha na contagem de linhas
            for col in range(self.table.columnCount()):#para cada coluna na contagem de colunas
                #abaixo adiciona a linha e colunas da planilha dentro da table com as linhas e colunas
                df.at[row, columnHeaders[col]] = self.table.item(row, col).text()
        
        df.to_excel('testExelCreated.xlsx', index=False)#cria o arquivo exel
        print("pasta criada")
    def LoadData(self):#funcao para garregar planilha
        self.headerLabels = list("ABCDFGH")#cria/pega a coluna ABCDEFGH

        n = 39#quantidade de registros(linhas)
        self.table.setRowCount(n)#colocando o numero de linhas na table
        self.table.setColumnCount(len(self.headerLabels))#coloca a numeracao de quantas coluna tem na table
        self.table.setHorizontalHeaderLabels(self.headerLabels)#coloca essas numeracoes no cabecario
        
        for row in range(n):#loop pra cada linha
            for col in range(len(self.headerLabels)):# e para cada coluna
                itemTable = QTableWidgetItem(f'cell {self.headerLabels[col]:0}-{row+1:1}')#insere cada coluna e linha na variavel
                #a linha a acima ira imprimir qual coluna esta (-) o numero da linha 
                self.table.setItem(row, col, itemTable)#insere esses valores na table
        
        self.table.resizeColumnsToContents()#redimensiona a coluna pra cabe o conteudo
        self.table.resizeRowsToContents()#redimensiona a linha pra cabe o conteudo

if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = MyApp()
    window.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print("closing")