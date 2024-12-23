#!/usr/bin/env python3
from enum import Enum

from PySide6 import QtCore
from __feature__ import snake_case


class Orientation(Enum):
    """Flag enumeration."""
    VERTICAL = 0
    HORIZONTAL = 1

    def __str__(self):
        return f'<Orientation: {id(self)}>'
