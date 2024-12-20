#!/usr/bin/env python3
import sys

from PySide6 import QtWidgets, QtGui
from __feature__ import snake_case

from .core import ApplicationManager


class Application(object):
    """Application manager.

    Configures parameters and events external to the application.
    """
    def __init__(self, *args, **kwargs) -> None:
        """Class constructor."""
        self.__args = args[0]
        self.__application = QtWidgets.QApplication(self.__args)
        self.__frame = None
        self.__icon_path = None
        self.__icon = None
        self.__devel = ApplicationManager(args)

    @property
    def frame(self) -> QtWidgets:
        """Application frame.
        
        That is, the main application window.
        """
        return self.__frame

    @frame.setter
    def frame(self, frame: QtWidgets) -> None:
        self.__frame = frame

    @property
    def icon(self) -> str:
        """Frame icon path string.

        Application Icon.
        """
        return self.__icon_path

    @icon.setter
    def icon(self, path: str) -> None:
        self.__icon_path = path
        if self.__frame:
            self.__icon = QtGui.QIcon(QtGui.QPixmap(path))
            self.__frame.icon = self.__icon
            self.__devel.icon = path

    @property
    def frame_id(self) -> list:
        """Frame identity list.

        List containing app identity information.
        The first item is the main file, __file__, followed by an ID
        Example:
            [__file__, 'app_id', 'App Name']

        ID name must be 3 characters or more, and can only contain lowercase 
        letters, numbers or underscores '_', such as:
            [__file__, 'app_4_me', 'App 4 me' ]

        When set the list, all items are optional, but the order is mandatory.
        """
        return self.__frame_id_list

    @frame_id.setter
    def frame_id(self, frame_id: list) -> None:
        self.__frame_id_list = frame_id
        self.__devel.frame_id = frame_id
        self.__application.set_desktop_file_name(self.__devel.wm_class)
    
    def exec(self) -> None:
        """Runs and displays the application.

        Starts the main loop and renders frames.
        """
        if '--deploy' in self.__args:
            self.__devel.deploy()
            sys.exit(0)

        if not self.__frame:
            self.__devel.clear_tmp()
            sys.exit(-1)

        self.__frame.show()
        exit_code = self.__application.exec()
        
        self.__devel.clear_tmp()
        sys.exit(exit_code)
