#!/usr/bin/env python3
from enum import Enum


class Event(Enum):
    """Event enumeration"""
    NONE = 'NONE'
    CLOSE = 'CLOSE'
    DRAG = 'DRAG'
    DROP = 'DROP'
    FOCUS_IN = 'FOCUS_IN'
    FOCUS_OUT = 'FOCUS_OUT'
    MOUSE_BUTTON_PRESS = 'MOUSE_BUTTON_PRESS'
    MOUSE_BUTTON_RELEASE = 'MOUSE_BUTTON_RELEASE'
    MOUSE_DOUBLE_CLICK = 'MOUSE_DOUBLE_CLICK'
    MOUSE_HOVER_ENTER = 'MOUSE_HOVER_ENTER'
    MOUSE_HOVER_LEAVE = 'MOUSE_HOVER_LEAVE'
    MOUSE_HOVER_MOVE = 'MOUSE_HOVER_MOVE'
    MOUSE_RIGHT_BUTTON_PRESS = 'MOUSE_RIGHT_BUTTON_PRESS'
    MOUSE_WHEEL = 'MOUSE_WHEEL'
    RESIZE = 'RESIZE'
    STATE_CHANGE = 'STATE_CHANGE'
    TITLE_CHANGE = 'TITLE_CHANGE'

    def __str__(self):
        return f'<Event: {id(self)}>'
