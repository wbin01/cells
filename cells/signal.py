#!/usr/bin/env python3
import pathlib
import sys

from PySide6 import QtCore
from __feature__ import snake_case


class Signal(QtCore.QObject):
    """..."""
    _signal = QtCore.Signal()

    def __init__(self, obj: any = None, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        """Class constructor"""
        self.__obj = obj

    @property
    def obj(self) -> str:
        """..."""
        return self.__obj

    @obj.setter
    def obj(self, obj: str) -> None:
        self.__obj = obj

    def callback(self, function) -> None:
        """..."""
        self._signal.connect(function)

    def send(self) -> None:
        """..."""
        self._signal.emit()

    def __str__(self) -> str:
        return f'<cells.Signal({type(self.__obj)}) at {id(self)}>'
