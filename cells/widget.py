#!/usr/bin/env python3
import logging

from PySide6 import QtWidgets, QtGui
from __feature__ import snake_case

from .align import Align
from .box import Box
from .core.modules import StyleManager
from .event import Event
from .orientation import Orientation
from .signal import Signal


class CoreWidget(QtWidgets.QFrame):
    """Core Widget."""
    def __init__(self, *args, **kwargs):
        """Class constructor."""
        super().__init__(*args, **kwargs)
        self.mouse_button_press_signal = Signal()
        self.mouse_button_release_signal = Signal()
        self.mouse_double_click_signal = Signal()
        self.mouse_hover_enter_signal = Signal()
        self.mouse_hover_leave_signal = Signal()
        self.mouse_hover_move_signal = Signal()

        self.mouse_right_button_press_signal = Signal()
        self.mouse_wheel_signal = Signal()
        self.resize_signal = Signal()
        self.set_object_name('Widget')

    def mouse_press_event(self, e):
        self.mouse_button_press_signal.emit()

    def mouse_release_event(self, e):
        self.mouse_button_release_signal.emit()

    def mouse_double_click_event(self, e):
        self.mouse_double_click_signal.emit()

    def enter_event(self, e):
        self.mouse_hover_enter_signal.emit()

    def leave_event(self, e):
        self.mouse_hover_leave_signal.emit()

    def mouse_move_event(self, e):
        self.mouse_hover_move_signal.emit()


class Widget(object):
    """Widget."""
    def __init__(self, *args, **kwargs) -> None:
        """Class constructor."""


