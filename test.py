#!/usr/bin/env python3
import sys

from PySide6 import QtGui, QtWidgets
from PySide6.QtWidgets import QApplication, QGridLayout, QPushButton, QStyle, QWidget


class Window(QWidget):
    def __init__(self):
        super().__init__()

        icons = sorted(
            [attr for attr in dir(QStyle.StandardPixmap) if attr.startswith("SP_")]
        )
        layout = QGridLayout()
        
        # label = QLabel(self)
        # pixmap = QPixmap('cat.jpg')
        # label.setPixmap(pixmap)
        # label.setScaledContents(True)

        image = QtWidgets.QLabel()
        image.setPixmap(QtGui.QIcon.fromTheme('folder-download-symbolic').pixmap(96, 96))
        layout.addWidget(image)
        
        for n, name in enumerate(icons):
            btn = QPushButton(name)

            pixmapi = getattr(QStyle, name)
            icon = self.style().standardIcon(pixmapi)
            btn.setIcon(icon)
            layout.addWidget(btn, n / 4, n % 4)

        self.setLayout(layout)


app = QApplication(sys.argv)

w = Window()
w.show()

app.exec()
