#!/usr/bin/env python3
from PySide6 import QtWidgets
from __feature__ import snake_case


class Component(object):
    """..."""
    def __init__(self, horizontal: bool = False, *args, **kwargs) -> None:
        self.__widget = QtWidgets.QWidget()

    @property
    def qt_obj(self):
        """Direct access to Qt classes.

        Warning: Direct access is discouraged and may break the project. 
        This access is considered a hacking for complex Qt implementations, 
        and should only be used for testing and analysis purposes.
        """
        return self.__widget

    @qt_obj.setter
    def qt_obj(self, obj: QtWidgets) -> None:
        self.__widget = obj
