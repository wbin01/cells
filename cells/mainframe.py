#!/usr/bin/env python3
from .core import CoreMainFrame
from .icon import Icon
from .signal import Signal


class MainFrame(object):
    """Main frame
    
    That is, the main application window
    """

    def __init__(self, *args, **kwargs) -> None:
        """Class constructor"""
        super().__init__(*args, **kwargs)
        self.__frame = CoreMainFrame()
        self._qt_class = self.__frame

        self.__icon = None
        self.__icon_path = None
    
    @property
    def style(self) -> dict:
        """Style as dict

        Get the style as a dictionary or submit a new dictionary style to 
        update it
        """
        return self.__frame.stylesheet
    
    @style.setter
    def style(self, style: dict) -> None:
        self.__frame.stylesheet = style

    @property
    def icon(self) -> Icon:
        """Frame icon
        
        Application Icon
        """
        return self.__icon

    @icon.setter
    def icon(self, path: str) -> None:
        self.__icon = Icon(path)
        self.__frame.set_window_icon(self.__icon)

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
        elif name == 'mouse-left-click':
            return self.__frame.mouse_left_click

        # BUG: Only one works (release or press)
        # elif name == 'mouse-button-press':
        #     return self.__frame.mouse_button_press_signal
        # elif name == 'mouse-button-release':
        #     return self.__frame.mouse_button_release_signal

    def show(self) -> None:
        # Starts the main loop
        self.__frame.show()

    def __str__(self):
        return f'<MainFrame() {id(self)}>'