class Widget(Widget):
    """Widget.

    Tip: The base widget is an empty object, with no margins or spacing, and 
    is visually imperceptible, as it does not take up a single pixel. Adding 
    height, width or background color will help to make it noticeable.
    """
    def __init__(
            self,
            main_parent = None,
            orientation: Orientation = Orientation.VERTICAL,
            *args, **kwargs) -> None:
        """Class constructor.

        :main_parent: MainFrame object
        """
        super().__init__(*args, **kwargs)
        # Param
        self.__main_parent = main_parent

        # Signals | TODO: for all properties and methods
        self.__alignment_signal = Signal()
        self.__enabled_change_signal = Signal()
        self.__insert_item_signal = Signal()
        self.__main_parent_added_signal = Signal()
        self.__remove_item_signal = Signal()
        self.__style_change_signal = Signal()
        self.__style_id_change_signal = Signal()

        # Flags
        self.__is_enabled = True
        self.__is_inactive = False
        self.__visible = False  # Hack: Fix aways is False | Box active this

        # Obj
        self.__widget = CoreWidget()
        self.__widget.set_object_name('Widget')
        self.__style_id = 'Widget'

        self.__box = Box(orientation=orientation)
        self.__box.signal(Event.INSERT_ITEM).connect(
            lambda: self.__insert_item_signal.emit())
        self.__box.signal(Event.REMOVE_ITEM).connect(
            lambda: self.self.__remove_item_signal.emit())
        self.__widget.set_layout(self.__box._obj)

        # Style
        self.__style_manager = StyleManager()
        self.__stylesheet = self.__style_manager.stylesheet
        self.__accent = self.__style_manager.accent
        self.__style = {}
        self.__normal_style = None
        self.__hover_style = None
        self.__pressed_style = None
        self.__inactive_style = None
        self.__style_state()
        self.__style_class = 'Accent'
        self.__style_class_saved = None

        # Settings
        self.signal(Event.MOUSE_BUTTON_RELEASE).connect(self.__on_release)
        self.signal(Event.MOUSE_BUTTON_PRESS).connect(self.__on_press)
        self.signal(Event.MOUSE_HOVER_ENTER).connect(self.__on_hover)
        self.signal(Event.MOUSE_HOVER_LEAVE).connect(self.__on_leave)

    @property
    def accent(self) -> str:
        """..."""
        return self.__accent

    @accent.setter
    def accent(self, accent: str) -> None:
        self.__accent = accent

    @property
    def enabled(self) -> bool:
        """Enables the Widget.

        When False, the Widget is inactive both in appearance and in the 
        Event.MOUSE_BUTTON_PRESS and Event.MOUSE_BUTTON_RELEASE events.
        """
        return self.__is_enabled

    @enabled.setter
    def enabled(self, value: bool) -> None:
        self.__is_enabled = value

        if self.__is_enabled:
            self._obj.set_style_sheet(self.__normal_style)
            if hasattr(self._obj, 'mouse_button_press_signal'):
                self._obj.mouse_button_press_signal.connect()
                self._obj.mouse_button_release_signal.connect()
        else:
            self._obj.set_style_sheet(self.__inactive_style)

            if hasattr(self._obj, 'mouse_button_press_signal'):
                self._obj.mouse_button_press_signal.disconnect()
                self._obj.mouse_button_release_signal.disconnect()

        self.__enabled_change_signal.emit()

    @property
    def height(self) -> int:
        """Returns the height of the Widget.

        Pass a new integer value to update the height.
        """
        return self.__widget.height()

    @height.setter
    def height(self, height: int) -> None:
        self.__widget.set_fixed_height(height)

    @property
    def margin(self) -> tuple:
        """Utility to set widget margins using a simple int tuple.

        Will affect all widget states, such as pressed, hover and inactive.

        Note: The Box's 'spacing' property takes precedence over the widget's 
        margins, unless the widget is the only one isolated within a Box. If 
        the Box is vertical, then only the side margins of the widgets will be 
        respected. The Box does not activate the spacing with a single 
        isolated widget.
        """
        m = self.style[f'[{self.style_id}]']['margin'].replace(
            'px', '').split()
        return int(m[0]), int(m[1]), int(m[2]), int(m[3])
    
    @margin.setter
    def margin(self, margin: tuple) -> None:
        for item in margin:
            if not isinstance(item, int):
                logging.error(
                    'The values of the "margin" tuple must be of type "int".')
                return

        for key in self.style.keys():
            self.style[key]['margin'
                ] = f'{margin[0]}px {margin[1]}px {margin[2]}px {margin[3]}px'
        self.style = self.style

    @property
    def maximum_height(self) -> int:
        """Returns the Widget maximum height.

        Pass a new integer value to update the maximum height the Widget can 
        have.
        """
        return self.__widget.maximum_height()

    @maximum_height.setter
    def maximum_height(self, height: int) -> None:
        self.__widget.set_maximum_height(height)

    @property
    def maximum_width(self) -> int:
        """Returns the Widget maximum width.

        Pass a new integer value to update the maximum width the Widget can 
        have.
        """
        return self.__widget.maximum_width()

    @maximum_width.setter
    def maximum_width(self, width: int) -> None:
        self.__widget.set_maximum_width(width)

    @property
    def minimum_height(self) -> int:
        """Returns the Widget minimum height.

        Pass a new integer value to update the minimum height the Widget can 
        have.
        """
        return self.__widget.minimum_height()

    @minimum_height.setter
    def minimum_height(self, height: int) -> None:
        self.__widget.set_minimum_height(height)

    @property
    def minimum_width(self) -> int:
        """Returns the Widget minimum width.

        Pass a new integer value to update the minimum width the Widget can 
        have.
        """
        return self.__widget.minimum_width()

    @minimum_width.setter
    def minimum_width(self, width: int) -> None:
        self.__widget.set_minimum_width(width)

    @property
    def style(self) -> str:
        """Style as dict.

        The style is a 'dict' that goes back to the style INI file. The 
        contents of this file are something like:

            [Widget]
            background=rgba(200, 0, 0, 1.00)
            margin=5px 5px 5px 5px

        So the dictionary will be:

            {'[Widget]': {
                'background': 'rgba(200, 0, 0, 1.00)',
                'margin': '5px 5px 5px 5px',}
            }

        Simply changing the existing dictionary does not update the style, 
        the property actually needs to be updated with a new dictionary:

            new_style = my_widget.style
            new_style['[Widget]']['margin'] = '05px 05px 05px 05px'
            my_widget.style = new_style

        Shortened:

            my_widget.style['[Widget]']['margin'] = '05px 05px 05px 05px'
            my_widget.style = my_widget.style

        Note: The Box's 'spacing' property takes precedence over the widget's 
        margins, unless the widget is the only one isolated within a Box.
        """
        return self.__style

    @style.setter
    def style(self, style: dict) -> None:
        self.__style = style
        self.__style_state()
        self.__style_change_signal.emit()

    @property
    def style_class(self) -> str | None:
        """..."""
        return self.__style_class

    @style_class.setter
    def style_class(self, value: str) -> None:
        self.__style_class = value
        if self._main_parent:
            if not self.__style_class_saved:
                style = {
                    f'[{self.style_id}]': self.style[
                        f'[{self.style_id}]'],
                    f'[{self.style_id}:hover]': self.style[
                        f'[{self.style_id}:hover]'],
                    f'[{self.style_id}:pressed]': self.style[
                        f'[{self.style_id}:pressed]'],
                    f'[{self.style_id}:inactive]': self.style[
                        f'[{self.style_id}:inactive]']}
                self.__style_class_saved = style

            if (self.__style_class and
                    f'[{self.__style_class}]' in self._main_parent.style):
                self.style = {
                    f'[{self.style_id}]': self._main_parent.style[
                        f'[{self.__style_class}]'],
                    f'[{self.style_id}:hover]': self._main_parent.style[
                        f'[{self.__style_class}:hover]'],
                    f'[{self.style_id}:pressed]': self._main_parent.style[
                        f'[{self.__style_class}:pressed]'],
                    f'[{self.style_id}:inactive]': self._main_parent.style[
                        f'[{self.__style_class}:inactive]']}
            else:
                if self.__style_class_saved:
                    self.style = self.__style_class_saved
                    self.__style_class_saved = None

    @property
    def style_id(self) -> str:
        """Style ID.

        An ID allows you to define a unique style that does not distort 
        parent objects of the same type that inherit from the class.

        Send a string with a unique ID to set the style for this Widget only.
        """
        return self.__style_id

    @style_id.setter
    def style_id(self, style_id: str) -> None:
        # In order
        new_style = {
            f'[{style_id}]':
                self.__stylesheet[f'[{self.__style_id}]'],
            f'[{style_id}:inactive]':
                self.__stylesheet[f'[{self.__style_id}:inactive]'],
            f'[{style_id}:hover]':
                self.__stylesheet[f'[{self.__style_id}:hover]'],
            f'[{style_id}:pressed]':
                self.__stylesheet[f'[{self.__style_id}:pressed]']}

        self.__widget.set_object_name(style_id)
        self.__style_id = style_id

        self.__style = new_style
        self.__style_state()

        self.__style_id_change_signal.emit()

    @property
    def visible(self) -> bool:
        """Widget Visibility.

        Qt has minor issues when calculating pixels to render areas that are 
        repeatedly hidden and visible, so clearly define the sizes and spacing 
        to avoid minor visual discomforts.
        """
        return self.__visible

    @visible.setter
    def visible(self, value: bool) -> None:
        self.__visible = value
        self.__widget.set_visible(value)

    @property
    def width(self) -> int:
        """Returns the Widget width.

        Pass a new integer value to update the width.
        """
        return self.__widget.width()

    @width.setter
    def width(self, width: int) -> int:
        self.__widget.set_fixed_width(width)

    @property
    def _main_parent(self):
        """Main frame of the application.

        Use only to access properties and methods of the Main Frame, defining 
        a new frame will break the application.
        """
        return self.__main_parent
    
    @_main_parent.setter
    def _main_parent(self, parent) -> None:
        self.__main_parent = parent
        self.__on_main_added()
        self.__main_parent_added_signal.emit()

    @property
    def _obj(self):
        """Direct access to Qt classes.

        Warning: Direct access is discouraged and may break the project. 
        This access is considered a hacking for complex Qt implementations, 
        and should only be used for testing and analysis purposes.
        """
        return self.__widget

    @_obj.setter
    def _obj(self, obj: QtWidgets) -> None:
        self.__widget = obj

    def insert(self, item: Widget | Box, index: int = -1) -> Widget | Box:
        """Inserts a Widget or a Box.

        Returns the reference to the inserted item.
        
        :param item: It can be a Widget (Widget, Label, Button...) or a Box.
        :param index: Index number where the item should be inserted 
            (Default is -1)
        """
        _, item = setattr(self, str(item), item), getattr(self, str(item))
        if self.__main_parent:
            item._main_parent = self.__main_parent

        if isinstance(item, Box):
            self.__box._obj.insert_layout(index, item._obj)
        else:
            item.style_id = item.style_id
            item.visible = True
            self.__box._obj.insert_widget(index, item._obj)

        return item

    def move(self, x: int, y: int) -> None:
        """Move the Widget.

        The X and Y positions are relative to the main parent.
        
        :param x: Horizontal position relative to the main parent.
        :param y: Vertical position relative to the main parent.
        """
        self.__widget.move(x, y)

    def signal(self, event: Event) -> Signal:
        """Event Signals.

        Signals are connections to events. When an event such as a mouse 
        click or other event occurs, a signal is sent. The signal can be 
        assigned a function to be executed when the signal is sent.

        :param event:
            Event enumeration (Enum) corresponding to the requested event, 
            such as Event.HOVER_ENTER . All possible names are:
            
            NONE, MOUSE_BUTTON_PRESS, MOUSE_BUTTON_RELEASE, 
            MOUSE_DOUBLE_CLICK, MOUSE_HOVER_ENTER, MOUSE_HOVER_LEAVE, 
            MOUSE_HOVER_MOVE, MOUSE_RIGHT_BUTTON_PRESS, MOUSE_WHEEL, RESIZE, 
            STYLE_CHANGE, STYLE_ID_CHANGE.
        """
        if event == Event.MOUSE_BUTTON_PRESS:
            return self.__widget.mouse_button_press_signal
        elif event == Event.MOUSE_BUTTON_RELEASE:
            return self.__widget.mouse_button_release_signal
        elif event == Event.MOUSE_DOUBLE_CLICK:
            return self.__widget.mouse_double_click_signal
        elif event == Event.MOUSE_HOVER_ENTER:
            return self.__widget.mouse_hover_enter_signal
        elif event == Event.MOUSE_HOVER_LEAVE:
            return self.__widget.mouse_hover_leave_signal
        elif event == Event.MOUSE_HOVER_MOVE:
            return self.__widget.mouse_hover_move_signal
        # elif event == Event.MOUSE_RIGHT_BUTTON_PRESS:
        #     return self.__widget.mouse_right_button_press_signal
        elif event == Event.MOUSE_WHEEL:
            return self.__widget.mouse_wheel_signal
        elif event == Event.RESIZE:
            return self.__widget.resize_signal

        # self.__widget -> self
        elif event == Event.ALIGNMENT_CHANGE:
            return self.__alignment_signal
        elif event == Event.ENABLED_CHANGE:
            return self.__enabled_change_signal
        elif event == Event.INSERT_ITEM:
            return self.__insert_item_signal
        elif event == Event.MAIN_PARENT_ADDED:
            return self.__main_parent_added_signal
        elif event == Event.REMOVE_ITEM:
            return self.__remove_item_signal
        elif event == Event.STYLE_CHANGE:
            return self.__style_change_signal
        elif event == Event.STYLE_ID_CHANGE:
            return self.__style_id_change_signal
        else:
            return Signal(Event.NONE)

    def __focus_in(self) -> None:
        self.__is_inactive = False
        if self.__is_enabled:
            self._obj.set_style_sheet(self.__normal_style)

    def __focus_out(self) -> None:
        self.__is_inactive = True
        if self.__is_enabled:
            self._obj.set_style_sheet(self.__inactive_style)

    def __on_hover(self) -> None:
        if not self.__is_inactive and self.__is_enabled:
                self._obj.set_style_sheet(self.__hover_style)

    def __on_leave(self) -> None:
        # self._obj.set_style_sheet('')
        # self.__label._obj.set_style_sheet('')

        # if self.__is_inactive:
        #     self.__focus_out()
        # else:
        #     self._obj.set_style_sheet(self.__normal_style)
        if not self.__is_inactive and self.__is_enabled:
            self._obj.set_style_sheet(self.__normal_style)

    def __on_main_added(self) -> None:
        self.__main_parent.signal(Event.FOCUS_IN).connect(self.__focus_in)
        self.__main_parent.signal(Event.FOCUS_OUT).connect(self.__focus_out)
        for item in self.__box.items():
            if not item._main_parent:
                item._main_parent = self._main_parent

    def __on_press(self) -> None:
        if self.__is_enabled:
            self.__widget.set_style_sheet(self.__pressed_style)

    def __qss_piece(
            self,
            style: dict = None,
            state: str = '',
            inactive: bool = False) -> str:
        return self.__style_manager.style_to_qss(
            {
                f'[{self.style_id}{state}]':
                style[f'[{self.style_id}{state}]']
            },
            inactive=inactive).split('{')[1].replace('}', '').strip()

    def __on_release(self) -> None:
        if not self.__is_inactive and self.__is_enabled:
            self._obj.set_style_sheet(self.__hover_style)

    def __style_state(self) -> None:
        if not self.__style:
            self.__style[f'[{self.__style_id}]'] = self.__stylesheet[
                f'[{self.__style_id}]']
            self.__style[f'[{self.__style_id}:hover]'] = self.__stylesheet[
                f'[{self.__style_id}:hover]']
            self.__style[f'[{self.__style_id}:pressed]'] = self.__stylesheet[
                f'[{self.__style_id}:pressed]']
            self.__style[f'[{self.__style_id}:inactive]'] = self.__stylesheet[
                f'[{self.__style_id}:inactive]']

        self.__normal_style = self.__qss_piece(self.__style)
        self.__hover_style = self.__qss_piece(self.__style, ':hover')
        self.__pressed_style = self.__qss_piece(self.__style, ':pressed')
        self.__inactive_style = self.__qss_piece(
            self.__style, ':inactive', True)

        self.__widget.set_style_sheet(self.__normal_style)

    def __str__(self):
        return f'<Widget: {id(self)}>'
