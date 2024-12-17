#!/usr/bin/env python3
from PySide6 import QtCore, QtGui, QtWidgets
from __feature__ import snake_case

from .modules import colorconverter
from .modules import StyleManager
from .coreshadow import CoreFrameShadow


class CoreFrame(CoreFrameShadow):
    """Complete Frame

    Using style integration and shadow
    """
    def __init__(self, *args, **kwargs) -> None:
        """Class constructor"""
        super().__init__(*args, **kwargs)
        self.__is_dark = colorconverter.is_dark(
            QtGui.QPalette().color(QtGui.QPalette.Window).to_tuple())

        self.hide_shadow(True)

        self.__style_manager = StyleManager()
        self.__qss_styles = self.__style_manager.stylesheet_qss()
        self.set_style_sheet(self.__qss_styles['active'])
