#!/usr/bin/env python3
from .core import CoreFrame

class Frame(object):
    """Main frame
    
    That is, the main application window
    """
    
    def __init__(self, *args, **kwargs) -> None:
        """Class constructor"""
        super().__init__(*args, **kwargs)
        self.__frame = CoreFrame()
        self._qt_class = self.__frame

    def show(self) -> None:
        # Starts the main loop
        self.__frame.show()