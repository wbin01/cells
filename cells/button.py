#!/usr/bin/env python3
from PySide6 import QtWidgets
from __feature__ import snake_case

from .component import Component
from .event import Event
from .box import Box
from .label import Label


class Button(Component):
    """Button Component Widget."""
    def __init__(self, text: str = '', *args, **kwargs) -> None:
        """Class constructor."""
        super().__init__(*args, **kwargs)

        self.__box = Box(True)
        self.add_box(self.__box)

        self.__label = Label(text)
        self.__box.add_component(self.__label)

    @property
    def text(self) -> str:
        """Button text.
        
        Pass a new string to update the text.
        """
        return self.__label.text

    @text.setter
    def text(self, text: str) -> None:
        self.__label.text = text

    def connect(self, function: callable) -> None:
        """Connection to function.

        Executes a function when the button is clicked.

        :param function: Function to be executed.
        """
        self.event_signal(Event.MOUSE_BUTTON_PRESS).connect(function)

    def __str__(self):
        return f'<Button: {id(self)}>'
