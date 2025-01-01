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
    def __init__(
            self,
            path: str = None,
            width: int = None,
            height: int = None,
            *args, **kwargs) -> None:
        """Class constructor.

        The Image is rendered from the path of a passed file.

        :param path: Image path.
        :param width: Integer with the value of the image width.
        :param height: Integer with the value of the image height.
        """
        super().__init__(*args, **kwargs)
        # https://doc.qt.io/qtforpython-6/PySide6/QtGui/QPixmap.html#pixmap-transformations
        self.__path = path if path else os.path.join(
                os.path.dirname(__file__), 'core', 'static', 'icon.svg')
        self.__width = width
        self.__height = height

        self._obj = QtWidgets.QLabel()
        self.style_id = 'Image'

        if isinstance(self.__path, Icon):
            self.__pixmap = QtGui.QPixmap(
                self.__path._obj.pixmap(self.__path.width, self.__path.height))
        else:
            self.__pixmap = QtGui.QPixmap(self.__path)
        self._obj.set_pixmap(self.__pixmap)

    @property
    def height(self) -> int:
        """Returns the height of the Image.

        Pass a new integer value to update the height.
        """
        return self.__height

    @height.setter
    def height(self, height) -> None:
        self.__height = height

    @property
    def path(self) -> str:
        """Image path.

        Pass a new path to update the Image.
        """
        return self.__path

    @path.setter
    def path(self, path: str) -> None:
        self.__path = path
        self.__pixmap = QtGui.QPixmap(self.__path)
        self._obj.set_pixmap(self.__pixmap)

    @property
    def width(self) -> int:
        """Returns the Image width.

        Pass a new integer value to update the width.
        """
        return self.__width

    @width.setter
    def width(self, width) -> None:
        self.__width = width

    def __str__(self):
        return f'<Image: {id(self)}>'
