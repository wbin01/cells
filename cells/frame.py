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
    def alignment(self) -> Align:
        """Alignment enum.

        Sets the alignment of the Box.
        """
        return self.__frame_box._obj.alignment()

    @alignment.setter
    def alignment(self, alignment: Align) -> None:
        self.__frame_box._obj.set_alignment(alignment.value)

    @property
    def flags(self) -> list:
        """..."""
        return self.__frame_flags

    @flags.setter
    def flags(self, flags: list) -> None:
        """..."""
        for flag in flags:
            if flag not in self.__frame_flags:
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

    def add_box(self, box: Box) -> Box:
        """..."""
        box._main_parent = self
        _, box = setattr(self, str(box), box), getattr(self, str(box))
        self.__frame_box.add_box(box)
        return box

    def add_widget(self, widget: Widget) -> Widget:
        """..."""
        widget._main_parent = self
        _, widget = setattr(self, str(widget), widget), getattr(
            self, str(widget))
        self.__frame_box.add_widget(widget)
        return widget

    def move(self, x: int, y: int) -> None:
        """..."""
        # cc = QtGui.QCursor()
        # cc.pos()
        # eve=QtGui.QContextMenuEvent(QtGui.QContextMenuEvent.Mouse, cc.pos())
        # pos = self.__frame.map_to_global(event.pos())
        # self.__frame.move(pos.x(), pos.y())
        self.__frame.move(x, y)

    def show(self) -> None:
        # Starts the main loop
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
