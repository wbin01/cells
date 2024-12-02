#!/usr/bin/env python3
from PySide6 import QtWidgets
from __feature__ import snake_case

from ..signal import Signal


class CoreComponent(QtWidgets.QWidget):
    """..."""
    mouse_button_press_signal = Signal()
    mouse_button_release_signal = Signal()
    mouse_double_click_signal = Signal()
    mouse_hover_enter_signal = Signal()
    mouse_hover_leave_signal = Signal()
    mouse_hover_move_signal = Signal()

    mouse_right_button_press_signal = Signal()
    mouse_wheel_signal = Signal()
    resize_signal = Signal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def mouse_press_event(self, e):
        self.mouse_button_press_signal.emit()

    def mouse_release_event(self, e):
        self.mouse_button_release_signal.emit()

    def mouse_double_click_event(self, e):
        self.mouse_double_click_signal.emit()

    def enter_event(self, e):
        self.mouse_hover_enter_signal.emit()

    def enter_leave(self, e):
        self.mouse_hover_leave_signal.emit()

    def mouse_move_event(self, e):
        self.mouse_hover_move_signal.emit()
