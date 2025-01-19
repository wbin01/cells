#!/usr/bin/env python3
from .event import Event
from .widget import Widget


class CheckGroup(Widget):
    """Check Buttons Group Widget."""
    def __init__(self, buttons: list, *args, **kwargs) -> None:
        """Class constructor.

        :param buttons: List with all CheckButton's configured to display.
        """
        super().__init__(*args, **kwargs)
        self.__buttons = buttons

        self.style_id = 'CheckGroup'

        self.__selected_buttons = []
        self.__items = []
        self.signal(Event.MAIN_PARENT).connect(self.__on_main_parent)

    @property
    def buttons(self) -> list:
        """List with all CheckButton's configured to display."""
        return self.__buttons

    @buttons.setter
    def buttons(self, buttons: list) -> None:
        self.__buttons = buttons
        self.__add_buttons()

    def selected_buttons(self) -> list:
        """Selected CheckButton."""
        return self.__selected_buttons

    def __add_buttons(self) -> None:
        for check_button in self.__buttons:
            check_button._main_parent = self._main_parent

            if check_button.selected:
                self.__selected_buttons.append(check_button)

            item = self.add(check_button)
            _, item = setattr(self, str(item), item), getattr(self, str(item))

            item.signal(Event.MOUSE_PRESS).connect(self.__on_value)
            self.__items.append(item)

    def __on_main_parent(self) -> None:
        self.__add_buttons()

    def __on_value(self) -> None:
        self.__selected_buttons = []
        for item in self.__items:
            if item.selected:
                self.__selected_buttons.append(item)

    def __str__(self) -> str:
        return f'<CheckGroup: {id(self)}>'
