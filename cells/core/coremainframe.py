#!/usr/bin/env python3
from PySide6 import QtCore, QtGui, QtWidgets
from __feature__ import snake_case

from .modules import colorconverter
from .modules import StyleManager
from .coreshadow import CoreMainFrameShadow
from ..signal import Signal
from ..event import Event


class CoreMainFrame(CoreMainFrameShadow):
    """Complete Frame.

    Using style integration.
    """
    close_signal = Signal()
    focus_in_signal = Signal()
    focus_out_signal = Signal()
    mouse_button_press_signal = Signal()
    mouse_button_release_signal = Signal()
    mouse_double_click_signal = Signal()
    mouse_hover_enter_signal = Signal()
    mouse_hover_leave_signal = Signal()
    mouse_hover_move_signal = Signal()
    mouse_right_button_press_signal = Signal()
    mouse_wheel_signal = Signal()
    resize_signal = Signal()
    state_change_signal = Signal()
    title_change_signal = Signal()

    boxes = []

    def __init__(self, *args, **kwargs) -> None:
        """Class constructor."""
        super().__init__(*args, **kwargs)
        self.set_minimum_width(50)
        self.set_minimum_height(50)

        self.__shadow_size = 8
        self.__edge_cursor_position = None
        self.__edge_resize_area_ssd = 5
        self.__edge_resize_area = self.__edge_resize_area_ssd
        self.__is_csd = True
        self.__show_shadow = False
        self.__event_filter_count = 1
        self.__event_filter_can_emit = False
        self.__is_dark = colorconverter.is_dark(
            QtGui.QPalette().color(QtGui.QPalette.Window).to_tuple())

        self.__press = False

        if self.__is_csd:
            self.set_window_flags(
                QtCore.Qt.FramelessWindowHint | QtCore.Qt.Window)
            self.__window_shadow_visible(True)

        self.__style_manager = StyleManager()
        self.__qss_styles = self.__style_manager.stylesheets_for_qss()

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
        self.__style_manager.stylesheet = style
        self.__qss_styles = self.__style_manager.stylesheets_for_qss()
        if self.is_maximized() or self.is_full_screen():
            self.set_style_sheet(self.__qss_styles['fullscreen'])
        else:
            self.set_style_sheet(self.__qss_styles['active'])

    def __set_edge_cursor_position(self, event: QtCore.QEvent) -> None:
        # Saves the position of the window where the mouse cursor is
        shadow_size = self.__shadow_size if self.is_shadow_visible() else 0
        resize_area = (-3 if not self.__is_csd else shadow_size - 3)

        pos = event.position().to_point()  # QtGui.QHoverEvent(ev.clone())
        window_area = [
            resize_area < pos.x() < self.width() - resize_area,
            resize_area < pos.y() < self.height() - resize_area]

        if not self.__is_csd:
            window_area = [
                pos.x() < self.width(), pos.y() < self.height()]

        if all(window_area):
            # top-right, top-left, bottom-right, bottom-left
            if (pos.x() > (self.width() - self.__edge_resize_area) and
                    pos.y() < self.__edge_resize_area):
                self.__edge_cursor_position = (
                        QtCore.Qt.Edge.RightEdge | QtCore.Qt.Edge.TopEdge)
            elif (pos.x() < self.__edge_resize_area and
                  pos.y() < self.__edge_resize_area):
                self.__edge_cursor_position = (
                        QtCore.Qt.Edge.LeftEdge | QtCore.Qt.Edge.TopEdge)
            elif (pos.x() > (self.width() - self.__edge_resize_area) and
                  pos.y() > (self.height() - self.__edge_resize_area)):
                self.__edge_cursor_position = (
                        QtCore.Qt.Edge.RightEdge | QtCore.Qt.Edge.BottomEdge)
            elif (pos.x() < self.__edge_resize_area and
                  pos.y() > (self.height() - self.__edge_resize_area)):
                self.__edge_cursor_position = (
                        QtCore.Qt.Edge.LeftEdge | QtCore.Qt.Edge.BottomEdge)

            # left, right, top, bottom
            elif pos.x() <= self.__edge_resize_area:
                self.__edge_cursor_position = QtCore.Qt.Edge.LeftEdge
            elif pos.x() >= (self.width() - self.__edge_resize_area):
                self.__edge_cursor_position = QtCore.Qt.Edge.RightEdge
            elif pos.y() <= self.__edge_resize_area:
                self.__edge_cursor_position = QtCore.Qt.Edge.TopEdge
            elif pos.y() >= (self.height() - self.__edge_resize_area):
                self.__edge_cursor_position = QtCore.Qt.Edge.BottomEdge
            else:
                self.__edge_cursor_position = None
        else:
            self.__edge_cursor_position = None

    def __set_edge_cursor_position_shape(self) -> None:
        # Updates the mouse cursor appearance
        if not self.__edge_cursor_position:
            self.set_cursor(QtCore.Qt.CursorShape.ArrowCursor)
        else:
            if (self.__edge_cursor_position == QtCore.Qt.Edge.LeftEdge or
                    self.__edge_cursor_position == QtCore.Qt.Edge.RightEdge):
                self.set_cursor(QtCore.Qt.CursorShape.SizeHorCursor)

            elif (self.__edge_cursor_position == QtCore.Qt.Edge.TopEdge or
                  self.__edge_cursor_position == QtCore.Qt.Edge.BottomEdge):
                self.set_cursor(QtCore.Qt.CursorShape.SizeVerCursor)

            elif (self.__edge_cursor_position == QtCore.Qt.Edge.LeftEdge |
                  QtCore.Qt.Edge.TopEdge or
                  self.__edge_cursor_position == QtCore.Qt.Edge.RightEdge |
                  QtCore.Qt.Edge.BottomEdge):
                self.set_cursor(QtCore.Qt.CursorShape.SizeFDiagCursor)

            elif (self.__edge_cursor_position == QtCore.Qt.Edge.RightEdge |
                  QtCore.Qt.Edge.TopEdge or
                  self.__edge_cursor_position == QtCore.Qt.Edge.LeftEdge |
                  QtCore.Qt.Edge.BottomEdge):
                self.set_cursor(QtCore.Qt.CursorShape.SizeBDiagCursor)

    def __window_shadow_visible(self, visible: bool) -> None:
        # if self.__shadow_is_disabled:
        if not self.__is_csd:
            self.__edge_resize_area = self.__edge_resize_area_ssd
        else:
            if self.__show_shadow:
                self.hide_shadow(False if visible else True)
            else:
                self.hide_shadow(True)

            if visible:
                self.__edge_resize_area = (
                    self.__edge_resize_area_ssd + self.__shadow_size
                    if self.__show_shadow else self.__edge_resize_area_ssd)
            else:
                self.__edge_resize_area = self.__edge_resize_area_ssd

    def event_filter(
            self, watched: QtCore.QObject, event: QtCore.QEvent) -> bool:
        if event.type() == QtCore.QEvent.FocusIn:
            self.focus_in_signal.emit()
            if self.is_maximized() or self.is_full_screen():
                self.set_style_sheet(self.__qss_styles['fullscreen'])
            else:
                self.set_style_sheet(self.__qss_styles['active'])

        elif event.type() == QtCore.QEvent.FocusOut:
            self.focus_out_signal.emit()
            if self.is_maximized() or self.is_full_screen():
                self.set_style_sheet(self.__qss_styles['inactive_fullscreen'])
            else:
                # ActiveWindowFocusReason
                # if event.reason() != QtCore.Qt.MouseFocusReason:
                self.set_style_sheet(self.__qss_styles['inactive'])

        elif event.type() == QtCore.QEvent.HoverMove:
            self.mouse_hover_move_signal.emit()
            self.__set_edge_cursor_position(event)
            self.__set_edge_cursor_position_shape()

        elif event.type() == QtCore.QEvent.Type.HoverEnter:
            self.mouse_hover_enter_signal.emit()
            if self.__press:
                self.mouse_button_release_signal.emit()
                self.__press = False

        elif event.type() == QtCore.QEvent.Type.HoverLeave:
            self.mouse_hover_leave_signal.emit()

        elif event.type() == QtCore.QEvent.MouseButtonPress:
            self.__set_edge_cursor_position_shape()

            if self.__edge_cursor_position:
                self.window_handle().start_system_resize(
                    self.__edge_cursor_position)

            elif self.under_mouse():
                self.window_handle().start_system_move()

        elif event.type() == QtCore.QEvent.MouseButtonRelease:
            if 'RightButton' in event.__str__():
                self.mouse_right_button_press_signal.emit()
            else:
                self.mouse_button_press_signal.emit()

            self.__press = True
            self.set_cursor(QtCore.Qt.CursorShape.ArrowCursor)

        elif event.type() == QtCore.QEvent.MouseButtonDblClick:
            self.mouse_double_click_signal.emit()

        elif event.type() == QtCore.QEvent.Wheel:
            self.mouse_wheel_signal.emit()

        elif event.type() == QtCore.QEvent.Resize:
            self.resize_signal.emit()

            if self.__is_csd:
                if self.is_maximized() or self.is_full_screen():
                    self.set_style_sheet(self.__qss_styles['fullscreen'])
                    self.__window_shadow_visible(False)
                else:
                    self.set_style_sheet(self.__qss_styles['active'])
                    self.__window_shadow_visible(True)

        elif event.type() == QtCore.QEvent.WindowStateChange:
            self.state_change_signal.emit()

        elif event.type() == QtCore.QEvent.WindowTitleChange:
            self.title_change_signal.emit()

        elif event.type() == QtCore.QEvent.Close:
            self.close_signal.emit()

        return QtWidgets.QMainWindow.event_filter(self, watched, event)
