#!/usr/bin/env python3
from PySide6 import QtCore, QtGui, QtWidgets
from __feature__ import snake_case

from .coreshadow import CoreFrameShadow
from .modules import colorconverter
from .modules import StyleManager
from ..signal import Signal


class CoreFrame(CoreFrameShadow):
    """Complete Frame.

    Using style integration and shadow.
    """
    close_signal = Signal()
    focus_in_signal = Signal()
    focus_out_signal = Signal()
    mouse_press_signal = Signal()
    mouse_release_signal = Signal()
    mouse_double_click_signal = Signal()
    mouse_hover_enter_signal = Signal()
    mouse_hover_leave_signal = Signal()
    mouse_hover_move_signal = Signal()
    mouse_r_press_signal = Signal()
    mouse_wheel_signal = Signal()
    size_signal = Signal()
    # state_signal = Signal()
    # title_signal = Signal()

    def __init__(self, *args, **kwargs) -> None:
        """Class constructor."""
        super().__init__(*args, **kwargs)
        self.__is_dark = colorconverter.is_dark(
            QtGui.QPalette().color(QtGui.QPalette.Window).to_tuple())

        self.hide_shadow(True)

        self.__style_manager = StyleManager()
        self.__qss_styles = self.__style_manager.stylesheet_qss()
        self.set_style_sheet(self.__qss_styles['active'])

        self.set_focus_policy(QtCore.Qt.ClickFocus)
        self.install_event_filter(self)

    @property
    def stylesheet(self) -> dict:
        """Style as dict.

        Get the style as a dictionary or submit a new dictionary style to 
        update it.
        """
        return self.__style_manager.stylesheet

    @stylesheet.setter
    def stylesheet(self, style) -> None:
        self.__style_manager.stylesheet.update(style)
        self.__style_manager.stylesheet = self.__style_manager.stylesheet
        self.__qss_styles = self.__style_manager.stylesheet_qss()
        self.set_style_sheet(self.__qss_styles['active'])

    def event_filter(
            self, watched: QtCore.QObject, event: QtCore.QEvent) -> bool:
        if event.type() == QtCore.QEvent.FocusIn:
            self.focus_in_signal.emit()

        elif event.type() == QtCore.QEvent.FocusOut:
            self.focus_out_signal.emit()

        elif event.type() == QtCore.QEvent.HoverMove:
            self.mouse_hover_move_signal.emit()

        elif event.type() == QtCore.QEvent.Type.HoverEnter:
            self.mouse_hover_enter_signal.emit()
            if self.__press:
                self.mouse_release_signal.emit()
                self.__press = False

        elif event.type() == QtCore.QEvent.Type.HoverLeave:
            self.mouse_hover_leave_signal.emit()

        # elif event.type() == QtCore.QEvent.MouseButtonPress:
        elif event.type() == QtCore.QEvent.MouseButtonRelease:
            if 'RightButton' in event.__str__():
                self.mouse_r_press_signal.emit()
            else:
                self.mouse_press_signal.emit()

            self.__press = True
            self.set_cursor(QtCore.Qt.CursorShape.ArrowCursor)

        elif event.type() == QtCore.QEvent.MouseButtonDblClick:
            self.mouse_double_click_signal.emit()

        elif event.type() == QtCore.QEvent.Wheel:
            self.mouse_wheel_signal.emit()

        elif event.type() == QtCore.QEvent.Resize:
            self.size_signal.emit()

        elif event.type() == QtCore.QEvent.Close:
            self.close_signal.emit()

        return QtWidgets.QMainWindow.event_filter(self, watched, event)
