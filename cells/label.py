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
        

        self._obj = QtWidgets.QLabel(text)
        self.style_id = 'Label'
        self.signal(Event.MAIN_PARENT_ADDED).connect(self.__main_added)

    @property
    def text(self) -> str:
        """Label text.
        
        Pass a new string to update the text.
        """
        return self._obj.text()

    @text.setter
    def text(self, text: str) -> None:
        self._obj.set_text(text)

    def __main_added(self) -> None:
        if '[Label]' in self._main_parent.style:
            self.style[f'[{self.style_id}]'] = {
                'color': self._main_parent.style['[Label]']['color']}

        if '[Label:inactive]' in self._main_parent.style:
            self.style[f'[{self.style_id}:inactive]'] = {
                'color': self._main_parent.style['[Label:inactive]']['color']}

        if '[Label:hover]' in self._main_parent.style:
            self.style[f'[{self.style_id}:hover]'] = {
                'color': self._main_parent.style['[Label:hover]']['color']}

        if '[Label:pressed]' in self._main_parent.style:
            self.style[f'[{self.style_id}:pressed]'] = {
                'color': self._main_parent.style['[Label:pressed]']['color']}

        self.style = self.style

    def __str__(self):
        return f'<Label: {id(self)}>'
