#!/usr/bin/env python3
from PySide6 import QtWidgets
from __feature__ import snake_case

from .event import Event
from .signal import Signal
from .widget import Widget


class MoveFrame(Widget):
    """Move Frame Widget."""
    def __init__(self, *args, **kwargs) -> None:
        """Class constructor."""
        super().__init__(*args, **kwargs)
        self.style_id = 'MoveFrame'
        self.minimum_height = 20
        self.signal(Event.MAIN_PARENT).connect(self.__on_main_added)

    def __on_double_click(self) -> None:
        if self._main_parent.maximized or self._main_parent.fullscreen:
            self._main_parent.maximized = False
        else:
            self._main_parent.maximized = True

    def __on_main_added(self):
        self.signal(Event.MOUSE_PRESS).connect(self.__on_press)
        self.signal(Event.MOUSE_DOUBLE_PRESS).connect(self.__on_double_click)

    def __on_press(self) -> None:
        if self._obj.under_mouse():
            self._main_parent._obj.window_handle().start_system_move()

    def __str__(self):
        return f'<MoveFrame: {id(self)}>'
