#!/usr/bin/env python3
from PySide6 import QtWidgets
from __feature__ import snake_case

from .widget import Widget


class Label(Widget):
    """Label Widget Widget."""
    def __init__(self, text: str = '', *args, **kwargs) -> None:
        """Class constructor."""
        super().__init__(*args, **kwargs)
        self._obj = QtWidgets.QLabel(text)
        self.style_id = 'Label'

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
        return f'<Label: {id(self)}>'
