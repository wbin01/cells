#!/usr/bin/env python3
from PySide6 import QtGui
from __feature__ import snake_case


class Icon(QtGui.QIcon):
    def __init__(self, *args, **kwargs) -> None:
        """Class constructor"""
        super().__init__(*args, **kwargs)

    def __str__(self):
        return f'<Icon: {id(self)}>'