#!/usr/bin/env python3
from PySide6 import QtWidgets
from __feature__ import snake_case

from .widget import Widget


class Label(Widget):
    """Label Widget."""
    def __init__(self, text: str = '', *args, **kwargs) -> None:
        """Class constructor."""
        super().__init__(*args, **kwargs)
        self.style_id = 'Label'

        self.__label = QtWidgets.QLabel(text)
        self.__label.set_object_name('Label')
        self.__label.set_contents_margins(0, 0, 0, 0)

        setattr(self.__label, '_obj', self.__label)
        self.insert(self.__label)

    @property
    def text(self) -> str:
        """Label text.
        
        Pass a new string to update the text.
        """
        return self.__label._obj.text()

    @text.setter
    def text(self, text: str) -> None:
        self.__label._obj.set_text(text)

    def __str__(self):
        return f'<Label: {id(self)}>'
