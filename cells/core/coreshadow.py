#!/usr/bin/env python3
import os
import pathlib

from PySide6 import QtCore, QtGui, QtWidgets
from __feature__ import snake_case


class CoreShadow(QtWidgets.QFrame):
    """Specific part of a frame's shadow"""
    
    def __init__(self, position: str, *args, **kwargs) -> None:
        """Class constructor"""
        super().__init__(*args, **kwargs)
        self.set_object_name('toplevelwindowshadow')
        self.__shadow_color = 'rgba(0, 0, 0, 20)'
        self.__corner_shadow_color = 'rgba(0, 0, 0, 15)'
        self.__end_color = 'rgba(0, 0, 0, 0)'

        if position == 'top-left':
            self.set_style_sheet(
                '#toplevelwindowshadow {'
                'background:'
                '  qradialgradient('
                '  cx: 0.7, cy: 0.7, radius: 2, fx: 1.0, fy: 1.0,'
                f' stop: 0.0 {self.__corner_shadow_color},'
                f' stop: 0.4 {self.__end_color});'
                '}')

        elif position == 'top':
            self.set_style_sheet(
                '#toplevelwindowshadow {'
                'background: qlineargradient('
                '  x1:0 y1:0, x2:0 y2:1,'
                f' stop:0.0 {self.__end_color},'
                f' stop:1.0 {self.__shadow_color});'
                '}')

        elif position == 'top-right':
            self.set_style_sheet(
                '#toplevelwindowshadow {'
                'background:'
                '  qradialgradient('
                '  cx: 0.3, cy: 0.7, radius: 2, fx: 0.0, fy: 1.0,'
                f' stop: 0.0 {self.__corner_shadow_color},'
                f' stop: 0.4 {self.__end_color});'
                '}')

        elif position == 'left':
            self.set_style_sheet(
                '#toplevelwindowshadow {'
                'background: qlineargradient('
                '  x1:0 y1:0, x2:1 y2:0,'
                f' stop:0.0 {self.__end_color},'
                f' stop:1.0 {self.__shadow_color});'
                '}')

        elif position == 'right':
            self.set_style_sheet(
                '#toplevelwindowshadow {'
                'background: qlineargradient('
                '  x1:0 y1:0, x2:1 y2:0,'
                f' stop:0.0 {self.__shadow_color},'
                f' stop:1.0 {self.__end_color});'
                '}')

        elif position == 'bottom-left':
            self.set_style_sheet(
                '#toplevelwindowshadow {'
                'background:'
                '  qradialgradient('
                '  cx: 0.7, cy: 0.3, radius: 2, fx: 1.0, fy: 0.0,'
                f' stop: 0.0 {self.__corner_shadow_color},'
                f' stop: 0.4 {self.__end_color});'
                '}')

        elif position == 'bottom':
            self.set_style_sheet(
                '#toplevelwindowshadow {'
                'background: qlineargradient('
                '  x1:0 y1:0, x2:0 y2:1,'
                f' stop:0.0 {self.__shadow_color},'
                f' stop:1.0 {self.__end_color});'
                '}')

        elif position == 'bottom-right':
            self.set_style_sheet(
                '#toplevelwindowshadow {'
                'background:'
                '  qradialgradient('
                '  cx: 0.3, cy: 0.3, radius: 2, fx: 0.0, fy: 0.0,'
                f' stop: 0.0 {self.__corner_shadow_color},'
                f' stop: 0.4 {self.__end_color});'
                '}')
        else:
            self.set_style_sheet(
                '#toplevelwindowshadow {'
                f'background-color: {self.__shadow_color};'
                '}')

    def hide_shadow(self, hide: bool) -> None:
        """Hides or displays this shadow"""
        if hide:
            self.set_style_sheet(
                '#toplevelwindowshadow {'
                f'background-color: {self.__end_color};'
                '}')
            
        else:
            self.set_style_sheet(
                '#toplevelwindowshadow {'
                f'background-color: {self.__shadow_color};'
                '}')


class CoreFrameShadow(QtWidgets.QFrame):
    """Frame with shadow

    Only frame without integration
    """
    def __init__(self, *args, **kwargs) -> None:
        """Class constructor"""
        super().__init__(*args, **kwargs)
        self.set_attribute(QtCore.Qt.WA_TranslucentBackground)
        self.set_window_flags(QtCore.Qt.FramelessWindowHint)
        self.set_contents_margins(0, 0, 0, 0)
        self.set_minimum_width(90)
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
        self.__central_shadow_widget.set_object_name('Frame-Shadow')
        self.__central_shadow_box.add_widget(self.__central_shadow_widget)

        self.__central_border_box = QtWidgets.QVBoxLayout()
        self.__central_border_box.set_contents_margins(0, 0, 0, 0)
        self.__central_border_box.set_spacing(0)
        self.__central_shadow_widget.set_layout(self.__central_border_box)

        self.__central_border_widget = QtWidgets.QFrame()
        self.__central_border_widget.set_object_name('Frame-Border')
        self.__central_border_box.add_widget(self.__central_border_widget)

        self.__central_widget_box = QtWidgets.QVBoxLayout()
        self.__central_widget_box.set_contents_margins(0, 0, 0, 0)
        self.__central_widget_box.set_spacing(0)
        self.__central_border_widget.set_layout(self.__central_widget_box)

        self.__central_widget = QtWidgets.QFrame()
        self.__central_widget.set_object_name('Frame')
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
            self.set_minimum_height(30)
            self.set_minimum_width(90)

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
            self.set_minimum_height(30 + self.__shadow_size)
            self.set_minimum_width(90 + self.__shadow_size)


class CoreMainFrameShadow(QtWidgets.QMainWindow):
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
        self.__central_shadow_widget.set_object_name('MainFrame-Shadow')
        self.__central_shadow_box.add_widget(self.__central_shadow_widget)

        self.__central_border_box = QtWidgets.QVBoxLayout()
        self.__central_border_box.set_contents_margins(0, 0, 0, 0)
        self.__central_border_box.set_spacing(0)
        self.__central_shadow_widget.set_layout(self.__central_border_box)

        self.__central_border_widget = QtWidgets.QFrame()
        self.__central_border_widget.set_object_name('MainFrame-Border')
        self.__central_border_box.add_widget(self.__central_border_widget)

        self.__central_widget_box = QtWidgets.QVBoxLayout()
        self.__central_widget_box.set_contents_margins(0, 0, 0, 0)
        self.__central_widget_box.set_spacing(0)
        self.__central_border_widget.set_layout(self.__central_widget_box)

        self.__central_widget = QtWidgets.QFrame()
        self.__central_widget.set_object_name('MainFrame')
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
