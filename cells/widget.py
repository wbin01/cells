#!/usr/bin/env python3
from PySide6 import QtWidgets
from __feature__ import snake_case

from .core import CoreWidget
from .core.modules import StyleManager
from .event import Event
from .signal import Signal


class Widget(object):
    """Widget."""
    def __init__(self, *args, **kwargs) -> None:
        """Class constructor."""


class Widget(Widget):
    """Widget."""
    def __init__(self, *args, **kwargs) -> None:
        """Class constructor."""
        super().__init__(*args, **kwargs)
        self.style_change_signal = Signal()
        self.style_id_change_signal = Signal()
        self.main_parent_added = Signal()

        self.__widget = CoreWidget()
        self.__main_parent = None

        self.__box = QtWidgets.QVBoxLayout()
        self.__widget.set_layout(self.__box)

        self.__style_manager = StyleManager()
        self.__normal_style = self.__get_qss_style()
        self.__hover_style = self.__get_qss_style(':hover')
        self.__pressed_style = self.__get_qss_style(':pressed')
        self.__inactive_style = self.__get_qss_style(':inactive', True)

        self._is_inactive = False

        self.event_signal(Event.MAIN_PARENT_ADDED).connect(self.__main_added)
        self.event_signal(Event.MOUSE_BUTTON_PRESS).connect(self.__press)
        self.event_signal(Event.MOUSE_BUTTON_RELEASE).connect(self.__release)
        self.event_signal(Event.MOUSE_HOVER_ENTER).connect(self.__hover)
        self.event_signal(Event.MOUSE_HOVER_LEAVE).connect(self.__leave)

    @property
    def style(self) -> str:
        """..."""
        if self.__main_parent:
            return self.__main_parent.style
        return None

    @style.setter
    def style(self, style: dict) -> None:
        self.style_change_signal.emit()
        self.__main_parent.style = style
        # self.__main_parent.event_signal(
        #     Event.STYLE_CHANGE).connect(self.__create_new_style)

    @property
    def style_id(self) -> str:
        """Style ID.

        An ID allows you to define a unique style that does not distort parent 
        objects of the same type that inherit from the class.

        Send a string with a unique ID to set the style for this Widget only.
        """
        return self.__widget.object_name()

    @style_id.setter
    def style_id(self, style_id: str) -> None:
        self.style_id_change_signal.emit()
        self.__widget.set_object_name(style_id)
        if self.__main_parent:
                self.__create_new_style()

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
        self.main_parent_added.emit()

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

    def add_box(self, box) -> None:
        """Add a Box inside this Widget"""
        box._main_parent = self._main_parent
        self.__box.add_layout(box._obj)

    def add_widget(self, widget: Widget) -> None:
        """Add a new Widget inside this Widget"""
        widget.main_parent = self._main_parent
        self.__box.add_widget(widget._obj)

    def event_signal(self, event: Event) -> Signal:
        """Event Signals.

        Signals are connections to events. When an event such as a mouse click 
        or other event occurs, a signal is sent. The signal can be assigned a 
        function to be executed when the signal is sent.

        :param event:
            Event enumeration (Enum) corresponding to the requested event, 
            such as Event.HOVER_ENTER . All possible names are:
            
            NONE, MOUSE_BUTTON_PRESS, MOUSE_BUTTON_RELEASE, MOUSE_DOUBLE_CLICK, 
            MOUSE_HOVER_ENTER, MOUSE_HOVER_LEAVE, MOUSE_HOVER_MOVE, 
            MOUSE_RIGHT_BUTTON_PRESS, MOUSE_WHEEL, RESIZE, STYLE_CHANGE,
            STYLE_ID_CHANGE.
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

        # TODO
        elif event == Event.MOUSE_RIGHT_BUTTON_PRESS:
            return self.__widget.mouse_right_button_press_signal
        elif event == Event.MOUSE_WHEEL:
            return self.__widget.mouse_wheel_signal
        elif event == Event.RESIZE:
            return self.__widget.resize_signal

        # self.__widget -> self
        elif event == Event.MAIN_PARENT_ADDED:
            return self.main_parent_added
        elif event == Event.STYLE_CHANGE:
            return self.style_change_signal
        elif event == Event.STYLE_ID_CHANGE:
            return self.style_id_change_signal
        else:
            return Signal(Event.NONE)

    def __create_new_style(self) -> None:
        self.__main_parent.style[f'[{self.style_id}]'] = self.__main_parent.style[
            '[Widget]']
        self.__main_parent.style[f'[{self.style_id}:inactive]'] = self.__main_parent.style[
            '[Widget:inactive]']
        self.__main_parent.style[f'[{self.style_id}:hover]'] = self.__main_parent.style[
            '[Widget:hover]']
        self.__main_parent.style[f'[{self.style_id}:pressed]'] = self.__main_parent.style[
            '[Widget:pressed]']

        self.__main_parent.style = self.__main_parent.style

    def __focus_in(self) -> None:
        self._is_inactive = False
        self._obj.set_style_sheet(self.__normal_style)

    def __focus_out(self) -> None:
        self._is_inactive = True
        self._obj.set_style_sheet(self.__inactive_style)

    def __get_qss_style(self, state: str = '', inactive: bool = False) -> str:
        return self.__style_manager.style_to_qss(
            {
                f'[{self.style_id}{state}]':
                self.__style_manager.stylesheet[f'[{self.style_id}{state}]']
            },
            inactive=inactive).split('{')[1].replace('}', '').strip()

    def __leave(self) -> None:
        if self._is_inactive:
            # self._obj.set_style_sheet('')
            # self.__label._obj.set_style_sheet('')
            self.__focus_out()
        else:
            self._obj.set_style_sheet(self.__normal_style)

    def __main_added(self) -> None:
        self.__main_parent.event_signal(Event.FOCUS_IN).connect(self.__focus_in)
        self.__main_parent.event_signal(Event.FOCUS_OUT).connect(self.__focus_out)

    def __press(self) -> None:
        self.__widget.set_style_sheet(self.__pressed_style)

    def __release(self) -> None:
        self._obj.set_style_sheet(self.__hover_style)

    def __hover(self) -> None:
        self._obj.set_style_sheet(self.__hover_style)

    def __str__(self):
        return f'<Widget: {id(self)}>'
