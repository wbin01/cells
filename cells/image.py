#!/usr/bin/env python3
import os

from PySide6 import QtWidgets, QtGui
from __feature__ import snake_case

from .event import Event
from .signal import Signal
from .widget import Widget


class Image(object):
    """Image Widget."""
    def __init__(self, path: str = None, *args, **kwargs) -> None:
        """Class constructor."""
        super().__init__(*args, **kwargs)
        self.__path = path if path else os.path.join(
            os.path.dirname(__file__), 'core', 'static', 'icon.svg')

        self._obj = QtWidgets.QLabel()
        self.style_id = 'Image'
        
        self._obj.set_pixmap(QtGui.QPixmap(self.__path))

    def __str__(self):
        return f'<Image: {id(self)}>'
