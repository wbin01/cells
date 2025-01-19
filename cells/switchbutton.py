#!/usr/bin/env python3
import os
import pathlib

from .event import Event
from .label import Label
from .orientation import Orientation
from .svgwidget import SvgWidget
from .widget import Widget


class SwitchButton(Widget):
    """Switch Button Widget."""
    def __init__(
            self,
            text: str = None,
            value: any = None,
            selected: bool = False,
            orientation: Orientation = Orientation.HORIZONTAL,
            *args, **kwargs) -> None:
        """Class constructor.
        
        :param text: SwitchButton text label.
        :param selected: True to start already selected.
        :param value: Value of any type to capture as an identifier.
        """
        super().__init__(orientation=orientation, *args, **kwargs)
        # Param
        self.__text = text if text else ''
        self.__selected = selected
        self.__value = value

        # Flags
        self.__icon_on_right = False
        self.__focus = True

        # Obj
        self.style_id = 'SwitchButton'

        self.__switch = os.path.join(
            pathlib.Path(__file__).resolve().parent,
            'core', 'static', 'switch.svg')

        self.__switch_selected = os.path.join(
            pathlib.Path(__file__).resolve().parent,
            'core', 'static', 'switchselected.svg')
        
        self.__icon = SvgWidget(self.__switch)
        self.__icon.width = 32

        if not self.__icon_on_right:
            self.insert(self.__icon)
        
        self.__label = Label(self.__text)
        if self.__text:
            self.insert(self.__label)

        if self.__icon_on_right:
            self.insert(self.__icon)
        
        self.__icon.style_id = 'Switch'

        # Signals
        self.signal(Event.ENABLED).connect(self.__on_enabled_change)
        self.signal(Event.MAIN_PARENT).connect(self.__on_main_parent)
        self.signal(Event.MOUSE_HOVER_ENTER).connect(self.__on_hover_enter)
        self.signal(Event.MOUSE_HOVER_LEAVE).connect(self.__on_hover_leave)
        self.signal(Event.MOUSE_PRESS).connect(self.__on_press)
        self.signal(Event.MOUSE_RELEASE).connect(self.__on_release)
        self.signal(Event.STATE).connect(self.__on_state)

    @property
    def text(self) -> str:
        """Button text.
        
        Pass a new string to update the text.
        """
        return self.__label.text

    @text.setter
    def text(self, text: str) -> None:
        self.__text = text
        self.__label.text = text

    @property
    def selected(self) -> bool:
        """If Widget is selected.

        Use True or False to select or deselect the widget.
        """
        return self.__selected

    @selected.setter
    def selected(self, value: bool) -> None:
        self.__selected = value

        if self.__selected:
            self.__icon.load(self.__switch_selected)
            self.__icon.style_class = 'Switch.selected'
        else:
            self.__icon.load(self.__switch)
            self.__icon.style_class = None

        self.__icon.state = None

    @property
    def value(self) -> any:
        """Button value.
        
        Pass a new value to update.
        """
        return self.__value

    @value.setter
    def value(self, value: any) -> None:
        self.__value = value

    def __on_enabled_change(self) -> None:
        if self.enabled:
            self.__on_main_parent_focus_in()
        else:
            self.__on_main_parent_focus_out()

        if self.__icon:
            self.__icon.enabled = self.enabled

    def __on_main_parent(self) -> None:
        self._main_parent.signal(Event.FOCUS_IN).connect(
            self.__on_main_parent_focus_in)
        self._main_parent.signal(Event.FOCUS_OUT).connect(
            self.__on_main_parent_focus_out)
        
        if self.__icon:
            self.__icon._main_parent = self._main_parent
            self.__icon.style_id = 'Switch'
            if self.__selected:
                self.__icon.load(self.__switch_selected)
                self.__icon.style_class = 'Switch.selected'

    def __on_main_parent_focus_in(self) -> None:
        self.__focus = True
        if self.enabled:
            self.__label.style['[Label]']['color'] = self.style[
                f'[{self.style_id}]']['color']
            self.__label.style = self.__label.style
            self.__icon.state = None

    def __on_main_parent_focus_out(self) -> None:
        self.__focus = False
        self.__label.style['[Label]']['color'] = self.style[
            f'[{self.style_id}:inactive]']['color']
        self.__label.style = self.__label.style
        self.__icon.state = 'inactive'

    def __on_hover_enter(self) -> None:
        if self.enabled and self.__focus:
            self.__label.style['[Label]']['color'] = self.style[
                f'[{self.style_id}:hover]']['color']
            self.__label.style = self.__label.style
            self.__icon.state = 'hover'

    def __on_hover_leave(self) -> None:
        if self.enabled and self.__focus:
            self.__label.style['[Label]']['color'] = self.style[
                f'[{self.style_id}]']['color']
            self.__label.style = self.__label.style
            self.__icon.state = None

    def __on_press(self) -> None:
        if self.enabled and self.__focus:
            self.__label.style['[Label]']['color'] = self.style[
                f'[{self.style_id}:pressed]']['color']
            self.__label.style = self.__label.style

            self.__selected = False if self.__selected else True
            if self.__selected:
                self.__icon.load(self.__switch_selected)
                self.__icon.style_class = 'Switch.selected'
            else:
                self.__icon.load(self.__switch)
                self.__icon.style_class = None

            self.__icon.state = 'pressed'

    def __on_release(self) -> None:
        if self.enabled and self.__focus:
            self.__label.style['[Label]']['color'] = self.style[
                f'[{self.style_id}:hover]']['color']
            self.__label.style = self.__label.style
            self.__icon.state = 'hover'

    def __on_state(self) -> None:
        if not self._main_parent:
            return

        if not self.state:
            self.__icon.state = None
        elif self.state == 'hover':
            self.__icon.state = 'hover'
        elif self.state == 'pressed':
            self.__icon.state = 'pressed'
        else:
            self.__icon.state = 'inactive'

    def __str__(self) -> str:
        return f'<SwitchButton: {id(self)}>'
