#!/usr/bin/env python3
from PySide6 import QtCore, QtGui, QtWidgets
from __feature__ import snake_case

from . import color
from .modules import StyleManager
from .coreshadow import CoreShadow


class ProtoFrame(QtWidgets.QFrame):
    """Frame with shadow

    Only frame without integration
    """
    
    def __init__(self, *args, **kwargs) -> None:
        """Class constructor"""
        super().__init__(*args, **kwargs)
        self.set_attribute(QtCore.Qt.WA_TranslucentBackground)
        self.set_window_flags(QtCore.Qt.FramelessWindowHint)
        self.set_contents_margins(0, 0, 0, 0)
        self.set_minimum_width(60)
        self.set_minimum_height(30)

        self.__is_shadow_has_added = True
        self.__shadow_size = 8

        self.__main_box = QtWidgets.QVBoxLayout()
        self.__main_box.set_contents_margins(0, 0, 0, 0)
        self.__main_box.set_spacing(0)
        self.set_layout(self.__main_box)

        # Top
        self.__top_box = QtWidgets.QHBoxLayout()
        self.__main_box.add_layout(self.__top_box)

        self.__top_left_shadow = CoreShadow('top-left')
        self.__top_left_shadow.set_fixed_width(self.__shadow_size)
        self.__top_left_shadow.set_fixed_height(self.__shadow_size)
        self.__top_box.add_widget(self.__top_left_shadow)

        self.__top_shadow = CoreShadow('top')
        self.__top_shadow.set_fixed_height(self.__shadow_size)
        self.__top_box.add_widget(self.__top_shadow)

        self.__top_right_shadow = CoreShadow('top-right')
        self.__top_right_shadow.set_fixed_width(self.__shadow_size)
        self.__top_right_shadow.set_fixed_height(self.__shadow_size)
        self.__top_box.add_widget(self.__top_right_shadow)

        # Left
        self.__left_center_right_box = QtWidgets.QHBoxLayout()
        self.__main_box.add_layout(self.__left_center_right_box)

        self.__left_shadow = CoreShadow('left')
        self.__left_shadow.set_fixed_width(self.__shadow_size)
        self.__left_center_right_box.add_widget(self.__left_shadow)

        # Center
        self.__center_shadow = CoreShadow('center')
        self.__left_center_right_box.add_widget(self.__center_shadow)

        self.__central_shadow_box = QtWidgets.QVBoxLayout()
        self.__central_shadow_box.set_contents_margins(0, 0, 0, 0)
        self.__central_shadow_box.set_spacing(0)
        self.__center_shadow.set_layout(self.__central_shadow_box)

        self.__central_shadow_widget = QtWidgets.QFrame()
        self.__central_shadow_widget.set_object_name('FrameCentralShadow')
        self.__central_shadow_box.add_widget(self.__central_shadow_widget)

        self.__central_border_box = QtWidgets.QVBoxLayout()
        self.__central_border_box.set_contents_margins(0, 0, 0, 0)
        self.__central_border_box.set_spacing(0)
        self.__central_shadow_widget.set_layout(self.__central_border_box)

        self.__central_border_widget = QtWidgets.QFrame()
        self.__central_border_widget.set_object_name('FrameCentralBorder')
        self.__central_border_box.add_widget(self.__central_border_widget)

        self.__central_widget_box = QtWidgets.QVBoxLayout()
        self.__central_widget_box.set_contents_margins(0, 0, 0, 0)
        self.__central_widget_box.set_spacing(0)
        self.__central_border_widget.set_layout(self.__central_widget_box)

        self.__central_widget = QtWidgets.QFrame()
        self.__central_widget.set_object_name('FrameCentral')
        self.__central_widget_box.add_widget(self.__central_widget)

        # Right
        self.__right_shadow = CoreShadow('right')
        self.__right_shadow.set_fixed_width(self.__shadow_size)
        self.__left_center_right_box.add_widget(self.__right_shadow)

        # Bottom
        self.__bottom_box = QtWidgets.QHBoxLayout()
        self.__main_box.add_layout(self.__bottom_box)

        self.__bottom_left_shadow = CoreShadow('bottom-left')
        self.__bottom_left_shadow.set_fixed_width(self.__shadow_size)
        self.__bottom_left_shadow.set_fixed_height(self.__shadow_size)
        self.__bottom_box.add_widget(self.__bottom_left_shadow)

        self.__bottom_shadow = CoreShadow('bottom')
        self.__bottom_shadow.set_fixed_height(self.__shadow_size)
        self.__bottom_box.add_widget(self.__bottom_shadow)

        self.__bottom_right_shadow = CoreShadow('bottom-right')
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


class CoreFrame(ProtoFrame):
    """Complete Frame

    Using style integration
    """

    def __init__(self, *args, **kwargs) -> None:
        """Class constructor"""
        super().__init__(*args, **kwargs)
        self.__is_dark = color.is_dark(
            QtGui.QPalette().color(QtGui.QPalette.Window).to_tuple())
        self.__style_manager = StyleManager()
        self.__style_sheet = self.__style_manager.qss_style
        self.__style_sheet_fullscreen = self.__style_sheet

        self.set_style_sheet(self.__style_sheet)
        self.hide_shadow(True)
