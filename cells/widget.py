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
    def __init__(self, main_parent = None, *args, **kwargs) -> None:
        """Class constructor.

        :main_parent: MainFrame object
        """
        super().__init__(*args, **kwargs)
        self.style_change_signal = Signal()
        self.style_id_change_signal = Signal()
        self.main_parent_added = Signal()

        self._is_inactive = False

        self.__widget = CoreWidget()
        self.__main_parent = main_parent

        self.__box = QtWidgets.QVBoxLayout()
        self.__widget.set_layout(self.__box)

        self.__style_manager = StyleManager()
        self.__normal_style = None
        self.__hover_style = None
        self.__pressed_style = None
        self.__inactive_style = None
        self.__style = None
        self.__styles(self.__style_manager.stylesheet, 'Widget', 'Widget')

        self.event_signal(Event.MAIN_PARENT_ADDED).connect(self.__main_added)
        self.event_signal(Event.MOUSE_BUTTON_PRESS).connect(self.__press)
        self.event_signal(Event.MOUSE_BUTTON_RELEASE).connect(self.__release)
        self.event_signal(Event.MOUSE_HOVER_ENTER).connect(self.__hover)
        self.event_signal(Event.MOUSE_HOVER_LEAVE).connect(self.__leave)

    @property
    def style(self) -> str:
        """Style

        The style is accessed from the main frame (`MainFrame`), so the main 
        frame property (`self.my_widget._main_parent`) needs to be set first. 
        When adding the widget (`Widget`, `Button`, `Label`...) to a `Box` it 
        will do this automatically.
        Equivalent ways to set up access to the style:

        1) my_widget = Widget(main_parent=self)

        2) my_widget = Widget()
           my_box.add_widget(my_widget)

        3) my_widget = Widget()
           my_widget._main_parent = self

        The second way is the recommended one. First we add the widget to the 
        `Box`, and only then we configure the widget.
        """
        return self.__style

    @style.setter
    def style(self, style: dict) -> None:
        self.style_change_signal.emit()
        self.__styles(style, self.style_id, self.style_id)

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

        inherited_id = self.style_id if self.style_id else 'Widget'
        self.__widget.set_object_name(style_id)
        self.__styles(self.__style, style_id, inherited_id)

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

    def add_box(self, box):
        """Add a Box inside this Widget"""
        box._main_parent = self._main_parent
        _, box = setattr(self, str(box), box), getattr(self, str(box))
        self.__box.add_layout(box._obj)
        return box

    def add_widget(self, widget: Widget) -> Widget:
        """Add a new Widget inside this Widget"""
        widget.main_parent = self._main_parent
        _, widget = setattr(self, str(widget), widget), getattr(self, str(widget))
        self.__box.add_widget(widget._obj)
        return widget

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

    def __focus_in(self) -> None:
        self._is_inactive = False
        self._obj.set_style_sheet(self.__normal_style)

    def __focus_out(self) -> None:
        self._is_inactive = True
        self._obj.set_style_sheet(self.__inactive_style)

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

    def __styles(self, style: dict, updated_id: str, inherited_id: str) -> None:
        self.__style = {
            f'[{updated_id}]': style[f'[{inherited_id}]'],
            f'[{updated_id}:inactive]': style[f'[{inherited_id}:inactive]'],
            f'[{updated_id}:hover]': style[f'[{inherited_id}:hover]'],
            f'[{updated_id}:pressed]': style[f'[{inherited_id}:pressed]']}
        
        self.__normal_style = self.__qss_piece(self.__style)
        self.__hover_style = self.__qss_piece(self.__style, ':hover')
        self.__pressed_style = self.__qss_piece(self.__style, ':pressed')
        self.__inactive_style = self.__qss_piece(self.__style, ':inactive', True)

    def __release(self) -> None:
        if not self._is_inactive:
            self._obj.set_style_sheet(self.__hover_style)

    def __hover(self) -> None:
        if not self._is_inactive:
            self._obj.set_style_sheet(self.__hover_style)

    def __str__(self):
        return f'<Widget: {id(self)}>'
