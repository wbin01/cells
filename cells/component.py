#!/usr/bin/env python3
from PySide6 import QtWidgets
from __feature__ import snake_case

from .core import CoreComponent
from .event import Event
from .signal import Signal


class Component(object):
    """Component widget."""
    def __init__(self, *args, **kwargs) -> None:
        """Class constructor."""


class Component(Component):
    """Component widget."""
    def __init__(self, *args, **kwargs) -> None:
        """Class constructor."""
        super().__init__(*args, **kwargs)
        self.__component = CoreComponent()
        self.__main_parent = None

        self.__box = QtWidgets.QVBoxLayout()
        self.__component.set_layout(self.__box)

    @property
    def style_id(self) -> str:
        """Style ID.

        An ID allows you to define a unique style that does not distort parent 
        objects of the same type that inherit from the class.

        Send a string with a unique ID to set the style for this Component only.
        """
        return self.__component.object_name()

    @style_id.setter
    def style_id(self, style_id: str) -> None:
        self.__component.set_object_name(style_id)

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
        return self.__component

    @_obj.setter
    def _obj(self, obj: QtWidgets) -> None:
        self.__component = obj

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
            return self.__component.mouse_button_press_signal
        elif event == Event.MOUSE_BUTTON_RELEASE:
            return self.__component.mouse_button_release_signal
        elif event == Event.MOUSE_DOUBLE_CLICK:
            return self.__component.mouse_double_click_signal
        elif event == Event.MOUSE_HOVER_ENTER:
            return self.__component.mouse_hover_enter_signal
        elif event == Event.MOUSE_HOVER_LEAVE:
            return self.__component.mouse_hover_leave_signal
        elif event == Event.MOUSE_HOVER_MOVE:
            return self.__component.mouse_hover_move_signal

        elif event == Event.MOUSE_RIGHT_BUTTON_PRESS:
            return self.__component.mouse_right_button_press_signal
        elif event == Event.MOUSE_WHEEL:
            return self.__component.mouse_wheel_signal
        elif event == Event.RESIZE:
            return self.__component.resize_signal
        else:
            return Signal(Event.NONE)

    def add_box(self, box) -> None:
        """Add a Box inside this Component"""
        box._main_parent = self._main_parent
        self.__box.add_layout(box._obj)

    def add_component(self, component: Component) -> None:
        """Add a new Component inside this Component"""
        component.main_parent = self._main_parent
        self.__box.add_widget(component.qt_obj)

    def __str__(self):
        return f'<Component: {id(self)}>'
