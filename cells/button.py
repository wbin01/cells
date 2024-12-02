#!/usr/bin/env python3
from PySide6 import QtWidgets
from __feature__ import snake_case

from .component import Component
from .event import Event


class Button(Component):
    def __init__(self, text: str = '', *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        # self.qt_obj = QtWidgets.QPushButton(text)
        self.__label = ''

    @property
    def text(self) -> str:
        """..."""
        return self.__label

    @text.setter
    def text(self, text: str) -> None:
        """..."""
        self.__label = text

    def connect(self, function: callable) -> None:
        self.event_signal(Event.MOUSE_BUTTON_PRESS).connect(function)
