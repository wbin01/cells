#!/usr/bin/env python3
from PySide6 import QtWidgets
from __feature__ import snake_case

from .component import Component
from .event import Event
from .box import Box
from .label import Label
from .core.modules import StyleManager


class Button(Component):
    """Button Component Widget."""
    def __init__(self, text: str = '', *args, **kwargs) -> None:
        """Class constructor."""
        super().__init__(*args, **kwargs)
        self.style_id = 'Button'

        self.__box = Box(True)
        self.add_box(self.__box)

        self.__label = Label(text)
        self.__label.style_id = 'ButtonLabel'
        self.__box.add_component(self.__label)
        # self.__label._obj.set_size_policy(
        #     QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)

        self.__normal_style = None
        self.__normal_style_label = None
        self.__inactive_style = None
        self.__inactive_style_label = None
        self.__hover_style = None
        self.__hover_style_label = None
        self.__pressed_style = None
        self.__pressed_style_label = None
        self.__set_styles()
    
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

    def __set_styles(self):
        style_manager = StyleManager()
        normal_stl = style_manager.qss_button(only_normal=True)
        inactive_stl = style_manager.qss_button(inactive=True, only_normal=True)
        hover_stl = style_manager.qss_button(only_hover=True)
        pressed_stl = style_manager.qss_button(only_pressed=True)

        normal_style = normal_stl.split('#ButtonLabel {')
        self.__normal_style = normal_style[0].replace(
            '#Button {', '').replace('}', '').strip()
        self.__normal_style_label = normal_style[1].replace(
            '#ButtonLabel {', '').replace('}', '').strip()

        inactive_style = normal_stl.split('#ButtonLabel {')
        self.__inactive_style = inactive_style[0].replace(
            '#Button {', '').replace('}', '').strip()
        self.__inactive_style_label = inactive_style[1].replace(
            '#ButtonLabel {', '').replace('}', '').strip()

        hover_style = hover_stl.split('#ButtonLabel:hover {')
        self.__hover_style = hover_style[0].replace(
            '#Button:hover {', '').replace('}', '').strip()
        self.__hover_style_label = hover_style[1].replace(
            '#ButtonLabel:hover {', '').replace('}', '').strip()

        pressed_style = pressed_stl.split('#ButtonLabel:pressed {')
        self.__pressed_style = pressed_style[0].replace(
            '#Button:pressed {', '').replace('}', '').strip()
        self.__pressed_style_label = pressed_style[1].replace(
            '#ButtonLabel:pressed {', '').replace('}', '').strip()

        self.event_signal(Event.MOUSE_BUTTON_PRESS).connect(self.__pressed)
        self.event_signal(Event.MOUSE_BUTTON_RELEASE).connect(self.__release)
        self.event_signal(Event.MOUSE_HOVER_ENTER).connect(self.__hover)
        self.event_signal(Event.MOUSE_HOVER_LEAVE).connect(self.__leave)

    def __pressed(self) -> None:
        self._obj.set_style_sheet(self.__pressed_style)
        self.__label._obj.set_style_sheet(self.__pressed_style_label)

    def __release(self) -> None:
        self.__hover()

    def __hover(self) -> None:
        self._obj.set_style_sheet(self.__hover_style)
        self.__label._obj.set_style_sheet(self.__hover_style_label)

    def __leave(self) -> None:
        # self._obj.set_style_sheet(self.__normal_style)
        # self.__label._obj.set_style_sheet(self.__normal_style_label)
        self._obj.set_style_sheet('')
        self.__label._obj.set_style_sheet('')

    def __str__(self):
        return f'<Button: {id(self)}>'
