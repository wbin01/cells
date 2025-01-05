#!/usr/bin/env python3
from PySide6 import QtWidgets
from __feature__ import snake_case

from .orientation import Orientation
from .widget import Widget


class RadioButton(Widget):
    """Radio Button Widget."""
    def __init__(
        self,
        text: str = '',
        orientation: Orientation = Orientation.HORIZONTAL,
        *args, **kwargs) -> None:
        """Class constructor."""
        super().__init__(orientation=orientation, *args, **kwargs)
        self.__text = text if text else ''
        self.style_id = 'RadioButton'
        self.min_height = 22

    @property
    def text(self) -> str:
        """Label text.
        
        Pass a new string to update the text.
        """
        return self._obj.text()

    @text.setter
    def text(self, text: str) -> None:
        self._obj.set_text(text)

    def __str__(self):
        return f'<RadioButton: {id(self)}>'
