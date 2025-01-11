#!/usr/bin/env python3
from .event import Event
from .radiobutton import RadioButton
from .widget import Widget


class RadioGroup(Widget):
    """Radio Buttons Group Widget."""
    def __init__(self, radio_buttons: list, *args, **kwargs) -> None:
        """Class constructor.

        :param radio_buttons:
            List with all radio buttons configured to display.
        """
        super().__init__(*args, **kwargs)
        self.__radio_buttons = radio_buttons

        self.style_id = 'RadioGroup'

        self.__value = None
        self.__selected_button = None
        self.__items = []
        self.signal(Event.MAIN_PARENT).connect(self.__on_main_added)

    def selected_button(self) -> RadioButton:
        """Selected RadioButton."""
        return self.__selected_button

    def __add_buttons(self) -> None:
        for radio_button in self.__radio_buttons:
            radio_button._main_parent = self._main_parent

            if not self.__value:
                if radio_button.selected:
                    self.__value = radio_button.value
                    self.__selected_button = radio_button
            else:
                radio_button.selected = False

            
            item = self.insert(radio_button)
            _, item = setattr(self, str(item), item), getattr(self, str(item))

            item.signal(Event.MOUSE_PRESS).connect(self.__on_value)
            self.__items.append(item)

    def __on_main_added(self) -> None:        
        self.__add_buttons()

    def __on_value(self) -> None:
        for item in self.__items:
            if item.selected and item.value != self.__value:
                self.__value = item.value
                self.__selected_button = item
                break

        for item in self.__items:
            if item.value == self.__value:
                item.selected = True
            else:
                item.selected = False

    def __str__(self) -> str:
        return f'<RadioGroup: {id(self)}>'
