#!/usr/bin/env python3
import pathlib
import os

from PySide6 import QtCore, QtGui, QtWidgets
from __feature__ import snake_case

from . import color
from .modules import StyleManager
from .edgeshadow import EdgeShadow


class ProtoFrame(QtWidgets.QMainWindow):
    """Frame with shadow

    Only frame without integration
    """

    def __init__(self, *args, **kwargs) -> None:
        """Class constructor"""
        super().__init__(*args, **kwargs)
        self.set_attribute(QtCore.Qt.WA_TranslucentBackground)
        self.set_contents_margins(0, 0, 0, 0)

        base_dir = pathlib.Path(__file__).resolve().parent
        icon_path = os.path.join(base_dir, 'icon.svg')
        self.__app_icon = QtGui.QIcon(QtGui.QPixmap(icon_path))
        self.set_window_icon(self.__app_icon)

        self.__is_shadow_has_added = True
        self.__shadow_size = 8

        self.__mainwidget = QtWidgets.QWidget()
        self.__mainwidget.set_contents_margins(0, 0, 0, 0)
        self.set_central_widget(self.__mainwidget)

        self.__main_box = QtWidgets.QVBoxLayout()
        self.__main_box.set_contents_margins(0, 0, 0, 0)
        self.__main_box.set_spacing(0)
        self.__mainwidget.set_layout(self.__main_box)

        # Top
        self.__top_box = QtWidgets.QHBoxLayout()
        self.__main_box.add_layout(self.__top_box)

        self.__top_left_shadow = EdgeShadow('top-left')
        self.__top_left_shadow.set_fixed_width(self.__shadow_size)
        self.__top_left_shadow.set_fixed_height(self.__shadow_size)
        self.__top_box.add_widget(self.__top_left_shadow)

        self.__top_shadow = EdgeShadow('top')
        self.__top_shadow.set_fixed_height(self.__shadow_size)
        self.__top_box.add_widget(self.__top_shadow)

        self.__top_right_shadow = EdgeShadow('top-right')
        self.__top_right_shadow.set_fixed_width(self.__shadow_size)
        self.__top_right_shadow.set_fixed_height(self.__shadow_size)
        self.__top_box.add_widget(self.__top_right_shadow)

        # Left
        self.__left_center_right_box = QtWidgets.QHBoxLayout()
        self.__main_box.add_layout(self.__left_center_right_box)

        self.__left_shadow = EdgeShadow('left')
        self.__left_shadow.set_fixed_width(self.__shadow_size)
        self.__left_center_right_box.add_widget(self.__left_shadow)

        # Center
        self.__center_shadow = EdgeShadow('center')
        self.__left_center_right_box.add_widget(self.__center_shadow)

        self.__central_shadow_box = QtWidgets.QVBoxLayout()
        self.__central_shadow_box.set_contents_margins(0, 0, 0, 0)
        self.__central_shadow_box.set_spacing(0)
        self.__center_shadow.set_layout(self.__central_shadow_box)

        self.__central_shadow_widget = QtWidgets.QFrame()
        self.__central_shadow_widget.set_object_name('CentralShadow')
        self.__central_shadow_box.add_widget(self.__central_shadow_widget)

        self.__central_border_box = QtWidgets.QVBoxLayout()
        self.__central_border_box.set_contents_margins(0, 0, 0, 0)
        self.__central_border_box.set_spacing(0)
        self.__central_shadow_widget.set_layout(self.__central_border_box)

        self.__central_border_widget = QtWidgets.QFrame()
        self.__central_border_widget.set_object_name('CentralBorder')
        self.__central_border_box.add_widget(self.__central_border_widget)

        self.__central_widget_box = QtWidgets.QVBoxLayout()
        self.__central_widget_box.set_contents_margins(0, 0, 0, 0)
        self.__central_widget_box.set_spacing(0)
        self.__central_border_widget.set_layout(self.__central_widget_box)

        self.__central_widget = QtWidgets.QFrame()
        self.__central_widget.set_object_name('Central')
        self.__central_widget_box.add_widget(self.__central_widget)

        # Right
        self.__right_shadow = EdgeShadow('right')
        self.__right_shadow.set_fixed_width(self.__shadow_size)
        self.__left_center_right_box.add_widget(self.__right_shadow)

        # Bottom
        self.__bottom_box = QtWidgets.QHBoxLayout()
        self.__main_box.add_layout(self.__bottom_box)

        self.__bottom_left_shadow = EdgeShadow('bottom-left')
        self.__bottom_left_shadow.set_fixed_width(self.__shadow_size)
        self.__bottom_left_shadow.set_fixed_height(self.__shadow_size)
        self.__bottom_box.add_widget(self.__bottom_left_shadow)

        self.__bottom_shadow = EdgeShadow('bottom')
        self.__bottom_shadow.set_fixed_height(self.__shadow_size)
        self.__bottom_box.add_widget(self.__bottom_shadow)

        self.__bottom_right_shadow = EdgeShadow('bottom-right')
        self.__bottom_right_shadow.set_fixed_width(self.__shadow_size)
        self.__bottom_right_shadow.set_fixed_height(self.__shadow_size)
        self.__bottom_box.add_widget(self.__bottom_right_shadow)

    def central_widget(self) -> QtWidgets:
        """Central widget
        
        First widget. Is the frame body
        """
        return self.__central_widget

    def is_shadow_visible(self) -> bool:
        """If the shadow is visible"""
        return self.__is_shadow_has_added

    def hide_shadow(self, hide: bool) -> None:
        """Hides or displays the frame shadow"""
        if hide:
            self.__center_shadow.hide_shadow(True)

            self.__bottom_left_shadow.set_visible(False)
            self.__bottom_shadow.set_visible(False)
            self.__bottom_right_shadow.set_visible(False)

            self.__top_left_shadow.set_visible(False)
            self.__top_shadow.set_visible(False)
            self.__top_right_shadow.set_visible(False)

            self.__left_shadow.set_visible(False)
            self.__right_shadow.set_visible(False)

            self.__is_shadow_has_added = False

        else:
            self.__center_shadow.hide_shadow(False)

            self.__bottom_left_shadow.set_visible(True)
            self.__bottom_shadow.set_visible(True)
            self.__bottom_right_shadow.set_visible(True)

            self.__top_left_shadow.set_visible(True)
            self.__top_shadow.set_visible(True)
            self.__top_right_shadow.set_visible(True)

            self.__left_shadow.set_visible(True)
            self.__right_shadow.set_visible(True)

            self.__is_shadow_has_added = True


