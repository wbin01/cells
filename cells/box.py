#!/usr/bin/env python3
from PySide6 import QtWidgets
from __feature__ import snake_case

from .align import Align
from .event import Event
from .orientation import Orientation
from .signal import Signal


class Box(object):
    """Box layout

    # Internal control!
    """
    def __init__(self, *args, **kwargs) -> None:
        """Class constructor."""


class Widget(object):
    """Widget. xxx
    
    # Internal control!
    """
    def __init__(self, *args, **kwargs) -> None:
        """Class constructor. xxx"""


class Box(Box):
    """Box layout"""
    def __init__(
            self,
            orientation: Orientation = Orientation.VERTICAL,
            *args, **kwargs) -> None:
        """Class constructor.

        By default the Box orientation is vertical. Use the horizontal 
        parameter to change it.

        :param orientation: Changes the orientation of the Box to horizontal
        """
        super().__init__(*args, **kwargs)
        # Param
        if orientation == Orientation.HORIZONTAL:
            self.__box = QtWidgets.QHBoxLayout()
        else:
            self.__box = QtWidgets.QVBoxLayout()

        # Signals
        self.__signals = {
            Event.DELETE: Signal(),
            Event.INSERT: Signal(),
            Event.REMOVE: Signal()}

        self.__box.set_contents_margins(0, 0, 0, 0)
        self.__box.set_spacing(0)
        self.__main_parent = None

        self.__items = []

    @property
    def align(self) -> Align:
        """Align enum.

        Sets the Box alignment.
        """
        return self.__box.alignment()

    @align.setter
    def align(self, align: Align) -> None:
        self.__box.set_alignment(align.value)

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
    def _main_parent(self):
        """Main frame of the application.

        Use only to access properties and methods of the Main Frame, defining a 
        new frame will break the application.
        """
        return self.__main_parent
    
    @_main_parent.setter
    def _main_parent(self, parent) -> None:
        self.__main_parent = parent
        for item in self.items():
            if not item._main_parent:
                item._main_parent = parent

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

    def delete(self, item: Widget | Box) -> None:
        """Delete a Widget or a Box.

        When an item is deleted, the reference to it no longer exists. Using 
        the old variable for this item causes an error. In order to use the 
        old variable, the item will need to be instantiated again.

        :param item: A Widget (Widget, Label, Button...) or a Box.
        """
        self.__items.remove(item)
        item._obj.delete_later()
        self.__signals[Event.DELETE].emit()

    def add(self, item: Widget | Box, index: int = -1) -> Widget | Box:
        """Inserts a Widget or a Box.

        Returns the reference to the added item.
        
        :param item: It can be a Widget (Widget, Label, Button...) or a Box.
        :param index: Index number where the item should be added 
            (Default is -1)
        """
        _, item = setattr(self, str(item), item), getattr(self, str(item))
        if self.__main_parent:
            item._main_parent = self.__main_parent

        if isinstance(item, Box):
            self.__box.insert_layout(index, item._obj)
        else:
            item.style_id = item.style_id
            if hasattr(item, 'visible'):
                item.visible = True
            self.__box.insert_widget(index, item._obj)

        self.__items.append(item)
        self.__signals[Event.INSERT].emit()

        return item

    def items(self) -> list:
        """List with added widgets."""
        return self.__items

    def remove(self, item: Widget | Box) -> None:
        """Removes a Widget or a Box.

        This only removes the widget, but does not delete it. The variable 
        referring to it still works and can be added again later. To 
        completely delete the widget from the variable, use the 'delete()' 
        method.

        :param item: A Widget (Widget, Label, Button...) or a Box.
        """
        if isinstance(item, Box):
            self.__box.remove_layout(item._obj)
        else:
            self.__box.remove_widget(item._obj)
        item._obj.set_parent(None)

        self.__items.remove(item)
        self.__signals[Event.REMOVE].emit()

    def signal(self, event: Event) -> Signal:
        """Event Signals.

        Signals are connections to events. When an event such as a mouse 
        click (Event.MOUSE_BUTTON_PRESS) or other event occurs, a signal is 
        sent. The signal can be assigned a function to be executed when the 
        signal is sent.

        Use the 'events_available_for_signal()' method to see all available 
        events.

        :param event:
            Event enumeration (Enum) corresponding to the requested event, 
            such as Event.HOVER_ENTER. See: events_available_for_signal().
        """
        if event in self.__signals:
            return self.__signals[event]

    def __str__(self):
        return f'<Box: {id(self)}>'
