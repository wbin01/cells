#!/usr/bin/env python3
from PySide6 import QtWidgets
from __feature__ import snake_case

from .event import Event
from .widget import Widget
from .signal import Signal


class CoreWidgetBase(QtWidgets.QWidget):
    """Core Widget."""
    def __init__(self, *args, **kwargs):
        """Class constructor."""
        super().__init__(*args, **kwargs)
        self.mouse_button_press_signal = Signal()
        self.mouse_button_release_signal = Signal()
        self.mouse_double_click_signal = Signal()
        self.mouse_hover_enter_signal = Signal()
        self.mouse_hover_leave_signal = Signal()
        self.mouse_hover_move_signal = Signal()

        self.mouse_right_button_press_signal = Signal()
        self.mouse_wheel_signal = Signal()
        self.resize_signal = Signal()

        self.set_object_name('Widget')

    def mouse_press_event(self, e):
        self.mouse_button_press_signal.emit()

    def mouse_release_event(self, e):
        self.mouse_button_release_signal.emit()

    def mouse_double_click_event(self, e):
        self.mouse_double_click_signal.emit()

    def enter_event(self, e):
        self.mouse_hover_enter_signal.emit()

    def leave_event(self, e):
        self.mouse_hover_leave_signal.emit()

    def mouse_move_event(self, e):
        self.mouse_hover_move_signal.emit()


class WidgetBase(Widget):
    """Label Widget."""
    def __init__(self, *args, **kwargs) -> None:
        """Class constructor."""
        super().__init__(*args, **kwargs)
        self._obj = CoreWidgetBase()

    def __str__(self):
        return f'<WidgetBase: {id(self)}>'
