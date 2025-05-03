from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QWindow
from PySide6.QtCore import QLibrary, QPluginLoader, QMetaObject

import ctypes

app = QApplication([])

win = QMainWindow()
win.setAttribute(103)  # Qt.WA_TranslucentBackground
win.setStyleSheet("background-color: rgba(0, 0, 0, 150);")
win.resize(400, 300)
win.show()

# Carregar plugin
from PySide6.QtCore import QLibrary, QPluginLoader, QMetaObject

loader = QPluginLoader("build/libblurplugin.so")
plugin = loader.instance()

if plugin:
    QMetaObject.invokeMethod(plugin, "setBlur", Qt.QueuedConnection, win.windowHandle())
else:
    print("Erro ao carregar plugin:", loader.errorString())

app.exec()
