#!/usr/bin/env python3
from .core import CoreFrame
from .signal import Signal


class Frame(object):
    """Main frame
    
    That is, the main application window
    """
    
    def __init__(self, *args, **kwargs) -> None:
        """Class constructor"""
        super().__init__(*args, **kwargs)
        self.__frame = CoreFrame()

    def qt_class(self):
        """Direct access to Qt classes (QtWidgets.QFrame)

        Warning: Direct access is discouraged and may break the project. 
        This access is considered a hacking for complex Qt implementations, 
        and should only be used for testing and analysis purposes.
        """
        return self.__frame

    def signal(self, name: str) -> Signal:
        """Event Signals.

        Signals are connections to events. When an event such as a mouse click 
        or other event occurs, a signal is sent. The signal can be assigned a 
        function to be executed when the signal is sent.

        :param name:
            String containing a signal type name, such as 'mouse-click'. 
            All possible names are: 'event-filter'
        """
        if name == 'event-filter':
            return self.__frame.event_filter_signal

    def show(self) -> None:
        # Starts the main loop
        self.__frame.show()