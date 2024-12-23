#!/usr/bin/env python3
from PySide6 import QtWidgets
from __feature__ import snake_case

from .event import Event


class Box(object):
    """Box layout"""
    def __init__(self, *args, **kwargs) -> None:
        """Class constructor."""


class Widget(object):
    """Widget."""
    def __init__(self, *args, **kwargs) -> None:
        """Class constructor."""


class Box(Box):
    """Box layout"""
    def __init__(self, horizontal: bool = False, *args, **kwargs) -> None:
        """Class constructor.

        By default the Box orientation is vertical. Use the horizontal 
        parameter to change it.

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
    def margin(self) -> tuple:
        """Box Margins"""
        margin = self.__box.contents_margins()
        return margin.top(), margin.right(), margin.bottom(), margin.left()
    
    @margin.setter
    def margin(self, margin: tuple) -> None:
        self.__box.set_contents_margins(
            margin[3], margin[0], margin[1], margin[2])

    @property
    def spacing(self) -> int:
        """
        The space between widgets inside the box.

        This property takes precedence over the margins of the widgets that 
        are added (add_widgets), so if the Box is vertical, then only the side 
        margins of the widgets will be respected. The Box does not activate 
        the spacing with a single isolated widget.
        """
        return self.__box.spacing()

    @spacing.setter
    def spacing(self, spacing: int) -> None:
        self.__box.set_spacing(spacing)

    @property
    def _main_parent(self) -> Widget | Box:
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

    def insert(self, item: Widget | Box, index: int = -1) -> Widget | Box:
        """Inserts a Widget or a Box.

        Returns the reference to the inserted item.
        
        :param item: It can be a Widget (Widget, Label, Button...) or a Box.
        :param index: Index number where the item should be inserted 
            (Default is -1)
        """
        _, item = setattr(self, str(item), item), getattr(self, str(item))
        item._main_parent = self.__main_parent

        if isinstance(item, Box):
            self.__box.insert_layout(index, item._obj)
        else:
            self.__box.insert_widget(index, item._obj)

        return item

    def __str__(self):
        return f'<Box: {id(self)}>'
