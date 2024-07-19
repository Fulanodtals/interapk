import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLabel

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Cria o QVBoxLayout principal
        self.vbox = QVBoxLayout()

        # Adiciona alguns widgets ao QVBoxLayout
        self.vbox.addWidget(QLabel("Label no QVBoxLayout"))
        self.vbox.addWidget(QPushButton("Botão no QVBoxLayout"))

        # Cria um QWidget para conter o QGridLayout
        self.grid_widget = QWidget()

        # Cria o QGridLayout
        self.grid = QGridLayout()
        self.grid.addWidget(QLabel("Label 1 no QGridLayout"), 0, 0)
        self.grid.addWidget(QPushButton("Botão 1 no QGridLayout"), 0, 1)
        self.grid.addWidget(QLabel("Label 2 no QGridLayout"), 1, 0)
        self.grid.addWidget(QPushButton("Botão 2 no QGridLayout"), 1, 1)

        # Define o QGridLayout como layout do QWidget
        self.grid_widget.setLayout(self.grid)

        # Adiciona o QWidget (que contém o QGridLayout) ao QVBoxLayout
        self.vbox.addWidget(self.grid_widget)

        # Define o QVBoxLayout como layout principal da janela
        self.setLayout(self.vbox)

        self.setWindowTitle("Exemplo de QVBoxLayout com QGridLayout")
        self.resize(300, 200)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
