#!/usr/bin/env python3
import logging

from PySide6 import QtWidgets
from __feature__ import snake_case

from .core import CoreWidget, CoreBaseWidget
from .core.modules import StyleManager
from .event import Event
from .signal import Signal


class Widget(object):
    """Widget."""
    def __init__(self, *args, **kwargs) -> None:
        """Class constructor."""


class Widget(Widget):
    """Widget."""
    def __init__(
            self, main_parent = None, base: bool = True,
            *args, **kwargs) -> None:
        """Class constructor.

        :main_parent: MainFrame object
        """
        super().__init__(*args, **kwargs)
        self.__main_parent = main_parent
        self.__base = base

        self.style_change_signal = Signal()
        self.style_id_change_signal = Signal()
        self.main_parent_added = Signal()

        self._is_inactive = False
        self.__widget = CoreWidget() if not self.__base else CoreBaseWidget()

        self.__box = QtWidgets.QVBoxLayout()
        self.__widget.set_layout(self.__box)

        self.__style_manager = StyleManager()
        self.__normal_style = None
        self.__hover_style = None
        self.__pressed_style = None
        self.__inactive_style = None
        self.__style = None
        self.__style = self.__style_manager.stylesheet
        self.__styles(self.__style, 'Widget', 'Widget')

        if not self.__base:
            self.event_signal(
                Event.MAIN_PARENT_ADDED).connect(self.__main_added)
            self.event_signal(
                Event.MOUSE_BUTTON_RELEASE).connect(self.__release)
            self.event_signal(Event.MOUSE_BUTTON_PRESS).connect(self.__press)
            self.event_signal(Event.MOUSE_HOVER_ENTER).connect(self.__hover)
            self.event_signal(Event.MOUSE_HOVER_LEAVE).connect(self.__leave)

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
        if self.__base:
            margin = self.__widget.contents_margins()
            return margin.top(), margin.right(), margin.bottom(), margin.left()

        m = self.style[f'[{self.style_id}]']['margin'].replace(
            'px', '').split()
        return int(m[0]), int(m[1]), int(m[2]), int(m[3])
    
    @margin.setter
    def margin(self, margin: tuple) -> None:
        if self.__base:
            self.__widget.set_contents_margins(
                margin[3], margin[0], margin[1], margin[2])
            return

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

        The base widget (Widget) does not respond to style settings because it 
        is the base element from which all other widgets are built. However, 
        the 'margin' property can still be used. In order for the style to be 
        affected, it must have the 'base' parameter set to 'False':

            Widget(base=False)

        This will enable color style support in any state, such as the 'hover' 
        and 'pressed' states.

        Note: The Box's 'spacing' property takes precedence over the widget's 
        margins, unless the widget is the only one isolated within a Box.
        """
        return self.__style

    @style.setter
    def style(self, style: dict) -> None:
        self.style_change_signal.emit()
        self.__styles(style, self.style_id, self.style_id)

    @property
    def style_id(self) -> str:
        """Style ID.

        An ID allows you to define a unique style that does not distort 
        parent objects of the same type that inherit from the class.

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

        Use only to access properties and methods of the Main Frame, defining 
        a new frame will break the application.
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

    def add_box(self, box = None, horizontal: bool = False):
        """Add a Box inside this Widget."""
        if not box:
            box = Box(horizontal)

        _, box = setattr(self, str(box), box), getattr(self, str(box))
        box._main_parent = self._main_parent
        self.__box.add_layout(box._obj)
        return box

    def add_widget(self, widget: Widget) -> Widget:
        """Add a new Widget inside this Widget."""
        _, widget = setattr(self, str(widget), widget), getattr(
            self, str(widget))
        widget._main_parent = self._main_parent
        self.__box.add_widget(widget._obj)
        return widget

    def event_signal(self, event: Event) -> Signal:
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

    def __hover(self) -> None:
        if not self._is_inactive:
            self._obj.set_style_sheet(self.__hover_style)

    def __leave(self) -> None:
        if self._is_inactive:
            # self._obj.set_style_sheet('')
            # self.__label._obj.set_style_sheet('')
            self.__focus_out()
        else:
            self._obj.set_style_sheet(self.__normal_style)

    def __main_added(self) -> None:
        self.__main_parent.event_signal(
            Event.FOCUS_IN).connect(self.__focus_in)
        self.__main_parent.event_signal(
            Event.FOCUS_OUT).connect(self.__focus_out)
        self.__main_parent.event_signal(
            Event.STYLE_CHANGE).connect(self.__update_style)

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

    def __release(self) -> None:
        if not self._is_inactive:
            self._obj.set_style_sheet(self.__hover_style)

    def __styles(
            self, style: dict, updated_id: str, inherited_id: str) -> None:
        self.__style = {
            f'[{updated_id}]': style[f'[{inherited_id}]'],
            f'[{updated_id}:inactive]': style[f'[{inherited_id}:inactive]'],
            f'[{updated_id}:hover]': style[f'[{inherited_id}:hover]'],
            f'[{updated_id}:pressed]': style[f'[{inherited_id}:pressed]']}
        
        self.__normal_style = self.__qss_piece(self.__style)
        self.__hover_style = self.__qss_piece(self.__style, ':hover')
        self.__pressed_style = self.__qss_piece(self.__style, ':pressed')
        self.__inactive_style = self.__qss_piece(
            self.__style, ':inactive', True)

        if self._main_parent:
            self._main_parent.style.update(self.__style)

    def __update_style(self) -> None:
        self.style.update(self._main_parent.style)
        self.style = self.style


    def __str__(self):
        return f'<Widget: {id(self)}>'
