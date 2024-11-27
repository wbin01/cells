#!/usr/bin/env python3
from PySide6 import QtCore
from __feature__ import snake_case


class Signal(QtCore.QObject):
    """..."""
    _signal = QtCore.Signal()

    def __init__(self, name: str = 'Signal', *args, **kwargs):
        super().__init__(*args, **kwargs)
        """Class constructor"""
        self.__name = name

    @property
    def name(self) -> str:
        """..."""
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    def callback(self, function) -> None:
        """..."""
        self._signal.connect(function)

    def send_signal(self) -> None:
        """..."""
        self._signal.emit()

    def __str__(self) -> str:
        return f'<cells.Signal("{self.__name}") at {id(self)}>'
