#!/usr/bin/env python3
from PySide6 import QtWidgets
from __feature__ import snake_case

from .event import Event
from .label import Label
from .orientation import Orientation
from .widget import Widget
from .box import Box


class Button(Widget):
    """Button Widget."""
    def __init__(self, text: str = '', *args, **kwargs) -> None:
        """Class constructor."""
        super().__init__(*args, **kwargs)
        self.__text = text
        self.style_id = 'Button'

        self.__base_box = self.insert(Box(orientation=Orientation.HORIZONTAL))
        self.__label =  self.__base_box.insert(
            Label(self.__text))
        self.__label.margin = 0, 5, 0, 5
        
        self.signal(Event.MAIN_PARENT_ADDED).connect(self.__on_main_added)
        self.signal(Event.ENABLED_CHANGE).connect(self.__on_enabled_change)

    @property
    def text(self) -> str:
        """Button text.
        
        Pass a new string to update the text.
        """
        return self.__label.text

    @text.setter
    def text(self, text: str) -> None:
        self.__text = text
        self.__label.text = text

    def __on_enabled_change(self) -> None:
        if self.enabled:
            self.__on_main_parent_focus_in()
        else:
            self.__on_main_parent_focus_out()

    def __on_main_added(self) -> None:
        self._main_parent.signal(Event.FOCUS_IN).connect(
            self.__on_main_parent_focus_in)
        self._main_parent.signal(Event.FOCUS_OUT).connect(
            self.__on_main_parent_focus_out)

    def __on_main_parent_focus_in(self) -> None:
        if self.enabled:
            self.__label.style['[Label]']['color'] = self.style[
                '[Button]']['color']
            self.__label.style = self.__label.style

    def __on_main_parent_focus_out(self) -> None:
        self.__label.style['[Label]']['color'] = self.style[
            '[Button:inactive]']['color']
        self.__label.style = self.__label.style

    def __str__(self) -> str:
        return f'<Button: {id(self)}>'
