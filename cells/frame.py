#!/usr/bin/env python3
from PySide6 import QtWidgets
from __feature__ import snake_case

from .core import CoreFrame
from .signal import Signal


class Frame(object):
    """Main frame.
    
    That is, the main application window.
    """
    
    def __init__(self, main_parent = None, *args, **kwargs) -> None:
        """Class constructor."""
        super().__init__(*args, **kwargs)
        self.main_parent_added = Signal()
        self.__main_parent = main_parent

        self.__frame = CoreFrame()
        
    @property
    def _obj(self):
        """Direct access to Qt classes.

        Warning: Direct access is discouraged and may break the project. 
        This access is considered a hacking for complex Qt implementations, 
        and should only be used for testing and analysis purposes.
        """
        return self.__frame

    @_obj.setter
    def _obj(self, obj: QtWidgets) -> None:
        self.__frame = obj

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
        self.main_parent_added.emit()

    def signal(self, name: str) -> Signal:
        """Event Signals.

        Signals are connections to events. When an event such as a mouse click 
        or other event occurs, a signal is sent. The signal can be assigned a 
        function to be executed when the signal is sent.

        :param name:
            String containing a signal type name, such as 'mouse-click'. 
            All possible names are: 'event-filter'.
        """
        if name == 'event-filter':
            return self.__frame.event_filter_signal

    def show(self) -> None:
        # Starts the main loop
        self.__frame.show()

    def __str__(self):
        return f'<Frame: {id(self)}>'
