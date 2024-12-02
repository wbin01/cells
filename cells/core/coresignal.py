#!/usr/bin/env python3
from PySide6 import QtCore
from __feature__ import snake_case


class CoreSignal(QtCore.QObject):
    """Event Signals.

    Signals are connections to events. When an event such as a mouse click 
    or other event occurs, a signal is sent. The signal can be assigned a 
    function to be executed when the signal is sent.
    """
    __signal = QtCore.Signal()

    def __init__(self, value: any = None, *args, **kwargs) -> None:
        """Class constructor.

        :param value: Object of any type. 
            Use when you need to pass and retrieve a value.
        """
        super().__init__(*args, **kwargs)
        self._qt_class = self.__signal

        self.__value = value

    @property
    def value(self) -> str:
        """Value of any type passed to the class constructor."""
        return self.__value

    @value.setter
    def value(self, value: str) -> None:
        self.__value = value

    def callback(self, function, *args) -> None:
        """Function to be executed.

        :param function: Function to be executed when the signal is sent.
        """
        self.__signal.connect(function)

    def send(self) -> None:
        """Send this signal.

        This method should be executed when you need to send the signal.
        """
        self.__signal.emit()

    def __str__(self) -> str:
        return f'<CoreSignal: {id(self)}>'
