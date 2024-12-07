#!/usr/bin/env python3
from PySide6 import QtWidgets
from __feature__ import snake_case

from ..signal import Signal


class CoreWidget(QtWidgets.QFrame):
    """Core Widget"""
    def __init__(self, *args, **kwargs):
        """Class constructor"""
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

        self.set_object_name('FrameWidget')

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
