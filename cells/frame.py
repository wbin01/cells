#!/usr/bin/env python3
from PySide6 import QtCore, QtGui, QtWidgets
from __feature__ import snake_case

from .align import Align
from .box import Box
from .core import CoreFrame
from .core.modules import desktopentryparse
from .event import Event
from .flag import Flag
from .orientation import Orientation
from .signal import Signal
from .widget import Widget


class Frame(object):
    """Main frame.
    
    That is, the main application window.
    """
    
    def __init__(
        self,
        main_parent = None,
        orientation: Orientation = Orientation.VERTICAL,
        *args, **kwargs) -> None:
        """Class constructor."""
        super().__init__(*args, **kwargs)
        self.main_parent_added_signal = Signal()
        self.__frame_flags = []
        self.__main_parent = main_parent
        self.__frame = CoreFrame()
        self.__frame_box = Box(orientation=orientation)
        self.__frame_box._main_parent = self
        self.__frame.central_widget().set_layout(self.__frame_box._obj)

    @property
    def align(self) -> Align:
        """Align enum.

        Sets the alignment of the Box.
        """
        return self.__frame_box._obj.alignment()

    @align.setter
    def align(self, align: Align) -> None:
        self.__frame_box._obj.set_alignment(align.value)

    @property
    def flag(self) -> list:
        """Frame flags.

        They are used to configure the native behavior of the Frame.
        For example, the POPUP flag configures that the frame can appear on 
        the indicated position on the X and Y axes, and also that the Frame 
        closes by itself.
        """
        return self.__frame_flags

    @flag.setter
    def flag(self, flag: Flag) -> None:
        self.__frame_flags.append(flag)
        self.__frame.set_window_flags(flag.value)
    
    @property
    def height(self) -> int:
        """Returns the height of the Frame.

        Pass a new integer value to update the height.
        """
        return self.__frame.height()

    @height.setter
    def height(self, height: int) -> None:
        self.__frame.set_fixed_height(height)

    @property
    def maximum_height(self) -> int:
        """Returns the Frame maximum height.

        Pass a new integer value to update the maximum height the Frame can 
        have.
        """
        return self.__frame.maximum_height()

    @maximum_height.setter
    def maximum_height(self, height: int) -> None:
        self.__frame.set_maximum_height(height)

    @property
    def maximum_width(self) -> int:
        """Returns the Frame maximum width.

        Pass a new integer value to update the maximum width the Frame can 
        have.
        """
        return self.__frame.maximum_width()

    @maximum_width.setter
    def maximum_width(self, width: int) -> None:
        self.__frame.set_maximum_width(width)

    @property
    def minimum_height(self) -> int:
        """Returns the Frame minimum height.

        Pass a new integer value to update the minimum height the Frame can 
        have.
        """
        return self.__frame.minimum_height()

    @minimum_height.setter
    def minimum_height(self, height: int) -> None:
        self.__frame.set_minimum_height(height)

    @property
    def minimum_width(self) -> int:
        """Returns the Frame minimum width.

        Pass a new integer value to update the minimum width the Frame can 
        have.
        """
        return self.__frame.minimum_width()

    @minimum_width.setter
    def minimum_width(self, width: int) -> None:
        self.__frame.set_minimum_width(width)

    @property
    def style(self) -> dict:
        """Style as dict.

        Get the style as a dictionary or submit a new dictionary style to 
        update it.
        """
        return self.__frame.stylesheet
    
    @style.setter
    def style(self, style: dict) -> None:
        self.__frame.stylesheet = style
        self.__frame.style_change_signal.emit()

    @property
    def width(self) -> int:
        """Returns the Frame width.

        Pass a new integer value to update the width.
        """
        return self.__frame.width()

    @width.setter
    def width(self, width: int) -> int:
        self.__frame.set_fixed_width(width)

    @property
    def _main_parent(self):
        """Main frame of the application.

        Use only to access properties and methods of the Main Frame, defining a 
        new frame will break the application.
        """
        return self.__main_parent
    
    @_main_parent.setter
    def _main_parent(self, parent) -> None:
        self.__main_parent = parent
        self.main_parent_added_signal.emit()

    @property
    def _obj(self):
        """Direct access to Qt classes.

        Warning: Direct access is discouraged and may break the project. 
        This access is considered a hacking for complex Qt implementations, 
        and should only be used for testing and analysis purposes.
        """
        return self.__frame

    @_obj.setter
    def _obj(self, obj: QtWidgets) -> None:
        self.__frame = obj

    def insert(self, item: Widget | Box, index: int = -1) -> Widget | Box:
        """Inserts a Widget or a Box.

        Returns the reference to the inserted item.
        
        :param item: It can be a Widget (Widget, Label, Button...) or a Box.
        :param index: Index number where the item should be inserted 
            (Default is -1)
        """
        _, item = setattr(self, str(item), item), getattr(self, str(item))
        item._main_parent = self

        if isinstance(item, Box):
            self.__frame_box._obj.insert_layout(index, item._obj)
        else:
            item.visible = True
            self.__frame_box._obj.insert_widget(index, item._obj)

        return item

    def move(self, x: int, y: int) -> None:
        """Move the Frame.

        The X and Y positions are relative to the main parent.
        
        :param x: Horizontal position relative to the main parent.
        :param y: Vertical position relative to the main parent.
        """
        self.__frame.move(x, y)

    def show(self) -> None:
        """Renders and displays the Frame."""
        self.__frame.show()

    def signal(self, event: Event) -> Signal:
        """Event Signals.

        Signals are connections to events. When an event such as a mouse click 
        or other event occurs, a signal is sent. The signal can be assigned a 
        function to be executed when the signal is sent.

        :param event:
            Event enumeration (Enum) corresponding to the requested event, 
            such as Event.HOVER_ENTER . All possible names are:
            
            NONE, CLOSE, DRAG, DROP, FOCUS_IN, FOCUS_OUT, MOUSE_BUTTON_PRESS, 
            MOUSE_BUTTON_RELEASE, MOUSE_DOUBLE_CLICK, MOUSE_HOVER_ENTER, 
            MOUSE_HOVER_LEAVE, MOUSE_HOVER_MOVE, MOUSE_RIGHT_BUTTON_PRESS, 
            MOUSE_WHEEL, RESIZE, STATE_CHANGE, TITLE_CHANGE.
        """
        if event == Event.CLOSE:
            return self.__frame.close_signal
        # elif event == Event.DRAG:
        #     return self.__frame.drag_signal
        # elif event == Event.DROP:
        #     return self.__frame.drop_signal
        
        elif event == Event.FOCUS_IN:
            return self.__frame.focus_in_signal
        elif event == Event.FOCUS_OUT:
            return self.__frame.focus_out_signal
        elif event == Event.MOUSE_BUTTON_PRESS:
            return self.__frame.mouse_button_press_signal
        elif event == Event.MOUSE_BUTTON_RELEASE:
            return self.__frame.mouse_button_release_signal
        elif event == Event.MOUSE_DOUBLE_CLICK:
            return self.__frame.mouse_double_click_signal
        elif event == Event.MOUSE_HOVER_ENTER:
            return self.__frame.mouse_hover_enter_signal
        elif event == Event.MOUSE_HOVER_LEAVE:
            return self.__frame.mouse_hover_leave_signal
        elif event == Event.MOUSE_HOVER_MOVE:
            return self.__frame.mouse_hover_move_signal
        elif event == Event.MOUSE_RIGHT_BUTTON_PRESS:
            return self.__frame.mouse_right_button_press_signal
        elif event == Event.MOUSE_WHEEL:
            return self.__frame.mouse_wheel_signal
        elif event == Event.RESIZE:
            return self.__frame.resize_signal
        # elif event == Event.STATE_CHANGE:
        #     return self.__frame.state_change_signal
        # elif event == Event.TITLE_CHANGE:
        #     return self.__frame.title_change_signal

        elif event == Event.STYLE_CHANGE:
            return self.__frame.style_change_signal
        elif event == Event.STYLE_ID_CHANGE:
            return self.__frame.style_id_change_signal
        else:
            return Signal(Event.NONE)

    def style_from_file(self, path: str) -> dict:
        """..."""
        style_file = desktopentryparse.DesktopFile(path)
        return style_file.content

    def __str__(self):
        return f'<Frame: {id(self)}>'
