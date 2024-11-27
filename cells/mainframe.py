#!/usr/bin/env python3
from .core import CoreMainFrame, CoreIcon, CoreImage
from .signal import Signal


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

        self.event_filter_signal = self.__frame.event_filter_signal

    @property
    def icon(self) -> CoreIcon:
        """Frame icon
        
        Application Icon
        """
        return self.__icon

    @icon.setter
    def icon(self, path: str) -> None:
        self.__icon = CoreIcon(path)
        self.__frame.set_window_icon(self.__icon)

    def _show(self) -> None:
        # Starts the main loop
        self.__frame.show()
