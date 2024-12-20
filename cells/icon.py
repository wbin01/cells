#!/usr/bin/env python3
from PySide6 import QtGui
from __feature__ import snake_case


class Icon(object):
    """Icon."""
    def __init__(self, path: str = None) -> None:
        """Class constructor."""
        self.__icon = QtGui.QIcon(path)

    @property
    def _obj(self):
        """Direct access to Qt classes.

        Warning: Direct access is discouraged and may break the project. 
        This access is considered a hacking for complex Qt implementations, 
        and should only be used for testing and analysis purposes.
        """
        return self.__icon

    @_obj.setter
    def _obj(self, obj: QtGui) -> None:
        self.__icon = obj

    def __str__(self):
        return f'<Icon: {id(self)}>'
