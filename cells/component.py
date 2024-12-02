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
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.__component = CoreComponent()
        self._main_parent = None

        self.__box = QtWidgets.QVBoxLayout()
        self.__component.set_layout(self.__box)

    @property
    def main_parent(self):
        """..."""
        return self._main_parent
    
    @main_parent.setter
    def main_parent(self, parent) -> None:
        self._main_parent = parent

    @property
    def qt_obj(self):
        """Direct access to Qt classes.

        Warning: Direct access is discouraged and may break the project. 
        This access is considered a hacking for complex Qt implementations, 
        and should only be used for testing and analysis purposes.
        """
        return self.__component

    @qt_obj.setter
    def qt_obj(self, obj: QtWidgets) -> None:
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
        # ...
        box.main_parent = self.main_parent
        self.__box.add_layout(box.qt_obj)

    def add_component(self, component: Component) -> None:
        # ...
        component.main_parent = self.main_parent
        self.__box.add_widget(component.qt_obj)
