#!/usr/bin/env python3
from PySide6 import QtWidgets
from __feature__ import snake_case

from .event import Event
from .widget import Widget
from .signal import Signal


class Label(Widget):
    """Label Widget."""
    def __init__(self, text: str = '', *args, **kwargs) -> None:
        """Class constructor."""
        super().__init__(*args, **kwargs)
        

        self._obj = QtWidgets.QLabel(text)
        self.style_id = 'Label'
        # self.signal(Event.MAIN_PARENT_ADDED).connect(self.__main_added)

    @property
    def text(self) -> str:
        """Label text.
        
        Pass a new string to update the text.
        """
        return self._obj.text()

    @text.setter
    def text(self, text: str) -> None:
        self._obj.set_text(text)

    def __alignment_change(self) -> None:
        # self.__label.set_alignment(self.alignment)
        pass

    def __main_added(self) -> None:
        self.style[f'[{self.style_id}]'] = self._main_parent.style['[Label]']
        self.style[f'[{self.style_id}:inactive]'] = self._main_parent.style['[Label:inactive]']
        self.style[f'[{self.style_id}:hover]'] = self._main_parent.style['[Label:hover]']
        self.style[f'[{self.style_id}:pressed]'] = self._main_parent.style['[Label:pressed]']
        self.style = self.style

    def __str__(self):
        return f'<Label: {id(self)}>'
