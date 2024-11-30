#!/usr/bin/env python3
from PySide6 import QtCore, QtGui, QtWidgets
from __feature__ import snake_case


class Cursor(object):
    """..."""
    def __init__(self) -> None:
        self.__cursor = QtGui.QCursor()

    def position(self) -> tuple:
        return self.__cursor.pos().x(),self.__cursor.pos().y()

    def __str__(self):
        return f'<Cursor: {id(self)}>'
