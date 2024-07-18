import sys
import os
from time import sleep
from PyQt6.QtWidgets import QApplication, QWidget,QPushButton, QLineEdit, QLabel, QGridLayout, QSizePolicy
import pandas as pd #biblioteca para ver exel


class MainApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("main")
        self.resize(600, 500)
        label = QLabel('main app')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = MainApp()
    Window.show()
    try:
        sys.exit(app.exec())
    except SystemExit:
        print("closing")