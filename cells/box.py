#!/usr/bin/env python3
from PySide6 import QtWidgets
from __feature__ import snake_case

from .component import Component

class Box(object):
    """Box layout"""
    def __init__(self, *args, **kwargs) -> None:
        """Class constructor."""


class Box(Box):
    """Box layout"""
    def __init__(self, horizontal: bool = False, *args, **kwargs) -> None:
        """Class constructor.

        By default the Box orientation is vertical. Use the horizontal parameter to change it.

        :param horizontal: Changes the orientation of the Box to horizontal
        """
        super().__init__(horizontal, *args, **kwargs)
        self.__box = QtWidgets.QVBoxLayout()
        if horizontal:
            self.__box = QtWidgets.QHBoxLayout()

        self.__box.set_contents_margins(0, 0, 0, 0)
        self.__box.set_spacing(0)
        self.__main_parent = None

    @property
    def _main_parent(self) -> Component | Box:
        """Main frame of the application.

        Use only to access properties and methods of the Main Frame, defining a 
        new frame will break the application.
        """
        return self.__main_parent
    
    @_main_parent.setter
    def _main_parent(self, parent) -> None:
        self.__main_parent = parent

    @property
    def _obj(self):
        """Direct access to Qt classes.

        Warning: Direct access is discouraged and may break the project. 
        This access is considered a hacking for complex Qt implementations, 
        and should only be used for testing and analysis purposes.
        """
        return self.__box

    @_obj.setter
    def _obj(self, obj: QtWidgets) -> None:
        self.__box = obj

    def add_box(self, box: Box) -> None:
        """Add a new Box inside this Box"""
        box.main_parent = self.__main_parent
        self.__box.add_layout(box._obj)

    def add_component(self, component: Component) -> None:
        """Add a Component inside this Box"""
        component._main_parent = self._main_parent
        self.__box.add_widget(component._obj)

    def __str__(self):
        return f'<Box: {id(self)}>'
