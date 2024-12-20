#!/usr/bin/env python3
from enum import Enum

from PySide6 import QtCore
from __feature__ import snake_case


class Flag(Enum):
    """Flag enumeration."""
    POPUP = QtCore.Qt.Popup

    def __str__(self):
        return f'<Flag: {id(self)}>'
