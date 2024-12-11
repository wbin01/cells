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
        self.__label.style_id = 'Button-Label'
        self.__box.add_widget(self.__label)
        # self.__label._obj.set_size_policy(
        #     QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        self._is_inactive = False

        self.__style_manager = StyleManager()
        # self.__default_style = {}
        self.__normal_style = None
        self.__normal_style_label = None
        self.__inactive_style = None
        self.__inactive_style_label = None
        self.__hover_style = None
        self.__hover_style_label = None
        self.__pressed_style = None
        self.__pressed_style_label = None
        self.__set_styles()

        self.event_signal(Event.MAIN_PARENT_ADDED).connect(self.__main_added)
        self.event_signal(Event.MOUSE_BUTTON_PRESS).connect(self.__pressed)
        self.event_signal(Event.MOUSE_BUTTON_RELEASE).connect(self.__release)
        self.event_signal(Event.MOUSE_HOVER_ENTER).connect(self.__hover)
        self.event_signal(Event.MOUSE_HOVER_LEAVE).connect(self.__leave)

        self.event_signal(Event.STYLE_CHANGE).connect(self.__create_new_style)
        self.event_signal(Event.STYLE_ID_CHANGE).connect(self.__style_id_changed)
    
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

    def __active(self) -> None:
        self._is_inactive = False
        # self.__leave()

        self._obj.set_style_sheet(self.__normal_style)
        self.__label._obj.set_style_sheet(self.__normal_style_label)

    def __hover(self) -> None:
        self._obj.set_style_sheet(self.__hover_style)
        self.__label._obj.set_style_sheet(self.__hover_style_label)

    def __inactive(self) -> None:
        self._is_inactive = True
        self._obj.set_style_sheet(self.__inactive_style)
        self.__label._obj.set_style_sheet(self.__inactive_style_label)

    def __leave(self) -> None:
        if self._is_inactive:
            # self._obj.set_style_sheet('')
            # self.__label._obj.set_style_sheet('')
            self.__inactive()
        else:
            self._obj.set_style_sheet(self.__normal_style)
            self.__label._obj.set_style_sheet(self.__normal_style_label)

    def __main_added(self) -> None:
        self._main_parent.event_signal(Event.FOCUS_IN).connect(self.__active)
        self._main_parent.event_signal(Event.FOCUS_OUT).connect(self.__inactive)

    def __pressed(self) -> None:
        self._obj.set_style_sheet(self.__pressed_style)
        self.__label._obj.set_style_sheet(self.__pressed_style_label)

    def __release(self) -> None:
        self.__hover()

    def __set_styles(self):
        style_id = self.style_id

        self.__normal_style = self.__style_manager.style_to_qss(
            {f'[{self.style_id}]': self.__style_manager.stylesheet['[Button]']})
        self.__hover_style = self.__style_manager.style_to_qss(
            {f'[{self.style_id}:hover]': self.__style_manager.stylesheet['[Button:hover]']})
        self.__pressed_style = self.__style_manager.style_to_qss(
            {f'[{self.style_id}:pressed]': self.__style_manager.stylesheet['[Button:pressed]']})
        self.__inactive_style = self.__style_manager.style_to_qss(
            {f'[{self.style_id}:inactive]': self.__style_manager.stylesheet['[Button:inactive]']})

        self.__normal_style_label = self.__style_manager.style_to_qss(
            {f'[{self.style_id}-Label]': self.__style_manager.stylesheet['[Label]']})
        self.__hover_style_label = self.__style_manager.style_to_qss(
            {f'[{self.style_id}-Label:hover]': self.__style_manager.stylesheet['[Label:hover]']})
        self.__pressed_style_label = self.__style_manager.style_to_qss(
            {f'[{self.style_id}-Label:pressed]': self.__style_manager.stylesheet['[Label:pressed]']})
        self.__inactive_style_label = self.__style_manager.style_to_qss(
            {f'[{self.style_id}-Label:inactive]': self.__style_manager.stylesheet['[Label:inactive]']})


    def __create_new_style(self) -> None:
        if self._main_parent:
            default_style = {}
            default_style[
                f'[{self.style_id}]'] = self._main_parent.style['[Button]']
            default_style[
                f'[{self.style_id}:inactive]'] = self._main_parent.style[
                '[Button:inactive]']
            default_style[
                f'[{self.style_id}:hover]'] = self._main_parent.style[
                '[Button:hover]']
            default_style[
                f'[{self.style_id}:pressed]'] = self._main_parent.style[
                '[Button:pressed]']

            self._main_parent.style.update(default_style)
            self._main_parent.style = self._main_parent.style
            self.__style_manager.stylesheet = self._main_parent.style

            self.__set_styles()
            # self._obj.set_style_sheet(self.__normal_style)
            # self.__label._obj.set_style_sheet(self.__normal_style_label)

    def __style_id_changed(self) -> None:
        self.__label.style_id = f'{self.style_id}-Label'

        self.__main_parent.style[f'[{self.style_id}-Label]'] = self.__main_parent.style[
            '[Label]']
        self.__main_parent.style[f'[{self.style_id}-Label:inactive]'] = self.__main_parent.style[
            '[Label:inactive]']
        self.__main_parent.style[f'[{self.style_id}-Label:hover]'] = self.__main_parent.style[
            '[Label:hover]']
        self.__main_parent.style[f'[{self.style_id}-Label:pressed]'] = self.__main_parent.style[
            '[Label:pressed]']

        if self._main_parent:
            if not f'[{self.style_id}]' in self._main_parent.style:
                self.__create_new_style()
        self.__set_styles()

    def __str__(self):
        return f'<Button: {id(self)}>'
