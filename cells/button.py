#!/usr/bin/env python3
from PySide6 import QtWidgets
from __feature__ import snake_case

from .event import Event
from .label import Label
from .orientation import Orientation
from .widget import Widget


class Button(Widget):
    """Button Widget."""
    def __init__(self, text: str = '', *args, **kwargs) -> None:
        """Class constructor."""
        super().__init__(*args, **kwargs)
        self.style_id = 'Button'
        # self.left_box = self.insert(Box(orientation=Orientation.HORIZONTAL))
        # self.insert
        # self.right_box = self.insert(Box(orientation=Orientation.HORIZONTAL))

        self.__label =  self.insert(Label('xxx'))
        self.__label.style_id = 'Button_Label'
        self.minimum_height = 30
        self.minimum_width = 30
        self.signal(Event.MAIN_PARENT_ADDED).connect(self.__on_main_added)

    @property
    def text(self) -> str:
        """Button text.
        
        Pass a new string to update the text.
        """
        # return self._obj.text()
        pass

    @text.setter
    def text(self, text: str) -> None:
        # self._obj.set_text(text)
        pass

    def __on_main_added(self) -> None:
        print('lololo')
        z_style = {
            'margin': '0px 0px 0px 0px',
            'padding': '0px 0px 0px 0px',
            'background': 'rgba(0, 0, 0, 0.00)',
            'border': '0px 0px 0px 0px',
        }
        self.__label.style['[Button_Label]'] = z_style
        self.__label.style['[Button_Label:hover]'] = z_style
        self.__label.style['[Button_Label:pressed]'] = z_style
        self.__label.style['[Button_Label:inactive]'] = z_style

        if '[Button]' in self._main_parent.style:
            self.style['[Button]'] = self._main_parent.style['[Button]']
            # self.__label.style['[Button_Label]']['color'
            #     ] = self._main_parent.style['[Button]']['color']

        if '[Button:inactive]' in self._main_parent.style:
            self.style['[Button:inactive]'] = self._main_parent.style[
                '[Button:inactive]']
            # self.__label.style['[Button_Label:inactive]']['color'
            #     ] = self._main_parent.style['[Button:inactive]']['color']

        if '[Button:hover]' in self._main_parent.style:
            self.style['[Button:hover]'] = self._main_parent.style[
                '[Button:hover]']
            # self.__label.style['[Button_Label:hover]']['color'
            #     ] = self._main_parent.style['[Button:hover]']['color']

        if '[Button:pressed]' in self._main_parent.style:
            self.style['[Button:pressed]'] = self._main_parent.style[
                '[Button:pressed]']
            # self.__label.style['[Button_Label:pressed]']['color'
            #     ] = self._main_parent.style['[Button:pressed]']['color']

        self.style = self.style
        self.__label.style = self.__label.style

    def __str__(self):
        return f'<Button: {id(self)}>'
