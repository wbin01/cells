#!/usr/bin/env python3
from enum import Enum


class Event(Enum):
    NONE = 0
    FOCUS_IN = 1
    FOCUS_OUT = 2
    MOUSE_CLICK = 3
    MOUSE_DOUBLE_CLICK = 4
    MOUSE_HOVER_ENTER = 5
    MOUSE_HOVER_LEAVE = 6
    MOUSE_HOVER_MOVE = 7
    MOUSE_RIGHT_CLICK = 8
    MOUSE_WHEEL = 9
    # EVENT_FILTER
