#!/usr/bin/env python3
from .core import CoreMainFrame
from .icon import Icon
from .signal import Signal
from .event import Event


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

    def signal(self, event: Event) -> Signal:
        """Event Signals.

        Signals are connections to events. When an event such as a mouse click 
        or other event occurs, a signal is sent. The signal can be assigned a 
        function to be executed when the signal is sent.

        :param event:
            Event enumeration (Enum) corresponding to the requested event, 
            such as Event.HOVER_ENTER . All possible names are:
            
            FOCUS_IN
            FOCUS_OUT
            HOVER_ENTER
            HOVER_LEAVE
            HOVER_MOVE
            MOUSE_LEFT_CLICK
            NONE
        """
        # if event == Event.EVENT_FILTER:
        #     return self.__frame.event_filter_signal
        if event == Event.FOCUS_IN:
            return self.__frame.focus_in_signal
        elif event == Event.FOCUS_OUT:
            return self.__frame.focus_out_signal
        elif event == Event.HOVER_ENTER:
            return self.__frame.hover_enter_signal
        elif event == Event.HOVER_LEAVE:
            return self.__frame.hover_leave_signal
        elif event == Event.HOVER_MOVE:
            return self.__frame.hover_move_signal
        elif event == Event.MOUSE_LEFT_CLICK:
            return self.__frame.mouse_left_click_signal
            # BUG: Only one works, release or press
        else:
            return Signal(Event.NONE)

    def show(self) -> None:
        # Starts the main loop
        self.__frame.show()

    def __str__(self):
        return f'<MainFrame() {id(self)}>'
