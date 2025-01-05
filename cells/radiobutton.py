#!/usr/bin/env python3
import os
import pathlib

from PySide6.QtSvgWidgets import QSvgWidget
from PySide6.QtCore import QByteArray
from __feature__ import snake_case

from .align import Align
from .box import Box
from .event import Event
from .icon import Icon
from .image import Image
from .label import Label
from .orientation import Orientation
from .widget import Widget


class RadioButton(Widget):
    """Radio Button Widget."""
    def __init__(
            self,
            text: str = None,
            orientation: Orientation = Orientation.HORIZONTAL,
            *args, **kwargs) -> None:
        """Class constructor."""
        super().__init__(orientation=orientation, *args, **kwargs)
        self.__text = text if text else ''
        self.style_id = 'RadioButton'

        self.__focus = True
        self.__icon_on_right = True
        self.__tool = True

        self.spacing = 2
        self.align = Align.CENTER

        self.__svg_content = self.__load_svg('')
        self.__svg_data = QByteArray(self.__svg_content.encode('utf-8'))
        self.__icon = QSvgWidget()
        self.__icon.load(self.__svg_data)
        self.__icon.set_fixed_size(16, 16)
        self.__icon.style_id = 'RadioButton'
        self.__icon._obj = self.__icon
        
        if not self.__icon_on_right:
            self.insert(self.__icon)
        
        self.__label = Label(self.__text)
        if self.__text:
            self.insert(self.__label)
            if self.__icon_on_right:
                self.__label.margin = 0, 0, 0, 5
            else:
                self.__label.margin = 0, 5, 0, 0

        if self.__icon_on_right:
            self.insert(self.__icon)

        if not self.__text and self.__icon:
                self.__icon.margin = 0, 5, 0, 5
        elif self.__text and not self.__icon:
                self.__label.margin = 0, 5, 0, 5

        self.signal(Event.MAIN_PARENT).connect(self.__on_main_added)
        self.signal(Event.ENABLED).connect(self.__on_enabled_change)

        self.signal(Event.MOUSE_HOVER_ENTER).connect(
            self.__on_mouse_hover_enter)
        self.signal(Event.MOUSE_HOVER_LEAVE).connect(
            self.__on_mouse_hover_leave)
        self.signal(Event.MOUSE_PRESS).connect(
            self.__on_mouse_button_press)
        self.signal(Event.MOUSE_RELEASE).connect(
            self.__on_mouse_button_release)

    def __load_svg(self, state: str) -> str:
        path = os.path.join(
            pathlib.Path(__file__).resolve().parent,
            'core', 'static', 'radio.svg')
        
        r, g, b, ba = self.style[f'[RadioButton{state}]']['border'].replace(
            'accent_red', '45').replace('accent_green', '90').replace(
            'accent_blue', '165').replace(' ', '').split('rgba(')[1].rstrip(
            ')').split(',')
        border = f"#{int(r):02X}{int(g):02X}{int(b):02X}".lower()

        r, g, b, a = self.style[f'[RadioButton{state}]']['color'].replace(
            'accent_red', '45').replace('accent_green', '90').replace(
            'accent_blue', '165').replace(' ', '').replace('rgba(', '').rstrip(
            ')').split(',')

        center = f"#{int(r):02X}{int(g):02X}{int(b):02X}".lower()

        with open(path, "r") as f:
            cont = f.read()
        cont = cont.replace(
            'fill="#1a1a1a"', f'fill="{border}" fill-opacity="{ba}"').replace(
            'fill="#e5e5e5"', f'fill="{center}" fill-opacity="{a}"')
            
        return cont

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

        if self.__icon:
            self.__icon.enabled = self.enabled

    def __on_main_added(self) -> None:
        self._main_parent.signal(Event.FOCUS_IN).connect(
            self.__on_main_parent_focus_in)
        self._main_parent.signal(Event.FOCUS_OUT).connect(
            self.__on_main_parent_focus_out)
        
        if self.__icon:
            self.__icon._main_parent = self._main_parent

    def __on_main_parent_focus_in(self) -> None:
        self.__focus = True
        if self.enabled:
            self.__label.style['[Label]']['color'] = self.style[
                f'[{self.style_id}]']['color']
            self.__label.style = self.__label.style

            self.__svg_content = self.__load_svg('')
            self.__svg_data = QByteArray(self.__svg_content.encode('utf-8'))
            self.__icon.load(self.__svg_data)

    def __on_main_parent_focus_out(self) -> None:
        self.__focus = False
        self.__label.style['[Label]']['color'] = self.style[
            f'[{self.style_id}:inactive]']['color']
        self.__label.style = self.__label.style

        self.__svg_content = self.__load_svg(':inactive')
        self.__svg_data = QByteArray(self.__svg_content.encode('utf-8'))
        self.__icon.load(self.__svg_data)

    def __on_mouse_hover_enter(self) -> None:
        if self.enabled and self.__focus:
            self.__label.style['[Label]']['color'] = self.style[
                f'[{self.style_id}:hover]']['color']
            self.__label.style = self.__label.style

            self.__svg_content = self.__load_svg(':hover')
            self.__svg_data = QByteArray(self.__svg_content.encode('utf-8'))
            self.__icon.load(self.__svg_data)

    def __on_mouse_hover_leave(self) -> None:
        if self.enabled and self.__focus:
            self.__label.style['[Label]']['color'] = self.style[
                f'[{self.style_id}]']['color']
            self.__label.style = self.__label.style

            self.__svg_content = self.__load_svg('')
            self.__svg_data = QByteArray(self.__svg_content.encode('utf-8'))
            self.__icon.load(self.__svg_data)

    def __on_mouse_button_press(self) -> None:
        if self.enabled and self.__focus:
            self.__label.style['[Label]']['color'] = self.style[
                f'[{self.style_id}:pressed]']['color']
            self.__label.style = self.__label.style

            self.__svg_content = self.__load_svg(':pressed')
            self.__svg_data = QByteArray(self.__svg_content.encode('utf-8'))
            self.__icon.load(self.__svg_data)

    def __on_mouse_button_release(self) -> None:
        if self.enabled and self.__focus:
            self.__label.style['[Label]']['color'] = self.style[
                f'[{self.style_id}:hover]']['color']
            self.__label.style = self.__label.style

            self.__svg_content = self.__load_svg(':hover')
            self.__svg_data = QByteArray(self.__svg_content.encode('utf-8'))
            self.__icon.load(self.__svg_data)

    def __str__(self) -> str:
        return f'<RadioButton: {id(self)}>'