class CoreMainFrame(ProtoFrame):
    """Complete Frame

    Using style integration
    """

    def __init__(self, *args, **kwargs) -> None:
        """Class constructor"""
        super().__init__(*args, **kwargs)
        self.__shadow_size = 8
        self.__edge_cursor_position = None
        self.__edge_resize_area_ssd = 5
        self.__edge_resize_area = self.__edge_resize_area_ssd
        self.__is_csd = True
        self.__show_shadow = False
        self.__is_dark = color.is_dark(
            QtGui.QPalette().color(QtGui.QPalette.Window).to_tuple())

        if self.__is_csd:
            self.set_window_flags(
                QtCore.Qt.FramelessWindowHint | QtCore.Qt.Window)
            self.__window_shadow_visible(True)

        self.__style_manager = StyleManager()
        self.__style_sheet = self.__style_manager.qss_style
        self.__style_sheet_inactive = self.__style_manager.qss_inactive_style
        self.__style_sheet_fullscreen = self.__style_sheet

        self.set_focus_policy(QtCore.Qt.ClickFocus)
        self.install_event_filter(self)

    def __set_edge_cursor_position(self, event: QtCore.QEvent) -> None:
        # Saves the position of the window where the mouse cursor is
        shadow_size = self.__shadow_size if self.is_shadow_visible() else 0
        resize_area = (
            -3 if not self.__is_csd else shadow_size - 3)
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
                        self.__edge_resize_area_ssd + self.__shadow_size)
            else:
                self.__edge_resize_area = self.__edge_resize_area_ssd

    def event_filter(
            self, watched: QtCore.QObject, event: QtCore.QEvent) -> bool:
        if event.type() == QtCore.QEvent.FocusIn:
            self.set_style_sheet(self.__style_sheet)
        elif event.type() == QtCore.QEvent.FocusOut:
            self.set_style_sheet(self.__style_sheet_inactive)

        if not self.__is_csd:
            # self.central_widget().set_style_sheet(self.__style_sheet)
            if event.type() == QtCore.QEvent.Resize:
                self.resize_event_signal.emit(event)
        else:
            if event.type() == QtCore.QEvent.HoverMove:
                self.__set_edge_cursor_position(event)
                self.__set_edge_cursor_position_shape()

            elif event.type() == QtCore.QEvent.Type.HoverEnter:
                pass

            elif event.type() == QtCore.QEvent.MouseButtonPress:
                self.__set_edge_cursor_position_shape()
                if self.__edge_cursor_position:
                    self.window_handle().start_system_resize(
                        self.__edge_cursor_position)

            elif event.type() == QtCore.QEvent.MouseButtonRelease:
                self.set_cursor(QtCore.Qt.CursorShape.ArrowCursor)

            elif event.type() == QtCore.QEvent.Resize:
                if self.__is_csd:
                    if self.is_maximized() or self.is_full_screen():
                        # self.central_widget().set_style_sheet(
                        #     self.__style_sheet_fullscreen)
                        self.__window_shadow_visible(False)
                    else:
                        self.__window_shadow_visible(True)

        return QtWidgets.QMainWindow.event_filter(self, watched, event)
