#!/usr/bin/env python3
from PySide6 import QtCore
from __feature__ import snake_case


class CoreSignal(QtCore.QObject):
    """..."""
    __signal = QtCore.Signal()

    def __init__(self, signal_name: str = 'Signal', *args, **kwargs):
        super().__init__(*args, **kwargs)
        """Class constructor"""

        self.__signal_name = signal_name

    @property
    def signal_name(self) -> str:
        """..."""
        return self.__signal_name

    @signal_name.setter
    def signal_name(self, signal_name: str) -> None:
        self.__signal_name = signal_name

    def callback(self, function) -> None:
        """..."""
        self.__signal.connect(function)

    def send_signal(self) -> None:
        """..."""
        self.__signal.emit()

    def __str__(self) -> str:
        return f'<cells.Signal("{self.__signal_name}") at {id(self)}>'
