#!/usr/bin/env python3
from enum import Enum


class Event(Enum):
    """Event enumeration."""
    NONE = 'NONE'
    ALIGNMENT_CHANGE = 'ALIGNMENT_CHANGE'
    CLOSE = 'CLOSE'
    DELETE_ITEM = 'DELETE_ITEM'
    DRAG = 'DRAG'
    DROP = 'DROP'
    ENABLED_CHANGE = 'ENABLED_CHANGE'
    FOCUS_IN = 'FOCUS_IN'
    FOCUS_OUT = 'FOCUS_OUT'
    INSERT_ITEM = 'INSERT_ITEM'
    MAIN_PARENT_ADDED = 'MAIN_PARENT_ADDED'
    MOUSE_BUTTON_PRESS = 'MOUSE_BUTTON_PRESS'
    MOUSE_BUTTON_RELEASE = 'MOUSE_BUTTON_RELEASE'
    MOUSE_DOUBLE_CLICK = 'MOUSE_DOUBLE_CLICK'
    MOUSE_HOVER_ENTER = 'MOUSE_HOVER_ENTER'
    MOUSE_HOVER_LEAVE = 'MOUSE_HOVER_LEAVE'
    MOUSE_HOVER_MOVE = 'MOUSE_HOVER_MOVE'
    MOUSE_RIGHT_BUTTON_PRESS = 'MOUSE_RIGHT_BUTTON_PRESS'
    MOUSE_WHEEL = 'MOUSE_WHEEL'
    REMOVE_ITEM = 'REMOVE_ITEM'
    RESIZE = 'RESIZE'
    STATE_CHANGE = 'STATE_CHANGE'
    STYLE_CHANGE = 'STYLE_CHANGE'
    STYLE_CLASS_CHANGE = 'STYLE_CLASS_CHANGE'
    STYLE_ID_CHANGE = 'STYLE_ID_CHANGE'
    TITLE_CHANGE = 'TITLE_CHANGE'

    def __str__(self):
        return f'<Event: {id(self)}>'
