#!/usr/bin/env python3
from PySide6 import QtWidgets
from __feature__ import snake_case

from .core import CoreWidget
from .event import Event
from .signal import Signal


class Widget(object):
    """Widget."""
    def __init__(self, *args, **kwargs) -> None:
        """Class constructor."""


class Widget(Widget):
    """Widget."""
    def __init__(self, *args, **kwargs) -> None:
        """Class constructor."""
        super().__init__(*args, **kwargs)
        self.__widget = CoreWidget()
        self.__main_parent = None

        self.__box = QtWidgets.QVBoxLayout()
        self.__widget.set_layout(self.__box)

    @property
    def style_id(self) -> str:
        """Style ID.

        An ID allows you to define a unique style that does not distort parent 
        objects of the same type that inherit from the class.

        Send a string with a unique ID to set the style for this Widget only.
        """
        return self.__widget.object_name()

    @style_id.setter
    def style_id(self, style_id: str) -> None:
        self.__widget.set_object_name(style_id)

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

    @property
    def _obj(self):
        """Direct access to Qt classes.

        Warning: Direct access is discouraged and may break the project. 
        This access is considered a hacking for complex Qt implementations, 
        and should only be used for testing and analysis purposes.
        """
        return self.__widget

    @_obj.setter
    def _obj(self, obj: QtWidgets) -> None:
        self.__widget = obj

    def event_signal(self, event: Event) -> Signal:
        """Event Signals.

        Signals are connections to events. When an event such as a mouse click 
        or other event occurs, a signal is sent. The signal can be assigned a 
        function to be executed when the signal is sent.

        :param event:
            Event enumeration (Enum) corresponding to the requested event, 
            such as Event.HOVER_ENTER . All possible names are:
            
            NONE, MOUSE_BUTTON_PRESS, MOUSE_BUTTON_RELEASE, MOUSE_DOUBLE_CLICK, 
            MOUSE_HOVER_ENTER, MOUSE_HOVER_LEAVE, MOUSE_HOVER_MOVE, 
            MOUSE_RIGHT_BUTTON_PRESS, MOUSE_WHEEL, RESIZE.
        """
        if event == Event.MOUSE_BUTTON_PRESS:
            return self.__widget.mouse_button_press_signal
        elif event == Event.MOUSE_BUTTON_RELEASE:
            return self.__widget.mouse_button_release_signal
        elif event == Event.MOUSE_DOUBLE_CLICK:
            return self.__widget.mouse_double_click_signal
        elif event == Event.MOUSE_HOVER_ENTER:
            return self.__widget.mouse_hover_enter_signal
        elif event == Event.MOUSE_HOVER_LEAVE:
            return self.__widget.mouse_hover_leave_signal
        elif event == Event.MOUSE_HOVER_MOVE:
            return self.__widget.mouse_hover_move_signal

        elif event == Event.MOUSE_RIGHT_BUTTON_PRESS:
            return self.__widget.mouse_right_button_press_signal
        elif event == Event.MOUSE_WHEEL:
            return self.__widget.mouse_wheel_signal
        elif event == Event.RESIZE:
            return self.__widget.resize_signal
        else:
            return Signal(Event.NONE)

    def add_box(self, box) -> None:
        """Add a Box inside this Widget"""
        box._main_parent = self._main_parent
        self.__box.add_layout(box._obj)

    def add_widget(self, widget: Widget) -> None:
        """Add a new Widget inside this Widget"""
        widget.main_parent = self._main_parent
        self.__box.add_widget(widget._obj)

    def __str__(self):
        return f'<Widget: {id(self)}>'
