#!/usr/bin/env python3
from PySide6 import QtWidgets
from __feature__ import snake_case

from .event import Event
from .widget import Widget


class Label(Widget):
    """Label Widget."""
    def __init__(self, text: str = '', *args, **kwargs) -> None:
        """Class constructor."""
        super().__init__(*args, **kwargs)
        self.style_id = 'Label'

        self.__label = QtWidgets.QLabel(text)
        self.__label.set_object_name('Label_Label')
        self.__label.set_style_sheet(
            'margin: 0px; padding: 0px; border: 0px; '
            'background-color: rgba(0, 0, 0, 0.00);')

        setattr(self.__label, '_obj', self.__label)
        self.insert(self.__label)
        
        self.signal(Event.STYLE_ID_CHANGE).connect(self.__style_id_change)

    @property
    def text(self) -> str:
        """Label text.
        
        Pass a new string to update the text.
        """
        return self.__label._obj.text()

    @text.setter
    def text(self, text: str) -> None:
        self.__label._obj.set_text(text)

    def __alignment_change(self) -> None:
        self.__label.set_alignment(self.alignment)

    def __style_id_change(self) -> None:
        self.__label.set_object_name(self.style_id)

    def __str__(self):
        return f'<Label: {id(self)}>'
