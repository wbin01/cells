#!/usr/bin/env python3
import os
import platform

from PySide6 import QtWidgets
from __feature__ import snake_case

from .align import Align
from .box import Box
from .core import CoreMainFrame
from .event import Event
from .flag import Flag
from .icon import Icon
from .core.modules import IniParse
from .orientation import Orientation
from .signal import Signal
from .widget import Widget


class MainFrame(object):
    """Main frame.
    
    That is, the main application window.
    """
    def __init__(
            self,
            orientation: Orientation = Orientation.VERTICAL,
            *args, **kwargs) -> None:
        """Class constructor."""
        super().__init__(*args, **kwargs)
        # Param
        self.__frame_flags = []
        self.__frame = CoreMainFrame()
        self.__frame_box = Box(orientation=orientation)
        self.__frame_box._main_parent = self
        self.__frame.central_widget().set_layout(self.__frame_box._obj)

        # Signals
        self.__signals = {
            Event.CLOSE: self.__frame.close_signal,
            Event.FOCUS_IN: self.__frame.focus_in_signal,
            Event.FOCUS_OUT: self.__frame.focus_out_signal,
            Event.DELETE: self.__frame_box.signal(Event.DELETE),
            Event.INSERT: self.__frame_box.signal(Event.INSERT),
            Event.MOUSE_DOUBLE_PRESS: self.__frame.mouse_double_click_signal,
            Event.MOUSE_HOVER_ENTER: self.__frame.mouse_hover_enter_signal,
            Event.MOUSE_HOVER_LEAVE: self.__frame.mouse_hover_leave_signal,
            Event.MOUSE_HOVER_MOVE: self.__frame.mouse_hover_move_signal,
            Event.MOUSE_PRESS: self.__frame.mouse_press_signal,
            Event.MOUSE_RELEASE: self.__frame.mouse_release_signal,
            Event.MOUSE_RIGHT_PRESS: self.__frame.mouse_r_press_signal,
            Event.MOUSE_WHEEL: self.__frame.mouse_wheel_signal,
            Event.REMOVE: self.__frame_box.signal(Event.REMOVE),
            Event.SIZE: self.__frame.size_signal,
            Event.STATE: self.__frame.state_signal,
            Event.TITLE: self.__frame.title_signal,
            Event.STYLE: Signal(),
            Event.STYLE_ID: Signal()}
            # rm ENABLED, MAIN_PARENT, STYLE_CLASS

        # Style
        self.__icon = None
        self.__icon_path = None
        self.__user_settings()

    @property
    def align(self) -> Align:
        """Alignment enum.

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
        # https://doc.qt.io/qtforpython-6/PySide6/QtCore/Qt.html
        # #PySide6.QtCore.Qt.WindowType
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
    def icon(self) -> Icon:
        """Frame icon.
        
        Application Icon.
        """
        return self.__icon

    @icon.setter
    def icon(self, path: str) -> None:
        self.__icon = Icon(path)
        self.__frame.set_window_icon(self.__icon._obj)

    @property
    def fullscreen(self) -> bool:
        """If the Frame is full screen.

        Use a boolean value to change the state of the Frame.
        """
        return self.__frame.is_full_screen()

    @fullscreen.setter
    def fullscreen(self, value: bool) -> None:
        if value:
            self.__frame.show_full_screen()
        else:
            self.__frame.show_normal()

    @property
    def maximized(self) -> bool:
        """If the Frame is maximized.

        Use a boolean value to change the state of the Frame.
        """
        return self.__frame.is_maximized()

    @maximized.setter
    def maximized(self, value: bool) -> None:
        if value:
            self.__frame.show_maximized()
        else:
            self.__frame.show_normal()

    @property
    def minimized(self) -> bool:
        """If the Frame is minimized.

        Use a boolean value to change the state of the Frame.
        """
        return self.__frame.is_minimized()

    @minimized.setter
    def minimized(self, value: bool) -> None:
        if value:
            self.__frame.show_minimized()
        else:
            self.__frame.show_normal()

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
    def spacing(self) -> int:
        """
        The space between widgets inside the Frame box.

        This property takes precedence over the margins of the widgets that 
        are added (add_widgets), so if the Box is vertical, then only the side 
        margins of the widgets will be respected. The Box does not activate 
        the spacing with a single isolated widget.
        """
        return self.__frame_box.spacing

    @spacing.setter
    def spacing(self, spacing: int) -> None:
        self.__frame_box.spacing = spacing

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
        self.__signals[Event.STYLE].emit()

    @property
    def title(self) -> str:
        """Returns the Frame title.

        Pass a new integer value to update the title.
        """
        return self.__frame.window_title()
    
    @title.setter
    def title(self, title: str) -> None:
        self.__frame.set_window_title(title)

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

    def delete(self, item: Widget | Box) -> None:
        """Delete a Widget or a Box.

        When an item is deleted, the reference to it no longer exists. Using 
        the old variable for this item causes an error. In order to use the 
        old variable, the item will need to be instantiated again.

        :param item: A Widget (Widget, Label, Button...) or a Box.
        """
        self.__frame_box.delete(item)

    def events_available_for_signal(self) -> str:
        """String with all available events."""
        return ', '.join([f'Event.{x.value}' for x in self.__signals.keys()])

    def insert(self, item: Widget | Box, index: int = -1) -> Widget | Box:
        """Inserts a Widget or a Box.

        Returns the reference to the inserted item.
        
        :param item: It can be a Widget (Widget, Label, Button...) or a Box.
        :param index: Index number where the item should be inserted 
            (Default is -1)
        """
        self.__frame_box.insert(item)
        return item

    def remove(self, item: Widget | Box) -> None:
        """Removes a Widget or a Box.

        This only removes the widget, but does not delete it. The variable 
        referring to it still works and can be inserted again later. To 
        completely delete the widget from the variable, use the 'delete()' 
        method.

        :param item: A Widget (Widget, Label, Button...) or a Box.
        """
        self.__frame_box.remove(item)

    def show(self) -> None:
        """Show the frame."""
        self.__frame.show()

    def signal(self, event: Event) -> Signal:
        """Event Signals.

        Signals are connections to events. When an event such as a mouse 
        click (Event.MOUSE_PRESS) or other event occurs, a signal is 
        sent. The signal can be assigned a function to be executed when the 
        signal is sent.

        Use the 'events_available_for_signal()' method to see all available 
        events.

        :param event:
            Event enumeration (Enum) corresponding to the requested event, 
            such as Event.HOVER_ENTER. See: events_available_for_signal().
        """
        if event in self.__signals:
            return self.__signals[event]

    def style_from_file(self, path: str) -> dict:
        """Convert the contents of a file into a valid dictionary style."""
        ini = IniParse(path)
        self.style.update(ini.content)
        self.style = self.style

    def __user_settings(self) -> None:
        static_url = os.path.join(
            os.path.expanduser('~user'), '.config', 'cells', 'static')

        if os.name == 'posix' and platform.system() == 'Linux':
            os.makedirs(static_url, exist_ok=True)
            home_style = os.path.join(static_url, 'stylerc')

            if os.path.isfile(home_style):
                self.style_from_file(home_style)

    def __str__(self):
        return f'<MainFrame: {id(self)}>'
