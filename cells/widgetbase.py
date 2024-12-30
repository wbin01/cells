#!/usr/bin/env python3
from PySide6 import QtWidgets, QtCore
from __feature__ import snake_case

from .event import Event
from .widget import Widget
from .signal import Signal


class CoreWidgetBase(QtWidgets.QWidget):
    """Core Widget base."""
    def __init__(self, *args, **kwargs):
        """Class constructor."""
        super().__init__(*args, **kwargs)
        self.set_object_name('Widget')
        self.mouse_button_press_signal = Signal()
        self.mouse_button_release_signal = Signal()
        self.mouse_double_click_signal = Signal()
        self.mouse_hover_enter_signal = Signal()
        self.mouse_hover_leave_signal = Signal()
        self.mouse_hover_move_signal = Signal()
        self.mouse_right_button_press_signal = Signal()
        self.mouse_wheel_signal = Signal()
        self.size_signal = Signal()

        self.install_event_filter(self)

    def event_filter(
            self, watched: QtCore.QObject, event: QtCore.QEvent) -> bool:
        # if event.type() == QtCore.QEvent.FocusIn:
        #     self.focus_in_signal.emit()

        # elif event.type() == QtCore.QEvent.FocusOut:
        #     self.focus_out_signal.emit()

        if event.type() == QtCore.QEvent.HoverMove:
            self.mouse_hover_move_signal.emit()

        elif event.type() == QtCore.QEvent.Type.HoverEnter:
            self.mouse_hover_enter_signal.emit()

        elif event.type() == QtCore.QEvent.Type.HoverLeave:
            self.mouse_hover_leave_signal.emit()

        elif event.type() == QtCore.QEvent.MouseButtonPress:
            if 'RightButton' in event.__str__():
                self.mouse_right_button_press_signal.emit()
            else:
                self.mouse_button_press_signal.emit()

        elif event.type() == QtCore.QEvent.MouseButtonRelease:
            self.mouse_button_release_signal.emit()

        elif event.type() == QtCore.QEvent.MouseButtonDblClick:
            self.mouse_double_click_signal.emit()

        elif event.type() == QtCore.QEvent.Wheel:
            self.mouse_wheel_signal.emit()

        elif event.type() == QtCore.QEvent.Resize:
            self.size_signal.emit()

        elif event.type() == QtCore.QEvent.Close:
            self.close_signal.emit()

        return QtWidgets.QMainWindow.event_filter(self, watched, event)


class WidgetBase(Widget):
    """Widget base."""
    def __init__(self, *args, **kwargs) -> None:
        """Class constructor."""
        super().__init__(*args, **kwargs)
        self._obj = CoreWidgetBase()

    def __str__(self):
        return f'<WidgetBase: {id(self)}>'
