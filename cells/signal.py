#!/usr/bin/env python3
from .core.coresignal import CoreSignal


class Signal(object):
    """Signal object."""
    def __init__(self):
        """Class constructor."""
        self.__signal = CoreSignal()

    @property
    def value(self) -> str:
        """Value of any type passed to the class constructor."""
        return self.__signal.value

    @value.setter
    def value(self, value: str) -> None:
        self.__signal.value = value

    def connect(self, function, *args) -> None:
        """Function to be executed.

        :param function: Function to be executed when the signal is sent.
        """
        self.__signal.callback(function)

    def emit(self) -> None:
        """Send this signal.

        This method should be executed when you need to send the signal.
        """
        self.__signal.send()

    def __str__(self) -> str:
        return f'<Signal: {id(self)}>'
