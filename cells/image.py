#!/usr/bin/env python3
import os

from PySide6 import QtWidgets, QtGui
from __feature__ import snake_case

from .event import Event
from .icon import Icon
from .signal import Signal
from .widget import Widget


class Image(Widget):
    """Image Widget."""
    def __init__(self, path: str = None, *args, **kwargs) -> None:
        """Class constructor."""
        super().__init__(*args, **kwargs)
        self.__path = path if path else os.path.join(
                os.path.dirname(__file__), 'core', 'static', 'icon.svg')

        self._obj = QtWidgets.QLabel()
        self.style_id = 'Image'

        if isinstance(self.__path, Icon):
            self.__pixmap = QtGui.QPixmap(
                self.__path._obj.pixmap(self.__path.width, self.__path.height))
        else:
            self.__pixmap = QtGui.QPixmap(self.__path)
        self._obj.set_pixmap(self.__pixmap)

    @property
    def path(self) -> str:
        """..."""
        return self.__path

    @path.setter
    def path(self, path: str) -> None:
        self.__path = path
        self.__pixmap = QtGui.QPixmap(self.__path)
        self._obj.set_pixmap(self.__pixmap)

    def __str__(self):
        return f'<Image: {id(self)}>'
