#!/usr/bin/env python3
import os
import pathlib
import pprint

from PySide6 import QtCore, QtSvgWidgets
from __feature__ import snake_case

from .align import Align
from .box import Box
from .event import Event
from .icon import Icon
from .image import Image
from .label import Label
from .orientation import Orientation
from .widget import Widget


class Svg(Widget):
    """Svg Widget."""
    def __init__(self, path: str = None, *args, **kwargs) -> None:
        """Class constructor."""
        super().__init__(*args, **kwargs)
        self.__path = path
        self._obj = QtSvgWidgets.QSvgWidget()
        self.style_id = 'Svg'
        self.height, self.width = 16, 16

        self.__selectable = False
        self.__selected = False
        self.__state = None

        self.__normal_style = None
        self.__hover_style = None
        self.__pressed_style = None
        self.__inactive_style = None

        self.signal(Event.STYLE_ID).connect(self.__on_style_id)
        self.signal(Event.STYLE_CLASS).connect(self.__on_style_id)

    def __on_style_id(self):
        if not self._main_parent:
            return

        self.__normal_style = {
            'background': self.style[f'[{self.style_id}]']['svg_background'],
            'color': self.style[f'[{self.style_id}]']['svg_color'],
            'border': self.style[f'[{self.style_id}]']['svg_border']}
        self.__hover_style = {
            'background': self.style[f'[{self.style_id}:hover]']['svg_background'],
            'color': self.style[f'[{self.style_id}:hover]']['svg_color'],
            'border': self.style[f'[{self.style_id}:hover]']['svg_border']}
        self.__pressed_style = {
            'background':
                self.style[f'[{self.style_id}:pressed]']['svg_background'],
            'color': self.style[f'[{self.style_id}:pressed]']['svg_color'],
            'border': self.style[f'[{self.style_id}:pressed]']['svg_border']}
        self.__inactive_style = {
            'background':
                self.style[f'[{self.style_id}:inactive]']['svg_background'],
            'color': self.style[f'[{self.style_id}:inactive]']['svg_color'],
            'border': self.style[f'[{self.style_id}:inactive]']['svg_border']}

    @property
    def selectable(self) -> bool:
        """..."""
        return self.__selectable

    @selectable.setter
    def selectable(self, value: bool) -> None:
        self.__selectable = value

    @property
    def selected(self) -> bool:
        """..."""
        return self.__selected

    @selected.setter
    def selected(self, value: bool) -> None:
        self.__selected = value

    @property
    def state(self) -> str:
        """..."""
        return self.__state

    @state.setter
    def state(self, state: str = None) -> None:
        self.__state = state
        state = '' if not state else ':' + state

        if not self.__path or not self._main_parent:
            return

        if not self.__state:
            style = self.__normal_style
        elif self.__state == 'hover':
            style = self.__hover_style
        elif self.__state == 'pressed':
            style = self.__pressed_style
        elif self.__state == 'inactive':
            style = self.__inactive_style
        else:
            style = self.__selected_style

        r, g, b, b_a = self.__border_or_color_to_rgba_list(style['border'])
        border = f'#{int(r):02X}{int(g):02X}{int(b):02X}'

        r, g, b, a = self.__border_or_color_to_rgba_list(style['color'])
        center = f'#{int(r):02X}{int(g):02X}{int(b):02X}'

        with open(self.__path, "r") as f:
            cont = f.read()
        cont = cont.replace(
            'fill="#1a1a1a"', f'fill="{border}" fill-opacity="{b_a}"').replace(
            'fill="#e5e5e5"', f'fill="{center}" fill-opacity="{a}"')

        self._obj.load(QtCore.QByteArray(cont.encode('utf-8')))

    @staticmethod
    def __border_or_color_to_rgba_list(border: str) -> list:
        # 1 rgb 0 0 0 0.00 | 1 rgb 0 0 0 | 1 #000000
        # rgb 0 0 0 0.00   | rgb 0 0 0   | #000000
        bd = border.replace('accent_red', '60').replace('accent_green', '140'
            ).replace('accent_blue', '189').replace('px', '').replace('a(', ' '
            ).replace('(', ' ').replace(')', '').replace(',', '')

        # ['1 ', '0 0 0 0.00'] | ['1 ', '0 0 0'] | ['1 ', '000000']
        sep = '#' if '#' in bd else 'rgb'
        color = bd.replace('  ', ' ').strip().split(sep)[-1]

        if sep == '#':
            if len(color) == 3:  # 000
                r, g, b = color[0], color[1], color[2]
                r, g, b = int(r + r, 16), int(g + g, 16), int(b + b, 16)
                a = 1.0
            
            else:  # 000000 | 00000000
                color += 'ff'
                r, g = int(color[:2], 16), int(color[2:4], 16)
                b, a = int(color[4:6], 16), round(int(color[6:8], 16) / 255, 2)
        
        else:  # '0 0 0 0.00' | '0 0 0'
            color = color.replace('  ', ' ').strip().split()

            if len(color) == 4:  # ['0', '0', '0', '0.00']
                r, g, b = int(color[0]), int(color[1]), int(color[2])
                a = round(float(color[3]), 2)
            else:
                r, g, b = int(color[0]), int(color[1]), int(color[2])
                a = 1.0

        return [r, g, b, a]


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
        self.spacing = 2

        self.__focus = True
        self.__icon_on_right = False
        self.__tool = True
        self.__selected = False

        self.__icon = Svg(os.path.join(pathlib.Path(__file__).resolve().parent,
            'core', 'static', 'radio.svg'))
        
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
        
        self.__icon.style_id = 'Radio'

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
            self.__icon.style_id = 'Radio'

    def __on_main_parent_focus_in(self) -> None:
        self.__focus = True
        if self.enabled:
            self.__label.style['[Label]']['color'] = self.style[
                f'[{self.style_id}]']['color']
            self.__label.style = self.__label.style
            self.__icon.state = None

    def __on_main_parent_focus_out(self) -> None:
        self.__focus = False
        self.__label.style['[Label]']['color'] = self.style[
            f'[{self.style_id}:inactive]']['color']
        self.__label.style = self.__label.style
        self.__icon.state = 'inactive'

    def __on_mouse_hover_enter(self) -> None:
        if self.enabled and self.__focus:
            self.__label.style['[Label]']['color'] = self.style[
                f'[{self.style_id}:hover]']['color']
            self.__label.style = self.__label.style
            self.__icon.state = 'hover'

    def __on_mouse_hover_leave(self) -> None:
        if self.enabled and self.__focus:
            self.__label.style['[Label]']['color'] = self.style[
                f'[{self.style_id}]']['color']
            self.__label.style = self.__label.style
            self.__icon.state = None

    def __on_mouse_button_press(self) -> None:
        if self.enabled and self.__focus:
            self.__label.style['[Label]']['color'] = self.style[
                f'[{self.style_id}:pressed]']['color']
            self.__label.style = self.__label.style

            self.__selected = False if self.__selected else True
            if self.__selected:
                self.__icon.style_class = 'RadioOn'
            else:
                self.__icon.style_class = None

            self.__icon.state = 'pressed'

    def __on_mouse_button_release(self) -> None:
        if self.enabled and self.__focus:
            self.__label.style['[Label]']['color'] = self.style[
                f'[{self.style_id}:hover]']['color']
            self.__label.style = self.__label.style
            self.__icon.state = 'hover'

    def __str__(self) -> str:
        return f'<RadioButton: {id(self)}>'
