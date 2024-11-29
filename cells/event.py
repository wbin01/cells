#!/usr/bin/env python3
from enum import Enum


class Event(Enum):
    # EVENT_FILTER = 'EVENT_FILTER'
    FOCUS_IN = 'FOCUS_IN'
    FOCUS_OUT = 'FOCUS_OUT'
    HOVER_ENTER = 'HOVER_ENTER'
    HOVER_LEAVE = 'HOVER_LEAVE'
    HOVER_MOVE = 'HOVER_MOVE'
    MOUSE_LEFT_CLICK = 'MOUSE_LEFT_CLICK'
    NONE = 'NONE'
