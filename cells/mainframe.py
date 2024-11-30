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

        self.__icon = None
        self.__icon_path = None

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

    def event_signal(self, event: Event) -> Signal:
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
        if event == Event.CLOSE:
            return self.__frame.close_signal
        elif event == Event.DRAG:
            return self.__frame.drag_signal
        elif event == Event.DROP:
            return self.__frame.drop_signal
        elif event == Event.FRAME_STATE_CHANGE:
            return self.__frame.frame_state_change
        elif event == Event.FOCUS_IN:
            return self.__frame.focus_in_signal
        elif event == Event.FOCUS_OUT:
            return self.__frame.focus_out_signal
        elif event == Event.MOUSE_BUTTON_PRESS:
            return self.__frame.mouse_button_press_signal
        elif event == Event.MOUSE_BUTTON_RELEASE:
            return self.__frame.mouse_button_release_signal
        elif event == Event.MOUSE_DOUBLE_CLICK:
            return self.__frame.mouse_double_click_signal
        elif event == Event.MOUSE_HOVER_ENTER:
            return self.__frame.mouse_hover_enter_signal
        elif event == Event.MOUSE_HOVER_LEAVE:
            return self.__frame.mouse_hover_leave_signal
        elif event == Event.MOUSE_HOVER_MOVE:
            return self.__frame.mouse_hover_move_signal
        elif event == Event.MOUSE_RIGHT_BUTTON_PRESS:
            return self.__frame.mouse_right_button_press_signal
        elif event == Event.MOUSE_WHEEL:
            return self.__frame.mouse_wheel_signal
        elif event == Event.RESIZE:
            return self.__frame.resize_signal
        else:
            return Signal(Event.NONE)

    def qt_class(self):
        """Direct access to Qt classes (QtWidgets.QMainWindow)

        Warning: Direct access is discouraged and may break the project. 
        This access is considered a hacking for complex Qt implementations, 
        and should only be used for testing and analysis purposes.
        """
        return self.__frame

    def show(self) -> None:
        # Starts the main loop
        self.__frame.show()

    def __str__(self):
        return f'<MainFrame: {id(self)}>'
