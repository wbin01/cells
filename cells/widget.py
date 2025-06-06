#!/usr/bin/env python3
import logging

from PySide6 import QtWidgets, QtCore
from __feature__ import snake_case

from .align import Align
from .box import Box
from .core.modules import StyleManager
from .event import Event
from .orientation import Orientation
from .signal import Signal


class CoreWidget(QtWidgets.QFrame):
    """Core Widget.

    # Internal control!
    """
    def __init__(self, *args, **kwargs):
        """Class constructor."""
        super().__init__(*args, **kwargs)
        # self.set_mouse_tracking(True)
        self.set_object_name('Widget')
        self.mouse_press_signal = Signal()
        self.mouse_release_signal = Signal()
        self.mouse_double_click_signal = Signal()
        self.mouse_hover_enter_signal = Signal()
        self.mouse_hover_leave_signal = Signal()
        self.mouse_hover_move_signal = Signal()
        self.mouse_right_press_signal = Signal()
        self.mouse_wheel_signal = Signal()
        self.size_signal = Signal()

        self.install_event_filter(self)

    def event_filter(
            self, watched: QtCore.QObject, event: QtCore.QEvent) -> bool:
        # if event.type() == QtCore.QEvent.FocusIn:
        #     self.focus_in_signal.emit()

        # elif event.type() == QtCore.QEvent.FocusOut:
        #     self.focus_out_signal.emit()

        if event.type() == QtCore.QEvent.HoverMove:
            self.mouse_hover_move_signal.emit()

        elif event.type() == QtCore.QEvent.Type.HoverEnter:
            self.mouse_hover_enter_signal.emit()

        elif event.type() == QtCore.QEvent.Type.HoverLeave:
            self.mouse_hover_leave_signal.emit()

        elif event.type() == QtCore.QEvent.MouseButtonPress:
            if 'RightButton' in event.__str__():
                self.mouse_right_press_signal.emit()
            else:
                self.mouse_press_signal.emit()

        elif event.type() == QtCore.QEvent.MouseButtonRelease:
            self.mouse_release_signal.emit()

        elif event.type() == QtCore.QEvent.MouseButtonDblClick:
            self.mouse_double_click_signal.emit()

        elif event.type() == QtCore.QEvent.Wheel:
            self.mouse_wheel_signal.emit()

        elif event.type() == QtCore.QEvent.Resize:
            self.size_signal.emit()

        elif event.type() == QtCore.QEvent.Close:
            self.close_signal.emit()

        return QtWidgets.QMainWindow.event_filter(self, watched, event)

