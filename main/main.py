import sys
import os
from time import sleep
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QVBoxLayout, QListWidget
import pandas as pd #biblioteca para ver exel
from PyQt6.QtCore import Qt

class MainApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("main")
        self.resize(300, 400)
        
        layout = QVBoxLayout()
        self.setLayout(layout)

        title = QLabel('Remote Control')
        title.setStyleSheet('font-size: 20px;font-weight:bold;')
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.list = QListWidget()

        widgets = [title, self.list]
        for widget in widgets:
            layout.addWidget(widget)
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = MainApp()
    Window.show()
    try:
        sys.exit(app.exec())
    except SystemExit:
        print("closing")