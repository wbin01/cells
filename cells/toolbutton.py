#!/usr/bin/env python3
from .align import Align
from .box import Box
from .event import Event
from .icon import Icon
from .image import Image
from .label import Label
from .orientation import Orientation
from .widget import Widget


class ToolButton(Widget):
    """Tool Button Widget."""
    def __init__(self, icon: str | Icon, *args, **kwargs) -> None:
        """Class constructor."""
        super().__init__(*args, **kwargs)
        # Param
        self.__icon = Icon(icon) if icon else icon

        # Obj
        self.style_id = 'ToolButton'
        self.__icon = self.add(Image(self.__icon))

        # Signals
        self.signal(Event.MAIN_PARENT).connect(self.__on_main_parent)
        self.signal(Event.MOUSE_PRESS).connect(self.__on_mouse_button_press)

        # Flags
        self.__selectable = True
        self.__selected = False

        # Style
        self.align = Align.CENTER
        self.width = 32
        self.height = 32
        self.margin = 0, 0, 0, 0

    @property
    def selectable(self) -> bool:
        """..."""
        return self.__selectable

    @selectable.setter
    def selectable(self, value: bool) -> None:
        self.__selectable = value

    @property
    def selected(self) -> bool:
        """..."""
        return self.__selected

    @selected.setter
    def selected(self, value: bool) -> None:
        if self.__selectable:
            self.__selected = value

            if self.__selected:
                self.style_class = 'ToolButton.selected'
                self.state = 'pressed'
            else:
                self.style_class = None
                self.state = None

    def __on_main_parent(self) -> None:
        self.__icon._main_parent = self._main_parent

    def __on_mouse_button_press(self) -> None:
        if self.enabled:
            if self.__selectable:
                if self.__selected:
                    self.__selected = False
                    self.style_class = None
                else:
                    self.__selected = True
                    self.style_class = 'ToolButton.selected'
                    self.state = 'pressed'
            else:
                if self.__selected:
                    self.__selected = False
                    self.style_class = None

    def __str__(self) -> str:
        return f'<ToolButton: {id(self)}>'