class Widget(object):
    """Widget.

    # Internal control!
    """
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

        # Obj
        self.__widget = CoreWidget()
        self.__widget.set_object_name('Widget')
        self.__widget.set_contents_margins(0, 0, 0, 0)
        self.__style_id = 'Widget'

        self.__box = Box(orientation=orientation)
        self.__widget.set_layout(self.__box._obj)

        # Signals
        self.__signals = {
            Event.DELETE: self.__box.signal(Event.DELETE),
            Event.ENABLED: Signal(),
            Event.INSERT: self.__box.signal(Event.INSERT),
            Event.MAIN_PARENT: Signal(),
            Event.MOUSE_PRESS: self.__widget.mouse_press_signal,
            Event.MOUSE_RELEASE: self.__widget.mouse_release_signal,
            Event.MOUSE_DOUBLE_PRESS: self.__widget.mouse_double_click_signal,
            Event.MOUSE_HOVER_ENTER: self.__widget.mouse_hover_enter_signal,
            Event.MOUSE_HOVER_LEAVE: self.__widget.mouse_hover_leave_signal,
            Event.MOUSE_HOVER_MOVE: self.__widget.mouse_hover_move_signal,
            Event.MOUSE_RIGHT_PRESS: self.__widget.mouse_right_press_signal,
            Event.MOUSE_WHEEL: self.__widget.mouse_wheel_signal,
            Event.REMOVE: self.__box.signal(Event.REMOVE),
            Event.SIZE: self.__widget.size_signal,
            Event.STATE: Signal(),
            Event.STYLE: Signal(),
            Event.STYLE_CLASS: Signal(),
            Event.STYLE_ID: Signal()}

        # Flags
        self.__is_enabled = True
        self.__is_inactive = False
        self.__visible = False

        # Style
        self.__state = None
        self.__style_manager = StyleManager()
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
        self.signal(Event.MOUSE_RELEASE).connect(self.__on_release)
        self.signal(Event.MOUSE_PRESS).connect(self.__on_press)
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
    def align(self) -> Align:
        """Align enum.

        Sets the Box alignment.
        """
        return self.__box.align

    @align.setter
    def align(self, align: Align) -> None:
        self.__box.align = align

    @property
    def enabled(self) -> bool:
        """Enables the Widget.

        When False, the Widget is inactive both in appearance and in the 
        Event.MOUSE_PRESS and Event.MOUSE_RELEASE events.
        """
        return self.__is_enabled

    @enabled.setter
    def enabled(self, value: bool) -> None:
        self.__is_enabled = value
        if self.__is_enabled:
            self._obj.set_style_sheet(self.__normal_style)

            if hasattr(self._obj, 'mouse_press_signal'):
                self._obj.mouse_press_signal.connect()
                self._obj.mouse_release_signal.connect()
        else:
            self._obj.set_style_sheet(self.__inactive_style)
            
            if hasattr(self._obj, 'mouse_press_signal'):
                self._obj.mouse_press_signal.disconnect()
                self._obj.mouse_release_signal.disconnect()

        self.__signals[Event.ENABLED].emit()

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
    def max_height(self) -> int:
        """Returns the Widget maximum height.

        Pass a new integer value to update the maximum height the Widget can 
        have.
        """
        return self.__widget.maximum_height()

    @max_height.setter
    def max_height(self, height: int) -> None:
        self.__widget.set_maximum_height(height)

    @property
    def max_width(self) -> int:
        """Returns the Widget maximum width.

        Pass a new integer value to update the maximum width the Widget can 
        have.
        """
        return self.__widget.maximum_width()

    @max_width.setter
    def max_width(self, width: int) -> None:
        self.__widget.set_maximum_width(width)

    @property
    def min_height(self) -> int:
        """Returns the Widget minimum height.

        Pass a new integer value to update the minimum height the Widget can 
        have.
        """
        return self.__widget.minimum_height()

    @min_height.setter
    def min_height(self, height: int) -> None:
        self.__widget.set_minimum_height(height)

    @property
    def min_width(self) -> int:
        """Returns the Widget minimum width.

        Pass a new integer value to update the minimum width the Widget can 
        have.
        """
        return self.__widget.minimum_width()

    @min_width.setter
    def min_width(self, width: int) -> None:
        self.__widget.set_minimum_width(width)

    @property
    def spacing(self) -> int:
        """
        The space between widgets inside the Widget box.

        This property takes precedence over the margins of the widgets that 
        are added (add_widgets), so if the Box is vertical, then only the side 
        margins of the widgets will be respected. The Box does not activate 
        the spacing with a single isolated widget.
        """
        return self.__box.spacing

    @spacing.setter
    def spacing(self, spacing: int) -> None:
        self.__box.spacing = spacing

    @property
    def state(self) -> str:
        """..."""
        return self.__state

    @state.setter
    def state(self, state: str = None) -> None:
        self.__state = state
        state = '' if not state else ':' + state

        if not self._main_parent:
            return

        if not self.__state:
            style = self.__normal_style
        elif self.__state == 'hover':
            style = self.__hover_style
        elif self.__state == 'pressed':
            style = self.__pressed_style
        else:
            style = self.__inactive_style

        self._obj.set_style_sheet(style)
        self.__signals[Event.STATE].emit()

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
        self.__signals[Event.STYLE].emit()

    @property
    def style_class(self) -> str | None:
        """Changes the style to that of the desired class.
        
        Use appropriate generic classes, such as 'Success', 'Danger', 
        'Warning' and 'Accent'.
        
            my_button.style_class = 'Danger'
        
        Use None to reset.

        The style class will only be changed if the Widget already contains a 
        _main_parent (The 'add' method automatically sets the _main_parent).
        """
        return self.__style_class

    @style_class.setter
    def style_class(self, value: str) -> None:
        if self._main_parent:
            self.__style_class = value

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
                style = {
                    f'[{self.style_id}]': self._main_parent.style[
                        f'[{self.__style_class}]'],
                    f'[{self.style_id}:hover]': self._main_parent.style[
                        f'[{self.__style_class}:hover]'],
                    f'[{self.style_id}:pressed]': self._main_parent.style[
                        f'[{self.__style_class}:pressed]'],
                    f'[{self.style_id}:inactive]': self._main_parent.style[
                        f'[{self.__style_class}:inactive]']}
                self.style = style
            else:
                if self.__style_class_saved:
                    self.style = self.__style_class_saved
                    self.__style_class_saved = None

            self.__signals[Event.STYLE_CLASS].emit()

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
        style_id_key = f'[{style_id}]'
        if self._main_parent and style_id_key in self._main_parent.style:
            stylesheet = self._main_parent.style
        # elif style_id_key in self.__stylesheet:
        #     stylesheet = self.__stylesheet
        else:
            stylesheet = self.style

        new_style = {
            f'[{style_id}]':
                stylesheet[f'[{self.__style_id}]'],
            f'[{style_id}:inactive]':
                stylesheet[f'[{self.__style_id}:inactive]'],
            f'[{style_id}:hover]':
                stylesheet[f'[{self.__style_id}:hover]'],
            f'[{style_id}:pressed]':
                stylesheet[f'[{self.__style_id}:pressed]']}

        self.__widget.set_object_name(style_id)
        self.__style_id = style_id

        self.__style = new_style
        self.__style_state()

        self.__style_class_saved = new_style

        self.__signals[Event.STYLE_ID].emit()

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

    # @property
    # def _box(self) -> Box:
    #     """Direct access to Box Layout of this widget.
    #
    #     Warning: Direct access is discouraged and may break the project. 
    #     This access is considered a hacking for complex Qt implementations, 
    #     and should only be used for testing and analysis purposes.
    #     """
    #     return self.__box
    #
    # @_box.setter
    # def _box(self, box: Box) -> None:
    #     self.__box = box
    #
    @_main_parent.setter
    def _main_parent(self, parent) -> None:
        if parent:
            self.__main_parent = parent
            self.__main_parent.signal(Event.FOCUS_IN).connect(
                self.__on_focus_in)
            self.__main_parent.signal(Event.FOCUS_OUT).connect(
                self.__on_focus_out)

            for item in self.__box.items():
                if not item._main_parent:
                    item._main_parent = self.__main_parent

            self.__signals[Event.MAIN_PARENT].emit()

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

    def add(self, item: Widget | Box, index: int = -1) -> Widget | Box:
        """Inserts a Widget or a Box.

        Returns the reference to the added item.
        
        :param item: It can be a Widget (Widget, Label, Button...) or a Box.
        :param index: Index number where the item should be added 
            (Default is -1)
        """
        item._main_parent = self._main_parent
        self.__box.add(item)
        return item

    def delete(self, item: Widget | Box) -> None:
        """Delete a Widget or a Box.

        When an item is deleted, the reference to it no longer exists. Using 
        the old variable for this item causes an error. In order to use the 
        old variable, the item will need to be instantiated again.

        :param item: A Widget (Widget, Label, Button...) or a Box.
        """
        self.__box.delete(item)

    def events_available_for_signal(self) -> str:
        """String with all available events."""
        return ', '.join([f'Event.{x.value}' for x in self.__signals.keys()])

    def items(self) -> list:
        """List with added widgets."""
        return self.__box.items

    def move(self, x: int, y: int) -> None:
        """Move the Widget.

        The X and Y positions are relative to the main parent.
        
        :param x: Horizontal position relative to the main parent.
        :param y: Vertical position relative to the main parent.
        """
        self.__widget.move(x, y)

    def remove(self, item: Widget | Box) -> None:
        """Removes a Widget or a Box.

        This only removes the widget, but does not delete it. The variable 
        referring to it still works and can be added again later. To 
        completely delete the widget from the variable, use the 'delete()' 
        method.

        :param item: A Widget (Widget, Label, Button...) or a Box.
        """
        self.__box.remove(item)

    def signal(self, event: Event) -> Signal:
        """Event Signals.

        Signals are connections to events. When an event such as a mouse 
        click (Event.MOUSE_PRESS) or other event occurs, a signal is sent. The 
        signal can be assigned a function to be executed when the signal is 
        sent.

        Use the 'events_available_for_signal()' method to see all available 
        events.

        :param event:
            Event enumeration (Enum) corresponding to the requested event, 
            such as Event.HOVER_ENTER. See: events_available_for_signal().
        """
        if event in self.__signals:
            return self.__signals[event]

    def __on_focus_in(self) -> None:
        self.__is_inactive = False
        if self.__is_enabled:
            self._obj.set_style_sheet(self.__normal_style)

    def __on_focus_out(self) -> None:
        self.__is_inactive = True
        if self.__is_enabled:
            self._obj.set_style_sheet(self.__inactive_style)

    def __on_hover(self) -> None:
        if not self.__is_inactive and self.__is_enabled:
            self._obj.set_style_sheet(self.__hover_style)

    def __on_leave(self) -> None:
        # self._obj.set_style_sheet('')
        # self.__label._obj.set_style_sheet('')
        if not self.__is_inactive and self.__is_enabled:
            self._obj.set_style_sheet(self.__normal_style)

    def __on_press(self) -> None:
        if self.__is_enabled:
            self.__widget.set_style_sheet(self.__pressed_style)

    def __on_release(self) -> None:
        if not self.__is_inactive and self.__is_enabled:
            self._obj.set_style_sheet(self.__hover_style)

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

    def __style_state(self) -> None:
        if not self.__style and self.__main_parent:
            self.__style = self.__main_parent.style

        if not self.__style:
            base = {
                'background': 'rgba(0, 0, 0, 0.0)',
                'color': 'rgba(0, 0, 0, 0.0)',
                'border': '1px rgba(0, 0, 0, 0.0)',
                'border_bottom': '0px rgba(0, 0, 0, 0.0)',
                'border_radius': '0px',
                'padding': '0px',
                'margin': '0px'}
            self.__style[f'[{self.__style_id}]'] = base
            self.__style[f'[{self.__style_id}:hover]'] = base
            self.__style[f'[{self.__style_id}:pressed]'] = base
            self.__style[f'[{self.__style_id}:inactive]'] = base

        self.__normal_style = self.__qss_piece(self.__style)
        self.__hover_style = self.__qss_piece(self.__style, ':hover')
        self.__pressed_style = self.__qss_piece(self.__style, ':pressed')
        self.__inactive_style = self.__qss_piece(
            self.__style, ':inactive', True)

        self.__widget.set_style_sheet(self.__normal_style)

    def __str__(self):
        return f'<Widget: {id(self)}>'
