#!/usr/bin/env python3
from PySide6 import QtWidgets
from __feature__ import snake_case

from .widget import Widget
from .event import Event
from .box import Box
from .label import Label
from .core.modules import StyleManager


class Button(Widget):
    """Button Widget Widget."""
    def __init__(self, text: str = '', *args, **kwargs) -> None:
        """Class constructor."""
        super().__init__(*args, **kwargs)
        self.style_id = 'Button'

        self.__box = Box(True)
        self.add_box(self.__box)

        self.__label = Label(text)
        self.__label.style_id = 'ButtonLabel'
        self.__box.add_widget(self.__label)
        # self.__label._obj.set_size_policy(
        #     QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)

        self.__style_manager = StyleManager()
        self.__default_style = {}

        self.__normal_style = None
        self.__normal_style_label = None
        self.__inactive_style = None
        self.__inactive_style_label = None
        self.__hover_style = None
        self.__hover_style_label = None
        self.__pressed_style = None
        self.__pressed_style_label = None
        self.__set_styles()

        self.event_signal(Event.STYLE_CHANGE).connect(self.__style_changed)
        self.event_signal(Event.STYLE_ID_CHANGE).connect(self.__style_id_changed)
        self.event_signal(Event.MOUSE_BUTTON_PRESS).connect(self.__pressed)
        self.event_signal(Event.MOUSE_BUTTON_RELEASE).connect(self.__release)
        self.event_signal(Event.MOUSE_HOVER_ENTER).connect(self.__hover)
        self.event_signal(Event.MOUSE_HOVER_LEAVE).connect(self.__leave)
        self.event_signal(Event.MAIN_PARENT_ADDED).connect(self.__main_added)
        
    @property
    def style(self) -> str:
        """..."""
        return self.__default_style


    @style.setter
    def style(self, style: dict) -> None:
        self.__main_parent.style = style
        self.style_change_signal.emit()
    
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

    def __main_added(self) -> None:
        self._main_parent.event_signal(Event.FOCUS_IN).connect(self.__active)
        self._main_parent.event_signal(Event.FOCUS_OUT).connect(self.__inactive)

    def __set_styles(self):
        # self.__style_manager = StyleManager()
        normal_stl = self.__style_manager.qss_button(
            name=self.style_id, only_normal=True)
        hover_stl = self.__style_manager.qss_button(
            name=self.style_id, only_hover=True)
        pressed_stl = self.__style_manager.qss_button(
            name=self.style_id, only_pressed=True)
        inactive_stl = self.__style_manager.qss_button(
            name=self.style_id, inactive=True, only_normal=True)

        normal_style = normal_stl.split(f'#{self.style_id}Label '+'{')
        self.__normal_style = normal_style[0].replace(
            f'#{self.style_id} '+'{', '').replace('}', '').strip()
        self.__normal_style_label = normal_style[1].replace(
            f'#{self.style_id}Label '+'{', '').replace('}', '').strip()

        inactive_style = inactive_stl.split(f'#{self.style_id}Label '+'{')
        self.__inactive_style = inactive_style[0].replace(
            f'#{self.style_id} '+'{', '').replace('}', '').strip()
        self.__inactive_style_label = inactive_style[1].replace(
            f'#{self.style_id}Label '+'{', '').replace('}', '').strip()

        hover_style = hover_stl.split(f'#{self.style_id}Label:hover '+'{')
        self.__hover_style = hover_style[0].replace(
            f'#{self.style_id}:hover '+'{', '').replace('}', '').strip()
        self.__hover_style_label = hover_style[1].replace(
            f'#{self.style_id}Label:hover '+'{', '').replace('}', '').strip()

        pressed_style = pressed_stl.split(f'#{self.style_id}Label:pressed '+'{')
        self.__pressed_style = pressed_style[0].replace(
            f'#{self.style_id}:pressed '+'{', '').replace('}', '').strip()
        self.__pressed_style_label = pressed_style[1].replace(
            f'#{self.style_id}Label:pressed '+'{', '').replace('}', '').strip()

    def __pressed(self) -> None:
        self._obj.set_style_sheet(self.__pressed_style)
        self.__label._obj.set_style_sheet(self.__pressed_style_label)

    def __release(self) -> None:
        self.__hover()

    def __hover(self) -> None:
        self._obj.set_style_sheet(self.__hover_style)
        self.__label._obj.set_style_sheet(self.__hover_style_label)

    def __leave(self) -> None:
        self._obj.set_style_sheet(self.__normal_style)
        self.__label._obj.set_style_sheet(self.__normal_style_label)
        # self._obj.set_style_sheet('')
        # self.__label._obj.set_style_sheet('')

    def __style_changed(self) -> None:
        # self.__label.style_id = f'{self.style_id}Label'
        pass

    def __inactive(self) -> None:
        self._obj.set_style_sheet(self.__inactive_style)
        self.__label._obj.set_style_sheet(self.__inactive_style_label)

    def __active(self) -> None:
        self.__leave()

    def __style_id_changed(self) -> None:
        self.__label.style_id = f'{self.style_id}Label'
        # self._main_parent.style[
        #     f'[{self.style_id}]'] = self.__style_manager.qss_button(
        #         only_normal=True)
        # self._main_parent.style[
        #     f'[{self.style_id}:inactive]'] = self.__style_manager.qss_button(
        #         inactive=True, only_normal=True)
        # self._main_parent.style[
        #     f'[{self.style_id}:hover]'] = self.__style_manager.qss_button(
        #         only_hover=True)
        # self._main_parent.style[
        #     f'[{self.style_id}:pressed]'] = self.__style_manager.qss_button(
        #         only_pressed=True)

        if self._main_parent:
            self.__default_style[
                f'[{self.style_id}]'] = self._main_parent.style['[Button]']
            self.__default_style[
                f'[{self.style_id}:inactive]'] = self._main_parent.style[
                '[Button:inactive]']
            self.__default_style[
                f'[{self.style_id}:hover]'] = self._main_parent.style[
                '[Button:hover]']
            self.__default_style[
                f'[{self.style_id}:pressed]'] = self._main_parent.style[
                '[Button:pressed]']

            # style = self._main_parent.style
            # style.update(self.__default_style)
            # self._main_parent.style = style
            # self.__style_manager.stylesheet = style
            self._main_parent.style.update(self.__default_style)
            self.__style_manager.stylesheet = self._main_parent.style

            self.__set_styles()
            self._obj.set_style_sheet(self.__normal_style)
            self.__label._obj.set_style_sheet(self.__normal_style_label)
            # self._obj.set_style_sheet('')
            # self.__label._obj.set_style_sheet('')

    def __str__(self):
        return f'<Button: {id(self)}>'
