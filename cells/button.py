#!/usr/bin/env python3
from .align import Align
from .box import Box
from .event import Event
from .icon import Icon
from .image import Image
from .label import Label
from .orientation import Orientation
from .widget import Widget


class Button(Widget):
    """Button Widget."""
    def __init__(
            self,
            text: str = None,
            icon: str = None,
            orientation: Orientation = Orientation.HORIZONTAL,
            *args, **kwargs) -> None:
        """Class constructor.

        The icon is rendered from the path of a passed file, or from the name 
        of an icon in the current operating system, such as "folder-download". 
        To find out all the system icon names, see the "freedesktop.org" 
        specification:
            https://specifications.freedesktop.org/icon-naming-spec/latest/

        Although the Freedesk specification is for Linux, we are making it 
        compatible with Windows (Aesthetically compatible alternative icons). 
        If an icon is not found, it will not give an error, but it will also 
        not render any image, so to ensure an image is rendered use a file 
        path as a fallback (fallback_path).

        :param text: Button text string.
        :param icon: Icon path or icon name from system, like "folder-download".
        """
        super().__init__(orientation=orientation, *args, **kwargs)
        # Param
        self.__text = text if text else ''
        self.__icon = Icon(icon) if icon else icon

        # Obj
        self.style_id = 'Button'
        self.__focus = True
        self.__icon_on_right = False

        if self.__icon and not self.__icon_on_right:
            self.__icon = self.insert(Image(self.__icon))
            self.__icon.margin = 0, 0, 0, 5
        
        self.__label = Label(self.__text)
        if self.__text:
            self.insert(self.__label)
            if self.__icon_on_right:
                self.__label.margin = 0, 0, 0, 5
            else:
                self.__label.margin = 0, 5, 0, 0

        if self.__icon and self.__icon_on_right:
            self.__icon = self.insert(Image(self.__icon))
            self.__icon.margin = 0, 5, 0, 0

        if not self.__text and self.__icon:
            self.__icon.margin = 0, 5, 0, 5
        elif self.__text and not self.__icon:
            self.__label.margin = 0, 5, 0, 5

        self.__saved_label_margin = None
        if self.__label:
            self.__saved_label_margin = self.__label.margin

        self.__saved_icon_margin = None
        if self.__icon:
            self.__saved_icon_margin = self.__icon.margin

        self.__saved_height = self.height
        self.__saved_width = self.width

        # Signals
        self.signal(Event.ENABLED).connect(self.__on_enabled_change)
        self.signal(Event.MAIN_PARENT).connect(self.__on_main_added)
        self.signal(Event.MOUSE_HOVER_ENTER).connect(self.__on_hover_enter)
        self.signal(Event.MOUSE_HOVER_LEAVE).connect(self.__on_hover_leave)
        self.signal(Event.MOUSE_PRESS).connect(self.__on_press)
        self.signal(Event.MOUSE_RELEASE).connect(self.__on_release)

        # Flags
        self.__selectable = False
        self.__selected = False

        # Style
        self.spacing = 2
        self.align = Align.CENTER
        self.min_height = 32

    @property
    def selectable(self) -> bool:
        """If it is selectable.

        Whether the widget is selectable as a toggle button.
        """
        return self.__selectable

    @selectable.setter
    def selectable(self, value: bool) -> None:
        self.__selectable = value

    @property
    def selected(self) -> bool:
        """If Widget is selected.

        Only works if the 'selectable' property is True.
        Use True or False to select or deselect the widget.
        """
        return self.__selected

    @selected.setter
    def selected(self, value: bool) -> None:
        if self.__selectable:
            self.__selected = value

            if self.__selected:
                self.style_class = 'Button.selected'
                self.state = 'pressed'
            else:
                self.style_class = None
                self.state = None

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

    def __on_enabled_change(self) -> None:
        if self.enabled:
            self.__on_main_parent_focus_in()
        else:
            self.__on_main_parent_focus_out()

        if self.__icon:
            self.__icon.enabled = self.enabled

    def __on_main_added(self) -> None:
        self._main_parent.signal(Event.FOCUS_IN).connect(
            self.__on_main_parent_focus_in)
        self._main_parent.signal(Event.FOCUS_OUT).connect(
            self.__on_main_parent_focus_out)
        
        if self.__icon:
            self.__icon._main_parent = self._main_parent
            self.__label._main_parent = self._main_parent

    def __on_main_parent_focus_in(self) -> None:
        self.__focus = True
        if self.enabled:
            self.__label.style['[Label]']['color'] = self.style[
                f'[{self.style_id}]']['color']
            self.__label.style = self.__label.style

    def __on_main_parent_focus_out(self) -> None:
        self.__focus = False
        self.__label.style['[Label]']['color'] = self.style[
            f'[{self.style_id}:inactive]']['color']
        self.__label.style = self.__label.style

    def __on_hover_enter(self) -> None:
        if self.enabled and self.__focus:
            self.__label.style['[Label]']['color'] = self.style[
                f'[{self.style_id}:hover]']['color']
            self.__label.style = self.__label.style

    def __on_hover_leave(self) -> None:
        if self.enabled and self.__focus:
            self.__label.style['[Label]']['color'] = self.style[
                f'[{self.style_id}]']['color']
            self.__label.style = self.__label.style

    def __on_press(self) -> None:
        if self.enabled and self.__focus:
            self.__label.style['[Label]']['color'] = self.style[
                f'[{self.style_id}:pressed]']['color']
            self.__label.style = self.__label.style

            if self.__selectable:
                if self.__selected:
                    self.__selected = False
                    self.style_class = None
                else:
                    self.__selected = True
                    self.style_class = 'Button.selected'
                    self.state = 'pressed'
            else:
                if self.__selected:
                    self.__selected = False
                    self.style_class = None

    def __on_release(self) -> None:
        if self.enabled and self.__focus:
            self.__label.style['[Label]']['color'] = self.style[
                f'[{self.style_id}:hover]']['color']
            self.__label.style = self.__label.style

    def __str__(self) -> str:
        return f'<Button: {id(self)}>'
