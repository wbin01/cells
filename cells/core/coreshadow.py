#!/usr/bin/env python3
from PySide6 import QtWidgets
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
