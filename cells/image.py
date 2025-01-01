#!/usr/bin/env python3
import os

from PySide6 import QtWidgets, QtGui, QtCore
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
            aspect_ratio: bool = True,
            smooth: bool = False,
            *args, **kwargs) -> None:
        """Class constructor.

        The Image is rendered from the path of a passed file.

        :param path: 
            Image path.
        :param width: 
            Integer with the value of the image width.
        :param height: 
            Integer with the value of the image height.
        :param aspect_ratio: 
            Flattening or stretching the image with width or height values not 
            equivalent to the original image. True will maintain the aspect 
            ratio without distorting or stretching.
        :param smooth: 
            It improves the appearance of scaled images, but the processing is 
            a little slower.
        """
        super().__init__(*args, **kwargs)
        # https://doc.qt.io/qtforpython-6/PySide6/QtGui/QPixmap.html
        # #pixmap-transformations
        self.__path = path if path else os.path.join(
                os.path.dirname(__file__), 'core', 'static', 'icon.svg')
        self.__width = width
        self.__height = height
        self.__aspect_ratio = (QtCore.Qt.KeepAspectRatio if aspect_ratio else
            QtCore.Qt.IgnoreAspectRatio)
        # QtCore.Qt.KeepAspectRatioByExpanding
        self.__smooth = (QtCore.Qt.SmoothTransformation if smooth else
            QtCore.Qt.FastTransformation)

        self._obj = QtWidgets.QLabel()
        self.style_id = 'Image'

        if isinstance(self.__path, Icon):
            pixmap = QtGui.QPixmap(
                self.__path._obj.pixmap(self.__path.width, self.__path.height))
        else:
            pixmap = QtGui.QPixmap(self.__path)

        if not self.__width:
            self.__width = pixmap.width()

        if not self.__height:
            self.__height = pixmap.height()

        self.__pixmap = pixmap.scaled(self.__width, self.__height,
            self.__aspect_ratio, self.__smooth)

        self._obj.set_pixmap(self.__pixmap)
        # self._obj.set_scaled_contents(True)

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

    def __str__(self):
        return f'<Image: {id(self)}>'
