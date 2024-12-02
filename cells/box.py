#!/usr/bin/env python3
from PySide6 import QtWidgets
from __feature__ import snake_case

from .component import Component

class Box(object):
    """Box layout"""
    def __init__(self, horizontal: bool = False, *args, **kwargs) -> None:
        """Class constructor.

        By default the Box orientation is vertical. Use the horizontal parameter to change it.

        :param horizontal: Changes the orientation of the Box to horizontal
        """
        self.__box = QtWidgets.QVBoxLayout()
        if horizontal:
            self.__box = QtWidgets.QHBoxLayout()

    @property
    def qt_obj(self):
        """Direct access to Qt classes.

        Warning: Direct access is discouraged and may break the project. 
        This access is considered a hacking for complex Qt implementations, 
        and should only be used for testing and analysis purposes.
        """
        return self.__box

    @qt_obj.setter
    def qt_obj(self, obj: QtWidgets) -> None:
        self.__box = obj


class Box(Box):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._main_parent = None

    @property
    def main_parent(self):
        """..."""
        return self._main_parent
    
    @main_parent.setter
    def main_parent(self, parent) -> None:
        self._main_parent = parent

    def add_box(self, box: Box) -> None:
        # ...
        box.main_parent = self.main_parent
        self.__box.add_layout(box.qt_obj)

    def add_component(self, component: Component) -> None:
        # ...
        component.main_parent = self.main_parent
        self.__box.add_widget(component.qt_obj)
